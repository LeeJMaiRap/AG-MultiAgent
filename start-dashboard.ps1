# PowerShell script to start the Agent Wall Chat FastAPI Dashboard (Windows Native)
# Run this script to start the Web preview locally on Windows

$scriptPath = Join-Path $PSScriptRoot "scripts\web_wall_chat.py"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Starting Agent Wall Chat Web-Teams (FastAPI)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Script Location: $scriptPath" -ForegroundColor Yellow

if (!(Test-Path $scriptPath)) {
    Write-Host "Error: Web-Teams script not found at $scriptPath" -ForegroundColor Red
    exit 1
}

# Automatically launch the web browser in background after 1.5s
Write-Host "Preparing to launch web browser at http://localhost:20130 ..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoProfile -Command Start-Sleep -Milliseconds 1500; Start-Process 'http://localhost:20130'" -WindowStyle Hidden

# Launch FastAPI server
Write-Host "Launching FastAPI Server on http://localhost:20130..." -ForegroundColor Green
python "$scriptPath"
