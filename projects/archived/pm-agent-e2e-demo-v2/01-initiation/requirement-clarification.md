# Requirement Clarification

## 1. Tóm tắt yêu cầu gốc
Cần xây dựng một hệ thống web nội bộ để quản lý công việc cho team nhỏ, thay thế cách làm việc rời rạc qua chat và file lẻ. Hệ thống ưu tiên MVP trong 6 tuần, nguồn lực nhỏ, ngân sách hạn chế, và có thể cắt bớt các tính năng phụ nếu timeline căng.

## 2. Mục tiêu chính
- Tạo hệ thống quản lý task nội bộ tập trung, dễ dùng cho team nhỏ
- Hỗ trợ giao người phụ trách, deadline, comment và theo dõi trạng thái task
- Ra được MVP usable trong khoảng 6 tuần với nguồn lực hiện có

## 3. Phạm vi sơ bộ
### Bao gồm
- Hệ thống web nội bộ
- Tạo task
- Giao người phụ trách
- Deadline
- Comment trong task
- Theo dõi trạng thái task
- Dashboard đơn giản nếu còn đủ nguồn lực

### Chưa rõ / chưa chốt
- Dashboard MVP cần hiển thị đến mức nào
- Có cần attachment trong MVP hay không
- Phân quyền có dừng ở admin/member hay cần chi tiết hơn
- Có cần lưu lịch sử thay đổi task/audit trail không

### Ngoài phạm vi (nếu suy ra được)
- Mobile app native
- Analytics nâng cao ở giai đoạn đầu
- Tích hợp hệ thống ngoài phức tạp

## 4. Danh sách yêu cầu đã bóc tách
### Yêu cầu nghiệp vụ
- Team cần quản lý công việc tập trung tại một nơi
- Giảm phụ thuộc vào chat và file rời để tránh thất lạc thông tin
- Có cách nhìn tổng quan tiến độ công việc nội bộ

### Yêu cầu chức năng
- Tạo task
- Giao người phụ trách cho task
- Đặt deadline cho task
- Cập nhật trạng thái task
- Comment trong task
- Dashboard tổng quan cơ bản

### Yêu cầu phi chức năng
- Dùng nội bộ
- Ưu tiên MVP trong 6 tuần
- Chi phí thấp
- Dễ dùng cho team nhỏ
- Có thể dùng ổn trên desktop; mobile browser cơ bản là điểm cộng nhưng không phải trọng tâm

### Ràng buộc / giả định
- 1 backend, 1 frontend, 1 tester part-time
- Ngân sách nhỏ
- Có thể cắt attachment hoặc analytics nâng cao nếu timeline căng
- Người dùng nội bộ có thể chấp nhận quy trình đơn giản hơn sản phẩm public

## 5. Điểm còn mơ hồ / chưa đủ dữ liệu
- Chỉ số cụ thể trên dashboard MVP
- Mức độ chi tiết của phân quyền
- Có cần attachment ngay từ MVP không
- Có cần audit trail / activity history không
- Tiêu chí thành công định lượng ngoài deadline 6 tuần

## 6. Câu hỏi cần xác nhận
1. Dashboard MVP cần hiển thị những chỉ số nào?
   - **Priority:** High
   - **Context:** Ảnh hưởng trực tiếp đến effort frontend, backend aggregate logic và khả năng giữ MVP trong 6 tuần.
   - **Options:**
     - A. Chỉ tổng số task và số task theo trạng thái
     - B. A + số task theo owner
     - C. B + số task overdue / sắp tới hạn
     - D. C + biểu đồ/trend đơn giản

2. Có cần attachment trong MVP hay để phase sau?
   - **Priority:** Medium
   - **Context:** Nếu cần ngay thì phải thêm upload flow, file storage, validation và policy bảo mật cơ bản.
   - **Options:**
     - A. Không cần trong MVP, để phase sau
     - B. Chỉ cần upload file đơn giản trong MVP
     - C. Cần đầy đủ attachment management ngay từ MVP

3. Phân quyền MVP nên dừng ở mức nào?
   - **Priority:** High
   - **Context:** Ảnh hưởng đến data model, API authorization và UI logic từ đầu.
   - **Options:**
     - A. 2 role: admin/member
     - B. 3 role: admin/member/viewer
     - C. Permission chi tiết theo hành động (create/edit/delete/assign)

4. Có cần lưu lịch sử thay đổi task (audit trail) trong MVP không?
   - **Priority:** Medium
   - **Context:** Nếu cần thì phải thêm event history hoặc activity log, làm tăng scope backend và UI.
   - **Options:**
     - A. Không cần trong MVP
     - B. Chỉ cần lưu comment và trạng thái cuối cùng
     - C. Cần activity history cơ bản (ai đổi gì, khi nào)

## 7. Đề xuất bước tiếp theo
- Chốt 4 câu hỏi xác nhận ưu tiên trên
- Tạo charter.md với scope MVP đã khóa
- Tạo requirements.md và spec.md dựa trên các quyết định đã chốt
