# Technical Architecture & API Contract — Web QuickPay MVP

**Project folder:** `projects/active/quickpay/`  
**Recommended spec file:** `projects/active/quickpay/02-planning/spec.md`  
**Stack:** React + Express + SQLite + JWT  
**Initial wallet balance:** `1,000,000 VND`, stored as integer `1000000`

---

# 1. Architecture Overview

## 1.1. System Components

```txt
React Frontend
   |
   | HTTPS/HTTP JSON API
   v
Express Backend API
   |
   | SQLite queries
   v
SQLite Database
```

## 1.2. Main Modules

### Frontend

- Authentication pages:
  - Register
  - Login
- User pages:
  - Dashboard
  - Transfer money
  - Generate QR
  - Pay by QR payload
  - Transaction history
- Admin pages:
  - Admin dashboard
  - User list
  - User detail
  - Transaction list

### Backend

- Auth module
- User module
- Wallet module
- Transaction module
- QR/payment module
- Admin module
- JWT authentication middleware
- Role-based authorization middleware

---

# 2. Core Business Rules

## 2.1. User Registration

When a user registers:

1. Create user with role `USER`.
2. Hash password with bcrypt.
3. Create default wallet.
4. Set wallet balance to `1000000`.
5. Generate unique wallet code.

## 2.2. Wallet Balance

- Balance is stored as integer VND.
- Balance must never be negative.
- Every successful transfer updates two wallets:
  - Sender balance decreases.
  - Receiver balance increases.
- Failed transfers must not mutate wallet balances.

## 2.3. Transfer Rules

A transfer is rejected if:

- Sender is same as receiver.
- Amount is less than or equal to `0`.
- Sender balance is insufficient.
- Receiver cannot be found.
- Receiver wallet is inactive or missing.

## 2.4. QR Payment MVP

QR payload is a JSON string encoded as QR.

Example payload:

```json
{
  "type": "QUICKPAY_QR",
  "receiverWalletCode": "QP123456789",
  "amount": 50000,
  "note": "Lunch payment"
}
```

For MVP:

- Backend generates the QR payload.
- Frontend may render QR image using a QR library.
- User can paste QR payload manually to pay.
- Camera scanning is optional and out of MVP scope.

---

# 3. Roles

```txt
USER
ADMIN
```

## 3.1. USER Permissions

- Register/login.
- View own profile.
- View own wallet.
- View own dashboard.
- Transfer money.
- Generate QR receive payload.
- Pay by QR payload.
- View own transaction history.

## 3.2. ADMIN Permissions

- Login.
- View admin dashboard.
- View all users.
- View user detail.
- View all transactions.
- Search/filter users and transactions.

---

# 4. Data Model

## 4.1. Entity Relationship

```txt
users 1---1 wallets
users 1---N transactions as sender
users 1---N transactions as receiver
```

---

## 4.2. Table: `users`

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PK, auto increment | User ID |
| `full_name` | TEXT | NOT NULL | Full name |
| `email` | TEXT | UNIQUE, NOT NULL | Login email |
| `password_hash` | TEXT | NOT NULL | Bcrypt hash |
| `role` | TEXT | NOT NULL, default `USER` | `USER` or `ADMIN` |
| `status` | TEXT | NOT NULL, default `ACTIVE` | `ACTIVE`, `LOCKED` |
| `created_at` | TEXT | NOT NULL | ISO datetime |
| `updated_at` | TEXT | NOT NULL | ISO datetime |

---

## 4.3. Table: `wallets`

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PK, auto increment | Wallet ID |
| `user_id` | INTEGER | FK users.id, UNIQUE, NOT NULL | Owner |
| `wallet_code` | TEXT | UNIQUE, NOT NULL | Public receiver code |
| `balance` | INTEGER | NOT NULL, default `1000000` | VND integer |
| `status` | TEXT | NOT NULL, default `ACTIVE` | `ACTIVE`, `LOCKED` |
| `created_at` | TEXT | NOT NULL | ISO datetime |
| `updated_at` | TEXT | NOT NULL | ISO datetime |

---

