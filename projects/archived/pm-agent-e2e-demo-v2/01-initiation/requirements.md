# Requirements Document: Hệ thống quản lý công việc nội bộ

## 1. Business Requirements
### BR-001: Quản lý công việc tập trung
- **Mô tả:** Tạo nền tảng nội bộ để team quản lý task tại một nơi.
- **Lý do:** Giảm rối do dùng chat và file rời.
- **Priority:** High
- **Status:** Approved

### BR-002: Cộng tác nội bộ rõ ràng hơn
- **Mô tả:** Hỗ trợ giao việc, deadline và comment để cộng tác tốt hơn.
- **Lý do:** Team cần theo dõi trách nhiệm và tiến độ rõ ràng.
- **Priority:** High
- **Status:** Approved

## 2. Functional Requirements
### FR-001: Tạo task
- **Mô tả:** Người dùng có thể tạo task mới.
- **Acceptance Criteria:**
  - [ ] Nhập được title và description
  - [ ] Lưu task thành công
  - [ ] Task xuất hiện ngay trong danh sách

### FR-002: Giao owner và deadline
- **Mô tả:** Gán owner và deadline cho task.
- **Acceptance Criteria:**
  - [ ] Chọn được owner
  - [ ] Đặt được deadline
  - [ ] Dữ liệu lưu đúng

### FR-003: Cập nhật trạng thái task
- **Mô tả:** Chuyển trạng thái Todo/In Progress/Done/Blocked.
- **Acceptance Criteria:**
  - [ ] Có trạng thái rõ ràng
  - [ ] Đổi trạng thái được
  - [ ] Trạng thái hiển thị đúng trên danh sách/task detail

### FR-004: Comment trong task
- **Mô tả:** Người dùng có thể trao đổi trong task.
- **Acceptance Criteria:**
  - [ ] Thêm comment được
  - [ ] Hiển thị đúng task
  - [ ] Có thời gian và người viết

### FR-005: Dashboard cơ bản
- **Mô tả:** Hiển thị tổng quan số task theo trạng thái và hỗ trợ mở rộng nhẹ nếu còn thời gian.
- **Acceptance Criteria:**
  - [ ] Hiển thị tổng task
  - [ ] Hiển thị số task theo trạng thái
  - [ ] Dễ đọc trên web nội bộ

## 3. Non-Functional Requirements
- **NFR-001 Usability:** Dễ dùng cho team nhỏ, không cần đào tạo phức tạp.
- **NFR-002 Security:** Có xác thực và phân quyền cơ bản.
- **NFR-003 Maintainability:** API contract và data model phải rõ để tránh rework.
- **NFR-004 Performance:** Danh sách task và dashboard cơ bản phản hồi đủ nhanh với quy mô team nhỏ.

## 4. User Stories
- **US-001:** Là thành viên team, tôi muốn tạo task để theo dõi việc cần làm.
- **US-002:** Là quản lý, tôi muốn giao người phụ trách để rõ trách nhiệm.
- **US-003:** Là thành viên team, tôi muốn comment trong task để trao đổi đúng ngữ cảnh.

## 5. Traceability Matrix
| Requirement ID | Type | Priority | Status | Linked Tasks |
|----------------|------|----------|--------|--------------|
| BR-001 | Business | High | Approved | TASK-001, TASK-002, TASK-003 |
| BR-002 | Business | High | Approved | TASK-002, TASK-004 |
| FR-001 | Functional | High | Approved | TASK-002 |
| FR-002 | Functional | High | Approved | TASK-003 |
| FR-003 | Functional | High | Approved | TASK-004 |
| FR-004 | Functional | Medium | Approved | TASK-006 |
| FR-005 | Functional | Medium | Approved | TASK-007 |
