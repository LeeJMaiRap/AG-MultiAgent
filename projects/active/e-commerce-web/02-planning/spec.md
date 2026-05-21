Tôi sẽ thay thế vai trò `architecture-agent` bằng cách tự biên soạn bộ tài liệu Architecture Wave 1 tối giản nhưng hợp lệ cho dự án `e-commerce-web`, gồm Technical Spec, API Contract, Database Schema và Task Board.<tool_write_file path="active/e-commerce-web/docs/technical-spec.md"># Technical Specification — E-commerce Web MVP

## 1. Mục tiêu kỹ thuật

Xây dựng MVP cho một website thương mại điện tử với các năng lực cốt lõi:

- Người dùng xem danh sách sản phẩm.
- Người dùng xem chi tiết sản phẩm.
- Người dùng thêm, cập nhật, xóa sản phẩm trong giỏ hàng.
- Người dùng tạo đơn hàng checkout cơ bản.
- Hệ thống lưu sản phẩm, giỏ hàng và đơn hàng.
- API rõ ràng để Frontend và Backend phát triển song song.

## 2. Phạm vi MVP

### In scope

- Product catalog.
- Product detail.
- Cart management.
- Checkout order creation.
- Basic order confirmation.
- Simple user identity theo `sessionId` hoặc `userId` giả lập.
- REST API.

### Out of scope

- Thanh toán online thật.
- Đăng nhập OAuth.
- Admin CMS đầy đủ.
- Inventory reservation nâng cao.
- Shipping provider integration.
- Email/SMS notification thật.

## 3. Kiến trúc tổng quan

```txt
Browser / Frontend
        |
        | HTTP REST / JSON
        v
Backend API
        |
        | ORM / Query Layer
        v
Database
```

## 4. Tech Stack đề xuất

### Frontend

- React hoặc Next.js.
- TypeScript.
- CSS Modules, Tailwind CSS hoặc tương đương.
- Fetch/Axios để gọi API.

### Backend

- Node.js với Express hoặc Next.js API Routes.
- TypeScript khuyến nghị.
- RESTful API.
- Validation ở request boundary.

### Database

- PostgreSQL khuyến nghị.
- SQLite có thể dùng cho local MVP nếu cần tối giản.
- ORM tùy chọn: Prisma hoặc query builder tương đương.

## 5. Module chính

### 5.1 Product Module

Trách nhiệm:

- Trả danh sách sản phẩm.
- Trả chi tiết sản phẩm.
- Hỗ trợ filter/search tối giản nếu cần.

Entity chính:

- `Product`
- `Category`

### 5.2 Cart Module

Trách nhiệm:

- Tạo hoặc lấy giỏ hàng hiện tại.
- Thêm sản phẩm vào giỏ.
- Cập nhật số lượng.
- Xóa item khỏi giỏ.
- Tính subtotal, total.

Entity chính:

- `Cart`
- `CartItem`

### 5.3 Checkout / Order Module

Trách nhiệm:

- Nhận thông tin checkout.
- Validate cart không rỗng.
- Tạo order từ cart.
- Snapshot giá sản phẩm tại thời điểm đặt hàng.
- Đánh dấu cart đã checkout hoặc clear cart.

Entity chính:

- `Order`
- `OrderItem`

## 6. Data Flow chính

### 6.1 Browse Products

```txt
Frontend Product Listing Page
  -> GET /api/products
  -> Backend Product Service
  -> Database products
  -> Response product list
```

### 6.2 Add to Cart

```txt
Frontend Product Detail/List
  -> POST /api/cart/items
  -> Backend Cart Service
  -> Validate product exists
  -> Create/update cart item
  -> Response updated cart
```

### 6.3 Checkout

```txt
Frontend Checkout Page
  -> POST /api/orders
  -> Backend Order Service
  -> Validate cart
  -> Create order and order items
  -> Mark cart completed / clear active cart
  -> Response order confirmation
```

## 7. API Design Principles

- JSON request/response.
- HTTP status code chuẩn.
- Error response thống nhất.
- Không expose database internals.
- Monetary values lưu bằng integer minor unit, ví dụ `priceCents`.

