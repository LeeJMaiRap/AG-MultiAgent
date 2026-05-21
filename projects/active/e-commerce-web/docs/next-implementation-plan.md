# Next Implementation Plan — e-commerce-web

## 1. Trạng thái hiện tại

Dự án `e-commerce-web` hiện đã có các tài liệu nền tảng:

- `docs/prd.md`
- `docs/acceptance-criteria.md`
- `docs/technical-spec.md`
- `docs/api-contract.md`
- `docs/database-schema.md`
- `docs/task-board.md`
- `docs/qa-test-plan.md`

Trạng thái QA hiện tại:

```txt
QA Agent Fallback: Completed
Artifact: qa-test-plan.md
Automated QA Execution: Not run
Quality Gate: Pending execution
```

Dự án chưa hoàn thành vì chưa có source code frontend/backend hoàn chỉnh và chưa chạy QA thực tế.

---

## 2. Mục tiêu tiếp theo

Hoàn thành MVP website bán hàng gồm:

### Customer site

- Trang chủ
- Danh sách sản phẩm
- Chi tiết sản phẩm
- Giỏ hàng
- Đăng ký
- Đăng nhập
- Checkout COD
- Lịch sử đơn hàng
- Chi tiết đơn hàng

### Admin site

- Admin login
- Dashboard
- Quản lý danh mục
- Quản lý sản phẩm
- Quản lý đơn hàng
- Quản lý khách hàng

### Backend/API

- Auth API
- Product API
- Category API
- Cart/Checkout logic
- Order API
- Admin API
- Database schema + seed data
- Authorization customer/admin

---

## 3. Quyết định kỹ thuật cần dùng cho Wave 2

Tech stack mặc định đã được duyệt:

```txt
Frontend:
- React + Vite
- TypeScript
- React Router
- CSS/Tailwind tùy preflight

Backend:
- Node.js + Express
- TypeScript
- Prisma ORM

Database:
- SQLite local MVP

Auth:
- JWT

Validation:
- Zod

Password:
- bcrypt

Runtime:
- Windows Native
```

Lưu ý:

- Không cài package ngoài nếu chưa có preflight approval.
- Không dùng Docker path `/root` hoặc `/workspace`.
- Dùng relative path hoặc Windows path.

---

## 4. Wave 2 — Implementation Plan

## 4.1 Preflight bắt buộc trước khi cài package

Trước khi cài đặt, PM cần báo danh sách package dự kiến.

### Frontend packages đề xuất

```txt
react
react-dom
@vitejs/plugin-react
vite
typescript
react-router-dom
```

Optional nếu được duyệt:

```txt
tailwindcss
postcss
autoprefixer
```

### Backend packages đề xuất

```txt
express
cors
dotenv
jsonwebtoken
bcryptjs
zod
@prisma/client
```

### Dev dependencies backend

```txt
typescript
tsx
prisma
@types/node
@types/express
@types/cors
@types/jsonwebtoken
```

---

## 4.2 Backend Agent Task Packet

### Task ID: W2-BE-001 — Setup backend foundation

Owner: Backend Agent

Mục tiêu:

- Tạo backend Express TypeScript.
- Cấu hình Prisma SQLite.
- Tạo health endpoint.

Files được phép sửa/tạo:

```txt
backend/**
```

Deliverables:

```txt
backend/package.json
backend/tsconfig.json
backend/.env.example
backend/prisma/schema.prisma
backend/src/app.ts
backend/src/server.ts
backend/src/routes/health.routes.ts
```

Acceptance Criteria:

- Backend chạy được local.
- `GET /api/health` trả `{ "status": "ok" }`.
- `.env.example` có `DATABASE_URL`, `JWT_SECRET`, `PORT`.

---

### Task ID: W2-BE-002 — Database schema and seed

Owner: Backend Agent

Mục tiêu:

- Tạo Prisma schema cho User, Category, Product, Order, OrderItem.
- Tạo seed data cho QA.

Deliverables:

```txt
backend/prisma/schema.prisma
backend/prisma/seed.ts
```

Seed bắt buộc:

