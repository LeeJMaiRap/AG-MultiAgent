# Prompt 3: Tạo Task Board

## Input
- WBS đã hoàn thành
- Schedule đã chốt
- Rules đã định nghĩa

## Nhiệm vụ

### Bước 1: Chuyển WBS thành task
Mỗi task cần:
- ID (TASK-001, TASK-002, ...)
- Tên
- Mô tả chi tiết
- Input (file nào cần đọc)
- Output (file nào cần tạo/sửa)
- Acceptance criteria
- Priority (High/Medium/Low)
- Dependency
- Assignee (PM Agent hoặc Worker)
- Status (Not Started)
- Estimate (hours)

### Bước 2: Phân loại task
- **Loại A (PM Agent tự làm):** Tài liệu, phân tích, cập nhật trạng thái
- **Loại B (giao Worker):** Code, triển khai, kiểm tra
- **Loại C (cần approval):** Thay đổi scope, chốt kết quả

### Bước 3: Sắp xếp thứ tự
- Task mở đường trước
- Task dependency thấp trước
- Task giảm rủi ro trước
- Task tạo artifact quan trọng trước

### Bước 4: Tạo task-board.md
Tạo file `projects/[project-name]/03-execution/task-board.md` với:
- Backlog (chưa bắt đầu)
- In Progress (đang làm)
- Done (hoàn thành)
- Blocked (bị chặn)
- Summary (tổng số, % hoàn thành)

### Bước 5: Chuẩn bị task prompt
Cho mỗi task giao Worker, chuẩn bị prompt rõ ràng:
- Mục tiêu task
- Input file
- Output file
- Acceptance criteria
- Điều gì không được làm
- Khi nào báo blocker

### Bước 6: Báo cáo lại
Trình bày:
- Task board đã tạo
- Tổng số task
- Thứ tự thực thi
- Task đầu tiên sẵn sàng
- Kế hoạch tiếp theo

## Output
- task-board.md
- Task prompts cho worker
- Sẵn sàng bắt đầu execution