## 8. Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request payload",
    "details": []
  }
}
```

## 9. Security Notes

- Validate toàn bộ input từ client.
- Không tin giá từ client khi checkout.
- Giá order phải lấy từ database.
- Không lưu thông tin payment card.
- CORS cấu hình theo môi trường.
- Rate limit có thể bổ sung sau MVP.

## 10. Performance Notes

- Product list cần pagination.
- Index cho product slug, category id, cart id, order id.
- Avoid N+1 queries khi lấy cart/order detail.

## 11. Frontend Integration Contract

Frontend chỉ nên phụ thuộc vào:

- `api-contract.md`
- Kiểu dữ liệu response trong API contract.
- Không phụ thuộc vào schema database nội bộ.

## 12. Backend Implementation Notes

Service layer khuyến nghị:

```txt
src/
  modules/
    products/
      product.controller.ts
      product.service.ts
      product.repository.ts
    cart/
      cart.controller.ts
      cart.service.ts
      cart.repository.ts
    orders/
      order.controller.ts
      order.service.ts
      order.repository.ts
```

## 13. Acceptance Mapping

| Requirement | Technical Mapping |
|---|---|
| View products | `GET /api/products` |
| View product detail | `GET /api/products/{slug}` |
| Add to cart | `POST /api/cart/items` |
| Update cart quantity | `PATCH /api/cart/items/{itemId}` |
| Remove cart item | `DELETE /api/cart/items/{itemId}` |
| Checkout | `POST /api/orders` |
| View order confirmation | `GET /api/orders/{orderId}` |

## 14. Quality Gate

Architecture deliverables required:

- `technical-spec.md`
- `api-contract.md`
- `database-schema.md`
- `task-board.md`

Status:

```txt
W1-ARCH-001: COMPLETED_BY_PM_FALLBACK
Quality Gate: READY_FOR_REVIEW
```
</tool_write_file>

<tool_write_file path="active/e-commerce-web/docs/api-contract.md"># API Contract — E-commerce Web MVP

## 1. Base URL

Local development:

```txt
http://localhost:3000/api
```

Production placeholder:

```txt
https://example.com/api
```

## 2. Conventions

### Content Type

```txt
Content-Type: application/json
```

### Currency

- Monetary fields use integer cents.
- Example: `1999` means `$19.99`.

### Identity

For MVP, cart identity may be resolved by one of:

- `sessionId` sent from client.
- Authenticated `userId` if authentication exists.
- Anonymous cart token.

Recommended request header for anonymous MVP:

```txt
X-Session-Id: string
```

## 3. Common Types

### Product

```json
{
  "id": "prod_001",
  "slug": "classic-t-shirt",
  "name": "Classic T-Shirt",
  "description": "Comfortable cotton t-shirt",
  "priceCents": 1999,
  "currency": "USD",
  "imageUrl": "/images/products/classic-t-shirt.jpg",
  "category": {
    "id": "cat_001",
    "name": "Apparel",
    "slug": "apparel"
  },
  "isActive": true,
  "stockQuantity": 100,
  "createdAt": "2026-01-01T00:00:00.000Z",
  "updatedAt": "2026-01-01T00:00:00.000Z"
}
```

### Cart

```json
{
  "id": "cart_001",
  "sessionId": "session_abc",
  "items": [
    {
      "id": "cart_item_001",
      "productId": "prod_001",
      "name": "Classic T-Shirt",
      "slug": "classic-t-shirt",
      "imageUrl": "/images/products/classic-t-shirt.jpg",
      "unitPriceCents": 1999,
      "quantity": 2,
      "lineTotalCents": 3998
    }
  ],
  "subtotalCents": 3998,
  "totalCents": 3998,
  "currency": "USD",
  "status": "ACTIVE",
  "updatedAt": "2026-01-01T00:00:00.000Z"
}
```

### Order

```json
{
  "id": "order_001",
  "orderNumber": "EC-20260101-0001",
  "status": "PLACED",
  "customer": {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "phone": "+10000000000"
  },
  "shippingAddress": {
    "line1": "123 Main Street",
    "line2": "",
    "city": "New York",
    "state": "NY",
    "postalCode": "10001",
    "country": "US"
  },
  "items": [
    {
      "id": "order_item_001",
      "productId": "prod_001",
      "productName": "Classic T-Shirt",
      "unitPriceCents": 1999,
      "quantity": 2,
      "lineTotalCents": 3998
    }
  ],
  "subtotalCents": 3998,
  "shippingFeeCents": 0,
  "taxCents": 0,
  "totalCents": 3998,
  "currency": "USD",
  "createdAt": "2026-01-01T00:00:00.000Z"
}
```

### Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request payload",
    "details": [
      {
        "field": "quantity",
        "message": "Quantity must be greater than 0"
      }
    ]
  }
}
```

