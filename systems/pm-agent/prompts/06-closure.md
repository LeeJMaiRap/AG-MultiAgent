# Prompt 6: Đóng Dự Án

## Input
- Tất cả task đã hoàn thành hoặc được hủy
- Deliverables đã sẵn sàng

## Nhiệm vụ

### Bước 1: Kiểm tra deliverables
Đối chiếu với:
- Success criteria
- Scope đã chốt
- Requirements
- Acceptance criteria

Liệt kê:
- Cái gì hoàn thành
- Cái gì chưa hoàn thành
- Cái gì là future work

### Bước 2: Xác nhận với user
Trình bày:
- Đã làm gì
- Kết quả đạt được
- Cái gì chưa làm
- Cái gì là future work
- Xin user xác nhận

### Bước 3: Tạo final report
Tạo file `projects/[project-name]/05-closure/final-report.md` với:
- Executive summary
- Project overview
- Objectives achievement
- Deliverables
- Final metrics (schedule, budget, quality, scope)
- Lessons learned
- Sign-off

### Bước 4: Tạo lessons learned
Tạo file `projects/[project-name]/05-closure/lessons-learned.md` với:
- What went well
- What could be improved
- Key insights
- Recommendations
- Metrics summary
- Knowledge transfer

### Bước 5: Archive tài liệu
- Tất cả file đã tạo
- Tất cả task board
- Tất cả issue/risk/change log
- Tất cả báo cáo

### Bước 6: Cập nhật memory
Cập nhật `agent-core/memory/observations/pm-projects.md`:
- Tên dự án
- Kết quả
- Bài học
- Liên kết đến final report

### Bước 7: Đánh dấu đóng
- Task board status = Closed
- Project status = Closed
- Tất cả open issues chuyển sang backlog/future work

### Bước 8: Báo cáo lại
Trình bày:
- Dự án đã đóng
- Kết quả cuối cùng
- Bài học chính
- Cảm ơn user

## Output
- final-report.md
- lessons-learned.md
- Dự án đóng chính thức
- Tri thức được lưu trữ
