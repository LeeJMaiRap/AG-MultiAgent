# Technical Architecture & API Contract — MVP Bán Hàng Trực Tuyến

> Do chưa có `project-name/project path`, tài liệu này chưa được ghi file. Khi có path, đề xuất lưu tại:  
> `projects/active/[project-name]/02-planning/api-contract.md`

---

## 1. Quyết định kỹ thuật mặc định cho MVP

| Hạng mục | Quyết định |
|---|---|
| Tiền tệ | VND |
| Thanh toán | COD |
| Tài khoản khách hàng | Không có trong MVP |
| Giỏ hàng | Lưu client-side bằng `localStorage` |
| Hình ảnh sản phẩm | Nhập URL ảnh |
| Admin | Một hoặc nhiều tài khoản admin, seed sẵn tài khoản đầu tiên |
| Product category | Không có trong MVP |
| Email xác nhận | Không có trong MVP |
| Tổng tiền đơn hàng | Backend tự tính, không tin client |
| Trừ tồn kho | Khi tạo đơn hàng thành công |
| Hủy đơn hàng | Nếu đơn đã trừ tồn kho, cộng lại tồn kho khi chuyển sang `CANCELLED` |
| Auth admin | Session cookie hoặc JWT HttpOnly cookie. Khuyến nghị HttpOnly cookie cho MVP web app |
| API format | REST JSON |
| DateTime format | ISO 8601 UTC |
| ID format | UUID string khuyến nghị, có thể thay bằng integer nếu stack yêu cầu |

---

## 2. Kiến trúc tổng quan

```text
Frontend Web App
  ├─ Public pages
  │   ├─ Product list
  │   ├─ Product detail
  │   ├─ Cart - localStorage
  │   ├─ Checkout
  │   └─ Order success
  │
  └─ Admin pages
      ├─ Login
      ├─ Product management
      └─ Order management

Backend API
  ├─ Public Product API
  ├─ Public Order API
  ├─ Admin Auth API
  ├─ Admin Product API
  └─ Admin Order API

Database
  ├─ products
  ├─ orders
  ├─ order_items
  └─ admin_users
```

---

## 3. Quy ước API chung

### 3.1 Base URL

```text
/api
```

### 3.2 Content Type

Request:

```http
Content-Type: application/json
```

Response:

```http
Content-Type: application/json
```

### 3.3 Authentication

Admin APIs yêu cầu đăng nhập.

Khuyến nghị dùng HttpOnly cookie:

```http
Cookie: admin_session=...
```

Nếu dùng Bearer token thì:

```http
Authorization: Bearer <token>
```

Contract này ưu tiên cookie-based session để phù hợp website admin MVP.

### 3.4 Response thành công chung

Response trả trực tiếp resource hoặc object bao ngoài tùy endpoint.

Ví dụ:

```json
{
  "id": "prd_123",
  "name": "Áo thun basic"
}
```

Với list:

```json
{
  "items": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "totalItems": 100,
    "totalPages": 5
  }
}
```

