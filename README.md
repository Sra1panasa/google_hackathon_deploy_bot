# 🚀 Auto-Deploy Bot - Google Hackathon

An AI-powered deployment automation agent that streamlines cloud deployments across AWS, Google Cloud, and Azure.

## 🎯 Concept

The Auto-Deploy Bot is an intelligent agent that automates the entire deployment workflow:

1. 🤖 **Ask**: Which cloud platform? (AWS, GCP, Azure)
2. 🔗 **Request**: GitHub repository URL
3. 📥 **Clone**: Repository automatically
4. 🧪 **Test**: Discover and run all tests
5. ✅ **Confirm**: Ask user before deploying
6. 🚀 **Deploy**: To Cloud Run (with UI)
7. 🌐 **Deliver**: Live service URL

## 📁 Project Structure

```
hackathon/
├── deploy_agent/          # Main deployment automation agent
│   ├── agent.py          # Agent with deployment tools
│   └── requirements.txt  # Dependencies
│
└── my_agent/             # Sample agent for testing
    ├── agent.py          # Simple time-telling agent
    ├── test_agent.py     # Tests for the sample agent
    └── requirements.txt  # Dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker Desktop (running)
- Google Cloud SDK (authenticated)
- Git

### 1. Install Dependencies

```bash
cd deploy_agent
pip install -r requirements.txt
```

### 2. Set Environment Variables

```bash
export GOOGLE_CLOUD_PROJECT=mbs-graphrag
export GOOGLE_CLOUD_LOCATION=europe-west2
```

### 3. Run the Deployment Agent Locally

```bash
cd deploy_agent
adk web --port 8000
```

Open browser: `http://localhost:8000`

### 4. Interact with the Agent

The agent will guide you through:

**Example conversation:**

```
You: "I want to deploy my app"

Agent: "Great! Which cloud platform would you like to use? 
        We support AWS, Google Cloud (GCP), and Azure."

You: "Google Cloud"

Agent: "Perfect! Google Cloud Platform selected. 
        Please provide your GitHub repository URL."

You: "https://github.com/Sra1panasa/google_hackathon_deploy_bot"

Agent: "Cloning repository and running tests... 
        ✓ test_agent.py: PASSED
        ✅ All tests passed successfully! 
        Would you like to proceed with deployment to Cloud Run?"

You: "Yes, deploy it!"

Agent: "🎉 Deployment successful!
        Your service is live at: https://deployed-repo-xxxxx.a.run.app"
```

## 🧪 Testing with Sample Agent

The repository includes `my_agent/` - a sample time-telling agent for testing the deployment flow.

**Test it locally:**

```bash
cd my_agent
python test_agent.py
```

**Deploy via the agent:**

1. Start deployment agent: `cd deploy_agent && adk web --port 8000`
2. Tell it to deploy: `https://github.com/Sra1panasa/google_hackathon_deploy_bot`
3. Watch automated deployment!

## 🛠️ Available Tools

The deployment agent has these capabilities:

### `ask_cloud_platform`
Handles cloud platform selection (AWS, GCP, Azure)

### `clone_and_test_repo`
- Clones GitHub repository
- Auto-discovers test files (`test_*.py`)
- Runs tests with pytest or direct Python
- Returns test results

### `deploy_to_cloud_run`
- Deploys to Google Cloud Run
- Sets up with UI automatically
- Returns live service URL

### `confirm_deployment`
- Gets user confirmation before deploying
- Safety check before cloud deployment

## 📦 Deployment Options

### Deploy the Deployment Agent Itself

To deploy the agent to Cloud Run so others can use it:

```bash
cd deploy_agent
export GOOGLE_CLOUD_PROJECT=mbs-graphrag
export GOOGLE_CLOUD_LOCATION=europe-west2

adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --with_ui \
  --service_name=deploy-automation-agent \
  "$PWD"
```

Then share the URL with your team!

## 🎥 Demo Flow for Hackathon

### 1. Show Local Testing (1 min)
```bash
cd deploy_agent
adk web --port 8000
```
Open `http://localhost:8000` and show the UI

### 2. Demonstrate Automation (3 min)
- Ask for cloud platform
- Provide GitHub URL
- Show automatic cloning
- Show test execution
- Confirm deployment
- Get live URL

### 3. Access Deployed Service (1 min)
- Open the returned URL
- Interact with deployed agent
- Show it's live!

### 4. Explain Vision (1 min)
- Multi-cloud support
- Enterprise CI/CD integration
- Automated rollback
- Cost optimization

## 🏗️ Architecture

```
User → Deployment Agent → GitHub Clone → Test Runner → Cloud Run Deploy → Live URL
                ↓
        [AWS | GCP | Azure]
```

**Current Implementation:**
- ✅ Google Cloud Platform (Cloud Run)
- ✅ Automated testing
- ✅ GitHub integration
- ✅ Interactive agent UI

**Future Enhancements:**
- 🚧 AWS Lambda deployment
- 🚧 Azure Functions deployment
- 🚧 Terraform integration
- 🚧 Kubernetes deployment
- 🚧 Rollback capabilities
- 🚧 Cost estimation

## 🔧 Configuration

### Environment Variables

```bash
# Required for deployment
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=your-region

# Optional
export TMPDIR=/tmp  # For temporary clone directory
```

### Custom Service Names

The agent automatically generates service names like `deployed-{repo-name}`. You can customize this in `agent.py`.

## 🐛 Troubleshooting

**Docker not running:**
```bash
# Start Docker Desktop first
docker ps  # Verify it's running
```

**Authentication issues:**
```bash
gcloud auth login
gcloud config set project mbs-graphrag
```

**Port already in use:**
```bash
adk web --port 8001  # Use different port
```

**Tests not found:**
Ensure test files follow naming convention: `test_*.py`

## 📝 Example Use Cases

### 1. Rapid Prototyping
Quickly deploy and test prototypes without manual setup.

### 2. CI/CD Integration
Integrate agent into your CI/CD pipeline for automated deployments.

### 3. Multi-Team Deployments
Non-technical teams can deploy services using natural language.

### 4. Hackathon Quick Deploys
Deploy your hackathon projects in minutes, not hours!

## 🔗 Links

- **GitHub**: https://github.com/Sra1panasa/google_hackathon_deploy_bot
- **Google ADK**: https://cloud.google.com/ai-development-kit
- **Cloud Run**: https://cloud.google.com/run

## 🎓 Learning Resources

Built with:
- **Google ADK** - AI Development Kit
- **Gemini 2.5 Flash** - LLM model
- **Cloud Run** - Serverless platform
- **Python** - Implementation language

## 📞 Support

Created for Google Hackathon 2024

For issues or questions, open an issue on GitHub.

---

⚡ **Built with Google ADK** | 🚀 **Deploy anywhere, anytime** | 🤖 **Powered by Gemini**