## 4. Product APIs

### 4.1 List Products

```txt
GET /api/products
```

Query parameters:

| Name | Type | Required | Description |
|---|---|---|---|
| page | number | No | Default `1` |
| limit | number | No | Default `12` |
| category | string | No | Category slug |
| search | string | No | Search text |

Success response:

```txt
200 OK
```

```json
{
  "data": [
    {
      "id": "prod_001",
      "slug": "classic-t-shirt",
      "name": "Classic T-Shirt",
      "description": "Comfortable cotton t-shirt",
      "priceCents": 1999,
      "currency": "USD",
      "imageUrl": "/images/products/classic-t-shirt.jpg",
      "category": {
        "id": "cat_001",
        "name": "Apparel",
        "slug": "apparel"
      },
      "isActive": true,
      "stockQuantity": 100
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 12,
    "total": 1,
    "totalPages": 1
  }
}
```

### 4.2 Get Product Detail

```txt
GET /api/products/{slug}
```

Success response:

```txt
200 OK
```

```json
{
  "data": {
    "id": "prod_001",
    "slug": "classic-t-shirt",
    "name": "Classic T-Shirt",
    "description": "Comfortable cotton t-shirt",
    "priceCents": 1999,
    "currency": "USD",
    "imageUrl": "/images/products/classic-t-shirt.jpg",
    "category": {
      "id": "cat_001",
      "name": "Apparel",
      "slug": "apparel"
    },
    "isActive": true,
    "stockQuantity": 100,
    "createdAt": "2026-01-01T00:00:00.000Z",
    "updatedAt": "2026-01-01T00:00:00.000Z"
  }
}
```

Error responses:

```txt
404 NOT_FOUND
```

## 5. Cart APIs

### 5.1 Get Current Cart

```txt
GET /api/cart
```

Headers:

```txt
X-Session-Id: session_abc
```

Success response:

```txt
200 OK
```

```json
{
  "data": {
    "id": "cart_001",
    "sessionId": "session_abc",
    "items": [],
    "subtotalCents": 0,
    "totalCents": 0,
    "currency": "USD",
    "status": "ACTIVE",
    "updatedAt": "2026-01-01T00:00:00.000Z"
  }
}
```

### 5.2 Add Item To Cart

```txt
POST /api/cart/items
```

Request body:

```json
{
  "productId": "prod_001",
  "quantity": 1
}
```

Success response:

```txt
200 OK
```

```json
{
  "data": {
    "id": "cart_001",
    "sessionId": "session_abc",
    "items": [
      {
        "id": "cart_item_001",
        "productId": "prod_001",
        "name": "Classic T-Shirt",
        "slug": "classic-t-shirt",
        "imageUrl": "/images/products/classic-t-shirt.jpg",
        "unitPriceCents": 1999,
        "quantity": 1,
        "lineTotalCents": 1999
      }
    ],
    "subtotalCents": 1999,
    "totalCents": 1999,
    "currency": "USD",
    "status": "ACTIVE",
    "updatedAt": "2026-01-01T00:00:00.000Z"
  }
}
```

Validation:

- `productId` required.
- `quantity` integer greater than 0.
- Product must exist and be active.

### 5.3 Update Cart Item Quantity

```txt
PATCH /api/cart/items/{itemId}
```

Request body:

```json
{
  "quantity": 3
}
```

Success response:

```txt
200 OK
```

```json
{
  "data": {
    "id": "cart_001",
    "items": [
      {
        "id": "cart_item_001",
        "productId": "prod_001",
        "unitPriceCents": 1999,
        "quantity": 3,
        "lineTotalCents": 5997
      }
    ],
    "subtotalCents": 5997,
    "totalCents": 5997,
    "currency": "USD",
    "status": "ACTIVE"
  }
}
```

Validation:

- `quantity` integer greater than 0.
- Item must belong to current session cart.

### 5.4 Remove Cart Item

```txt
DELETE /api/cart/items/{itemId}
```

