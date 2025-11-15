import os
import subprocess
import shutil
from google.adk.agents.llm_agent import Agent

def ask_cloud_platform(user_choice: str) -> dict:
    """
    Ask user which cloud platform they want to deploy to.
    Args:
        user_choice: The cloud platform choice (aws, gcp, azure)
    Returns:
        dict: Confirmation of cloud platform selection
    """
    valid_platforms = ['aws', 'gcp', 'azure', 'google', 'google cloud']
    choice = user_choice.lower()
    
    if any(platform in choice for platform in ['gcp', 'google']):
        return {
            "status": "success",
            "platform": "Google Cloud Platform (GCP)",
            "message": "Great! You selected Google Cloud Platform. Now, please provide the GitHub repository URL you want to deploy."
        }
    elif 'aws' in choice:
        return {
            "status": "info",
            "platform": "AWS",
            "message": "AWS deployment is coming soon! For this demo, we'll use Google Cloud Platform. Please provide your GitHub repository URL."
        }
    elif 'azure' in choice:
        return {
            "status": "info",
            "platform": "Azure",
            "message": "Azure deployment is coming soon! For this demo, we'll use Google Cloud Platform. Please provide your GitHub repository URL."
        }
    else:
        return {
            "status": "error",
            "message": "Please specify a cloud platform: AWS, Google Cloud (GCP), or Azure"
        }


def clone_and_test_repo(github_url: str) -> dict:
    """
    Clone a GitHub repository and run tests from the test folder.
    Args:
        github_url: The GitHub repository URL to clone
    Returns:
        dict: Results of cloning and testing
    """
    try:
        # Extract repo name from URL
        repo_name = github_url.rstrip('/').split('/')[-1].replace('.git', '')
        clone_path = f"/tmp/{repo_name}"
        
        # Remove if exists
        if os.path.exists(clone_path):
            shutil.rmtree(clone_path)
        
        # Clone repository
        print(f"Cloning repository: {github_url}")
        clone_result = subprocess.run(
            ['git', 'clone', github_url, clone_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if clone_result.returncode != 0:
            return {
                "status": "error",
                "message": f"Failed to clone repository: {clone_result.stderr}",
                "step": "clone"
            }
        
        # Look for test files
        test_files = []
        for root, dirs, files in os.walk(clone_path):
            for file in files:
                if file.startswith('test_') and file.endswith('.py'):
                    test_files.append(os.path.join(root, file))
        
        if not test_files:
            return {
                "status": "warning",
                "message": "No test files found (test_*.py). Proceeding without tests.",
                "step": "test",
                "clone_path": clone_path,
                "repo_name": repo_name
            }
        
        # Run tests
        print(f"Found {len(test_files)} test file(s). Running tests...")
        all_tests_passed = True
        test_results = []
        
        for test_file in test_files:
            test_dir = os.path.dirname(test_file)
            test_name = os.path.basename(test_file)
            
            # Try running with pytest first
            test_result = subprocess.run(
                ['python', '-m', 'pytest', test_file, '-v'],
                capture_output=True,
                text=True,
                cwd=test_dir,
                timeout=120
            )
            
            if test_result.returncode == 0:
                test_results.append(f"✓ {test_name}: PASSED")
            else:
                # Try running directly
                test_result = subprocess.run(
                    ['python', test_file],
                    capture_output=True,
                    text=True,
                    cwd=test_dir,
                    timeout=120
                )
                
                if test_result.returncode == 0:
                    test_results.append(f"✓ {test_name}: PASSED")
                else:
                    test_results.append(f"✗ {test_name}: FAILED")
                    all_tests_passed = False
        
        if all_tests_passed:
            return {
                "status": "success",
                "message": f"Repository cloned and all tests passed!\n" + "\n".join(test_results),
                "step": "test_passed",
                "clone_path": clone_path,
                "repo_name": repo_name,
                "ready_to_deploy": True
            }
        else:
            return {
                "status": "error",
                "message": f"Tests failed:\n" + "\n".join(test_results),
                "step": "test_failed"
            }
            
    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "message": "Operation timed out. Please try again.",
            "step": "timeout"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error: {str(e)}",
            "step": "exception"
        }


def deploy_to_cloud_run(repo_path: str, repo_name: str) -> dict:
    """
    Deploy the cloned repository to Google Cloud Run.
    Args:
        repo_path: Path to the cloned repository
        repo_name: Name of the repository
    Returns:
        dict: Deployment result with service URL
    """
    try:
        # Set environment variables
        project = os.environ.get('GOOGLE_CLOUD_PROJECT', 'mbs-graphrag')
        region = os.environ.get('GOOGLE_CLOUD_LOCATION', 'us-central1')
        service_name = f"deployed-{repo_name.lower()}"
        
        print(f"Deploying {repo_name} to Cloud Run...")
        print(f"Project: {project}, Region: {region}, Service: {service_name}")
        
        # Look for agent directory
        agent_path = repo_path
        potential_paths = [
            os.path.join(repo_path, 'my_agent'),
            os.path.join(repo_path, 'agent'),
            repo_path
        ]
        
        for path in potential_paths:
            if os.path.exists(os.path.join(path, 'agent.py')):
                agent_path = path
                break
        
        # Deploy using ADK
        deploy_cmd = [
            'adk', 'deploy', 'cloud_run',
            f'--project={project}',
            f'--region={region}',
            '--with_ui',
            f'--service_name={service_name}',
            agent_path
        ]
        
        deploy_result = subprocess.run(
            deploy_cmd,
            capture_output=True,
            text=True,
            timeout=600  # 10 minutes for deployment
        )
        
        if deploy_result.returncode == 0:
            # Extract URL from output
            output = deploy_result.stdout + deploy_result.stderr
            service_url = f"https://{service_name}-xxxxx-{region}.a.run.app"
            
            # Try to find actual URL in output
            for line in output.split('\n'):
                if 'https://' in line and '.run.app' in line:
                    # Extract URL
                    import re
                    urls = re.findall(r'https://[^\s]+\.run\.app', line)
                    if urls:
                        service_url = urls[0]
                        break
            
            return {
                "status": "success",
                "message": f"🎉 Deployment successful!",
                "service_url": service_url,
                "service_name": service_name,
                "project": project,
                "region": region
            }
        else:
            return {
                "status": "error",
                "message": f"Deployment failed: {deploy_result.stderr}",
                "details": deploy_result.stdout
            }
            
    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "message": "Deployment timed out. The service might still be deploying. Check Google Cloud Console."
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Deployment error: {str(e)}"
        }