## 4.4. Table: `transactions`

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PK, auto increment | Transaction ID |
| `transaction_code` | TEXT | UNIQUE, NOT NULL | Public transaction code |
| `sender_user_id` | INTEGER | FK users.id, NOT NULL | Sender |
| `receiver_user_id` | INTEGER | FK users.id, NOT NULL | Receiver |
| `sender_wallet_id` | INTEGER | FK wallets.id, NOT NULL | Sender wallet |
| `receiver_wallet_id` | INTEGER | FK wallets.id, NOT NULL | Receiver wallet |
| `amount` | INTEGER | NOT NULL | VND integer |
| `note` | TEXT | Nullable | Transfer note |
| `status` | TEXT | NOT NULL | `SUCCESS`, `FAILED` |
| `failure_reason` | TEXT | Nullable | Failure reason |
| `type` | TEXT | NOT NULL | `TRANSFER`, `QR_PAYMENT` |
| `created_at` | TEXT | NOT NULL | ISO datetime |

---

# 5. API Conventions

## 5.1. Base URL

```txt
/api
```

Example:

```txt
http://localhost:3000/api/auth/login
```

---

## 5.2. Auth Header

Protected endpoints require:

```http
Authorization: Bearer <jwt_token>
```

---

## 5.3. Standard Success Response

```json
{
  "success": true,
  "data": {}
}
```

---

## 5.4. Standard Error Response

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message"
  }
}
```

---

## 5.5. Common HTTP Status Codes

| Status | Meaning |
|---|---|
| `200` | OK |
| `201` | Created |
| `400` | Bad request or validation error |
| `401` | Unauthorized or invalid token |
| `403` | Forbidden |
| `404` | Resource not found |
| `409` | Conflict, e.g. duplicated email |
| `422` | Business rule violation |
| `500` | Internal server error |

---

# 6. API Contract

---

# 6.1. Auth APIs

## 6.1.1. Register

```http
POST /api/auth/register
```

### Request Body

```json
{
  "fullName": "Nguyen Van A",
  "email": "user@example.com",
  "password": "Password123"
}
```

### Validation

| Field | Rule |
|---|---|
| `fullName` | Required, 2-100 chars |
| `email` | Required, valid email, unique |
| `password` | Required, min 6 chars |

### Success Response `201`

```json
{
  "success": true,
  "data": {
    "user": {
      "id": 1,
      "fullName": "Nguyen Van A",
      "email": "user@example.com",
      "role": "USER",
      "status": "ACTIVE",
      "createdAt": "2026-05-21T10:00:00.000Z"
    },
    "wallet": {
      "id": 1,
      "walletCode": "QP123456789",
      "balance": 1000000,
      "status": "ACTIVE"
    }
  }
}
```

### Error Responses

#### `409` Email already exists

```json
{
  "success": false,
  "error": {
    "code": "EMAIL_ALREADY_EXISTS",
    "message": "Email already exists"
  }
}
```

#### `400` Validation error

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid registration data"
  }
}
```

---

## 6.1.2. Login

```http
POST /api/auth/login
```

### Request Body

```json
{
  "email": "user@example.com",
  "password": "Password123"
}
```

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "token": "jwt_token_here",
    "user": {
      "id": 1,
      "fullName": "Nguyen Van A",
      "email": "user@example.com",
      "role": "USER",
      "status": "ACTIVE"
    }
  }
}
```

### Error Responses

#### `401`

```json
{
  "success": false,
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Invalid email or password"
  }
}
```

#### `403`

```json
{
  "success": false,
  "error": {
    "code": "ACCOUNT_LOCKED",
    "message": "Account is locked"
  }
}
```

---

## 6.1.3. Get Current User

```http
GET /api/auth/me
```

### Auth

Required.

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "user": {
      "id": 1,
      "fullName": "Nguyen Van A",
      "email": "user@example.com",
      "role": "USER",
      "status": "ACTIVE",
      "createdAt": "2026-05-21T10:00:00.000Z"
    },
    "wallet": {
      "id": 1,
      "walletCode": "QP123456789",
      "balance": 1000000,
      "status": "ACTIVE"
    }
  }
}
```

