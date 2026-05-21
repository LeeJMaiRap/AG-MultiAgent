Đã nhận trạng thái QA: **BLOCKED** cho project `user-project`.

Mình sẽ xử lý theo vai trò PM Orchestrator như sau: QA bị chặn là hợp lệ vì hiện chưa có đủ thông tin runnable environment. Trước khi QA kiểm thử, cần chốt lại **project path, cấu trúc repo, lệnh chạy, seed data và tài khoản admin**.

---

# Quyết định PM

## Trạng thái hiện tại

```text
Project: user-project
Type: MVP bán hàng trực tuyến
QA Status: BLOCKED
Blocker: Missing runnable local environment details
```

QA **chưa thể nghiệm thu** vì chưa có bằng chứng chạy được hệ thống.

---

# Đề xuất cấu trúc chuẩn cho MVP

Nếu bạn chưa có repo sẵn, mình đề xuất tạo project theo cấu trúc sau trên Windows:

```text
D:\Antigravity\projects\user-project\
  frontend\
  backend\
  docs\
    PRD.md
    technical-spec.md
    api-contract.md
    verification-report.md
  README.md
```

---

# Thông tin môi trường đề xuất

## Frontend

```text
Framework: React + Vite
Port: 5173
URL: http://localhost:5173
```

Lệnh chạy:

```powershell
cd D:\Antigravity\projects\user-project\frontend
npm install
npm run dev
```

## Backend

```text
Runtime: Node.js + Express
Database: SQLite cho MVP local
Port: 3000
API Base URL: http://localhost:3000/api
```

Lệnh chạy:

```powershell
cd D:\Antigravity\projects\user-project\backend
npm install
npm run dev
```

## Seed data

Cần có tối thiểu:

```text
Admin:
Email: admin@example.com
Password: admin123

Products:
1. Áo thun basic - còn hàng
2. Quần jeans slimfit - còn hàng
3. Giày sneaker trắng - hết hàng
4. Sản phẩm bị ẩn - không hiển thị với khách hàng
```

---

# Acceptance Criteria chính cho MVP

## Khách hàng

- Xem danh sách sản phẩm
- Xem chi tiết sản phẩm
- Thêm sản phẩm vào giỏ hàng
- Cập nhật số lượng trong giỏ
- Xóa sản phẩm khỏi giỏ
- Checkout không cần đăng nhập
- Backend tự tính tổng tiền, không tin giá từ frontend

## Admin

- Đăng nhập admin
- Xem danh sách đơn hàng
- Xem chi tiết đơn hàng
- Cập nhật trạng thái đơn hàng
- Quản lý sản phẩm: tạo, sửa, ẩn/hiện, cập nhật tồn kho

## Bảo mật tối thiểu

- Route admin yêu cầu đăng nhập
- API admin yêu cầu token hợp lệ
- Mật khẩu admin không lưu plain text
- Không cho khách hàng gọi API quản trị
- Tổng tiền đơn hàng phải được tính ở backend

---

# Task Packet cần gửi lại cho các Agent

## Wave 1 — Product & Architecture

### product-agent

```text
Objective:
Tạo PRD cho MVP bán hàng trực tuyến.

Deliverables:
- docs/PRD.md
- Acceptance Criteria theo từng module: customer, cart, checkout, admin, security

Must include:
- Product list
- Product detail
- Cart
- Checkout
- Admin login
- Product management
- Order management
```

### architecture-agent

```text
Objective:
Tạo technical spec và API contract cho MVP.

Deliverables:
- docs/technical-spec.md
- docs/api-contract.md

Tech proposal:
- Frontend: React + Vite
- Backend: Node.js + Express
- Database: SQLite local
- Auth: JWT admin
```

---

## Wave 2 — Implementation

### frontend-agent

```text
Objective:
Xây dựng giao diện MVP bán hàng.

Allowed files:
- frontend/**

Forbidden files:
- backend/**
- docs/api-contract.md nếu đã được chốt

Required pages:
- Home / Product List
- Product Detail
- Cart
- Checkout
- Admin Login
- Admin Products
- Admin Orders

Acceptance:
- Chạy được bằng npm run dev
- Gọi API đúng theo docs/api-contract.md
- Responsive cơ bản cho mobile/tablet/desktop
```

### backend-agent

```text
Objective:
Xây dựng backend API cho MVP bán hàng.

Allowed files:
- backend/**

Forbidden files:
- frontend/**
- docs/PRD.md nếu đã được chốt

Required APIs:
- Public products API
- Cart/checkout order API
- Admin auth API
- Admin product management API
- Admin order management API

Acceptance:
- Chạy được bằng npm run dev
- Có seed data
- Có admin mặc định
- Tổng tiền đơn hàng tính ở backend
- API admin được bảo vệ bằng JWT
```

---

## Wave 3 — QA

QA sẽ được unblock khi có đủ các thông tin sau:

```text
Project path:
D:\Antigravity\projects\user-project

Frontend path:
D:\Antigravity\projects\user-project\frontend

Backend path:
D:\Antigravity\projects\user-project\backend

Frontend URL:
http://localhost:5173

Backend API:
http://localhost:3000/api

Admin:
Email: admin@example.com
Password: admin123

Run frontend:
cd D:\Antigravity\projects\user-project\frontend
npm install
npm run dev

Run backend:
cd D:\Antigravity\projects\user-project\backend
npm install
npm run dev

Seed:
cd D:\Antigravity\projects\user-project\backend
npm run seed
```

---

# PM yêu cầu xác nhận

Để mình tiếp tục điều phối implementation và unblock QA, vui lòng xác nhận một trong hai lựa chọn:

## Lựa chọn A — Dùng project path đề xuất

```text
D:\Antigravity\projects\user-project
```

Mình sẽ dùng cấu trúc:

```text
frontend/
backend/
docs/
README.md
```

## Lựa chọn B — Bạn cung cấp project path khác

Vui lòng gửi:

```text
Project path:
Frontend path:
Backend path:
Database:
Port frontend:
Port backend:
```

---

# Trạng thái chờ

```text
Current Phase: Pre-Implementation / Environment Confirmation
QA Status: BLOCKED
Next Required Action: Confirm project path and stack
```

Sau khi bạn xác nhận path, mình sẽ chuyển sang Wave 1/Wave 2 và chuẩn hóa thông tin để QA có thể kiểm thử với evidence thực tế.