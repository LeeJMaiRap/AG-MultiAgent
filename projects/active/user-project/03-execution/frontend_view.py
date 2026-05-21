Tôi sẽ kiểm tra cấu trúc dự án frontend hiện có, sau đó triển khai UI React theo contract và chạy build để xác minh.Mình chưa thể triển khai trực tiếp vì trong phiên làm việc này không có quyền truy cập filesystem/terminal của dự án để xem và sửa file.

Để mình tiếp tục đúng vai trò Frontend Agent, bạn vui lòng cung cấp một trong các thông tin sau:

1. Cấu trúc thư mục hiện tại của `projects/active/quickpay/`, đặc biệt frontend nằm ở đâu, ví dụ:
   ```txt
   projects/active/quickpay/frontend/
   projects/active/quickpay/client/
   projects/active/quickpay/
   ```

2. Hoặc cấp môi trường có tool thao tác file/terminal.

Khi có quyền thao tác, mình sẽ triển khai phần frontend theo PRD/API contract gồm:

- Auth:
  - Register
  - Login
  - Logout
  - Auth guard theo JWT
- User:
  - Dashboard ví
  - Chuyển tiền
  - Tạo QR nhận tiền
  - Thanh toán bằng QR payload
  - Lịch sử giao dịch
- Admin:
  - Dashboard admin
  - Danh sách user
  - Chi tiết user
  - Danh sách giao dịch
- API client dùng đúng base `/api` và các endpoint đã khóa.
- Lưu token ở frontend.
- Điều hướng theo role `USER` / `ADMIN`.
- UI responsive cơ bản.
- Chạy kiểm tra:
  - `npm install` nếu cần
  - `npm run build`
  - báo lại bằng chứng build/dev server thành công.