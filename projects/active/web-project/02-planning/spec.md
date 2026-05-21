# Technical Architecture & API Contract — Ứng dụng Thanh toán Nhanh

> Trạng thái: **Draft v0.1 — cần PM xác nhận tên dự án và đường dẫn lưu file trước khi khóa API Contract**  
> Phạm vi dựa trên PRD hiện tại: mobile/web app thanh toán nhanh với ví nội bộ, QR payment, chuyển tiền nội bộ, OTP, PIN giao dịch, admin portal MVP.

---

## 1. Assumptions tạm thời

Do PRD chưa chốt các thông tin PM yêu cầu, bản thiết kế này dùng các giả định sau:

| Hạng mục | Giả định |
|---|---|
| Tên dự án | `quickpay` |
| Nền tảng | Mobile app + Admin web portal |
| Tiền tệ | `VND` |
| Ví nội bộ | Có |
| QR payment | Có |
| Liên kết ngân hàng | Không trong MVP |
| KYC nâng cao | Không trong MVP |
| Admin portal | Có |
| Auth user | Email/số điện thoại + password + OTP |
| Xác thực giao dịch | Transaction PIN 6 số |
| Idempotency | Bắt buộc với API tạo/xác nhận giao dịch |
| API version | `/api/v1` |

---

## 2. Kiến trúc hệ thống đề xuất

## 2.1. High-level Architecture

```text
Client Mobile/Web
   |
   | HTTPS REST API
   v
API Gateway / Backend API
   |
   +-- Auth Service
   +-- User Service
   +-- Wallet Service
   +-- Transaction Service
   +-- QR Payment Service
   +-- Notification Service
   +-- Admin Service
   +-- Audit Log Service
   |
   +-- PostgreSQL
   +-- Redis
   +-- Message Queue / Job Queue
   +-- Object Storage for receipt export, optional
```

---

## 2.2. Core Modules

### 2.2.1. Authentication & Authorization

Chịu trách nhiệm:

- Đăng ký.
- Đăng nhập.
- Refresh token.
- Logout.
- OTP verification.
- Role-based access control.

Roles:

```text
USER
MERCHANT
ADMIN
SUPPORT
```

MVP có thể dùng:

```text
USER
ADMIN
```

---

### 2.2.2. User Management

Chịu trách nhiệm:

- Hồ sơ người dùng.
- Trạng thái xác thực.
- Trạng thái tài khoản.
- Tìm kiếm người nhận theo phone/email/user code.

---

### 2.2.3. Wallet Service

Chịu trách nhiệm:

- Tạo ví khi user được tạo.
- Quản lý số dư khả dụng.
- Quản lý số dư tạm giữ nếu có.
- Đảm bảo cập nhật số dư atomic.

---

### 2.2.4. Transaction Service

Chịu trách nhiệm:

- Tạo giao dịch.
- Xác nhận giao dịch bằng PIN.
- Chuyển tiền nội bộ.
- Ghi transaction ledger.
- Đảm bảo idempotency.
- Đảm bảo rollback hoặc trạng thái `PROCESSING` khi lỗi.

---

### 2.2.5. QR Payment Service

Chịu trách nhiệm:

- Decode QR payload.
- Validate QR.
- Trả thông tin người nhận/merchant.
- Xử lý QR có fixed amount hoặc dynamic amount.

---

### 2.2.6. Notification Service

Chịu trách nhiệm:

- Lưu notification trong app.
- Gửi push notification nếu tích hợp.
- Không chứa thông tin nhạy cảm.

---

### 2.2.7. Admin Service

Chịu trách nhiệm:

- Admin login.
- Quản lý user.
- Tra cứu transaction.
- Ghi audit log.

---

### 2.2.8. Audit Log Service

Chịu trách nhiệm ghi log:

- Login/logout.
- Tạo giao dịch.
- Xác nhận giao dịch.
- Admin action.
- User status change.

---

## 3. Data Model

## 3.1. users

```sql
users (
  id UUID PRIMARY KEY,
  full_name VARCHAR(255) NOT NULL,
  phone VARCHAR(30) UNIQUE,
  email VARCHAR(255) UNIQUE,
  password_hash TEXT NOT NULL,
  status VARCHAR(30) NOT NULL, -- ACTIVE, LOCKED, UNVERIFIED
  is_phone_verified BOOLEAN DEFAULT false,
  is_email_verified BOOLEAN DEFAULT false,
  role VARCHAR(30) NOT NULL DEFAULT 'USER',
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)
```

