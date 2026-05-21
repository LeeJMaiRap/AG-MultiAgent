# Backup và Recreate Docker Container cho OpenClaw Gateway
# Chạy script này từ PowerShell/CMD trên máy Windows

# Cấu hình
$CONTAINER_NAME = "openclawgateway"
$BACKUP_NAME = "${CONTAINER_NAME}-backup-$(Get-Date -Format 'yyyy-MM-dd-HH-mm-ss')"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Backup và Recreate Docker Container" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Container name: $CONTAINER_NAME" -ForegroundColor Yellow
Write-Host "Backup name: $BACKUP_NAME" -ForegroundColor Yellow
Write-Host ""

# Bước 1: Backup container thành image
Write-Host "Bước 1: Backup container thành image..." -ForegroundColor Green
docker commit $CONTAINER_NAME "${CONTAINER_NAME}:backup-$(Get-Date -Format 'yyyy-MM-dd')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Lỗi khi backup container!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Backup image thành công: ${CONTAINER_NAME}:backup-$(Get-Date -Format 'yyyy-MM-dd')" -ForegroundColor Green
Write-Host ""

# Bước 2: Export container thành file
Write-Host "Bước 2: Export container thành file..." -ForegroundColor Green
docker export $CONTAINER_NAME > "${BACKUP_NAME}.tar"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Lỗi khi export container!" -ForegroundColor Red
    exit 1
}
$FILE_SIZE = (Get-Item "${BACKUP_NAME}.tar").Length / 1MB
Write-Host "✓ Export thành công: ${BACKUP_NAME}.tar (${ROUND($FILE_SIZE, 2)} MB)" -ForegroundColor Green
Write-Host ""

# Bước 3: Kiểm tra backup
Write-Host "Bước 3: Kiểm tra backup..." -ForegroundColor Green
Write-Host "Docker images:" -ForegroundColor White
docker images | Select-String $CONTAINER_NAME
Write-Host ""
Write-Host "Backup files:" -ForegroundColor White
Get-ChildItem "${BACKUP_NAME}.*" | Format-Table Name, Length
Write-Host ""

# Bước 4: Stop container
Write-Host "Bước 4: Stop container..." -ForegroundColor Green
docker stop $CONTAINER_NAME
if ($LASTEXITCODE -ne 0) {
    Write-Host "Lỗi khi stop container!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Container đã stop" -ForegroundColor Green
Write-Host ""

# Bước 5: Xóa container
Write-Host "Bước 5: Xóa container..." -ForegroundColor Green
docker rm $CONTAINER_NAME
if ($LASTEXITCODE -ne 0) {
    Write-Host "Lỗi khi xóa container!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Container đã xóa" -ForegroundColor Green
Write-Host ""

# Bước 6: Chạy lại container với port mapping mới
Write-Host "Bước 6: Chạy lại container với port mapping..." -ForegroundColor Green
docker run -d `
  --name $CONTAINER_NAME `
  -p 22:22 `
  -p 18789:18789 `
  -p 3000:3000 `
  -p 5000:5000 `
  "${CONTAINER_NAME}:backup-$(Get-Date -Format 'yyyy-MM-dd')"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Lỗi khi chạy container mới!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Container đã chạy lại với port mapping mới" -ForegroundColor Green
Write-Host ""

# Bước 7: Kiểm tra container
Write-Host "Bước 7: Kiểm tra container..." -ForegroundColor Green
docker ps | Select-String $CONTAINER_NAME
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Hoàn tất!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Frontend: http://localhost:3000" -ForegroundColor White
Write-Host "Backend: http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "Backup files đã lưu tại:" -ForegroundColor White
Write-Host "  - ${BACKUP_NAME}.tar" -ForegroundColor Gray
Write-Host "  - Image: ${CONTAINER_NAME}:backup-$(Get-Date -Format 'yyyy-MM-dd')" -ForegroundColor Gray
Write-Host ""
