## PM Orchestrator — Phân tích brief MVP bán hàng trực tuyến

### 1. Mục tiêu MVP
Xây dựng phiên bản tối thiểu của hệ thống bán hàng trực tuyến cho phép:

- Khách hàng xem danh sách sản phẩm
- Xem chi tiết sản phẩm
- Thêm sản phẩm vào giỏ hàng
- Tạo đơn hàng
- Quản trị cơ bản sản phẩm và đơn hàng
- Theo dõi trạng thái đơn hàng ở mức đơn giản

### 2. Phạm vi MVP đề xuất

#### Chức năng khách hàng
- Trang chủ / danh sách sản phẩm
- Tìm kiếm hoặc lọc cơ bản
- Trang chi tiết sản phẩm
- Giỏ hàng
- Checkout tạo đơn hàng
- Xác nhận đặt hàng thành công

#### Chức năng quản trị
- Đăng nhập admin đơn giản
- CRUD sản phẩm
- Xem danh sách đơn hàng
- Cập nhật trạng thái đơn hàng

#### Ngoài phạm vi MVP ban đầu
- Thanh toán online
- Giao hàng tự động
- Voucher / khuyến mãi phức tạp
- Đánh giá sản phẩm
- Chat realtime
- Multi-vendor marketplace

---

## 3. Sơ đồ thực thi Multi-Agent

```text
Wave 1: Khởi động & Đặc tả
 ├── Product Agent
 │    └── PRD, user stories, acceptance criteria
 └── Architecture Agent
      └── Tech spec, database schema, API contract

Wave 2: Thực thi song song
 ├── Frontend Agent
 │    └── UI khách hàng + admin dashboard
 └── Backend Agent
      └── API sản phẩm, giỏ hàng, đơn hàng, admin auth

Wave 3: Tích hợp & Kiểm thử
 └── QA Agent
      └── Test API, UI flow, business logic, bug report

Wave 4: Đóng gói
 └── PM Orchestrator
      └── Tổng hợp final-report.md, kiểm tra nghiệm thu
```

---

## 4. Phân rã công việc sơ bộ

### Product Agent
**Nhiệm vụ:**
- Làm rõ chân dung người dùng:
  - Khách mua hàng
  - Admin cửa hàng
- Viết PRD cho MVP
- Định nghĩa user stories
- Đưa ra acceptance criteria cho từng flow chính

**Deliverables:**
- `docs/prd.md`
- `docs/user-stories.md`
- `docs/acceptance-criteria.md`

---

### Architecture Agent
**Nhiệm vụ:**
- Đề xuất kiến trúc tổng thể
- Thiết kế database schema
- Thiết kế API contract
- Quy định phân tách frontend/backend
- Đề xuất cấu trúc thư mục dự án

**Deliverables:**
- `docs/technical-spec.md`
- `docs/api-contract.md`
- `docs/database-schema.md`

---

### Frontend Agent
**Nhiệm vụ:**
- Xây dựng giao diện khách hàng:
  - Trang danh sách sản phẩm
  - Trang chi tiết sản phẩm
  - Giỏ hàng
  - Checkout
- Xây dựng giao diện admin:
  - Đăng nhập
  - Quản lý sản phẩm
  - Quản lý đơn hàng
- Kết nối API theo contract

**Deliverables:**
- UI pages/components
- API integration layer
- Form validation cơ bản

---

### Backend Agent
**Nhiệm vụ:**
- Xây dựng API:
  - Products
  - Cart/session cart hoặc client-side cart support
  - Orders
  - Admin auth
- Thiết kế database models
- Seed dữ liệu mẫu
- Xử lý validation và error response

**Deliverables:**
- Backend endpoints
- Database migrations/schema
- Seed sample products
- API documentation cập nhật nếu cần

---

### QA Agent
**Nhiệm vụ:**
- Kiểm thử flow người mua:
  - Xem sản phẩm
  - Thêm giỏ hàng
  - Checkout
  - Tạo đơn hàng thành công
- Kiểm thử flow admin:
  - Đăng nhập
  - CRUD sản phẩm
  - Cập nhật trạng thái đơn hàng
- Kiểm thử API contract
- Ghi nhận bug và bằng chứng kiểm thử

**Deliverables:**
- `docs/test-plan.md`
- `docs/qa-report.md`
- Danh sách bug/blocker nếu có

---

## 5. Quality Gates

### Gate 1 — Sau đặc tả
Chỉ chuyển sang build khi có:
- PRD
- Acceptance criteria
- API contract
- Database schema

### Gate 2 — Sau triển khai
Chỉ chuyển sang QA khi:
- Frontend gọi được API thật hoặc mock chuẩn contract
- Backend endpoint chạy được
- Có dữ liệu mẫu
- Không có lỗi build nghiêm trọng

### Gate 3 — Trước bàn giao
Chỉ hoàn tất khi:
- Flow mua hàng chạy end-to-end
- Admin quản lý được sản phẩm và đơn hàng
- QA có bằng chứng test
- Có báo cáo tổng kết

---

## 6. Cần làm rõ trước khi bắt đầu

1. MVP dùng web app đơn giản hay cần responsive mobile-first?
2. Có yêu cầu đăng ký/đăng nhập khách hàng không, hay checkout không cần tài khoản?
3. Thanh toán chỉ là “COD / đặt hàng” hay cần tích hợp cổng thanh toán?
4. Admin có một tài khoản cố định hay cần quản lý nhiều admin?
5. Dự án ưu tiên tốc độ demo hay nền tảng mở rộng lâu dài?

Đề xuất mặc định: **MVP web app responsive, khách hàng không cần đăng nhập, thanh toán COD, admin một tài khoản, ưu tiên demo nhanh nhưng cấu trúc đủ mở rộng.**