---

## 3.2. wallets

```sql
wallets (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  available_balance BIGINT NOT NULL DEFAULT 0,
  held_balance BIGINT NOT NULL DEFAULT 0,
  currency CHAR(3) NOT NULL DEFAULT 'VND',
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,
  UNIQUE(user_id, currency)
)
```

> Tiền nên lưu bằng integer minor unit. Với VND, `1000` nghĩa là `1.000 ₫`.

---

## 3.3. transaction_pins

```sql
transaction_pins (
  user_id UUID PRIMARY KEY REFERENCES users(id),
  pin_hash TEXT NOT NULL,
  failed_attempts INT NOT NULL DEFAULT 0,
  locked_until TIMESTAMP NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)
```

---

## 3.4. otp_requests

```sql
otp_requests (
  id UUID PRIMARY KEY,
  user_id UUID NULL REFERENCES users(id),
  destination VARCHAR(255) NOT NULL,
  channel VARCHAR(20) NOT NULL, -- SMS, EMAIL
  purpose VARCHAR(50) NOT NULL, -- REGISTER, LOGIN, RESET_PIN
  otp_hash TEXT NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  verified_at TIMESTAMP NULL,
  failed_attempts INT NOT NULL DEFAULT 0,
  resend_available_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP NOT NULL
)
```

---

## 3.5. transactions

```sql
transactions (
  id UUID PRIMARY KEY,
  reference_id VARCHAR(64) UNIQUE NOT NULL,
  type VARCHAR(40) NOT NULL, -- TRANSFER, QR_PAYMENT
  sender_user_id UUID NULL REFERENCES users(id),
  receiver_user_id UUID NULL REFERENCES users(id),
  merchant_id UUID NULL,
  amount BIGINT NOT NULL,
  fee BIGINT NOT NULL DEFAULT 0,
  total_amount BIGINT NOT NULL,
  currency CHAR(3) NOT NULL DEFAULT 'VND',
  status VARCHAR(30) NOT NULL,
  description TEXT NULL,
  failure_reason TEXT NULL,
  idempotency_key VARCHAR(128) NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,
  completed_at TIMESTAMP NULL,
  UNIQUE(sender_user_id, idempotency_key)
)
```

---

## 3.6. wallet_ledger_entries

```sql
wallet_ledger_entries (
  id UUID PRIMARY KEY,
  wallet_id UUID NOT NULL REFERENCES wallets(id),
  transaction_id UUID NOT NULL REFERENCES transactions(id),
  direction VARCHAR(10) NOT NULL, -- DEBIT, CREDIT
  amount BIGINT NOT NULL,
  balance_after BIGINT NOT NULL,
  currency CHAR(3) NOT NULL DEFAULT 'VND',
  created_at TIMESTAMP NOT NULL
)
```

---

## 3.7. qr_codes

```sql
qr_codes (
  id UUID PRIMARY KEY,
  owner_user_id UUID NULL REFERENCES users(id),
  merchant_id UUID NULL,
  qr_type VARCHAR(30) NOT NULL, -- USER_PAYMENT, MERCHANT_PAYMENT
  payload TEXT NOT NULL,
  fixed_amount BIGINT NULL,
  currency CHAR(3) NOT NULL DEFAULT 'VND',
  status VARCHAR(20) NOT NULL, -- ACTIVE, INACTIVE, EXPIRED
  expires_at TIMESTAMP NULL,
  created_at TIMESTAMP NOT NULL
)
```

---

## 3.8. notifications

```sql
notifications (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  type VARCHAR(50) NOT NULL,
  title VARCHAR(255) NOT NULL,
  body TEXT NOT NULL,
  data JSONB NULL,
  read_at TIMESTAMP NULL,
  created_at TIMESTAMP NOT NULL
)
```

---

## 3.9. audit_logs

