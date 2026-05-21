# Requirements Document: Hệ thống quản lý task nội bộ

## 1. Business Requirements

### BR-001: Quản lý task nội bộ hiệu quả
- **Mô tả:** Xây dựng hệ thống web nội bộ để team có thể tạo, phân công và theo dõi task trong một nền tảng tập trung
- **Lý do:** Công cụ hiện tại chưa đáp ứng đủ nhu cầu quản lý công việc của team
- **Priority:** High
- **Status:** Approved

### BR-002: Tăng khả năng cộng tác trong team
- **Mô tả:** Hệ thống cần hỗ trợ comment, đính kèm file và deadline để các thành viên phối hợp tốt hơn
- **Lý do:** Team cần trao đổi trực tiếp trong từng task thay vì phân tán qua nhiều kênh
- **Priority:** High
- **Status:** Approved

## 2. Functional Requirements

### FR-001: Tạo task
- **Mô tả:** Người dùng có thể tạo task mới với tiêu đề, mô tả, deadline và người phụ trách
- **Input:** Form tạo task
- **Process:** Lưu thông tin task vào hệ thống
- **Output:** Task mới được tạo và hiển thị trong danh sách
- **Acceptance Criteria:**
  - [ ] Có form tạo task với các trường cơ bản
  - [ ] Có thể nhập deadline
  - [ ] Có thể chọn người phụ trách
  - [ ] Task mới hiển thị ngay sau khi tạo

### FR-002: Phân công người thực hiện
- **Mô tả:** Người dùng có quyền có thể gán task cho thành viên phù hợp
- **Input:** Chọn task và chọn người phụ trách
- **Process:** Cập nhật owner của task
- **Output:** Task hiển thị đúng người phụ trách mới
- **Acceptance Criteria:**
  - [ ] Có thể chọn người phụ trách từ danh sách thành viên
  - [ ] Hiển thị rõ owner của task
  - [ ] Owner mới được lưu thành công

### FR-003: Theo dõi trạng thái task
- **Mô tả:** Người dùng có thể cập nhật và theo dõi trạng thái task
- **Input:** Chọn trạng thái mới cho task
- **Process:** Cập nhật trạng thái trong hệ thống
- **Output:** Task hiển thị trạng thái mới
- **Acceptance Criteria:**
  - [ ] Có ít nhất các trạng thái Todo, In Progress, Done
  - [ ] Có thể cập nhật trạng thái task
  - [ ] Trạng thái được hiển thị rõ ràng trong danh sách

### FR-004: Comment trong task
- **Mô tả:** Người dùng có thể để lại bình luận trong từng task
- **Input:** Nội dung comment
- **Process:** Lưu comment theo task tương ứng
- **Output:** Comment được hiển thị trong task
- **Acceptance Criteria:**
  - [ ] Có ô nhập comment trong task
  - [ ] Lưu và hiển thị comment đúng task
  - [ ] Hiển thị thời gian và người viết comment

### FR-005: Đính kèm file
- **Mô tả:** Người dùng có thể đính kèm file liên quan vào task
- **Input:** File upload
- **Process:** Upload và liên kết file với task
- **Output:** File đính kèm hiển thị trong task
- **Acceptance Criteria:**
  - [ ] Có thể upload file vào task
  - [ ] Hiển thị danh sách file đã đính kèm
  - [ ] Có thể tải lại file đã upload

### FR-006: Phân quyền người dùng
- **Mô tả:** Hệ thống cần hỗ trợ ít nhất 2 vai trò: admin và member
- **Input:** Thông tin role của user
- **Process:** Kiểm tra quyền trước khi cho phép thao tác
- **Output:** Người dùng chỉ thấy/thực hiện được chức năng phù hợp với role
- **Acceptance Criteria:**
  - [ ] Hệ thống có role admin và member
  - [ ] Admin có quyền quản lý cao hơn member
  - [ ] Member chỉ thao tác trong phạm vi được phép

## 3. Non-Functional Requirements

### NFR-001: Responsive Design
- **Mô tả:** Hệ thống phải dùng tốt trên mobile và desktop
- **Metric:** Responsive tối thiểu trên mobile 375px và desktop 1024px+

### NFR-002: Security
- **Mô tả:** Bảo mật thông tin người dùng và dữ liệu task
- **Metric:** Tài khoản phải có cơ chế xác thực, dữ liệu phân quyền đúng role

### NFR-003: Usability
- **Mô tả:** Giao diện cần đơn giản, dễ học và dễ sử dụng cho team nội bộ
- **Metric:** Người dùng có thể tạo và cập nhật task mà không cần đào tạo phức tạp

## 4. User Stories (nếu dùng Agile)

### US-001: Là thành viên team, tôi muốn tạo task để theo dõi công việc cần làm
- **Acceptance Criteria:**
  - [ ] Có thể tạo task mới
  - [ ] Có thể nhập mô tả và deadline
- **Priority:** High
- **Estimate:** 2h

### US-002: Là quản lý, tôi muốn phân công task để biết ai chịu trách nhiệm việc gì
- **Acceptance Criteria:**
  - [ ] Có thể chọn người phụ trách cho task
  - [ ] Hiển thị rõ owner của task
- **Priority:** High
- **Estimate:** 2h

### US-003: Là thành viên team, tôi muốn comment trong task để trao đổi trực tiếp theo từng công việc
- **Acceptance Criteria:**
  - [ ] Có thể viết comment
  - [ ] Comment hiển thị đúng task
- **Priority:** Medium
- **Estimate:** 2h

## 5. Traceability Matrix
| Requirement ID | Type | Priority | Status | Linked Tasks |
|----------------|------|----------|--------|--------------|
| BR-001 | Business | High | Approved | TASK-001, TASK-002, TASK-003 |
| BR-002 | Business | High | Approved | TASK-004, TASK-005 |
| FR-001 | Functional | High | Approved | TASK-001 |
| FR-002 | Functional | High | Approved | TASK-002 |
| FR-003 | Functional | High | Approved | TASK-003 |
| FR-004 | Functional | Medium | Approved | TASK-004 |
| FR-005 | Functional | Medium | Approved | TASK-005 |
| FR-006 | Functional | High | Approved | TASK-006 |
| NFR-001 | Non-Functional | Medium | Approved | TASK-007 |
| NFR-002 | Non-Functional | High | Approved | TASK-008 |
| NFR-003 | Non-Functional | Medium | Approved | TASK-009 |