### 3.5 Error response chuẩn

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": [
      {
        "field": "customerName",
        "message": "Vui lòng nhập họ tên"
      }
    ]
  }
}
```

### 3.6 HTTP status code chuẩn

| Status | Ý nghĩa |
|---:|---|
| `200` | Thành công |
| `201` | Tạo mới thành công |
| `204` | Thành công, không có body |
| `400` | Request không hợp lệ |
| `401` | Chưa đăng nhập |
| `403` | Không có quyền |
| `404` | Không tìm thấy |
| `409` | Conflict, ví dụ tồn kho không đủ hoặc trạng thái không hợp lệ |
| `422` | Validation error |
| `500` | Lỗi server |

### 3.7 Error codes

| Code | Ý nghĩa |
|---|---|
| `VALIDATION_ERROR` | Dữ liệu đầu vào không hợp lệ |
| `UNAUTHENTICATED` | Chưa đăng nhập |
| `FORBIDDEN` | Không có quyền |
| `NOT_FOUND` | Không tìm thấy resource |
| `INVALID_CREDENTIALS` | Sai email hoặc mật khẩu |
| `INSUFFICIENT_STOCK` | Tồn kho không đủ |
| `INVALID_ORDER_STATUS_TRANSITION` | Chuyển trạng thái đơn hàng không hợp lệ |
| `PRODUCT_NOT_VISIBLE` | Sản phẩm không visible với public API |
| `INTERNAL_ERROR` | Lỗi hệ thống |

---

## 4. Data Model

## 4.1 Product

### Table: `products`

| Field | Type | Required | Constraint |
|---|---|---:|---|
| `id` | string UUID | Yes | Primary key |
| `name` | string | Yes | Not empty |
| `description` | text nullable | No |  |
| `price` | decimal/integer | Yes | `> 0` |
| `imageUrl` | string nullable | No | URL string |
| `stockQuantity` | integer | Yes | `>= 0` |
| `isVisible` | boolean | Yes | Default `true` |
| `createdAt` | datetime | Yes |  |
| `updatedAt` | datetime | Yes |  |

> Khuyến nghị lưu tiền VND bằng integer minor unit, ví dụ `price = 150000`, tránh lỗi floating point.

### Product API shape

```json
{
  "id": "prd_123",
  "name": "Áo thun basic",
  "description": "Áo thun cotton",
  "price": 150000,
  "imageUrl": "https://example.com/image.jpg",
  "stockQuantity": 10,
  "isVisible": true,
  "stockStatus": "IN_STOCK",
  "createdAt": "2026-05-21T10:00:00.000Z",
  "updatedAt": "2026-05-21T10:00:00.000Z"
}
```

`stockStatus` là computed field:

```text
IN_STOCK | OUT_OF_STOCK
```

---

## 4.2 Order

### Table: `orders`

| Field | Type | Required | Constraint |
|---|---|---:|---|
| `id` | string UUID | Yes | Primary key |
| `customerName` | string | Yes | Not empty |
| `customerPhone` | string | Yes | Valid phone |
| `customerEmail` | string nullable | No | Valid email nếu có |
| `shippingAddress` | text | Yes | Not empty |
| `note` | text nullable | No |  |
| `totalAmount` | integer/decimal | Yes | Backend calculated |
| `status` | enum | Yes | Default `NEW` |
| `paymentMethod` | enum | Yes | `COD` |
| `stockRestoredAt` | datetime nullable | No | Set khi hủy đơn và đã hoàn tồn kho |
| `createdAt` | datetime | Yes |  |
| `updatedAt` | datetime | Yes |  |

### Order status enum

Internal values:

```text
NEW
PROCESSING
SHIPPING
COMPLETED
CANCELLED
```

Display labels:

| Internal | Display |
|---|---|
| `NEW` | Mới |
| `PROCESSING` | Đang xử lý |
| `SHIPPING` | Đang giao |
| `COMPLETED` | Hoàn tất |
| `CANCELLED` | Đã hủy |

### Payment method enum

```text
COD
```

---

## 4.3 Order Item

### Table: `order_items`

| Field | Type | Required | Constraint |
|---|---|---:|---|
| `id` | string UUID | Yes | Primary key |
| `orderId` | string UUID | Yes | FK orders.id |
| `productId` | string UUID | Yes | FK products.id |
| `productName` | string | Yes | Snapshot |
| `unitPrice` | integer/decimal | Yes | Snapshot |
| `quantity` | integer | Yes | `>= 1` |
| `lineTotal` | integer/decimal | Yes | `unitPrice * quantity` |
| `createdAt` | datetime | Yes |  |

---

## 4.4 Admin User

### Table: `admin_users`

| Field | Type | Required | Constraint |
|---|---|---:|---|
| `id` | string UUID | Yes | Primary key |
| `email` | string | Yes | Unique |
| `passwordHash` | string | Yes | Hashed |
| `role` | enum/string | Yes | `ADMIN` |
| `createdAt` | datetime | Yes |  |
| `updatedAt` | datetime | Yes |  |

---

## 5. Business Rules

## 5.1 Product Rules

- `name` bắt buộc.
- `price > 0`.
- `stockQuantity >= 0`.
- Public API chỉ trả về sản phẩm `isVisible = true`.
- Admin API trả cả sản phẩm visible và hidden.
- Sản phẩm `stockQuantity = 0` được xem là hết hàng.

## 5.2 Cart Rules

- Cart lưu client-side.
- Cart item chỉ gồm:
  - `productId`
  - `quantity`
- Frontend có thể validate số lượng dựa trên product detail/latest product data.
- Backend vẫn phải kiểm tra tồn kho khi tạo order.

## 5.3 Order Creation Rules

- Client gửi danh sách `items` gồm `productId`, `quantity`.
- Client không gửi `unitPrice`, `lineTotal`, `totalAmount` làm nguồn tin cậy.
- Backend lấy giá hiện tại từ database.
- Backend kiểm tra:
  - Product tồn tại.
  - Product visible.
  - Product có đủ tồn kho.
  - Quantity hợp lệ.
- Nếu hợp lệ:
  - Tạo order.
  - Tạo order items với snapshot `productName`, `unitPrice`.
  - Trừ tồn kho.
  - Tính `totalAmount`.
- Tất cả thao tác phải chạy trong transaction.

## 5.4 Order Status Transition Rules

Allowed transitions:

```text
NEW -> PROCESSING
NEW -> CANCELLED
PROCESSING -> SHIPPING
PROCESSING -> CANCELLED
SHIPPING -> COMPLETED
```

Disallowed examples:

```text
COMPLETED -> NEW
CANCELLED -> COMPLETED
CANCELLED -> NEW
COMPLETED -> CANCELLED
SHIPPING -> CANCELLED
```

> Theo PRD có rule hủy ở `NEW` hoặc `PROCESSING`. Không cho hủy khi `SHIPPING` trong MVP.

### Stock restore rule

- Khi chuyển order sang `CANCELLED`:
  - Nếu order đã được trừ tồn kho lúc tạo.
  - Và `stockRestoredAt` chưa set.
  - Backend cộng lại tồn kho theo order items.
  - Set `stockRestoredAt`.
- Không cộng tồn kho nhiều lần.

---

# 6. API Contract

---

# 6.1 Public Product APIs

## GET `/api/products`

Lấy danh sách sản phẩm visible cho khách hàng.

### Auth

Không yêu cầu.

### Query parameters

| Name | Type | Required | Default | Description |
|---|---|---:|---|---|
| `page` | integer | No | `1` | Trang hiện tại |
| `limit` | integer | No | `20` | Số item mỗi trang, max `100` |

### Request example

```http
GET /api/products?page=1&limit=20
```

### Response `200`

```json
{
  "items": [
    {
      "id": "prd_001",
      "name": "Áo thun basic",
      "description": "Áo thun cotton",
      "price": 150000,
      "imageUrl": "https://example.com/images/ao-thun.jpg",
      "stockQuantity": 10,
      "stockStatus": "IN_STOCK",
      "createdAt": "2026-05-21T10:00:00.000Z",
      "updatedAt": "2026-05-21T10:00:00.000Z"
    },
    {
      "id": "prd_002",
      "name": "Quần jeans",
      "description": "Quần jeans xanh",
      "price": 350000,
      "imageUrl": null,
      "stockQuantity": 0,
      "stockStatus": "OUT_OF_STOCK",
      "createdAt": "2026-05-21T10:00:00.000Z",
      "updatedAt": "2026-05-21T10:00:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "totalItems": 2,
    "totalPages": 1
  }
}
```

### Notes

- Chỉ trả sản phẩm `isVisible = true`.
- Public response có thể không cần trả `isVisible`.

---

## GET `/api/products/{id}`

Lấy chi tiết một sản phẩm visible.

### Auth

Không yêu cầu.

### Path parameters

| Name | Type | Required |
|---|---|---:|
| `id` | string | Yes |

### Request example

```http
GET /api/products/prd_001
```

### Response `200`

```json
{
  "id": "prd_001",
  "name": "Áo thun basic",
  "description": "Áo thun cotton thoáng mát",
  "price": 150000,
  "imageUrl": "https://example.com/images/ao-thun.jpg",
  "stockQuantity": 10,
  "stockStatus": "IN_STOCK",
  "createdAt": "2026-05-21T10:00:00.000Z",
  "updatedAt": "2026-05-21T10:00:00.000Z"
}
```

### Error `404`

Khi product không tồn tại hoặc `isVisible = false`.

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Không tìm thấy sản phẩm"
  }
}
```

---

# 6.2 Public Order APIs

## POST `/api/orders`

Tạo đơn hàng COD từ giỏ hàng client-side.

### Auth

Không yêu cầu.

### Request body

```json
{
  "customerName": "Nguyễn Văn A",
  "customerPhone": "0901234567",
  "customerEmail": "a@example.com",
  "shippingAddress": "123 Nguyễn Trãi, Quận 1, TP.HCM",
  "note": "Giao giờ hành chính",
  "items": [
    {
      "productId": "prd_001",
      "quantity": 2
    },
    {
      "productId": "prd_002",
      "quantity": 1
    }
  ]
}
```

### Validation

| Field | Rule |
|---|---|
| `customerName` | Required, trim not empty |
| `customerPhone` | Required, valid phone |
| `customerEmail` | Optional, valid email if provided |
| `shippingAddress` | Required, trim not empty |
| `note` | Optional |
| `items` | Required, array, min length 1 |
| `items[].productId` | Required |
| `items[].quantity` | Required, integer, `>= 1` |

### Response `201`

```json
{
  "id": "ord_001",
  "customerName": "Nguyễn Văn A",
  "customerPhone": "0901234567",
  "customerEmail": "a@example.com",
  "shippingAddress": "123 Nguyễn Trãi, Quận 1, TP.HCM",
  "note": "Giao giờ hành chính",
  "totalAmount": 650000,
  "status": "NEW",
  "statusLabel": "Mới",
  "paymentMethod": "COD",
  "items": [
    {
      "id": "ori_001",
      "productId": "prd_001",
      "productName": "Áo thun basic",
      "unitPrice": 150000,
      "quantity": 2,
      "lineTotal": 300000
    },
    {
      "id": "ori_002",
      "productId": "prd_002",
      "productName": "Quần jeans",
      "unitPrice": 350000,
      "quantity": 1,
      "lineTotal": 350000
    }
  ],
  "createdAt": "2026-05-21T10:00:00.000Z",
  "updatedAt": "2026-05-21T10:00:00.000Z"
}
```

### Error `422` validation

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": [
      {
        "field": "customerName",
        "message": "Vui lòng nhập họ tên"
      },
      {
        "field": "customerPhone",
        "message": "Số điện thoại không hợp lệ"
      },
      {
        "field": "shippingAddress",
        "message": "Vui lòng nhập địa chỉ giao hàng"
      }
    ]
  }
}
```

### Error `409` insufficient stock

```json
{
  "error": {
    "code": "INSUFFICIENT_STOCK",
    "message": "Một số sản phẩm không đủ tồn kho",
    "details": [
      {
        "productId": "prd_001",
        "productName": "Áo thun basic",
        "requestedQuantity": 5,
        "availableQuantity": 2,
        "message": "Số lượng vượt quá tồn kho"
      }
    ]
  }
}
```

### Error `404` product not found

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Không tìm thấy sản phẩm",
    "details": [
      {
        "productId": "prd_unknown",
        "message": "Sản phẩm không tồn tại"
      }
    ]
  }
}
```