---

## 6.1.4. Logout

JWT logout is handled on the frontend by deleting the token.

Optional backend endpoint:

```http
POST /api/auth/logout
```

### Auth

Required.

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "message": "Logged out successfully"
  }
}
```

---

# 6.2. User Wallet APIs

## 6.2.1. Get My Wallet

```http
GET /api/wallet/me
```

### Auth

Required, `USER` or `ADMIN`.

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "wallet": {
      "id": 1,
      "walletCode": "QP123456789",
      "balance": 1000000,
      "status": "ACTIVE",
      "createdAt": "2026-05-21T10:00:00.000Z"
    }
  }
}
```

---

## 6.2.2. Get User Dashboard

```http
GET /api/dashboard/me
```

### Auth

Required, `USER`.

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "balance": 950000,
    "walletCode": "QP123456789",
    "totalSent": 100000,
    "totalReceived": 50000,
    "recentTransactions": [
      {
        "id": 10,
        "transactionCode": "TXN202605210001",
        "type": "TRANSFER",
        "direction": "SENT",
        "amount": 50000,
        "note": "Coffee",
        "status": "SUCCESS",
        "counterparty": {
          "id": 2,
          "fullName": "Tran Thi B",
          "email": "b@example.com",
          "walletCode": "QP987654321"
        },
        "createdAt": "2026-05-21T11:00:00.000Z"
      }
    ]
  }
}
```

---

# 6.3. Transfer APIs

## 6.3.1. Transfer Money

```http
POST /api/transfers
```

### Auth

Required, `USER`.

### Request Body

At least one receiver identifier is required: `receiverEmail` or `receiverWalletCode`.

```json
{
  "receiverEmail": "receiver@example.com",
  "receiverWalletCode": "QP987654321",
  "amount": 50000,
  "note": "Lunch payment"
}
```

### Validation

| Field | Rule |
|---|---|
| `receiverEmail` | Optional if `receiverWalletCode` is provided |
| `receiverWalletCode` | Optional if `receiverEmail` is provided |
| `amount` | Required, integer, greater than `0` |
| `note` | Optional, max 255 chars |

### Success Response `201`

```json
{
  "success": true,
  "data": {
    "transaction": {
      "id": 10,
      "transactionCode": "TXN202605210001",
      "type": "TRANSFER",
      "amount": 50000,
      "note": "Lunch payment",
      "status": "SUCCESS",
      "sender": {
        "id": 1,
        "fullName": "Nguyen Van A",
        "email": "user@example.com",
        "walletCode": "QP123456789"
      },
      "receiver": {
        "id": 2,
        "fullName": "Tran Thi B",
        "email": "receiver@example.com",
        "walletCode": "QP987654321"
      },
      "createdAt": "2026-05-21T11:00:00.000Z"
    },
    "wallet": {
      "balance": 950000
    }
  }
}
```

### Error Responses

#### `404` Receiver not found

```json
{
  "success": false,
  "error": {
    "code": "RECEIVER_NOT_FOUND",
    "message": "Receiver not found"
  }
}
```

#### `422` Insufficient balance

```json
{
  "success": false,
  "error": {
    "code": "INSUFFICIENT_BALANCE",
    "message": "Insufficient balance"
  }
}
```

#### `422` Cannot transfer to self

```json
{
  "success": false,
  "error": {
    "code": "CANNOT_TRANSFER_TO_SELF",
    "message": "Cannot transfer money to yourself"
  }
}
```

#### `400` Invalid amount

```json
{
  "success": false,
  "error": {
    "code": "INVALID_AMOUNT",
    "message": "Amount must be greater than 0"
  }
}
```

---

# 6.4. QR APIs

## 6.4.1. Generate QR Receive Payload

```http
POST /api/qr/generate
```

### Auth

Required, `USER`.

### Request Body

```json
{
  "amount": 50000,
  "note": "Payment request"
}
```

### Notes

- `amount` is optional.
- `note` is optional.
- If amount is not included, payer must enter amount manually before paying.

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "payload": {
      "type": "QUICKPAY_QR",
      "receiverWalletCode": "QP123456789",
      "amount": 50000,
      "note": "Payment request"
    },
    "payloadString": "{\"type\":\"QUICKPAY_QR\",\"receiverWalletCode\":\"QP123456789\",\"amount\":50000,\"note\":\"Payment request\"}"
  }
}
```

