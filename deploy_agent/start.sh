#!/bin/bash

# Startup script for deployment agent
# Sets environment and starts the agent

echo "========================================"
echo "Deployment Automation Agent - Startup"
echo "========================================"
echo ""

# Set environment variables
export GOOGLE_CLOUD_PROJECT=mbs-graphrag
export GOOGLE_CLOUD_LOCATION=europe-west2

echo "Environment Configuration:"
echo "   Project: $GOOGLE_CLOUD_PROJECT"
echo "   Location: $GOOGLE_CLOUD_LOCATION"
echo ""

# Verify authentication
echo "Checking Google Cloud authentication..."
AUTH_CHECK=$(gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>/dev/null)

if [ -n "$AUTH_CHECK" ]; then
    echo "[OK] Authenticated as: $AUTH_CHECK"
else
    echo "[WARNING] Not authenticated. Run: gcloud auth login"
fi
echo ""

# Start the agent
echo "Starting deployment agent on http://localhost:8000"
echo "Press Ctrl+C to stop"
echo ""

adk web --port 8000

