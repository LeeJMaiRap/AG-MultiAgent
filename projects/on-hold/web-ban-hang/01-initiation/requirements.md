# Requirements Document: Trang Web Bán Hàng

## 1. Business Requirements

### BR-001: Hệ thống bán hàng trực tuyến
- **Mô tả:** Xây dựng nền tảng web cho phép người dùng xem, tìm kiếm, và mua sản phẩm trực tuyến
- **Lý do:** Đáp ứng nhu cầu bán hàng trực tuyến, tiếp cận khách hàng rộng hơn
- **Priority:** High
- **Status:** Approved

### BR-002: Quản lý sản phẩm và đơn hàng
- **Mô tả:** Cung cấp công cụ quản lý sản phẩm và đơn hàng cho admin
- **Lý do:** Cần quản lý kho hàng và theo dõi đơn hàng
- **Priority:** High
- **Status:** Approved

## 2. Functional Requirements

### FR-001: Hiển thị danh sách sản phẩm
- **Mô tả:** Người dùng có thể xem danh sách sản phẩm với hình ảnh, tên, giá
- **Input:** Truy cập trang danh sách sản phẩm
- **Process:** Lấy dữ liệu từ database, hiển thị dạng grid/list
- **Output:** Danh sách sản phẩm với phân trang
- **Acceptance Criteria:**
  - [ ] Hiển thị ít nhất 12 sản phẩm mỗi trang
  - [ ] Có phân trang
  - [ ] Có hình ảnh, tên, giá cho mỗi sản phẩm
  - [ ] Responsive trên mobile và desktop

### FR-002: Tìm kiếm sản phẩm
- **Mô tả:** Người dùng có thể tìm kiếm sản phẩm theo tên
- **Input:** Nhập từ khóa vào ô tìm kiếm
- **Process:** Query database theo tên sản phẩm
- **Output:** Danh sách sản phẩm phù hợp
- **Acceptance Criteria:**
  - [ ] Tìm kiếm theo tên sản phẩm
  - [ ] Hiển thị kết quả real-time hoặc sau khi nhấn Enter
  - [ ] Hiển thị "Không tìm thấy" nếu không có kết quả

### FR-003: Lọc sản phẩm
- **Mô tả:** Người dùng có thể lọc sản phẩm theo danh mục, giá
- **Input:** Chọn bộ lọc
- **Process:** Query database theo điều kiện lọc
- **Output:** Danh sách sản phẩm đã lọc
- **Acceptance Criteria:**
  - [ ] Lọc theo danh mục
  - [ ] Lọc theo khoảng giá
  - [ ] Có thể kết hợp nhiều bộ lọc

### FR-004: Xem chi tiết sản phẩm
- **Mô tả:** Người dùng có thể xem thông tin chi tiết sản phẩm
- **Input:** Click vào sản phẩm
- **Process:** Lấy thông tin chi tiết từ database
- **Output:** Trang chi tiết với hình ảnh lớn, mô tả đầy đủ, giá, nút thêm vào giỏ
- **Acceptance Criteria:**
  - [ ] Hiển thị hình ảnh lớn
  - [ ] Hiển thị mô tả chi tiết
  - [ ] Hiển thị giá
  - [ ] Có nút "Thêm vào giỏ hàng"
  - [ ] Có thể chọn số lượng

### FR-005: Giỏ hàng
- **Mô tả:** Người dùng có thể thêm/xóa/sửa sản phẩm trong giỏ hàng
- **Input:** Thao tác với giỏ hàng
- **Process:** Cập nhật session/localStorage
- **Output:** Giỏ hàng được cập nhật
- **Acceptance Criteria:**
  - [ ] Thêm sản phẩm vào giỏ
  - [ ] Xóa sản phẩm khỏi giỏ
  - [ ] Thay đổi số lượng
  - [ ] Hiển thị tổng tiền
  - [ ] Icon giỏ hàng hiển thị số lượng sản phẩm

### FR-006: Thanh toán
- **Mô tả:** Người dùng có thể đặt hàng
- **Input:** Điền thông tin giao hàng, chọn phương thức thanh toán
- **Process:** Lưu đơn hàng vào database
- **Output:** Đơn hàng được tạo, hiển thị thông báo thành công
- **Acceptance Criteria:**
  - [ ] Form nhập thông tin giao hàng (tên, địa chỉ, SĐT)
  - [ ] Chọn phương thức thanh toán (COD, chuyển khoản)
  - [ ] Xác nhận đơn hàng
  - [ ] Hiển thị thông báo thành công
  - [ ] Gửi email xác nhận (optional cho MVP)