```txt
Admin:
- admin@example.com / Admin@123456

Customer:
- customer@example.com / Customer@123456
- customer2@example.com / Customer@123456

Categories:
- Điện thoại
- Laptop
- Phụ kiện

Products:
- Ít nhất 25 sản phẩm
- Có sản phẩm còn hàng
- Có sản phẩm hết hàng
- Có sản phẩm active/inactive
- Có sản phẩm nổi bật
```

Acceptance Criteria:

- Migration tạo SQLite DB thành công.
- Seed tạo dữ liệu mẫu.
- Password được hash.
- Không trả password hash qua API.

---

### Task ID: W2-BE-003 — Auth API

Owner: Backend Agent

Endpoints:

```txt
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
```

Acceptance Criteria:

- Register tạo customer mới.
- Login trả JWT.
- `GET /me` trả user hiện tại.
- Email unique.
- Password hash.
- Không expose password hash.

---

### Task ID: W2-BE-004 — Product and Category API

Owner: Backend Agent

Endpoints:

```txt
GET /api/categories
GET /api/products
GET /api/products/:slug
```

Query products:

```txt
keyword
category
minPrice
maxPrice
inStock
sort
page
limit
```

Acceptance Criteria:

- Customer chỉ thấy active product/category.
- Có pagination.
- Có search/filter/sort cơ bản.
- Product detail trả 404 nếu không tồn tại/inactive.

---

### Task ID: W2-BE-005 — Order API

Owner: Backend Agent

Endpoints:

```txt
POST /api/orders
GET  /api/orders/my
GET  /api/orders/my/:id
```

Acceptance Criteria:

- Chỉ customer đã login mới tạo order.
- Backend tự tính total.
- Kiểm tra tồn kho.
- Trừ tồn kho sau khi tạo order.
- Customer chỉ xem đơn của mình.
- Order mới có trạng thái `PENDING`.

---

### Task ID: W2-BE-006 — Admin API

Owner: Backend Agent

Endpoints:

```txt
GET    /api/admin/dashboard

GET    /api/admin/categories
POST   /api/admin/categories
PUT    /api/admin/categories/:id
DELETE /api/admin/categories/:id

GET    /api/admin/products
POST   /api/admin/products
PUT    /api/admin/products/:id
DELETE /api/admin/products/:id

GET    /api/admin/orders
GET    /api/admin/orders/:id
PATCH  /api/admin/orders/:id/status

GET    /api/admin/customers
PATCH  /api/admin/customers/:id/lock
PATCH  /api/admin/customers/:id/unlock
```

Acceptance Criteria:

- Chỉ role `ADMIN` truy cập được.
- Customer token bị forbidden.
- Admin CRUD category/product.
- Admin xem/cập nhật order status.
- Response customer không chứa password hash.

---

## 4.3 Frontend Agent Task Packet

### Task ID: W2-FE-001 — Setup frontend foundation

Owner: Frontend Agent

Mục tiêu:

- Tạo React Vite TypeScript app.
- Cấu hình routing.
- Tạo API client.

Files được phép sửa/tạo:

```txt
frontend/**
```

Deliverables:

```txt
frontend/package.json
frontend/.env.example
frontend/src/main.tsx
frontend/src/App.tsx
frontend/src/routes/**
frontend/src/services/api.ts
```

Acceptance Criteria:

- Frontend chạy local.
- Có routes customer/admin.
- API base URL lấy từ `.env`.

---

### Task ID: W2-FE-002 — Customer product pages

Owner: Frontend Agent

Pages:

```txt
/
 /products
 /products/:slug
```

Acceptance Criteria:

- Trang chủ hiển thị sản phẩm nổi bật hoặc mới.
- Product list có loading/error/empty state.
- Product detail hiển thị đủ thông tin.
- Sản phẩm hết hàng disable add-to-cart.

---

### Task ID: W2-FE-003 — Auth pages

Owner: Frontend Agent

Pages:

```txt
/register
/login
```

Acceptance Criteria:

- Register form validate cơ bản.
- Login lưu JWT.
- Logout xóa JWT.
- Header hiển thị trạng thái đăng nhập.
- Lỗi auth hiển thị thân thiện.

---

### Task ID: W2-FE-004 — Cart and checkout

Owner: Frontend Agent

Pages:

```txt
/cart
/checkout
/order-success/:id
```

Acceptance Criteria:

