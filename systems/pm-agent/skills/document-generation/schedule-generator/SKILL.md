---
name: schedule-generator
description: Tạo file `02-planning/schedule.md` - lịch trình dự án với milestones, timeline, gantt chart và critical path từ WBS, project plan hoặc spec; dùng khi cần chuyển task thành timeline cụ thể với target date, duration và dependencies để theo dõi tiến độ.
---

# Schedule Generator

## Mục tiêu

Tạo tài liệu Project Schedule để chuyển WBS và plan thành lịch trình cụ thể với timeline, milestones và critical path, giúp theo dõi tiến độ và điều chỉnh khi cần.

Skill này giúp:
- xác định milestones quan trọng với target date
- tạo timeline cho từng task/phase
- vẽ gantt chart dạng markdown table
- xác định critical path
- tính toán tổng duration và forecast end date

## Dùng khi nào

Dùng skill này khi:
- đã có WBS hoặc project plan với effort estimation
- cần chuyển từ "task list" sang "timeline"
- cần xác định milestones và target dates
- cần theo dõi tiến độ theo thời gian

## Không dùng khi nào

Không dùng skill này khi:
- chưa có WBS hoặc plan rõ ràng
- mục tiêu là tạo task-board vận hành hằng ngày (dùng `task-board-builder`)
- chỉ cần danh sách task, không cần timeline
- dự án quá linh hoạt để có schedule cố định

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- WBS với effort estimation
- project plan với phases và duration
- start date hoặc target end date

## Input tùy chọn

- dependencies giữa các task
- resource availability
- working hours per day
- buffer time
- constraints về deadline

## Output

Output là file `schedule.md` với 4 phần chính:

1. **Milestones** - các mốc quan trọng
2. **Timeline/Gantt Chart** - lịch trình chi tiết
3. **Critical Path** - chuỗi task quan trọng nhất
4. **Summary** - tổng quan duration và dates

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/schedule-template.md`.

## Quy tắc xử lý

### 1. Milestones phải phản ánh các mốc quan trọng
Milestones không phải là task thường, mà là:
- kết thúc một phase lớn
- deliverable quan trọng
- decision point
- go/no-go checkpoint

### 2. Timeline phải tính toán dựa trên dependencies
Không được gán date ngẫu nhiên. Phải:
- tính từ start date
- tôn trọng dependencies
- cộng dồn effort theo thứ tự
- xem xét resource availability

### 3. Gantt chart phải dễ đọc
Gantt chart dạng markdown table phải có:
- task name
- start date
- end date
- duration
- status
- progress (nếu có)

### 4. Critical path phải chính xác
Critical path là chuỗi task:
- không có slack time
- nếu trễ sẽ làm trễ toàn dự án
- thường là chuỗi dài nhất

### 5. Summary phải có thông tin hữu ích và giải thích variance
Summary cần:
- total duration
- start date
- planned end date
- buffer time (nếu có)
- current forecast (nếu đang execution)
- **variance explanation:** nếu forecast lệch planned, phải giải thích tại sao (+2 days do..., -1 day because...)

### 6. Dates phải realistic
Không được đặt deadline phi thực tế. Nếu input có constraint về deadline nhưng không khả thi, phải ghi chú rõ.

### 7. Phải có cơ chế tracking
Schedule không chỉ là plan ban đầu, mà phải:
- có cột status
- có cột actual date
- có cột progress
- dễ cập nhật khi execution

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Start date là khi nào?
- Các phase/milestone chính là gì?
- Task nào phụ thuộc task nào?
- Critical path là gì?
- Có constraint về deadline không?
- Có buffer time không?
- Resource làm việc bao nhiêu giờ/ngày?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `wbs-generator`
- `project-plan-generator`

Và hỗ trợ cho:
- `task-board-builder`
- execution tracking
- status reporting

Schedule là công cụ theo dõi tiến độ chính trong execution.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/02-planning/schedule.md
```

File này là timeline reference cho toàn bộ execution.

## Tiêu chí hoàn thành tốt

Một schedule tốt khi:
- milestones rõ ràng, có ý nghĩa
- timeline tính toán dựa trên dependencies
- gantt chart dễ đọc
- critical path chính xác
- summary đầy đủ thông tin
- có cơ chế tracking progress
- realistic và có buffer

## Lỗi thường gặp cần tránh

- milestones quá nhiều hoặc không có ý nghĩa
- timeline không tính dependencies
- gantt chart khó đọc
- critical path sai
- không có summary
- dates phi thực tế
- không có cơ chế tracking

## Cách dùng ngắn gọn

1. Đọc WBS / project plan
2. Xác định start date và milestones
3. Tính timeline dựa trên dependencies và effort
4. Tạo gantt chart
5. Xác định critical path
6. Tạo summary
7. Xuất file `schedule.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ schedule thực tế
- Tham khảo: `systems/pm-agent/templates/schedule-template.md`
- Tham khảo: `projects/active/web-ban-hang/02-planning/schedule.md`
