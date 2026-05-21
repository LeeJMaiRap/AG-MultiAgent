Mình đã nhận PRD và API Contract draft cho **ứng dụng thanh toán nhanh / QuickPay**.

Hiện tại với vai trò **Frontend Agent**, mình có thể bắt đầu thiết kế/triển khai UI theo các màn hình đã liệt kê, nhưng **chưa thể tạo/sửa file** vì còn thiếu thông tin bắt buộc về dự án frontend và phạm vi owned paths.

## Cần bạn cung cấp thêm để mình triển khai

Vui lòng xác nhận các thông tin sau:

```text
Tên dự án:
Đường dẫn thư mục frontend:
Framework frontend: React / Next.js / Vue / Angular / React Native / Flutter / khác
Package manager: npm / yarn / pnpm
Owned Paths frontend được phép sửa:
Có sẵn source code chưa: Có / Không
Có design file/mockup không: Có / Không
Có cần mock API khi backend chưa sẵn sàng không: Có / Không
Scope frontend MVP cần làm ngay:
- User app web/mobile?
- Admin portal?
- Cả hai?
```

Ví dụ:

```text
Tên dự án: quickpay
Đường dẫn thư mục frontend: C:\projects\quickpay\frontend
Framework frontend: React + Vite + TypeScript
Package manager: npm
Owned Paths frontend được phép sửa:
- frontend/src/**
- frontend/public/**
- frontend/package.json
Có sẵn source code chưa: Có
Có design file/mockup không: Không
Có cần mock API khi backend chưa sẵn sàng không: Có
Scope frontend MVP cần làm ngay: User web app + Admin portal
```

## Đề xuất phạm vi frontend MVP

Dựa trên PRD/API Contract, mình đề xuất chia frontend thành 2 phần:

### 1. User App

Các màn hình chính:

1. Đăng ký
2. Đăng nhập
3. Xác thực OTP
4. Thiết lập PIN giao dịch
5. Trang chủ ví
6. Quét QR / nhập QR payload giả lập nếu web không có camera
7. Nhập số tiền
8. Xác nhận thanh toán
9. Nhập PIN
10. Kết quả giao dịch
11. Biên nhận
12. Chuyển tiền
13. Lịch sử giao dịch
14. Chi tiết giao dịch
15. Thông báo

### 2. Admin Portal

Các màn hình chính:

1. Admin login
2. Admin dashboard
3. Danh sách người dùng
4. Chi tiết người dùng
5. Danh sách giao dịch
6. Chi tiết giao dịch
7. Cập nhật trạng thái user nếu nằm trong MVP

## API frontend sẽ tích hợp

Mình sẽ tích hợp đúng theo contract:

### Auth

```text
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
```

### OTP

```text
POST /api/v1/otp/request
POST /api/v1/otp/verify
```

### User / Wallet

```text
GET /api/v1/me
GET /api/v1/wallet
GET /api/v1/wallet/home-summary
```

### PIN

```text
POST /api/v1/me/transaction-pin
PUT /api/v1/me/transaction-pin
```

### QR

```text
POST /api/v1/qr/decode
```

### Transaction

```text
POST /api/v1/transactions/transfers
POST /api/v1/transactions/qr-payments
POST /api/v1/transactions/{transactionId}/confirm
GET /api/v1/transactions
GET /api/v1/transactions/{transactionId}
GET /api/v1/transactions/{transactionId}/receipt
```

### Notification

```text
GET /api/v1/notifications
PATCH /api/v1/notifications/{notificationId}/read
```

### Admin

```text
POST /api/v1/admin/auth/login
GET /api/v1/admin/users
GET /api/v1/admin/users/{userId}
PATCH /api/v1/admin/users/{userId}/status
GET /api/v1/admin/transactions
GET /api/v1/admin/transactions/{transactionId}
```

## Lưu ý kỹ thuật frontend

Khi có source path, mình sẽ triển khai theo các nguyên tắc:

- Không sửa backend/API contract.
- Tách rõ API client/service layer.
- Không log token, PIN, OTP.
- Tự động đính kèm `Authorization: Bearer <accessToken>`.
- Tạo `Idempotency-Key` cho:
  - Tạo giao dịch chuyển tiền.
  - Tạo giao dịch QR.
  - Confirm giao dịch.
- Validate form phía client theo PRD:
  - Password tối thiểu 8 ký tự.
  - OTP đúng 6 chữ số.
  - PIN đúng 6 chữ số.
  - Chặn PIN yếu: `000000`, `111111`, `123456`, `654321`.
  - Số tiền tối thiểu `1.000 ₫`.
  - Số tiền tối đa `50.000.000 ₫`.
- Format tiền tệ VND dạng: `1.000.000 ₫`.
- Hiển thị lỗi đúng message từ contract nếu có.

## Trạng thái hiện tại

Chưa thể bắt đầu sửa file vì thiếu:

1. Đường dẫn thư mục frontend.
2. Framework/package manager.
3. Owned Paths được phép sửa.
4. Xác nhận scope user app/admin portal.
5. Trạng thái backend: API thật đã có hay cần mock.

Sau khi bạn cung cấp các thông tin trên, mình sẽ bắt đầu triển khai frontend và báo cáo kèm bằng chứng kiểm tra như:

```text
npm install OK
npm run build OK
npm run dev live
Console không có lỗi runtime nghiêm trọng
Các route/màn hình chính đã hoạt động
```