```sql
audit_logs (
  id UUID PRIMARY KEY,
  actor_id UUID NULL,
  actor_type VARCHAR(30) NOT NULL, -- USER, ADMIN, SYSTEM
  action VARCHAR(100) NOT NULL,
  target_type VARCHAR(50) NULL,
  target_id UUID NULL,
  result VARCHAR(20) NOT NULL, -- SUCCESS, FAILED
  ip_address VARCHAR(64) NULL,
  user_agent TEXT NULL,
  metadata JSONB NULL,
  created_at TIMESTAMP NOT NULL
)
```

---

## 4. Transaction State Machine

```text
PENDING -> PROCESSING
PENDING -> CANCELLED
PENDING -> FAILED

PROCESSING -> SUCCESS
PROCESSING -> FAILED

SUCCESS -> REFUNDED

FAILED, REFUNDED, CANCELLED = terminal states
```

---

## 5. API Conventions

## 5.1. Base URL

```text
/api/v1
```

---

## 5.2. Authentication Header

```http
Authorization: Bearer <access_token>
```

---

## 5.3. Idempotency Header

Bắt buộc với API tạo hoặc xác nhận giao dịch:

```http
Idempotency-Key: <unique-client-generated-key>
```

Ví dụ:

```text
Idempotency-Key: 01HZPAYREQ8T6X4MF6QQS2ADZ4
```

---

## 5.4. Common Success Response

```json
{
  "success": true,
  "data": {},
  "meta": {}
}
```

---