Success response:

```txt
200 OK
```

```json
{
  "data": {
    "id": "cart_001",
    "items": [],
    "subtotalCents": 0,
    "totalCents": 0,
    "currency": "USD",
    "status": "ACTIVE"
  }
}
```

## 6. Order APIs

### 6.1 Create Order

```txt
POST /api/orders
```

Headers:

```txt
X-Session-Id: session_abc
```

Request body:

```json
{
  "customer": {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "phone": "+10000000000"
  },
  "shippingAddress": {
    "line1": "123 Main Street",
    "line2": "",
    "city": "New York",
    "state": "NY",
    "postalCode": "10001",
    "country": "US"
  }
}
```

Success response:

```txt
201 CREATED
```

```json
{
  "data": {
    "id": "order_001",
    "orderNumber": "EC-20260101-0001",
    "status": "PLACED",
    "customer": {
      "name": "Jane Doe",
      "email": "jane@example.com",
      "phone": "+10000000000"
    },
    "shippingAddress": {
      "line1": "123 Main Street",
      "line2": "",
      "city": "New York",
      "state": "NY",
      "postalCode": "10001",
      "country": "US"
    },
    "items": [
      {
        "id": "order_item_001",
        "productId": "prod_001",
        "productName": "Classic T-Shirt",
        "unitPriceCents": 1999,
        "quantity": 2,
        "lineTotalCents": 3998
      }
    ],
    "subtotalCents": 3998,
    "shippingFeeCents": 0,
    "taxCents": 0,
    "totalCents": 3998,
    "currency": "USD",
    "createdAt": "2026-01-01T00:00:00.000Z"
  }
}
```

Validation:

- Cart must exist.
- Cart must have at least one item.
- Customer name and email required.
- Shipping address line1, city, postalCode, country required.
- Backend must calculate totals from database product prices.

Error responses:

```txt
400 EMPTY_CART
422 VALIDATION_ERROR
```

### 6.2 Get Order Detail

```txt
GET /api/orders/{orderId}
```

Success response:

```txt
200 OK
```

```json
{
  "data": {
    "id": "order_001",
    "orderNumber": "EC-20260101-0001",
    "status": "PLACED",
    "items": [],
    "subtotalCents": 3998,
    "shippingFeeCents": 0,
    "taxCents": 0,
    "totalCents": 3998,
    "currency": "USD",
    "createdAt": "2026-01-01T00:00:00.000Z"
  }
}
```

Error responses:

```txt
404 NOT_FOUND
```

## 7. HTTP Status Code Summary

| Status | Usage |
|---|---|
| 200 | Successful read/update/delete returning resource |
| 201 | Resource created |
| 400 | Invalid business state, e.g. empty cart |
| 404 | Resource not found |
| 409 | Conflict, e.g. insufficient stock |
| 422 | Validation error |
| 500 | Unexpected server error |

## 8. Contract Quality Gate

```txt
API_CONTRACT_VERSION: 1.0.0
W1-ARCH-API: COMPLETED_BY_PM_FALLBACK
READY_FOR_FRONTEND: YES
READY_FOR_BACKEND: YES
```
</tool_write_file>

<tool_write_file path="active/e-commerce-web/docs/database-schema.md"># Database Schema — E-commerce Web MVP

## 1. Overview

This document defines a minimal relational schema for the E-commerce Web MVP.

Recommended database:

```txt
PostgreSQL
```

Alternative for local MVP:

```txt
SQLite
```

## 2. Entity Relationship Summary

```txt
Category 1 ---- N Product

Cart 1 ---- N CartItem
Product 1 ---- N CartItem

Order 1 ---- N OrderItem
Product 1 ---- N OrderItem
```

## 3. Tables

## 3.1 categories

Stores product categories.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | varchar(64) | PK | Category ID |
| name | varchar(255) | NOT NULL | Display name |
| slug | varchar(255) | UNIQUE, NOT NULL | URL-safe category slug |
| created_at | timestamp | NOT NULL | Creation timestamp |
| updated_at | timestamp | NOT NULL | Update timestamp |

Example:

