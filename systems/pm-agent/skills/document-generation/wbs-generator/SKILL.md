---
name: wbs-generator
description: Tạo file `02-planning/wbs.md` - phân rã công việc chi tiết từ project plan, spec hoặc requirements; dùng khi cần chia dự án thành cấu trúc phân cấp task với ID, description, effort, dependencies, assigned to và status để chuẩn bị cho task-board và execution.
---

# WBS Generator

## Mục tiêu

Tạo tài liệu Work Breakdown Structure (WBS) để phân rá dự án thành các task cụ thể, có thể theo dõi và thực thi, làm cầu nối giữa planning và execution.

Skill này giúp:
- chia dự án thành cấu trúc phân cấp từ module → feature → task
- gán ID duy nhất cho mỗi task
- ước lượng effort cho từng task
- xác định dependencies giữa các task
- chuẩn bị đầu vào cho task-board và schedule

## Dùng khi nào

Dùng skill này khi:
- đã có project plan hoặc spec
- cần phân rã công việc thành task-level
- cần chuẩn bị cho việc tạo task-board hoặc schedule
- cần ước lượng effort và dependencies chi tiết

## Không dùng khi nào

Không dùng skill này khi:
- đầu vào chưa có plan hoặc spec rõ ràng
- mục tiêu là tạo task-board vận hành hằng ngày (dùng `task-board-builder`)
- mục tiêu là tạo schedule với timeline (dùng `schedule-generator`)
- chỉ cần danh sách việc đơn giản, không cần cấu trúc phân cấp

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- project plan với WBS sơ bộ
- project spec với features chi tiết
- requirements document

## Input tùy chọn

- effort estimation đã có
- dependencies đã xác định
- resource allocation
- priority của từng module/feature

## Output

Output là file `wbs.md` theo cấu trúc phân cấp 4-5 level:

- **Level 1:** Tên dự án
- **Level 2:** Module/Phase chính
- **Level 3:** Feature/Component
- **Level 4:** Task cụ thể
- **Level 5:** Sub-task (nếu cần)

Mỗi task phải có:
- **ID:** TASK-XXX
- **Description:** Mô tả ngắn gọn
- **Estimated effort:** Ước lượng thời gian
- **Dependencies:** Task phụ thuộc
- **Assigned to:** Người/agent phụ trách
- **Status:** Not Started / In Progress / Done
- **Input:** (tùy chọn)
- **Output:** (tùy chọn)

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/wbs-template.md`.

## Quy tắc xử lý

### 1. Cấu trúc phân cấp phải logic
Cấu trúc phải phản ánh đúng bản chất công việc:
- Level 2: Module/Phase lớn
- Level 3: Feature/Component
- Level 4: Task thực thi được

Không được chia cấp quá sâu hoặc quá nông.

### 2. Task ID phải duy nhất và tuần tự
- Format: TASK-001, TASK-002, ...
- Đánh số tuần tự theo thứ tự xuất hiện
- Không được trùng ID

### 3. Task description phải rõ ràng và actionable
Mỗi task phải:
- bắt đầu bằng động từ
- đủ rõ để ai đọc cũng hiểu phải làm gì
- không quá dài (1-2 câu)

Ví dụ tốt:
- "Tạo API endpoint cho user authentication"
- "Implement product search với filter"

Ví dụ xấu:
- "Backend"
- "Làm giao diện"

### 4. Effort estimation phải tương đối hợp lý và breakdown task lớn
Effort không cần chính xác tuyệt đối, nhưng phải:
- phản ánh độ phức tạp tương đối
- có đơn vị rõ ràng (giờ, ngày)
- không quá lệch so với thực tế
- **Nếu task > 16h, nên gợi ý breakdown thành subtask**

Ví dụ:
- TASK-002: 20h → nên chia thành TASK-002a (8h), TASK-002b (12h)

### 5. Dependencies phải chính xác
Dependencies phải:
- chỉ ra task nào phải hoàn thành trước
- không tạo circular dependency
- giúp xác định critical path

### 6. Assigned to phải bám nguồn lực thực tế
Nếu có thông tin về người/agent, phải gán hợp lý.
Nếu chưa rõ, có thể để:
- Worker Agent
- TBD
- Team member

### 7. Phải có summary cuối file
Summary phải bao gồm:
- Total tasks
- Estimated total time
- Critical path (nếu xác định được)

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Dự án có những module/phase chính nào?
- Mỗi module có những feature/component nào?
- Mỗi feature cần những task cụ thể nào để hoàn thành?
- Task nào phụ thuộc task nào?
- Task nào là critical path?
- Effort ước lượng cho từng task là bao nhiêu?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `project-plan-generator`
- `project-spec-generator`

Và là đầu vào cho:
- `task-board-builder`
- `schedule-generator`

WBS là cầu nối quan trọng giữa planning và execution.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/02-planning/wbs.md
```

File này là danh sách task chi tiết nhất trong giai đoạn planning.

## Tiêu chí hoàn thành tốt

Một WBS tốt khi:
- cấu trúc phân cấp logic, dễ đọc
- mỗi task có đủ thông tin (ID, description, effort, dependencies)
- task description rõ ràng, actionable
- effort estimation hợp lý
- dependencies chính xác
- có thể chuyển trực tiếp sang task-board
- có summary tổng quan

## Lỗi thường gặp cần tránh

- cấu trúc phân cấp lộn xộn
- task description quá mơ hồ
- thiếu task ID hoặc ID trùng lặp
- effort estimation phi thực tế
- dependencies sai hoặc thiếu
- không có summary
- WBS quá sơ sài hoặc quá chi tiết

## Cách dùng ngắn gọn

1. Đọc project plan / spec
2. Xác định module/phase chính (Level 2)
3. Chia nhỏ thành feature/component (Level 3)
4. Tạo task cụ thể (Level 4)
5. Gán ID, description, effort, dependencies cho mỗi task
6. Tạo summary
7. Xuất file `wbs.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ WBS thực tế
- Tham khảo: `systems/pm-agent/templates/wbs-template.md`
- Tham khảo: `projects/active/web-ban-hang/02-planning/wbs.md`