def confirm_deployment(confirmation: str) -> dict:
    """
    Get user confirmation before deploying.
    Args:
        confirmation: User's response (yes/no)
    Returns:
        dict: Confirmation status
    """
    response = confirmation.lower()
    if any(word in response for word in ['yes', 'y', 'deploy', 'proceed', 'go']):
        return {
            "status": "confirmed",
            "message": "Starting deployment process..."
        }
    else:
        return {
            "status": "cancelled",
            "message": "Deployment cancelled. You can start again anytime!"
        }


# Create the deployment automation agent
root_agent = Agent(
    model='gemini-2.5-flash',
    model_kwargs={
        'vertexai': True,
        'project': os.environ.get('GOOGLE_CLOUD_PROJECT', 'mbs-graphrag'),
        'location': os.environ.get('GOOGLE_CLOUD_LOCATION', 'europe-west2'),
    },
    name='deploy_automation_agent',
    description="Automates deployment of applications to cloud platforms (AWS, GCP, Azure).",
    instruction="""You are an AI deployment automation assistant. Your job is to help users deploy their applications to cloud platforms.

Follow this workflow step by step:

1. **Ask for Cloud Platform**: First, ask the user which cloud platform they want to use (AWS, Google Cloud/GCP, or Azure). Use the 'ask_cloud_platform' tool with their response.

2. **Ask for GitHub URL**: Once they select a platform, ask for the GitHub repository URL they want to deploy. 

3. **Clone and Test**: Use the 'clone_and_test_repo' tool with the GitHub URL. This will:
   - Clone the repository
   - Automatically find and run test files (test_*.py)
   - Report test results

4. **If Tests Pass**: Tell the user "✅ All tests passed successfully! Would you like to proceed with deployment to Cloud Run?" Then wait for their confirmation.

5. **Get Confirmation**: Use the 'confirm_deployment' tool with their response.

6. **Deploy**: If they confirm, use the 'deploy_to_cloud_run' tool to deploy the application. Provide them with the deployment URL.

7. **Provide URL**: Give them the final service URL where they can access their deployed application.

Be friendly, clear, and guide them through each step. If something fails, explain what happened and offer to help troubleshoot.

IMPORTANT: 
- Always wait for user responses between steps
- Don't skip the confirmation step
- Provide clear feedback at each stage
- For this demo, we primarily support Google Cloud Platform deployment
""",
    tools=[
        ask_cloud_platform,
        clone_and_test_repo,
        deploy_to_cloud_run,
        confirm_deployment
    ],
)