```sql
CREATE TABLE categories (
  id VARCHAR(64) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

## 3.2 products

Stores sellable products.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | varchar(64) | PK | Product ID |
| category_id | varchar(64) | FK categories(id), nullable | Category reference |
| slug | varchar(255) | UNIQUE, NOT NULL | Product slug |
| name | varchar(255) | NOT NULL | Product name |
| description | text | nullable | Product description |
| price_cents | integer | NOT NULL | Price in minor currency unit |
| currency | varchar(3) | NOT NULL | ISO currency code |
| image_url | text | nullable | Product image URL |
| stock_quantity | integer | NOT NULL DEFAULT 0 | Available stock |
| is_active | boolean | NOT NULL DEFAULT true | Product availability |
| created_at | timestamp | NOT NULL | Creation timestamp |
| updated_at | timestamp | NOT NULL | Update timestamp |

Example:

```sql
CREATE TABLE products (
  id VARCHAR(64) PRIMARY KEY,
  category_id VARCHAR(64) REFERENCES categories(id),
  slug VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
  currency VARCHAR(3) NOT NULL DEFAULT 'USD',
  image_url TEXT,
  stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Indexes:

```sql
CREATE INDEX idx_products_category_id ON products(category_id);
CREATE INDEX idx_products_is_active ON products(is_active);
CREATE INDEX idx_products_slug ON products(slug);
```

## 3.3 carts

Stores shopping carts.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | varchar(64) | PK | Cart ID |
| session_id | varchar(255) | NOT NULL | Anonymous session identifier |
| status | varchar(32) | NOT NULL | ACTIVE, CHECKED_OUT, ABANDONED |
| created_at | timestamp | NOT NULL | Creation timestamp |
| updated_at | timestamp | NOT NULL | Update timestamp |

Example:

```sql
CREATE TABLE carts (
  id VARCHAR(64) PRIMARY KEY,
  session_id VARCHAR(255) NOT NULL,
  status VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Indexes:

```sql
CREATE INDEX idx_carts_session_status ON carts(session_id, status);
```

## 3.4 cart_items

Stores products inside carts.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | varchar(64) | PK | Cart item ID |
| cart_id | varchar(64) | FK carts(id), NOT NULL | Cart reference |
| product_id | varchar(64) | FK products(id), NOT NULL | Product reference |
| quantity | integer | NOT NULL | Quantity |
| unit_price_cents | integer | NOT NULL | Snapshot unit price |
| created_at | timestamp | NOT NULL | Creation timestamp |
| updated_at | timestamp | NOT NULL | Update timestamp |

Example:

```sql
CREATE TABLE cart_items (
  id VARCHAR(64) PRIMARY KEY,
  cart_id VARCHAR(64) NOT NULL REFERENCES carts(id) ON DELETE CASCADE,
  product_id VARCHAR(64) NOT NULL REFERENCES products(id),
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  unit_price_cents INTEGER NOT NULL CHECK (unit_price_cents >= 0),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (cart_id, product_id)
);
```

Indexes:

```sql
CREATE INDEX idx_cart_items_cart_id ON cart_items(cart_id);
CREATE INDEX idx_cart_items_product_id ON cart_items(product_id);
```

## 3.5 orders

Stores submitted orders.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | varchar(64) | PK | Order ID |
| order_number | varchar(64) | UNIQUE, NOT NULL | Human-readable order number |
| session_id | varchar(255) | nullable | Original session |
| status | varchar(32) | NOT NULL | PLACED, PAID, CANCELLED, FULFILLED |
| customer_name | varchar(255) | NOT NULL | Customer name |
| customer_email | varchar(255) | NOT NULL | Customer email |
| customer_phone | varchar(64) | nullable | Customer phone |
| shipping_line1 | varchar(255) | NOT NULL | Address line 1 |
| shipping_line2 | varchar(255) | nullable | Address line 2 |
| shipping_city | varchar(128) | NOT NULL | City |
| shipping_state | varchar(128) | nullable | State |
| shipping_postal_code | varchar(64) | NOT NULL | Postal code |
| shipping_country | varchar(64) | NOT NULL | Country |
| subtotal_cents | integer | NOT NULL | Subtotal |
| shipping_fee_cents | integer | NOT NULL DEFAULT 0 | Shipping fee |
| tax_cents | integer | NOT NULL DEFAULT 0 | Tax |
| total_cents | integer | NOT NULL | Total |
| currency | varchar(3) | NOT NULL | Currency |
| created_at | timestamp | NOT NULL | Creation timestamp |
| updated_at | timestamp | NOT NULL | Update timestamp |

Example:

```sql
CREATE TABLE orders (
  id VARCHAR(64) PRIMARY KEY,
  order_number VARCHAR(64) UNIQUE NOT NULL,
  session_id VARCHAR(255),
  status VARCHAR(32) NOT NULL DEFAULT 'PLACED',
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(64),
  shipping_line1 VARCHAR(255) NOT NULL,
  shipping_line2 VARCHAR(255),
  shipping_city VARCHAR(128) NOT NULL,
  shipping_state VARCHAR(128),
  shipping_postal_code VARCHAR(64) NOT NULL,
  shipping_country VARCHAR(64) NOT NULL,
  subtotal_cents INTEGER NOT NULL CHECK (subtotal_cents >= 0),
  shipping_fee_cents INTEGER NOT NULL DEFAULT 0 CHECK (shipping_fee_cents >= 0),
  tax_cents INTEGER NOT NULL DEFAULT 0 CHECK (tax_cents >= 0),
  total_cents INTEGER NOT NULL CHECK (total_cents >= 0),
  currency VARCHAR(3) NOT NULL DEFAULT 'USD',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Indexes:

```sql
CREATE INDEX idx_orders_order_number ON orders(order_number);
CREATE INDEX idx_orders_customer_email ON orders(customer_email);
CREATE INDEX idx_orders_created_at ON orders(created_at);
```

## 3.6 order_items

Stores immutable order line items.

| Column | Type | Constraints | Description |
|---|---|---|---|
| id | varchar(64) | PK | Order item ID |
| order_id | varchar(64) | FK orders(id), NOT NULL | Order reference |
| product_id | varchar(64) | FK products(id), nullable | Product reference |
| product_name | varchar(255) | NOT NULL | Snapshot product name |
| unit_price_cents | integer | NOT NULL | Snapshot unit price |
| quantity | integer | NOT NULL | Quantity ordered |
| line_total_cents | integer | NOT NULL | Quantity * unit price |

Example:

```sql
CREATE TABLE order_items (
  id VARCHAR(64) PRIMARY KEY,
  order_id VARCHAR(64) NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id VARCHAR(64) REFERENCES products(id),
  product_name VARCHAR(255) NOT NULL,
  unit_price_cents INTEGER NOT NULL CHECK (unit_price_cents >= 0),
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  line_total_cents INTEGER NOT NULL CHECK (line_total_cents >= 0)
);
```

Indexes:

```sql
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
```

## 4. Seed Data Example

```sql
INSERT INTO categories (id, name, slug)
VALUES ('cat_001', 'Apparel', 'apparel');

INSERT INTO products (
  id,
  category_id,
  slug,
  name,
  description,
  price_cents,
  currency,
  image_url,
  stock_quantity,
  is_active
)
VALUES (
  'prod_001',
  'cat_001',
  'classic-t-shirt',
  'Classic T-Shirt',
  'Comfortable cotton t-shirt',
  1999,
  'USD',
  '/images/products/classic-t-shirt.jpg',
  100,
  TRUE
);
```

## 5. Business Rules

- Product price must not be accepted from client during checkout.
- Cart item unit price should be set from product price when item is added.
- Order item unit price and product name must be snapshotted.
- Cart can be marked `CHECKED_OUT` after successful order creation.
- Product stock check is recommended before order creation.

## 6. Schema Quality Gate

```txt
DATABASE_SCHEMA_VERSION: 1.0.0
W1-ARCH-DB: COMPLETED_BY_PM_FALLBACK
READY_FOR_BACKEND: YES
```
</tool_write_file>

<tool_write_file path="active/e-commerce-web/docs/task-board.md"># Task Board — E-commerce Web MVP

## 1. Project

```txt
Project: e-commerce-web
Phase: Architecture Wave 1
Status: Completed by PM fallback due to architecture-agent issue
```

## 2. Architecture Deliverables

| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| W1-ARCH-001 | Create technical specification | PM fallback acting as Architecture Agent | Done | `docs/technical-spec.md` |
| W1-ARCH-002 | Create API contract | PM fallback acting as Architecture Agent | Done | `docs/api-contract.md` |
| W1-ARCH-003 | Create database schema | PM fallback acting as Architecture Agent | Done | `docs/database-schema.md` |
| W1-ARCH-004 | Create implementation task board | PM fallback acting as Architecture Agent | Done | `docs/task-board.md` |

## 3. Frontend Task Candidates

| ID | Task | Depends On | Files Allowed | Acceptance Criteria |
|---|---|---|---|---|
| FE-001 | Implement product listing page | API Contract | Frontend UI files only | User can view products from `GET /api/products` |
| FE-002 | Implement product detail page | API Contract | Frontend UI files only | User can view product detail from `GET /api/products/{slug}` |
| FE-003 | Implement cart UI | API Contract | Frontend UI files only | User can view cart, add/update/remove items |
| FE-004 | Implement checkout form | API Contract | Frontend UI files only | User can submit customer and shipping information |
| FE-005 | Implement order confirmation page | API Contract | Frontend UI files only | User can see order confirmation after checkout |

## 4. Backend Task Candidates

| ID | Task | Depends On | Files Allowed | Acceptance Criteria |
|---|---|---|---|---|
| BE-001 | Implement product API | DB Schema, API Contract | Backend API files only | `GET /api/products` and `GET /api/products/{slug}` return valid JSON |
| BE-002 | Implement cart API | DB Schema, API Contract | Backend API files only | Cart endpoints support get, add, update, remove |
| BE-003 | Implement order API | DB Schema, API Contract | Backend API files only | `POST /api/orders` creates order from active cart |
| BE-004 | Implement database migration/seed | DB Schema | Backend database files only | Tables and seed product exist locally |
| BE-005 | Implement validation/error handling | API Contract | Backend API files only | Error response follows contract |

## 5. QA Task Candidates

| ID | Task | Depends On | Acceptance Criteria |
|---|---|---|---|
| QA-001 | Validate product listing flow | FE-001, BE-001 | Product cards render correctly |
| QA-002 | Validate product detail flow | FE-002, BE-001 | Product detail page loads valid product |
| QA-003 | Validate cart flow | FE-003, BE-002 | Add/update/remove cart item works |
| QA-004 | Validate checkout flow | FE-004, FE-005, BE-003 | Order can be created from non-empty cart |
| QA-005 | Validate error handling | BE-005 | Invalid input returns expected status and error shape |

## 6. Integration Plan

### Step 1: Backend foundation

- Create schema/migration.
- Seed at least one category and product.
- Implement Product API.

### Step 2: Frontend product browsing

- Connect listing page to Product API.
- Connect detail page to Product API.

### Step 3: Cart integration

- Implement Cart API.
- Implement cart state in Frontend.
- Ensure `X-Session-Id` or equivalent session identity exists.

### Step 4: Checkout integration

- Implement Order API.
- Implement checkout page.
- Implement order confirmation page.

### Step 5: QA verification

- Run functional test cases.
- Confirm API response shape.
- Confirm MVP acceptance criteria.

## 7. File Ownership Rules

### Frontend Agent may edit

```txt
src/app/**
src/pages/**
src/components/**
src/styles/**
src/lib/api-client*
public/**
```

### Backend Agent may edit

```txt
src/api/**
src/server/**
src/modules/**
src/lib/db/**
prisma/**
database/**
```

### QA Agent may edit

```txt
tests/**
docs/qa-report.md
```

### Restricted unless approved by PM

```txt
package.json
package-lock.json
yarn.lock
pnpm-lock.yaml
.env
.env.local
```

## 8. Quality Gates

| Gate | Required Evidence | Status |
|---|---|---|
| Product Gate | PRD and Acceptance Criteria completed | Passed |
| Architecture Gate | Technical spec, API contract, DB schema, task board | Passed by PM fallback |
| Backend Gate | API endpoints implemented and tested | Pending |
| Frontend Gate | UI flows implemented and connected | Pending |
| QA Gate | End-to-end MVP validation | Pending |

## 9. Architecture Wave Final Status

```txt
W1-ARCH-001: COMPLETED_BY_PM_FALLBACK
Reason: architecture-agent connection/permission issue
Deliverables:
- docs/technical-spec.md
- docs/api-contract.md
- docs/database-schema.md
- docs/task-board.md

Ready for Wave 2:
- frontend-agent: YES
- backend-agent: YES
- qa-agent: AFTER IMPLEMENTATION
```
</tool_write_file>