---

## 6.4.2. Parse QR Payload

```http
POST /api/qr/parse
```

### Auth

Required, `USER`.

### Request Body

```json
{
  "payloadString": "{\"type\":\"QUICKPAY_QR\",\"receiverWalletCode\":\"QP123456789\",\"amount\":50000,\"note\":\"Payment request\"}"
}
```

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "payload": {
      "type": "QUICKPAY_QR",
      "receiverWalletCode": "QP123456789",
      "amount": 50000,
      "note": "Payment request"
    },
    "receiver": {
      "id": 1,
      "fullName": "Nguyen Van A",
      "email": "user@example.com",
      "walletCode": "QP123456789"
    }
  }
}
```

### Error Response `400`

```json
{
  "success": false,
  "error": {
    "code": "INVALID_QR_PAYLOAD",
    "message": "Invalid QR payload"
  }
}
```

---

## 6.4.3. Pay by QR Payload

```http
POST /api/qr/pay
```

### Auth

Required, `USER`.

### Request Body

```json
{
  "payloadString": "{\"type\":\"QUICKPAY_QR\",\"receiverWalletCode\":\"QP987654321\",\"amount\":50000,\"note\":\"Payment request\"}",
  "amount": 50000,
  "note": "Payment request"
}
```

### Notes

- If QR payload contains `amount`, backend should use the payload amount.
- If QR payload does not contain `amount`, request body `amount` is required.
- Request `note` may override or supplement payload note, depending on implementation. For MVP, use request `note` if provided; otherwise use payload `note`.

### Success Response `201`

```json
{
  "success": true,
  "data": {
    "transaction": {
      "id": 11,
      "transactionCode": "TXN202605210002",
      "type": "QR_PAYMENT",
      "amount": 50000,
      "note": "Payment request",
      "status": "SUCCESS",
      "sender": {
        "id": 2,
        "fullName": "Tran Thi B",
        "email": "payer@example.com",
        "walletCode": "QP222222222"
      },
      "receiver": {
        "id": 1,
        "fullName": "Nguyen Van A",
        "email": "receiver@example.com",
        "walletCode": "QP987654321"
      },
      "createdAt": "2026-05-21T11:05:00.000Z"
    },
    "wallet": {
      "balance": 900000
    }
  }
}
```

### Error Responses

Same as transfer:

- `INVALID_QR_PAYLOAD`
- `RECEIVER_NOT_FOUND`
- `INVALID_AMOUNT`
- `INSUFFICIENT_BALANCE`
- `CANNOT_TRANSFER_TO_SELF`

---

# 6.5. Transaction APIs

## 6.5.1. Get My Transactions

```http
GET /api/transactions/me
```

### Auth

Required, `USER`.

### Query Params

| Param | Type | Required | Description |
|---|---|---|---|
| `direction` | string | No | `ALL`, `SENT`, `RECEIVED` |
| `status` | string | No | `SUCCESS`, `FAILED` |
| `type` | string | No | `TRANSFER`, `QR_PAYMENT` |
| `fromDate` | string | No | ISO date |
| `toDate` | string | No | ISO date |
| `page` | number | No | Default `1` |
| `limit` | number | No | Default `20`, max `100` |

### Example

```http
GET /api/transactions/me?direction=ALL&status=SUCCESS&page=1&limit=20
```

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": 10,
        "transactionCode": "TXN202605210001",
        "type": "TRANSFER",
        "direction": "SENT",
        "amount": 50000,
        "note": "Lunch payment",
        "status": "SUCCESS",
        "failureReason": null,
        "counterparty": {
          "id": 2,
          "fullName": "Tran Thi B",
          "email": "receiver@example.com",
          "walletCode": "QP987654321"
        },
        "createdAt": "2026-05-21T11:00:00.000Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "totalItems": 1,
      "totalPages": 1
    }
  }
}
```

---