### Important backend behavior

Backend phải dùng transaction:

```text
BEGIN
  Validate customer info
  Validate items
  Lock products rows / ensure atomic stock check
  Check stock
  Create order
  Create order_items
  Decrease products.stockQuantity
COMMIT
```

---

# 6.3 Admin Auth APIs

## POST `/api/admin/login`

Đăng nhập admin.

### Auth

Không yêu cầu.

### Request body

```json
{
  "email": "admin@example.com",
  "password": "password123"
}
```

### Validation

| Field | Rule |
|---|---|
| `email` | Required, email |
| `password` | Required |

### Response `200`

Nếu dùng HttpOnly cookie, response set cookie:

```http
Set-Cookie: admin_session=<session>; HttpOnly; Secure; SameSite=Lax; Path=/
```

Body:

```json
{
  "user": {
    "id": "adm_001",
    "email": "admin@example.com",
    "role": "ADMIN"
  }
}
```

### Error `401`

```json
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Thông tin đăng nhập không chính xác"
  }
}
```

### Error `422`

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": [
      {
        "field": "email",
        "message": "Email không hợp lệ"
      },
      {
        "field": "password",
        "message": "Vui lòng nhập mật khẩu"
      }
    ]
  }
}
```

---

## POST `/api/admin/logout`

Đăng xuất admin.

### Auth

Yêu cầu admin session.

### Request body

Không có.

### Response `204`

Không có body.

### Behavior

- Xóa session server-side nếu có.
- Clear cookie:

```http
Set-Cookie: admin_session=; Max-Age=0; Path=/
```

---

## GET `/api/admin/me`

Kiểm tra session admin hiện tại.

### Auth

Yêu cầu admin session.

### Response `200`

```json
{
  "user": {
    "id": "adm_001",
    "email": "admin@example.com",
    "role": "ADMIN"
  }
}
```

### Error `401`

```json
{
  "error": {
    "code": "UNAUTHENTICATED",
    "message": "Vui lòng đăng nhập"
  }
}
```

---

# 6.4 Admin Product APIs

Tất cả endpoint trong nhóm này yêu cầu admin auth.

---

## GET `/api/admin/products`

Lấy danh sách toàn bộ sản phẩm cho admin.

### Query parameters

| Name | Type | Required | Default | Description |
|---|---|---:|---|---|
| `page` | integer | No | `1` | Trang hiện tại |
| `limit` | integer | No | `20` | Max `100` |
| `q` | string | No |  | Tìm theo tên sản phẩm, P1 |
| `visibility` | string | No | `ALL` | `ALL`, `VISIBLE`, `HIDDEN` |

### Request example

```http
GET /api/admin/products?page=1&limit=20&visibility=ALL
```

### Response `200`

```json
{
  "items": [
    {
      "id": "prd_001",
      "name": "Áo thun basic",
      "description": "Áo thun cotton",
      "price": 150000,
      "imageUrl": "https://example.com/images/ao-thun.jpg",
      "stockQuantity": 10,
      "stockStatus": "IN_STOCK",
      "isVisible": true,
      "createdAt": "2026-05-21T10:00:00.000Z",
      "updatedAt": "2026-05-21T10:00:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "totalItems": 1,
    "totalPages": 1
  }
}
```

---

## POST `/api/admin/products`

Tạo sản phẩm mới.

### Request body

```json
{
  "name": "Áo thun basic",
  "description": "Áo thun cotton",
  "price": 150000,
  "imageUrl": "https://example.com/images/ao-thun.jpg",
  "stockQuantity": 10,
  "isVisible": true
}
```

### Validation

| Field | Rule |
|---|---|
| `name` | Required, trim not empty |
| `description` | Optional |
| `price` | Required, number/integer, `> 0` |
| `imageUrl` | Optional, URL if provided |
| `stockQuantity` | Required, integer, `>= 0` |
| `isVisible` | Required boolean |

### Response `201`

```json
{
  "id": "prd_001",
  "name": "Áo thun basic",
  "description": "Áo thun cotton",
  "price": 150000,
  "imageUrl": "https://example.com/images/ao-thun.jpg",
  "stockQuantity": 10,
  "stockStatus": "IN_STOCK",
  "isVisible": true,
  "createdAt": "2026-05-21T10:00:00.000Z",
  "updatedAt": "2026-05-21T10:00:00.000Z"
}
```

### Error `422`

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": [
      {
        "field": "name",
        "message": "Vui lòng nhập tên sản phẩm"
      },
      {
        "field": "price",
        "message": "Giá bán phải lớn hơn 0"
      },
      {
        "field": "stockQuantity",
        "message": "Tồn kho không được nhỏ hơn 0"
      }
    ]
  }
}
```

---

## GET `/api/admin/products/{id}`

Lấy chi tiết sản phẩm cho admin.

### Path parameters

| Name | Type | Required |
|---|---|---:|
| `id` | string | Yes |

### Response `200`

```json
{
  "id": "prd_001",
  "name": "Áo thun basic",
  "description": "Áo thun cotton",
  "price": 150000,
  "imageUrl": "https://example.com/images/ao-thun.jpg",
  "stockQuantity": 10,
  "stockStatus": "IN_STOCK",
  "isVisible": true,
  "createdAt": "2026-05-21T10:00:00.000Z",
  "updatedAt": "2026-05-21T10:00:00.000Z"
}
```

### Error `404`

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Không tìm thấy sản phẩm"
  }
}
```

---

## PATCH `/api/admin/products/{id}`

Cập nhật sản phẩm.

### Request body

Partial update. Field nào gửi lên thì cập nhật field đó.

```json
{
  "name": "Áo thun basic updated",
  "description": "Mô tả mới",
  "price": 160000,
  "imageUrl": "https://example.com/images/new.jpg",
  "stockQuantity": 5,
  "isVisible": false
}
```

### Validation

Nếu field xuất hiện thì validate:

| Field | Rule |
|---|---|
| `name` | Trim not empty |
| `description` | Nullable/string |
| `price` | Number/integer, `> 0` |
| `imageUrl` | Nullable or valid URL |
| `stockQuantity` | Integer, `>= 0` |
| `isVisible` | Boolean |

### Response `200`

```json
{
  "id": "prd_001",
  "name": "Áo thun basic updated",
  "description": "Mô tả mới",
  "price": 160000,
  "imageUrl": "https://example.com/images/new.jpg",
  "stockQuantity": 5,
  "stockStatus": "IN_STOCK",
  "isVisible": false,
  "createdAt": "2026-05-21T10:00:00.000Z",
  "updatedAt": "2026-05-21T11:00:00.000Z"
}
```

### Error `404`

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Không tìm thấy sản phẩm"
  }
}
```

