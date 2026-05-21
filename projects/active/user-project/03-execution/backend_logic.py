I’ll inspect the project structure and implement the backend only under the backend-owned path.{"cmd": "dir"}Mình sẵn sàng triển khai backend cho **QuickPay MVP**, nhưng hiện tại phiên làm việc này **không có quyền truy cập filesystem / terminal / repository tools**, nên mình chưa thể:

- Tạo/sửa file trong thư mục `backend`
- Cài package
- Chạy migration SQLite
- Khởi động Express server
- Test API bằng curl/Postman
- Cung cấp evidence log thực tế

Để tiếp tục đúng vai trò Backend Agent, vui lòng cung cấp một trong các lựa chọn sau:

1. **Bật quyền tool/filesystem/terminal** cho workspace hiện tại; hoặc  
2. Gửi cấu trúc thư mục hiện có của project `quickpay`, đặc biệt là thư mục `backend`; hoặc  
3. Xác nhận cho phép mình trả về một bộ file backend hoàn chỉnh dạng code blocks để bạn copy vào repo.

Khi có quyền thao tác, mình sẽ triển khai trong `backend` בלבד, gồm:

- Express API theo contract:
  - `POST /api/auth/register`
  - `POST /api/auth/login`
  - `GET /api/auth/me`
  - `POST /api/auth/logout`
  - `GET /api/wallet/me`
  - `GET /api/dashboard/me`
  - `POST /api/transfers`
  - `POST /api/qr/generate`
  - `POST /api/qr/parse`
  - `POST /api/qr/pay`
  - `GET /api/transactions/me`
  - `GET /api/transactions/:transactionId`
  - Admin APIs
- SQLite schema:
  - `users`
  - `wallets`
  - `transactions`
- JWT auth middleware
- Role authorization middleware
- bcrypt password hashing
- Seed admin:
  - `admin@quickpay.local`
  - `Admin123`
- Business rules:
  - Initial balance `1000000`
  - Prevent self-transfer
  - Prevent insufficient balance
  - Atomic wallet update inside DB transaction
  - QR payload generation/parse/pay
- Standard response shape:
  - Success: `{ success: true, data: ... }`
  - Error: `{ success: false, error: { code, message } }`
- Evidence after implementation:
  - Server startup log
  - Register/login test
  - Transfer test
  - QR pay test
  - Admin dashboard test