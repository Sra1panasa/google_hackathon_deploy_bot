# Startup script for deployment agent
# Sets environment and starts the agent

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Deployment Automation Agent - Startup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Set environment variables
$env:GOOGLE_CLOUD_PROJECT = "mbs-graphrag"
$env:GOOGLE_CLOUD_LOCATION = "europe-west2"

Write-Host "Environment Configuration:" -ForegroundColor Yellow
Write-Host "   Project: $env:GOOGLE_CLOUD_PROJECT"
Write-Host "   Location: $env:GOOGLE_CLOUD_LOCATION"
Write-Host ""

# Verify authentication
Write-Host "Checking Google Cloud authentication..." -ForegroundColor Yellow
$authCheck = gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>$null

if ($authCheck) {
    Write-Host "[OK] Authenticated as: $authCheck" -ForegroundColor Green
} else {
    Write-Host "[WARNING] Not authenticated. Run: gcloud auth login" -ForegroundColor Yellow
}
Write-Host ""

# Start the agent
Write-Host "Starting deployment agent on http://localhost:8000" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

adk web --port 8000

