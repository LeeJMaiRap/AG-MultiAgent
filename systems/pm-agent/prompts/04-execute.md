# Prompt 4: Thực thi Task

## Input
- Task board đã tạo
- Task đầu tiên được chọn

## Nhiệm vụ

### Bước 1: Chọn task tiếp theo
Dựa trên:
- Dependency đã thỏa chưa?
- Priority?
- Blocker hiện tại?
- Giá trị tạo ra?

### Bước 2: Quyết định tự làm hay giao worker?

**Nếu tự làm:**
- Thực hiện task
- Tạo/sửa file cần thiết
- Kiểm tra acceptance criteria
- Cập nhật task-board.md

**Nếu giao worker:**
- Spawn sub-agent worker
- Truyền prompt rõ ràng
- Yêu cầu output cụ thể
- Chờ kết quả

### Bước 3: Review kết quả
- Output có đủ không?
- Có đúng file cần sửa không?
- Có đúng acceptance criteria không?
- Có phát sinh issue/risk mới không?

### Bước 4: Cập nhật tài liệu dự án
Cập nhật ngay:
- `task-board.md` - đánh dấu done/blocked/rework
- `issue-log.md` - nếu có lỗi
- `change-log.md` - nếu có thay đổi
- `status-dashboard.md` - cập nhật tiến độ
- `risk-register.md` - nếu có rủi ro mới

### Bước 5: Quyết định hành động tiếp theo
- Đánh dấu done → chọn task tiếp theo
- Yêu cầu rework → giao lại worker
- Escalate blocker → hỏi user
- Xin xác nhận → chờ user

### Bước 6: Báo cáo lại
Trình bày:
- Task vừa hoàn thành
- Kết quả đạt được
- Vấn đề phát sinh (nếu có)
- Task tiếp theo
- Tiến độ tổng thể

## Output
- Task completed hoặc escalated
- Tài liệu dự án được cập nhật
- Sẵn sàng task tiếp theo