### Error `422`

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": [
      {
        "field": "price",
        "message": "Giá bán phải lớn hơn 0"
      }
    ]
  }
}
```

---

# 6.5 Admin Order APIs

Tất cả endpoint trong nhóm này yêu cầu admin auth.

---

## GET `/api/admin/orders`

Lấy danh sách đơn hàng.

### Query parameters

| Name | Type | Required | Default | Description |
|---|---|---:|---|---|
| `page` | integer | No | `1` | Trang hiện tại |
| `limit` | integer | No | `20` | Max `100` |
| `status` | string | No |  | `NEW`, `PROCESSING`, `SHIPPING`, `COMPLETED`, `CANCELLED` |

### Request example

```http
GET /api/admin/orders?page=1&limit=20&status=NEW
```

### Response `200`

```json
{
  "items": [
    {
      "id": "ord_001",
      "customerName": "Nguyễn Văn A",
      "customerPhone": "0901234567",
      "totalAmount": 650000,
      "status": "NEW",
      "statusLabel": "Mới",
      "paymentMethod": "COD",
      "createdAt": "2026-05-21T10:00:00.000Z",
      "updatedAt": "2026-05-21T10:00:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "totalItems": 1,
    "totalPages": 1
  }
}
```

---

## GET `/api/admin/orders/{id}`

Lấy chi tiết đơn hàng.

### Path parameters

| Name | Type | Required |
|---|---|---:|
| `id` | string | Yes |

### Response `200`

```json
{
  "id": "ord_001",
  "customerName": "Nguyễn Văn A",
  "customerPhone": "0901234567",
  "customerEmail": "a@example.com",
  "shippingAddress": "123 Nguyễn Trãi, Quận 1, TP.HCM",
  "note": "Giao giờ hành chính",
  "totalAmount": 650000,
  "status": "NEW",
  "statusLabel": "Mới",
  "paymentMethod": "COD",
  "stockRestoredAt": null,
  "items": [
    {
      "id": "ori_001",
      "productId": "prd_001",
      "productName": "Áo thun basic",
      "unitPrice": 150000,
      "quantity": 2,
      "lineTotal": 300000
    },
    {
      "id": "ori_002",
      "productId": "prd_002",
      "productName": "Quần jeans",
      "unitPrice": 350000,
      "quantity": 1,
      "lineTotal": 350000
    }
  ],
  "createdAt": "2026-05-21T10:00:00.000Z",
  "updatedAt": "2026-05-21T10:00:00.000Z"
}
```

### Error `404`

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Không tìm thấy đơn hàng"
  }
}
```

---

## PATCH `/api/admin/orders/{id}/status`

Cập nhật trạng thái đơn hàng.

### Request body

```json
{
  "status": "PROCESSING"
}
```

### Validation

| Field | Rule |
|---|---|
| `status` | Required, one of `NEW`, `PROCESSING`, `SHIPPING`, `COMPLETED`, `CANCELLED` |

### Response `200`

```json
{
  "id": "ord_001",
  "status": "PROCESSING",
  "statusLabel": "Đang xử lý",
  "updatedAt": "2026-05-21T11:00:00.000Z"
}
```

### Error `404`

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Không tìm thấy đơn hàng"
  }
}
```

### Error `409` invalid transition

```json
{
  "error": {
    "code": "INVALID_ORDER_STATUS_TRANSITION",
    "message": "Không thể chuyển đơn hoàn tất về trạng thái mới",
    "details": {
      "currentStatus": "COMPLETED",
      "requestedStatus": "NEW"
    }
  }
}
```

### Error `422`

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": [
      {
        "field": "status",
        "message": "Trạng thái đơn hàng không hợp lệ"
      }
    ]
  }
}
```

