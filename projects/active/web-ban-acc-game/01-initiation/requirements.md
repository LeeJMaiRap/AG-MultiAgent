# Requirements Document: Web Bán Acc Game

## 1. Business Requirements

### BR-001: Nền tảng bán acc game trực tuyến
- **Mô tả:** Xây dựng website cho phép khách xem, lọc, và liên hệ mua tài khoản game
- **Lý do:** Tạo kênh bán acc game chuyên nghiệp, dễ quản lý, tăng niềm tin khách hàng
- **Priority:** High
- **Status:** Draft

### BR-002: Công cụ quản lý acc cho admin
- **Mô tả:** Cung cấp trang admin để anh CRUD acc game dễ dàng
- **Lý do:** Cần quản lý danh sách acc, cập nhật trạng thái còn/hết, thay đổi giá và thông tin nhanh
- **Priority:** High
- **Status:** Draft

## 2. Functional Requirements

### FR-001: Hiển thị danh sách acc game
- **Mô tả:** Khách xem danh sách acc với ảnh, tên game, rank, giá, trạng thái
- **Acceptance Criteria:**
  - [ ] Hiển thị grid acc rõ ràng
  - [ ] Mỗi acc có ảnh đại diện, tên game, rank, giá
  - [ ] Hiển thị trạng thái còn hàng / đã bán
  - [ ] Responsive mobile + desktop

### FR-002: Lọc acc theo game
- **Mô tả:** Khách lọc acc theo loại game
- **Acceptance Criteria:**
  - [ ] Có bộ lọc theo game
  - [ ] Có thể xem tất cả acc
  - [ ] Kết quả lọc cập nhật đúng

### FR-003: Tìm kiếm acc
- **Mô tả:** Khách tìm acc theo từ khóa cơ bản
- **Acceptance Criteria:**
  - [ ] Tìm theo tên game hoặc mô tả ngắn
  - [ ] Hiển thị "không tìm thấy" nếu rỗng

### FR-004: Xem chi tiết acc
- **Mô tả:** Khách xem chi tiết 1 acc game
- **Acceptance Criteria:**
  - [ ] Hiển thị nhiều ảnh nếu có
  - [ ] Hiển thị game, rank, skin/tài nguyên nổi bật, giá, mô tả
  - [ ] Hiển thị trạng thái còn/hết
  - [ ] Hiển thị thông tin liên hệ để mua

### FR-005: Liên hệ mua acc
- **Mô tả:** Khách liên hệ mua qua SĐT/Facebook
- **Acceptance Criteria:**
  - [ ] Có nút/cụm thông tin SĐT
  - [ ] Có link Facebook hoặc Messenger
  - [ ] CTA rõ ràng ở trang chi tiết acc

### FR-006: Admin đăng nhập
- **Mô tả:** Chỉ admin mới vào được khu vực quản trị
- **Acceptance Criteria:**
  - [ ] Có trang login admin
  - [ ] Sai thông tin thì báo lỗi
  - [ ] Đăng nhập thành công thì vào dashboard

### FR-007: Admin xem danh sách acc
- **Mô tả:** Admin xem toàn bộ acc trong hệ thống
- **Acceptance Criteria:**
  - [ ] Bảng danh sách acc
  - [ ] Hiển thị game, giá, trạng thái, ngày cập nhật
  - [ ] Có action sửa/xóa

### FR-008: Admin thêm acc mới
- **Mô tả:** Admin tạo acc mới
- **Acceptance Criteria:**
  - [ ] Form nhập game, tiêu đề, rank, giá, mô tả
  - [ ] Upload ảnh
  - [ ] Chọn trạng thái
  - [ ] Lưu thành công thì hiển thị ngoài web khách

### FR-009: Admin sửa acc
- **Mô tả:** Admin cập nhật thông tin acc
- **Acceptance Criteria:**
  - [ ] Sửa được mọi field chính
  - [ ] Cập nhật trạng thái còn/hết
  - [ ] Ảnh mới thay được ảnh cũ

### FR-010: Admin xóa acc
- **Mô tả:** Admin xóa acc khỏi hệ thống
- **Acceptance Criteria:**
  - [ ] Có xác nhận trước khi xóa
  - [ ] Xóa xong không còn hiển thị ngoài web khách

## 3. Non-Functional Requirements

### NFR-001: Simplicity
- UI đơn giản, sạch, dễ dùng

### NFR-002: Performance
- Trang danh sách acc load nhanh ở mức dữ liệu nhỏ-trung bình

### NFR-003: Responsive
- Dùng tốt trên điện thoại và desktop

### NFR-004: Security
- Khu admin có authentication
- Không lộ route admin public không bảo vệ
- Validate input cơ bản

## 4. Proposed MVP Scope
- Public listing page
- Filter theo game
- Chi tiết acc
- Contact CTA
- Admin login
- Admin CRUD acc
- Image upload
- Deploy public

## 5. Open Questions
- [ ] Danh sách game ưu tiên ban đầu là gì?
- [ ] SĐT liên hệ chính của anh?
- [ ] Facebook/Messenger link nào dùng cho CTA?
- [ ] Có cần gắn nhãn nổi bật như "hot", "giá tốt", "mới cập nhật" không?