### FR-007: Đăng ký tài khoản
- **Mô tả:** Người dùng có thể tạo tài khoản
- **Input:** Email, mật khẩu, tên
- **Process:** Lưu thông tin vào database, hash password
- **Output:** Tài khoản được tạo
- **Acceptance Criteria:**
  - [ ] Form đăng ký với email, password, tên
  - [ ] Validate email format
  - [ ] Validate password strength
  - [ ] Kiểm tra email đã tồn tại
  - [ ] Hash password trước khi lưu

### FR-008: Đăng nhập
- **Mô tả:** Người dùng có thể đăng nhập
- **Input:** Email, mật khẩu
- **Process:** Xác thực thông tin, tạo session/token
- **Output:** Đăng nhập thành công
- **Acceptance Criteria:**
  - [ ] Form đăng nhập
  - [ ] Xác thực thông tin
  - [ ] Tạo session/JWT token
  - [ ] Redirect về trang chủ hoặc trang trước đó

### FR-009: Quản lý sản phẩm (Admin)
- **Mô tả:** Admin có thể thêm/sửa/xóa sản phẩm
- **Input:** Thông tin sản phẩm
- **Process:** CRUD operations trên database
- **Output:** Sản phẩm được cập nhật
- **Acceptance Criteria:**
  - [ ] Trang danh sách sản phẩm admin
  - [ ] Form thêm sản phẩm mới
  - [ ] Form sửa sản phẩm
  - [ ] Nút xóa sản phẩm
  - [ ] Upload hình ảnh sản phẩm

### FR-010: Quản lý đơn hàng (Admin)
- **Mô tả:** Admin có thể xem và cập nhật trạng thái đơn hàng
- **Input:** Chọn đơn hàng, cập nhật trạng thái
- **Process:** Update database
- **Output:** Trạng thái đơn hàng được cập nhật
- **Acceptance Criteria:**
  - [ ] Danh sách đơn hàng
  - [ ] Xem chi tiết đơn hàng
  - [ ] Cập nhật trạng thái (Pending, Processing, Shipped, Delivered, Cancelled)
  - [ ] Hiển thị thông tin khách hàng

## 3. Non-Functional Requirements

### NFR-001: Performance
- **Mô tả:** Website phải load nhanh
- **Metric:** Trang chủ load < 3 giây

### NFR-002: Responsive Design
- **Mô tả:** Website hoạt động tốt trên mọi thiết bị
- **Metric:** Responsive trên mobile (375px), tablet (768px), desktop (1024px+)

### NFR-003: Security
- **Mô tả:** Bảo mật thông tin người dùng
- **Metric:** Password được hash, SQL injection prevention, XSS prevention

### NFR-004: Usability
- **Mô tả:** Giao diện dễ sử dụng, đẹp mắt
- **Metric:** UI/UX hiện đại, màu sắc hài hòa, navigation rõ ràng

## 4. User Stories

### US-001: Khách hàng muốn mua sản phẩm
- **Acceptance Criteria:**
  - [ ] Xem danh sách sản phẩm
  - [ ] Tìm kiếm sản phẩm
  - [ ] Thêm vào giỏ hàng
  - [ ] Thanh toán
- **Priority:** High
- **Estimate:** 8h

### US-002: Admin muốn quản lý sản phẩm
- **Acceptance Criteria:**
  - [ ] Thêm sản phẩm mới
  - [ ] Sửa thông tin sản phẩm
  - [ ] Xóa sản phẩm
- **Priority:** High
- **Estimate:** 4h

### US-003: Admin muốn quản lý đơn hàng
- **Acceptance Criteria:**
  - [ ] Xem danh sách đơn hàng
  - [ ] Cập nhật trạng thái đơn hàng
- **Priority:** Medium
- **Estimate:** 3h

## 5. Traceability Matrix
| Requirement ID | Type | Priority | Status | Linked Tasks |
|----------------|------|----------|--------|--------------|
| BR-001 | Business | High | Approved | TASK-001 to TASK-008 |
| BR-002 | Business | High | Approved | TASK-009, TASK-010 |
| FR-001 | Functional | High | Approved | TASK-003 |
| FR-002 | Functional | Medium | Approved | TASK-003 |
| FR-003 | Functional | Medium | Approved | TASK-003 |
| FR-004 | Functional | High | Approved | TASK-004 |
| FR-005 | Functional | High | Approved | TASK-005 |
| FR-006 | Functional | High | Approved | TASK-006 |
| FR-007 | Functional | High | Approved | TASK-007 |
| FR-008 | Functional | High | Approved | TASK-007 |
| FR-009 | Functional | High | Approved | TASK-009 |
| FR-010 | Functional | Medium | Approved | TASK-010 |
