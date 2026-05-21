# PowerShell script to start the Agent Wall Chat Dashboard
# Chạy script này để khởi chạy giao diện Web preview cục bộ trên Windows

$appDir = Join-Path $PSScriptRoot "apps\agent-wall-chat"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Starting Agent Wall Chat Dashboard (Windows Native)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Thư mục ứng dụng: $appDir" -ForegroundColor Yellow

if (!(Test-Path $appDir)) {
    Write-Host "Lỗi: Không tìm thấy thư mục ứng dụng tại $appDir" -ForegroundColor Red
    exit 1
}

# Di chuyển vào thư mục app
Push-Location $appDir

# Kiểm tra node_modules
if (!(Test-Path "node_modules")) {
    Write-Host "Không tìm thấy node_modules. Đang tiến hành cài đặt dependencies (npm install)..." -ForegroundColor Yellow
    npm install
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Lỗi: Không thể chạy npm install. Vui lòng kiểm tra xem Node.js đã được cài đặt chưa." -ForegroundColor Red
        Pop-Location
        exit 1
    }
    Write-Host "✓ Đã cài đặt dependencies thành công." -ForegroundColor Green
}

# Khởi chạy server
Write-Host "Khởi chạy server (http://localhost:20129)..." -ForegroundColor Green
npm start

Pop-Location