### Stock restore behavior on cancellation

Khi request:

```json
{
  "status": "CANCELLED"
}
```

Nếu transition hợp lệ:

- Backend cộng lại tồn kho cho từng item.
- Set `orders.stockRestoredAt`.
- Không restore lại nếu `stockRestoredAt` đã có giá trị.

Response:

```json
{
  "id": "ord_001",
  "status": "CANCELLED",
  "statusLabel": "Đã hủy",
  "stockRestoredAt": "2026-05-21T11:00:00.000Z",
  "updatedAt": "2026-05-21T11:00:00.000Z"
}
```

---

# 7. Frontend Route/API Mapping

## 7.1 Public Routes

| Route | API dùng |
|---|---|
| `/` | `GET /api/products` |
| `/products/:id` | `GET /api/products/:id` |
| `/cart` | `GET /api/products/:id` hoặc dùng product snapshot trong localStorage, khuyến nghị refresh lại product data |
| `/checkout` | Refresh product data, `POST /api/orders` |
| `/order-success/:id` | Dữ liệu có thể lấy từ response tạo order và lưu tạm client-side. MVP chưa có public get order endpoint |

> Nếu cần reload được trang `/order-success/:id`, cần thêm public endpoint `GET /api/orders/:id`. Tuy nhiên endpoint này có rủi ro lộ thông tin đơn hàng. MVP khuyến nghị không thêm, hoặc dùng token tra cứu riêng.

