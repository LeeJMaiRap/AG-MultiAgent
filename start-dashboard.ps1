# PowerShell script to start the Agent Wall Chat Dashboard
# Run this script to start the Web preview locally on Windows

$appDir = Join-Path $PSScriptRoot "apps\agent-wall-chat"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Starting Agent Wall Chat Dashboard (Windows Native)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Application Directory: $appDir" -ForegroundColor Yellow

if (!(Test-Path $appDir)) {
    Write-Host "Error: Application directory not found at $appDir" -ForegroundColor Red
    exit 1
}

# Navigate to app directory
Push-Location $appDir

# Check node_modules
if (!(Test-Path "node_modules")) {
    Write-Host "node_modules not found. Installing dependencies (npm install)..." -ForegroundColor Yellow
    npm install
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: npm install failed. Please ensure Node.js is installed." -ForegroundColor Red
        Pop-Location
        exit 1
    }
    Write-Host "Success: Installed dependencies." -ForegroundColor Green
}

# Automatically launch the web browser in background after 1.5s
Write-Host "Preparing to launch web browser at http://localhost:20129 ..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoProfile -Command Start-Sleep -Milliseconds 1500; Start-Process 'http://localhost:20129'" -WindowStyle Hidden

# Launch server
Write-Host "Launching server (http://localhost:20129)..." -ForegroundColor Green
npm start

Pop-Location