- Cart lưu localStorage hoặc state ổn định.
- Add/update/remove item hoạt động.
- Checkout yêu cầu login.
- Checkout gửi order lên backend.
- Sau khi thành công clear cart và hiển thị order success.

---

### Task ID: W2-FE-005 — Order history

Owner: Frontend Agent

Pages:

```txt
/my-orders
/my-orders/:id
```

Acceptance Criteria:

- Customer xem danh sách đơn của mình.
- Customer xem chi tiết đơn của mình.
- Không hiển thị đơn của user khác.

---

### Task ID: W2-FE-006 — Admin UI

Owner: Frontend Agent

Pages:

```txt
/admin/login
/admin
/admin/categories
/admin/products
/admin/orders
/admin/orders/:id
/admin/customers
```

Acceptance Criteria:

- Admin login.
- Admin dashboard hiển thị số liệu.
- CRUD category/product.
- Xem/cập nhật trạng thái order.
- Xem danh sách customer.
- Customer không truy cập được admin pages.

---

## 5. Wave 3 — Integration & QA Plan

Sau khi Frontend/Backend hoàn tất, QA Agent chạy theo `docs/qa-test-plan.md`.

### QA Task ID: W3-QA-001 — Setup verification

Kiểm tra:

```txt
backend npm install
backend migration
backend seed
backend dev server
frontend npm install
frontend dev server
```

Evidence cần có:

```txt
- Log backend chạy
- Log frontend chạy
- URL frontend
- URL backend
```

---

### QA Task ID: W3-QA-002 — API verification

Test các nhóm API:

```txt
GET /api/health
POST /api/auth/register
POST /api/auth/login
GET /api/categories
GET /api/products
GET /api/products/:slug
POST /api/orders
GET /api/orders/my
Admin APIs
```

Evidence:

```txt
docs/test-report.md
```

---

### QA Task ID: W3-QA-003 — Customer UI verification

Test:

- Product list
- Product detail
- Cart
- Register/login
- Checkout
- Order history

---

### QA Task ID: W3-QA-004 — Admin UI verification

Test:

- Admin login
- Dashboard
- Category management
- Product management
- Order management
- Customer management

---

### QA Task ID: W3-QA-005 — Security and authorization verification

Test:

- Không token bị 401.
- Customer gọi admin API bị 403.
- Customer không xem đơn người khác.
- Password hash không trả về response.
- Backend không tin total từ frontend.

---

## 6. Wave 4 — Finalization

Sau QA pass, tạo:

```txt
docs/test-report.md
docs/final-report.md
docs/known-issues.md
docs/next-steps.md
README.md
```

README cần có:

```txt
- Mô tả dự án
- Tech stack
- Hướng dẫn setup Windows Native
- Lệnh chạy backend
- Lệnh chạy frontend
- Account test
- API base URL
```

---

## 7. Dependencies and Execution Order

```txt
1. Preflight package approval
2. Backend setup + DB + seed
3. Backend APIs
4. Frontend setup
5. Frontend customer pages
6. Frontend auth/cart/checkout
7. Frontend admin pages
8. Integration
9. QA execution
10. Bug fixing
11. Final report
```

Backend và Frontend có thể làm song song sau khi API contract đã ổn định.

---

## 8. Quality Gates

| Gate | Owner | Required Evidence | Status |
|---|---|---|---|
| W1-PROD | PM/Product | PRD + AC files | Passed |
| W1-ARCH | PM/Architecture | Technical spec + API contract + DB schema + task board | Passed |
| W2-BE | Backend | API running, migration/seed, logs | Pending |
| W2-FE | Frontend | UI running, API integrated, screenshots/logs | Pending |
| W3-QA | QA | Test report, bug list, retest evidence | Pending |
| W4-CLOSE | PM | Final report, README, known issues | Pending |

---

## 9. PM Recommendation

Tiếp theo nên làm ngay:

```txt
Step 1: Preflight package approval
Step 2: Setup backend Express + Prisma + SQLite
Step 3: Setup frontend React + Vite
Step 4: Implement APIs and UI in parallel
Step 5: Run QA from qa-test-plan.md
```

Trạng thái dự án:

```txt
IN PROGRESS
Current Phase: Ready for Wave 2 Implementation
Next Required Approval: Package installation preflight
```
