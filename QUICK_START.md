# ⚡ Quick Start Guide - Hackathon Demo

## 🎯 What This Does

**Deployment Agent** automatically deploys apps to cloud by:
1. Asking which cloud platform
2. Cloning GitHub repo
3. Running tests automatically
4. Deploying to Cloud Run
5. Returning live URL

## 🚀 Run Demo (2 commands)

### 1. Start the Deployment Agent

```bash
cd deploy_agent
adk web --port 8000
```

Open: `http://localhost:8000`

### 2. Talk to the Agent

**You:** "Deploy my app to Google Cloud"

**Agent:** "Which GitHub repository?"

**You:** "https://github.com/Sra1panasa/google_hackathon_deploy_bot"

**Agent:** 
- Clones repo ✓
- Runs tests ✓
- Asks for confirmation
- Deploys to Cloud Run ✓
- Returns URL 🌐

## 🎥 Loom Video Script (5 minutes)

### Part 1: Introduction (30 sec)
"Hi! This is an AI agent that automates cloud deployments. Just give it a GitHub URL, and it handles everything - cloning, testing, and deploying."

### Part 2: Start Agent (30 sec)
```bash
cd deploy_agent
adk web --port 8000
```
Show browser opening to `http://localhost:8000`

### Part 3: Demo Conversation (2 min)
1. "I want to deploy an application"
2. Agent asks for cloud platform → "Google Cloud"
3. Agent asks for GitHub URL → Provide URL
4. Watch agent:
   - Clone repository
   - Run tests automatically
   - Show test results
5. Agent asks to deploy → "Yes"
6. Watch deployment progress
7. **Get live URL!**

### Part 4: Show Deployed App (1 min)
- Open the returned URL
- Interact with deployed service
- "The agent deployed this automatically!"

### Part 5: Vision (1 min)
"This prototype shows:
- ✅ Automated GitHub integration
- ✅ Automatic test discovery and execution
- ✅ One-command deployment
- 🚧 Future: AWS, Azure, Kubernetes
- 🚧 Future: Rollback, monitoring, cost optimization"

## 📋 Pre-Demo Checklist

- [ ] Docker Desktop running
- [ ] Google Cloud authenticated (`gcloud auth list`)
- [ ] Environment variables set:
```bash
export GOOGLE_CLOUD_PROJECT=mbs-graphrak
export GOOGLE_CLOUD_LOCATION=europe-west2
```
- [ ] Repository committed to GitHub
- [ ] Browser ready
- [ ] Screen recording ready

## 🔧 Test Locally First

### Test the sample agent:
```bash
cd my_agent
python test_agent.py
```
Expected: `[SUCCESS] All tests passed!`

### Test deployment agent:
```bash
cd deploy_agent
adk web --port 8000
```
Expected: Web UI opens at localhost:8000

## 📝 Key Demo Points

1. **Natural Language Interface** - Just talk to the agent
2. **Fully Automated** - Clone, test, deploy automatically
3. **Safe** - Tests must pass before deployment
4. **Fast** - Minutes, not hours
5. **Extensible** - Easy to add AWS, Azure support

## 🎯 Demo Commands

**Set environment:**
```bash
export GOOGLE_CLOUD_PROJECT=mbs-graphrag
export GOOGLE_CLOUD_LOCATION=europe-west2
```

**Run agent:**
```bash
cd deploy_agent
adk web --port 8000
```

**Example conversation:**
```
User: Deploy to Google Cloud
Agent: <asks for GitHub URL>
User: https://github.com/Sra1panasa/google_hackathon_deploy_bot
Agent: <clones, tests, deploys>
Agent: Service live at https://deployed-xxxxx.run.app
```

## 🚨 Troubleshooting

**Agent not starting:**
```bash
pip install google-adk
```

**Tests fail:**
Ensure `my_agent/test_agent.py` exists and works:
```bash
cd my_agent && python test_agent.py
```

**Deployment fails:**
- Check Docker is running
- Verify `gcloud auth list` shows your account
- Check project ID is correct

## 💡 Time-Saving Tips

1. **Have repo already on GitHub** - Don't upload during video
2. **Test the flow once before recording** - Know it works
3. **Use localhost** - Faster for demo than deployed agent
4. **Pre-set environment variables** - One less thing to type

## 🎬 After Demo

To deploy the agent itself to Cloud Run:

```bash
cd deploy_agent
adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --with_ui \
  --service_name=deploy-automation-agent \
  "$PWD"
```

Then anyone can use the URL to deploy their apps!

---

**Ready to record? Start with the checklist above! 🎥**