## 6.5.2. Get Transaction Detail

```http
GET /api/transactions/:transactionId
```

### Auth

Required.

### Authorization

- `USER`: can only view own related transactions.
- `ADMIN`: can view all transactions.

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "transaction": {
      "id": 10,
      "transactionCode": "TXN202605210001",
      "type": "TRANSFER",
      "amount": 50000,
      "note": "Lunch payment",
      "status": "SUCCESS",
      "failureReason": null,
      "sender": {
        "id": 1,
        "fullName": "Nguyen Van A",
        "email": "user@example.com",
        "walletCode": "QP123456789"
      },
      "receiver": {
        "id": 2,
        "fullName": "Tran Thi B",
        "email": "receiver@example.com",
        "walletCode": "QP987654321"
      },
      "createdAt": "2026-05-21T11:00:00.000Z"
    }
  }
}
```

---

# 6.6. Admin APIs

All admin APIs require:

```txt
Role: ADMIN
```

---

## 6.6.1. Admin Dashboard

```http
GET /api/admin/dashboard
```

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "totalUsers": 100,
    "totalTransactions": 250,
    "totalSuccessfulTransactionValue": 12500000,
    "recentTransactions": [
      {
        "id": 10,
        "transactionCode": "TXN202605210001",
        "type": "TRANSFER",
        "amount": 50000,
        "status": "SUCCESS",
        "sender": {
          "id": 1,
          "fullName": "Nguyen Van A",
          "email": "user@example.com"
        },
        "receiver": {
          "id": 2,
          "fullName": "Tran Thi B",
          "email": "receiver@example.com"
        },
        "createdAt": "2026-05-21T11:00:00.000Z"
      }
    ]
  }
}
```

---

## 6.6.2. Get Users

```http
GET /api/admin/users
```

### Query Params

| Param | Type | Required | Description |
|---|---|---|---|
| `search` | string | No | Search by name/email |
| `status` | string | No | `ACTIVE`, `LOCKED` |
| `role` | string | No | `USER`, `ADMIN` |
| `page` | number | No | Default `1` |
| `limit` | number | No | Default `20`, max `100` |

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": 1,
        "fullName": "Nguyen Van A",
        "email": "user@example.com",
        "role": "USER",
        "status": "ACTIVE",
        "wallet": {
          "walletCode": "QP123456789",
          "balance": 950000,
          "status": "ACTIVE"
        },
        "createdAt": "2026-05-21T10:00:00.000Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "totalItems": 1,
      "totalPages": 1
    }
  }
}
```

---

## 6.6.3. Get User Detail

```http
GET /api/admin/users/:userId
```

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "user": {
      "id": 1,
      "fullName": "Nguyen Van A",
      "email": "user@example.com",
      "role": "USER",
      "status": "ACTIVE",
      "createdAt": "2026-05-21T10:00:00.000Z",
      "updatedAt": "2026-05-21T10:00:00.000Z"
    },
    "wallet": {
      "id": 1,
      "walletCode": "QP123456789",
      "balance": 950000,
      "status": "ACTIVE"
    },
    "stats": {
      "totalSent": 100000,
      "totalReceived": 50000,
      "transactionCount": 3
    }
  }
}
```

---

## 6.6.4. Get User Transactions

```http
GET /api/admin/users/:userId/transactions
```

### Query Params