## 7.2 Admin Routes

| Route | API dùng |
|---|---|
| `/admin/login` | `POST /api/admin/login` |
| `/admin` | `GET /api/admin/me` |
| `/admin/products` | `GET /api/admin/products` |
| `/admin/products/new` | `POST /api/admin/products` |
| `/admin/products/:id/edit` | `GET /api/admin/products/:id`, `PATCH /api/admin/products/:id` |
| `/admin/orders` | `GET /api/admin/orders` |
| `/admin/orders/:id` | `GET /api/admin/orders/:id`, `PATCH /api/admin/orders/:id/status` |

---

# 8. LocalStorage Cart Contract

Frontend lưu giỏ hàng theo format:

```json
{
  "items": [
    {
      "productId": "prd_001",
      "quantity": 2
    }
  ],
  "updatedAt": "2026-05-21T10:00:00.000Z"
}
```

Key đề xuất:

```text
mvp_shop_cart
```

Frontend không nên lưu `price` làm nguồn tính tiền cuối cùng. Nếu có lưu để hiển thị nhanh thì phải refresh lại từ API trước checkout.

---

# 9. OpenAPI YAML Draft

```yaml
openapi: 3.0.3
info:
  title: Online Store MVP API
  version: 1.0.0
servers:
  - url: /api

paths:
  /products:
    get:
      summary: List visible products
      tags: [Public Products]
      parameters:
        - in: query
          name: page
          schema:
            type: integer
            default: 1
        - in: query
          name: limit
          schema:
            type: integer
            default: 20
            maximum: 100
      responses:
        "200":
          description: Product list
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ProductListResponse"

  /products/{id}:
    get:
      summary: Get visible product detail
      tags: [Public Products]
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Product detail
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PublicProduct"
        "404":
          $ref: "#/components/responses/NotFound"

  /orders:
    post:
      summary: Create COD order
      tags: [Public Orders]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreateOrderRequest"
      responses:
        "201":
          description: Order created
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/OrderDetail"
        "409":
          description: Insufficient stock
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
        "422":
          $ref: "#/components/responses/ValidationError"

  /admin/login:
    post:
      summary: Admin login
      tags: [Admin Auth]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/AdminLoginRequest"
      responses:
        "200":
          description: Logged in
          headers:
            Set-Cookie:
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AdminMeResponse"
        "401":
          description: Invalid credentials
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"

  /admin/logout:
    post:
      summary: Admin logout
      tags: [Admin Auth]
      security:
        - cookieAuth: []
      responses:
        "204":
          description: Logged out

  /admin/me:
    get:
      summary: Get current admin
      tags: [Admin Auth]
      security:
        - cookieAuth: []
      responses:
        "200":
          description: Current admin
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AdminMeResponse"
        "401":
          $ref: "#/components/responses/Unauthenticated"

  /admin/products:
    get:
      summary: List all products for admin
      tags: [Admin Products]
      security:
        - cookieAuth: []
      parameters:
        - in: query
          name: page
          schema:
            type: integer
            default: 1
        - in: query
          name: limit
          schema:
            type: integer
            default: 20
            maximum: 100
        - in: query
          name: visibility
          schema:
            type: string
            enum: [ALL, VISIBLE, HIDDEN]
            default: ALL
      responses:
        "200":
          description: Product list
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AdminProductListResponse"

    post:
      summary: Create product
      tags: [Admin Products]
      security:
        - cookieAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ProductInput"
      responses:
        "201":
          description: Product created
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AdminProduct"
        "422":
          $ref: "#/components/responses/ValidationError"

  /admin/products/{id}:
    get:
      summary: Get product detail for admin
      tags: [Admin Products]
      security:
        - cookieAuth: []
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Product detail
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AdminProduct"
        "404":
          $ref: "#/components/responses/NotFound"

    patch:
      summary: Update product
      tags: [Admin Products]
      security:
        - cookieAuth: []
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ProductPatchInput"
      responses:
        "200":
          description: Product updated
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AdminProduct"
        "404":
          $ref: "#/components/responses/NotFound"
        "422":
          $ref: "#/components/responses/ValidationError"

  /admin/orders:
    get:
      summary: List orders
      tags: [Admin Orders]
      security:
        - cookieAuth: []
      parameters:
        - in: query
          name: page
          schema:
            type: integer
            default: 1
        - in: query
          name: limit
          schema:
            type: integer
            default: 20
            maximum: 100
        - in: query
          name: status
          schema:
            $ref: "#/components/schemas/OrderStatus"
      responses:
        "200":
          description: Order list
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/OrderListResponse"

  /admin/orders/{id}:
    get:
      summary: Get order detail
      tags: [Admin Orders]
      security:
        - cookieAuth: []
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Order detail
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/OrderDetail"
        "404":
          $ref: "#/components/responses/NotFound"

  /admin/orders/{id}/status:
    patch:
      summary: Update order status
      tags: [Admin Orders]
      security:
        - cookieAuth: []
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [status]
              properties:
                status:
                  $ref: "#/components/schemas/OrderStatus"
      responses:
        "200":
          description: Order status updated
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/OrderStatusUpdateResponse"
        "409":
          description: Invalid status transition
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
        "422":
          $ref: "#/components/responses/ValidationError"

components:
  securitySchemes:
    cookieAuth:
      type: apiKey
      in: cookie
      name: admin_session

  schemas:
    StockStatus:
      type: string
      enum: [IN_STOCK, OUT_OF_STOCK]

    OrderStatus:
      type: string
      enum: [NEW, PROCESSING, SHIPPING, COMPLETED, CANCELLED]

    PaymentMethod:
      type: string
      enum: [COD]

    Pagination:
      type: object
      required: [page, limit, totalItems, totalPages]
      properties:
        page:
          type: integer
        limit:
          type: integer
        totalItems:
          type: integer
        totalPages:
          type: integer

    PublicProduct:
      type: object
      required: [id, name, price, stockQuantity, stockStatus, createdAt, updatedAt]
      properties:
        id:
          type: string
        name:
          type: string
        description:
          type: string
          nullable: true
        price:
          type: integer
          minimum: 1
        imageUrl:
          type: string
          nullable: true
        stockQuantity:
          type: integer
          minimum: 0
        stockStatus:
          $ref: "#/components/schemas/StockStatus"
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

    AdminProduct:
      allOf:
        - $ref: "#/components/schemas/PublicProduct"
        - type: object
          required: [isVisible]
          properties:
            isVisible:
              type: boolean

    ProductInput:
      type: object
      required: [name, price, stockQuantity, isVisible]
      properties:
        name:
          type: string
        description:
          type: string
          nullable: true
        price:
          type: integer
          minimum: 1
        imageUrl:
          type: string
          nullable: true
        stockQuantity:
          type: integer
          minimum: 0
        isVisible:
          type: boolean

    ProductPatchInput:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
          nullable: true
        price:
          type: integer
          minimum: 1
        imageUrl:
          type: string
          nullable: true
        stockQuantity:
          type: integer
          minimum: 0
        isVisible:
          type: boolean

    ProductListResponse:
      type: object
      required: [items, pagination]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/PublicProduct"
        pagination:
          $ref: "#/components/schemas/Pagination"

    AdminProductListResponse:
      type: object
      required: [items, pagination]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/AdminProduct"
        pagination:
          $ref: "#/components/schemas/Pagination"

    CreateOrderRequest:
      type: object
      required: [customerName, customerPhone, shippingAddress, items]
      properties:
        customerName:
          type: string
        customerPhone:
          type: string
        customerEmail:
          type: string
          nullable: true
        shippingAddress:
          type: string
        note:
          type: string
          nullable: true
        items:
          type: array
          minItems: 1
          items:
            type: object
            required: [productId, quantity]
            properties:
              productId:
                type: string
              quantity:
                type: integer
                minimum: 1

    OrderItem:
      type: object
      required: [id, productId, productName, unitPrice, quantity, lineTotal]
      properties:
        id:
          type: string
        productId:
          type: string
        productName:
          type: string
        unitPrice:
          type: integer
        quantity:
          type: integer
        lineTotal:
          type: integer

    OrderDetail:
      type: object
      required:
        - id
        - customerName
        - customerPhone
        - shippingAddress
        - totalAmount
        - status
        - statusLabel
        - paymentMethod
        - items
        - createdAt
        - updatedAt
      properties:
        id:
          type: string
        customerName:
          type: string
        customerPhone:
          type: string
        customerEmail:
          type: string
          nullable: true
        shippingAddress:
          type: string
        note:
          type: string
          nullable: true
        totalAmount:
          type: integer
        status:
          $ref: "#/components/schemas/OrderStatus"
        statusLabel:
          type: string
        paymentMethod:
          $ref: "#/components/schemas/PaymentMethod"
        stockRestoredAt:
          type: string
          format: date-time
          nullable: true
        items:
          type: array
          items:
            $ref: "#/components/schemas/OrderItem"
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

    OrderListItem:
      type: object
      required: [id, customerName, customerPhone, totalAmount, status, statusLabel, paymentMethod, createdAt, updatedAt]
      properties:
        id:
          type: string
        customerName:
          type: string
        customerPhone:
          type: string
        totalAmount:
          type: integer
        status:
          $ref: "#/components/schemas/OrderStatus"
        statusLabel:
          type: string
        paymentMethod:
          $ref: "#/components/schemas/PaymentMethod"
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

    OrderListResponse:
      type: object
      required: [items, pagination]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/OrderListItem"
        pagination:
          $ref: "#/components/schemas/Pagination"

    OrderStatusUpdateResponse:
      type: object
      required: [id, status, statusLabel, updatedAt]
      properties:
        id:
          type: string
        status:
          $ref: "#/components/schemas/OrderStatus"
        statusLabel:
          type: string
        stockRestoredAt:
          type: string
          format: date-time
          nullable: true
        updatedAt:
          type: string
          format: date-time

    AdminLoginRequest:
      type: object
      required: [email, password]
      properties:
        email:
          type: string
          format: email
        password:
          type: string

    AdminUser:
      type: object
      required: [id, email, role]
      properties:
        id:
          type: string
        email:
          type: string
          format: email
        role:
          type: string
          enum: [ADMIN]

    AdminMeResponse:
      type: object
      required: [user]
      properties:
        user:
          $ref: "#/components/schemas/AdminUser"

    ErrorResponse:
      type: object
      required: [error]
      properties:
        error:
          type: object
          required: [code, message]
          properties:
            code:
              type: string
            message:
              type: string
            details:
              nullable: true

  responses:
    ValidationError:
      description: Validation error
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"

    Unauthenticated:
      description: Unauthenticated
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ErrorResponse"
```