## 5.5. Common Error Response

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": []
  }
}
```

---

## 5.6. Common HTTP Status Codes

| Status | Meaning |
|---|---|
| `200` | Thành công |
| `201` | Tạo mới thành công |
| `202` | Đã nhận xử lý |
| `400` | Request không hợp lệ |
| `401` | Chưa xác thực |
| `403` | Không có quyền |
| `404` | Không tìm thấy |
| `409` | Conflict/idempotency duplicated |
| `422` | Business validation failed |
| `423` | Tài khoản/PIN/OTP đang bị khóa |
| `429` | Rate limit |
| `500` | Lỗi hệ thống |

---

# 6. API Contract

---

# 6.1. Auth APIs

## 6.1.1. Register

```http
POST /api/v1/auth/register
```

### Request

```json
{
  "fullName": "Nguyen Van A",
  "phone": "0912345678",
  "email": "a@example.com",
  "password": "Password123"
}
```

### Rules

- `phone` hoặc `email` bắt buộc có ít nhất một.
- `password` tối thiểu 8 ký tự.
- Nếu phone/email đã tồn tại trả `409`.

### Response `201`

```json
{
  "success": true,
  "data": {
    "userId": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
    "fullName": "Nguyen Van A",
    "phone": "0912345678",
    "email": "a@example.com",
    "status": "UNVERIFIED",
    "otpRequired": true
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `400` | `VALIDATION_ERROR` | Dữ liệu không hợp lệ |
| `409` | `ACCOUNT_EXISTS` | Tài khoản đã tồn tại |

---

## 6.1.2. Login

```http
POST /api/v1/auth/login
```

### Request

```json
{
  "identifier": "0912345678",
  "password": "Password123"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "accessToken": "jwt_access_token",
    "refreshToken": "jwt_refresh_token",
    "expiresIn": 900,
    "user": {
      "id": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
      "fullName": "Nguyen Van A",
      "role": "USER",
      "status": "ACTIVE",
      "hasTransactionPin": true
    }
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `401` | `INVALID_CREDENTIALS` | Email/số điện thoại hoặc mật khẩu không đúng |
| `423` | `ACCOUNT_LOCKED` | Tài khoản đang bị khóa |

---

## 6.1.3. Refresh Token

```http
POST /api/v1/auth/refresh
```

### Request

```json
{
  "refreshToken": "jwt_refresh_token"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "accessToken": "new_jwt_access_token",
    "refreshToken": "new_jwt_refresh_token",
    "expiresIn": 900
  }
}
```

---

## 6.1.4. Logout

```http
POST /api/v1/auth/logout
```

### Headers

```http
Authorization: Bearer <access_token>
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "loggedOut": true
  }
}
```

---

# 6.2. OTP APIs

## 6.2.1. Request OTP

```http
POST /api/v1/otp/request
```

### Request

```json
{
  "destination": "0912345678",
  "channel": "SMS",
  "purpose": "REGISTER"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "otpRequestId": "8d7d7dd7-f079-41d4-a7a8-222222222222",
    "expiresIn": 300,
    "resendAvailableIn": 60
  }
}
```

---

## 6.2.2. Verify OTP

```http
POST /api/v1/otp/verify
```

### Request

```json
{
  "otpRequestId": "8d7d7dd7-f079-41d4-a7a8-222222222222",
  "otpCode": "123456"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "verified": true
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `400` | `INVALID_OTP` | Mã OTP không đúng |
| `400` | `OTP_EXPIRED` | Mã OTP đã hết hạn |
| `423` | `OTP_LOCKED` | Bạn đã nhập sai quá số lần cho phép |

---

# 6.3. User APIs

## 6.3.1. Get Current User

```http
GET /api/v1/me
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "id": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
    "fullName": "Nguyen Van A",
    "phone": "0912345678",
    "email": "a@example.com",
    "status": "ACTIVE",
    "isPhoneVerified": true,
    "isEmailVerified": false,
    "hasTransactionPin": true,
    "createdAt": "2026-05-21T10:00:00Z"
  }
}
```

---

## 6.3.2. Resolve Recipient

Dùng khi chuyển tiền nội bộ.

```http
GET /api/v1/users/resolve-recipient?identifier=0912345679
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "userId": "9f65bd31-a343-4a86-8c90-333333333333",
    "displayName": "Tran Thi B",
    "maskedPhone": "091***5679",
    "maskedEmail": "b***@example.com"
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `404` | `RECIPIENT_NOT_FOUND` | Không tìm thấy người nhận |
| `422` | `SELF_TRANSFER_NOT_ALLOWED` | Không thể chuyển tiền cho chính mình |

---

# 6.4. Transaction PIN APIs

## 6.4.1. Setup Transaction PIN

```http
POST /api/v1/me/transaction-pin
```

### Request

```json
{
  "pin": "135790",
  "confirmPin": "135790"
}
```

### Response `201`

```json
{
  "success": true,
  "data": {
    "hasTransactionPin": true
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `400` | `PIN_MISMATCH` | PIN xác nhận không khớp |
| `422` | `WEAK_PIN` | PIN không được sử dụng vì quá dễ đoán |

---

## 6.4.2. Change Transaction PIN

```http
PUT /api/v1/me/transaction-pin
```

### Request

```json
{
  "currentPin": "135790",
  "newPin": "246801",
  "confirmNewPin": "246801"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "changed": true
  }
}
```

---

# 6.5. Wallet APIs

## 6.5.1. Get Wallet Balance

```http
GET /api/v1/wallet
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "walletId": "0bf82b5b-1194-43e2-9b48-444444444444",
    "availableBalance": 1000000,
    "heldBalance": 0,
    "currency": "VND",
    "updatedAt": "2026-05-21T10:00:00Z"
  }
}
```

---

## 6.5.2. Get Home Summary

```http
GET /api/v1/wallet/home-summary
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "wallet": {
      "availableBalance": 1000000,
      "currency": "VND"
    },
    "recentTransactions": [
      {
        "id": "3b593b5e-3f6b-4182-b10f-555555555555",
        "referenceId": "QP202605210001",
        "type": "TRANSFER",
        "direction": "OUT",
        "amount": 50000,
        "status": "SUCCESS",
        "counterpartyName": "Tran Thi B",
        "createdAt": "2026-05-21T10:00:00Z"
      }
    ]
  }
}
```

---

# 6.6. QR APIs

## 6.6.1. Decode QR

```http
POST /api/v1/qr/decode
```

### Request

```json
{
  "qrPayload": "quickpay://pay?receiverId=9f65bd31-a343-4a86-8c90-333333333333&amount=50000&type=USER_PAYMENT"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "valid": true,
    "qrType": "USER_PAYMENT",
    "receiver": {
      "id": "9f65bd31-a343-4a86-8c90-333333333333",
      "displayName": "Tran Thi B",
      "type": "USER"
    },
    "amount": 50000,
    "currency": "VND",
    "isAmountEditable": false,
    "minAmount": 1000,
    "maxAmount": 50000000
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `400` | `INVALID_QR` | Mã QR không hợp lệ |
| `410` | `QR_EXPIRED` | Mã QR đã hết hạn |

---

# 6.7. Transaction APIs

## 6.7.1. Create Transfer Transaction

Tạo giao dịch chuyển tiền nội bộ ở trạng thái `PENDING`.

```http
POST /api/v1/transactions/transfers
```

### Headers

```http
Authorization: Bearer <access_token>
Idempotency-Key: <unique-key>
```

### Request

```json
{
  "receiverUserId": "9f65bd31-a343-4a86-8c90-333333333333",
  "amount": 50000,
  "currency": "VND",
  "description": "An trua"
}
```

### Response `201`

```json
{
  "success": true,
  "data": {
    "transactionId": "3b593b5e-3f6b-4182-b10f-555555555555",
    "referenceId": "QP202605210001",
    "type": "TRANSFER",
    "status": "PENDING",
    "sender": {
      "id": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
      "displayName": "Nguyen Van A"
    },
    "receiver": {
      "id": "9f65bd31-a343-4a86-8c90-333333333333",
      "displayName": "Tran Thi B"
    },
    "amount": 50000,
    "fee": 0,
    "totalAmount": 50000,
    "currency": "VND",
    "description": "An trua",
    "createdAt": "2026-05-21T10:00:00Z"
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `400` | `VALIDATION_ERROR` | Dữ liệu không hợp lệ |
| `404` | `RECIPIENT_NOT_FOUND` | Không tìm thấy người nhận |
| `422` | `MIN_AMOUNT_NOT_MET` | Số tiền tối thiểu là 1.000 ₫ |
| `422` | `MAX_AMOUNT_EXCEEDED` | Số tiền vượt quá hạn mức |
| `422` | `SELF_TRANSFER_NOT_ALLOWED` | Không thể chuyển tiền cho chính mình |
| `409` | `IDEMPOTENCY_CONFLICT` | Idempotency key đã được sử dụng với nội dung khác |

---

## 6.7.2. Create QR Payment Transaction

```http
POST /api/v1/transactions/qr-payments
```

### Headers

```http
Authorization: Bearer <access_token>
Idempotency-Key: <unique-key>
```

### Request

```json
{
  "qrPayload": "quickpay://pay?receiverId=9f65bd31-a343-4a86-8c90-333333333333&type=USER_PAYMENT",
  "amount": 50000,
  "currency": "VND",
  "description": "Thanh toan QR"
}
```

### Response `201`

```json
{
  "success": true,
  "data": {
    "transactionId": "d51c8538-102e-4b67-8e66-666666666666",
    "referenceId": "QP202605210002",
    "type": "QR_PAYMENT",
    "status": "PENDING",
    "receiver": {
      "id": "9f65bd31-a343-4a86-8c90-333333333333",
      "displayName": "Tran Thi B",
      "type": "USER"
    },
    "amount": 50000,
    "fee": 0,
    "totalAmount": 50000,
    "currency": "VND",
    "description": "Thanh toan QR",
    "createdAt": "2026-05-21T10:00:00Z"
  }
}
```

---

## 6.7.3. Confirm Transaction with PIN

Thực thi trừ/cộng tiền. Bắt buộc idempotency.

```http
POST /api/v1/transactions/{transactionId}/confirm
```

### Headers

```http
Authorization: Bearer <access_token>
Idempotency-Key: <unique-key>
```

### Request

```json
{
  "pin": "135790"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "transactionId": "3b593b5e-3f6b-4182-b10f-555555555555",
    "referenceId": "QP202605210001",
    "status": "SUCCESS",
    "amount": 50000,
    "fee": 0,
    "totalAmount": 50000,
    "currency": "VND",
    "completedAt": "2026-05-21T10:00:03Z"
  }
}
```

### Possible Response `202`

Khi giao dịch cần xử lý bất đồng bộ:

```json
{
  "success": true,
  "data": {
    "transactionId": "3b593b5e-3f6b-4182-b10f-555555555555",
    "referenceId": "QP202605210001",
    "status": "PROCESSING",
    "message": "Giao dịch đang được xử lý"
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `400` | `INVALID_PIN` | PIN không đúng |
| `403` | `TRANSACTION_FORBIDDEN` | Bạn không có quyền xác nhận giao dịch này |
| `404` | `TRANSACTION_NOT_FOUND` | Không tìm thấy giao dịch |
| `422` | `INSUFFICIENT_BALANCE` | Số dư không đủ |
| `422` | `PIN_NOT_SET` | Bạn chưa thiết lập PIN giao dịch |
| `423` | `PIN_LOCKED` | PIN đang bị khóa do nhập sai quá số lần |
| `409` | `TRANSACTION_ALREADY_PROCESSED` | Giao dịch đã được xử lý |

---

## 6.7.4. Get Transaction History

```http
GET /api/v1/transactions?status=SUCCESS&type=TRANSFER&fromDate=2026-05-01&toDate=2026-05-21&page=1&pageSize=20
```

### Response `200`

```json
{
  "success": true,
  "data": [
    {
      "id": "3b593b5e-3f6b-4182-b10f-555555555555",
      "referenceId": "QP202605210001",
      "type": "TRANSFER",
      "direction": "OUT",
      "amount": 50000,
      "fee": 0,
      "totalAmount": 50000,
      "currency": "VND",
      "status": "SUCCESS",
      "counterparty": {
        "id": "9f65bd31-a343-4a86-8c90-333333333333",
        "displayName": "Tran Thi B"
      },
      "createdAt": "2026-05-21T10:00:00Z",
      "completedAt": "2026-05-21T10:00:03Z"
    }
  ],
  "meta": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 1,
    "totalPages": 1
  }
}
```

---

## 6.7.5. Get Transaction Detail

```http
GET /api/v1/transactions/{transactionId}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "id": "3b593b5e-3f6b-4182-b10f-555555555555",
    "referenceId": "QP202605210001",
    "type": "TRANSFER",
    "status": "SUCCESS",
    "amount": 50000,
    "fee": 0,
    "totalAmount": 50000,
    "currency": "VND",
    "description": "An trua",
    "sender": {
      "id": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
      "displayName": "Nguyen Van A"
    },
    "receiver": {
      "id": "9f65bd31-a343-4a86-8c90-333333333333",
      "displayName": "Tran Thi B"
    },
    "createdAt": "2026-05-21T10:00:00Z",
    "updatedAt": "2026-05-21T10:00:03Z",
    "completedAt": "2026-05-21T10:00:03Z"
  }
}
```

### Errors

| Status | Code | Message |
|---|---|---|
| `403` | `TRANSACTION_FORBIDDEN` | Không có quyền truy cập giao dịch |
| `404` | `TRANSACTION_NOT_FOUND` | Không tìm thấy giao dịch |

---

# 6.8. Receipt APIs

## 6.8.1. Get Receipt

```http
GET /api/v1/transactions/{transactionId}/receipt
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "transactionId": "3b593b5e-3f6b-4182-b10f-555555555555",
    "referenceId": "QP202605210001",
    "status": "SUCCESS",
    "amount": 50000,
    "currency": "VND",
    "receiverName": "Tran Thi B",
    "senderName": "Nguyen Van A",
    "completedAt": "2026-05-21T10:00:03Z",
    "appName": "QuickPay"
  }
}
```

---

# 6.9. Notification APIs

## 6.9.1. List Notifications

```http
GET /api/v1/notifications?page=1&pageSize=20
```

### Response `200`

```json
{
  "success": true,
  "data": [
    {
      "id": "e13c9cf1-cdd4-4b66-9041-777777777777",
      "type": "TRANSACTION_SUCCESS",
      "title": "Giao dịch thành công",
      "body": "Bạn đã chuyển 50.000 ₫ cho Tran Thi B",
      "readAt": null,
      "createdAt": "2026-05-21T10:00:03Z"
    }
  ],
  "meta": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 1,
    "totalPages": 1
  }
}
```

---

## 6.9.2. Mark Notification as Read

```http
PATCH /api/v1/notifications/{notificationId}/read
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "read": true
  }
}
```

---

# 6.10. Admin APIs

> Tất cả endpoint admin yêu cầu role `ADMIN`.

---

## 6.10.1. Admin Login

```http
POST /api/v1/admin/auth/login
```

### Request

```json
{
  "email": "admin@example.com",
  "password": "AdminPassword123"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "accessToken": "admin_jwt_access_token",
    "refreshToken": "admin_jwt_refresh_token",
    "expiresIn": 900,
    "admin": {
      "id": "a5a6d27c-0000-4a8e-9999-888888888888",
      "email": "admin@example.com",
      "role": "ADMIN",
      "lastLoginAt": "2026-05-21T09:00:00Z"
    }
  }
}
```

---

## 6.10.2. List Users

```http
GET /api/v1/admin/users?query=0912345678&status=ACTIVE&page=1&pageSize=20
```

### Response `200`

```json
{
  "success": true,
  "data": [
    {
      "id": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
      "fullName": "Nguyen Van A",
      "phone": "0912345678",
      "email": "a@example.com",
      "status": "ACTIVE",
      "createdAt": "2026-05-21T10:00:00Z"
    }
  ],
  "meta": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 1,
    "totalPages": 1
  }
}
```

---

## 6.10.3. Get User Detail

```http
GET /api/v1/admin/users/{userId}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "id": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
    "fullName": "Nguyen Van A",
    "phone": "0912345678",
    "email": "a@example.com",
    "status": "ACTIVE",
    "isPhoneVerified": true,
    "isEmailVerified": false,
    "wallet": {
      "availableBalance": 1000000,
      "heldBalance": 0,
      "currency": "VND"
    },
    "createdAt": "2026-05-21T10:00:00Z"
  }
}
```

---

## 6.10.4. Update User Status

```http
PATCH /api/v1/admin/users/{userId}/status
```

### Request

```json
{
  "status": "LOCKED",
  "reason": "Suspected fraud"
}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "userId": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
    "status": "LOCKED"
  }
}
```

---

## 6.10.5. List Transactions for Admin

```http
GET /api/v1/admin/transactions?query=QP202605210001&status=SUCCESS&type=TRANSFER&fromDate=2026-05-01&toDate=2026-05-21&page=1&pageSize=20
```

### Response `200`

```json
{
  "success": true,
  "data": [
    {
      "id": "3b593b5e-3f6b-4182-b10f-555555555555",
      "referenceId": "QP202605210001",
      "type": "TRANSFER",
      "senderName": "Nguyen Van A",
      "receiverName": "Tran Thi B",
      "amount": 50000,
      "fee": 0,
      "totalAmount": 50000,
      "currency": "VND",
      "status": "SUCCESS",
      "createdAt": "2026-05-21T10:00:00Z",
      "completedAt": "2026-05-21T10:00:03Z"
    }
  ],
  "meta": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 1,
    "totalPages": 1
  }
}
```

---

## 6.10.6. Get Transaction Detail for Admin

```http
GET /api/v1/admin/transactions/{transactionId}
```

### Response `200`

```json
{
  "success": true,
  "data": {
    "id": "3b593b5e-3f6b-4182-b10f-555555555555",
    "referenceId": "QP202605210001",
    "type": "TRANSFER",
    "status": "SUCCESS",
    "amount": 50000,
    "fee": 0,
    "totalAmount": 50000,
    "currency": "VND",
    "sender": {
      "id": "5e01a7b3-d6ff-4d6b-9c7c-111111111111",
      "fullName": "Nguyen Van A",
      "phone": "0912345678"
    },
    "receiver": {
      "id": "9f65bd31-a343-4a86-8c90-333333333333",
      "fullName": "Tran Thi B",
      "phone": "0912345679"
    },
    "description": "An trua",
    "failureReason": null,
    "createdAt": "2026-05-21T10:00:00Z",
    "updatedAt": "2026-05-21T10:00:03Z",
    "completedAt": "2026-05-21T10:00:03Z"
  }
}
```

---

# 7. Enums

## 7.1. User Status

```text
ACTIVE
LOCKED
UNVERIFIED
```

---

## 7.2. User Role

```text
USER
MERCHANT
ADMIN
SUPPORT
```

---

## 7.3. Transaction Type

```text
TRANSFER
QR_PAYMENT
```

---

## 7.4. Transaction Status

```text
PENDING
PROCESSING
SUCCESS
FAILED
REFUNDED
CANCELLED
```

---

## 7.5. Notification Type

```text
TRANSACTION_SUCCESS
TRANSACTION_FAILED
TRANSACTION_PROCESSING
MONEY_RECEIVED
SYSTEM
```

---

## 7.6. OTP Purpose

```text
REGISTER
LOGIN
RESET_PASSWORD
RESET_PIN
```

---

## 7.7. OTP Channel

```text
SMS
EMAIL
```

---

# 8. Critical Business Rules

## 8.1. Payment Limits

```text
MIN_TRANSACTION_AMOUNT = 1000 VND
MAX_TRANSACTION_AMOUNT = 50000000 VND
```

---

## 8.2. PIN Rules

PIN phải:

- Đúng 6 chữ số.
- Không thuộc danh sách dễ đoán:

```text
000000
111111
123456
654321
```

- Không lưu plain text.
- Hash bằng thuật toán mạnh như Argon2id hoặc bcrypt.

---

## 8.3. OTP Rules

```text
OTP length: 6 digits
TTL: 5 minutes
Max failed attempts: 5
Lock duration: 10 minutes
Resend cooldown: 60 seconds
```

---

## 8.4. Idempotency Rules

Áp dụng cho:

```text
POST /transactions/transfers
POST /transactions/qr-payments
POST /transactions/{transactionId}/confirm
```

Quy tắc:

1. Nếu cùng `Idempotency-Key` và cùng request body: trả lại response cũ.
2. Nếu cùng `Idempotency-Key` nhưng khác request body: trả `409 IDEMPOTENCY_CONFLICT`.
3. Idempotency key nên lưu tối thiểu 24 giờ.
4. Không xử lý trừ tiền hai lần cho cùng một giao dịch.

---

## 8.5. Wallet Consistency Rules

Khi confirm giao dịch thành công:

1. Lock wallet người gửi.
2. Kiểm tra số dư.
3. Trừ `totalAmount` khỏi ví người gửi.
4. Cộng `amount` vào ví người nhận.
5. Ghi ledger debit.
6. Ghi ledger credit.
7. Update transaction status `SUCCESS`.
8. Commit transaction DB.
9. Publish notification async.

Tất cả bước tài chính nên nằm trong cùng DB transaction nếu là chuyển tiền nội bộ.

---

# 9. Security Requirements

- HTTPS bắt buộc.
- Password hash bằng Argon2id/bcrypt.
- PIN hash bằng Argon2id/bcrypt.
- OTP chỉ lưu hash.
- Access token TTL ngắn, ví dụ 15 phút.
- Refresh token TTL dài hơn, ví dụ 7–30 ngày.
- Không log:
  - Password.
  - PIN.
  - OTP.
  - Access token.
  - Refresh token.
- Rate limit:
  - Login.
  - OTP request.
  - OTP verify.
  - PIN confirm.
  - Transaction confirm.
- Admin APIs bắt buộc RBAC.
- Audit log mọi hành động nhạy cảm.
- API thanh toán bắt buộc `Idempotency-Key`.

---

# 10. Đề xuất folder/file cần lưu

Sau khi PM xác nhận tên dự án, nên lưu tài liệu này tại:

```text
projects/active/[project-name]/02-planning/technical-architecture-and-api-contract.md
```

Ví dụ nếu project là `quickpay`:

```text
projects/active/quickpay/02-planning/technical-architecture-and-api-contract.md
```

---

# 11. Open Questions cần PM xác nhận trước khi khóa API

1. Tên dự án chính thức là gì?
2. Đường dẫn folder dự án chính thức?
3. MVP có cần merchant account riêng không, hay merchant chỉ là user thường?
4. Có cần nạp tiền ví trong MVP không?  
   Hiện PRD có ví nội bộ nhưng chưa có luồng top-up.
5. Số dư ví ban đầu lấy từ đâu trong MVP/testing?
6. Admin có được khóa/mở khóa user trong MVP không?
7. Receipt có cần export PDF trong MVP không, hay chỉ hiển thị dữ liệu?
8. QR format có theo chuẩn nội bộ `quickpay://...` hay chuẩn quốc gia/ngân hàng?
9. Có yêu cầu đa ngôn ngữ không?
10. Có cần webhook/payment gateway ở MVP không?

---

## 12. Kết luận

Bản contract trên đủ để Backend và Frontend bắt đầu alignment ở mức draft. Tuy nhiên **chưa nên khóa API** cho đến khi PM xác nhận các thông tin còn thiếu, đặc biệt:

```text
Tên dự án
Đường dẫn file planning
Nền tảng
Merchant scope
Top-up scope
QR format
Admin scope
```

Sau khi PM xác nhận, tôi sẽ chuẩn hóa thành bản **API Contract v1.0 Locked** để handoff cho Backend Agent và Frontend Agent.