Same as `/api/transactions/me`.

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": 10,
        "transactionCode": "TXN202605210001",
        "type": "TRANSFER",
        "direction": "SENT",
        "amount": 50000,
        "note": "Lunch payment",
        "status": "SUCCESS",
        "counterparty": {
          "id": 2,
          "fullName": "Tran Thi B",
          "email": "receiver@example.com",
          "walletCode": "QP987654321"
        },
        "createdAt": "2026-05-21T11:00:00.000Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "totalItems": 1,
      "totalPages": 1
    }
  }
}
```

---

## 6.6.5. Get All Transactions

```http
GET /api/admin/transactions
```

### Query Params

| Param | Type | Required | Description |
|---|---|---|---|
| `search` | string | No | Transaction code/email/name |
| `status` | string | No | `SUCCESS`, `FAILED` |
| `type` | string | No | `TRANSFER`, `QR_PAYMENT` |
| `fromDate` | string | No | ISO date |
| `toDate` | string | No | ISO date |
| `page` | number | No | Default `1` |
| `limit` | number | No | Default `20`, max `100` |

### Success Response `200`

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": 10,
        "transactionCode": "TXN202605210001",
        "type": "TRANSFER",
        "amount": 50000,
        "note": "Lunch payment",
        "status": "SUCCESS",
        "failureReason": null,
        "sender": {
          "id": 1,
          "fullName": "Nguyen Van A",
          "email": "user@example.com",
          "walletCode": "QP123456789"
        },
        "receiver": {
          "id": 2,
          "fullName": "Tran Thi B",
          "email": "receiver@example.com",
          "walletCode": "QP987654321"
        },
        "createdAt": "2026-05-21T11:00:00.000Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "totalItems": 1,
      "totalPages": 1
    }
  }
}
```

---

# 7. SQLite Schema Draft

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'USER',
  status TEXT NOT NULL DEFAULT 'ACTIVE',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE wallets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL UNIQUE,
  wallet_code TEXT NOT NULL UNIQUE,
  balance INTEGER NOT NULL DEFAULT 1000000,
  status TEXT NOT NULL DEFAULT 'ACTIVE',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE transactions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  transaction_code TEXT NOT NULL UNIQUE,
  sender_user_id INTEGER NOT NULL,
  receiver_user_id INTEGER NOT NULL,
  sender_wallet_id INTEGER NOT NULL,
  receiver_wallet_id INTEGER NOT NULL,
  amount INTEGER NOT NULL,
  note TEXT,
  status TEXT NOT NULL,
  failure_reason TEXT,
  type TEXT NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY (sender_user_id) REFERENCES users(id),
  FOREIGN KEY (receiver_user_id) REFERENCES users(id),
  FOREIGN KEY (sender_wallet_id) REFERENCES wallets(id),
  FOREIGN KEY (receiver_wallet_id) REFERENCES wallets(id)
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_wallets_wallet_code ON wallets(wallet_code);
CREATE INDEX idx_transactions_code ON transactions(transaction_code);
CREATE INDEX idx_transactions_sender ON transactions(sender_user_id);
CREATE INDEX idx_transactions_receiver ON transactions(receiver_user_id);
CREATE INDEX idx_transactions_created_at ON transactions(created_at);
```

---

# 8. JWT Payload

Recommended JWT payload:

```json
{
  "sub": 1,
  "email": "user@example.com",
  "role": "USER",
  "iat": 1779367200,
  "exp": 1779453600
}
```

Where:

| Field | Meaning |
|---|---|
| `sub` | User ID |
| `email` | User email |
| `role` | `USER` or `ADMIN` |
| `iat` | Issued at |
| `exp` | Expiration |

Recommended expiration:

```txt
24h
```

---

# 9. Seed Data Recommendation

For MVP development, create one admin account by seed script.

```txt
Email: admin@quickpay.local
Password: Admin123
Role: ADMIN
```

Admin may also have a wallet for consistency, but admin wallet is not required for MVP business flow.

---

# 10. Locked MVP API Contract Summary

The MVP contract includes these endpoint groups:

```txt
Auth:
POST   /api/auth/register
POST   /api/auth/login
GET    /api/auth/me
POST   /api/auth/logout

Wallet/User:
GET    /api/wallet/me
GET    /api/dashboard/me

Transfer:
POST   /api/transfers

QR:
POST   /api/qr/generate
POST   /api/qr/parse
POST   /api/qr/pay

Transactions:
GET    /api/transactions/me
GET    /api/transactions/:transactionId

Admin:
GET    /api/admin/dashboard
GET    /api/admin/users
GET    /api/admin/users/:userId
GET    /api/admin/users/:userId/transactions
GET    /api/admin/transactions
```

This API contract should be considered the baseline for Wave 1 implementation. Any future change to endpoint path, payload shape, response shape, status code, role behavior, or data model should be reviewed and approved before frontend/backend implementation continues.