---

# 10. Các điểm cần PM xác nhận trước khi khóa API

1. Có cần public endpoint để xem lại order success sau reload không?  
   - Đề xuất MVP: không cần, dùng response sau khi tạo đơn hàng.
2. ID dùng UUID string hay integer auto-increment?
3. Backend stack/database cụ thể là gì?
4. Auth admin dùng cookie session hay JWT?
5. Có cho admin xóa sản phẩm không?  
   - PRD không yêu cầu, contract hiện tại không có delete.
6. Có cho hủy đơn ở trạng thái `SHIPPING` không?  
   - Contract hiện tại không cho hủy khi đang giao.
7. Khi sản phẩm bị hidden, đơn hàng cũ vẫn hiển thị bình thường trong admin nhờ snapshot. OK?
8. Có cần endpoint upload ảnh không?  
   - Contract hiện tại chỉ dùng URL ảnh.

---

# 11. Trạng thái contract

```text
Status: DRAFT
Locked: No
Owner: Technical Architecture & API Contract Agent
```

Sau khi PM xác nhận các điểm ở mục 10, contract có thể chuyển sang:

```text
Status: LOCKED
```

Khi đã lock, Frontend/Backend không tự ý đổi endpoint, payload hoặc status code nếu chưa có phê duyệt từ PM Orchestrator.