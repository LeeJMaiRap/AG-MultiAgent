---
name: task-board-builder
description: Tạo hoặc cập nhật file `03-execution/task-board.md` từ WBS, schedule, action items hoặc trạng thái thực tế; dùng khi cần quản lý task theo trạng thái như backlog, in progress, done, blocked, cancelled để theo dõi execution hằng ngày.
---

# Task Board Builder

## Mục tiêu

Tạo và duy trì tài liệu Task Board để theo dõi execution hằng ngày của dự án, giúp nhìn rõ task nào chưa bắt đầu, đang làm, đã xong, bị chặn hoặc bị hủy.

Skill này giúp:
- chuyển WBS hoặc action items thành bảng task vận hành được
- phân loại task theo trạng thái execution
- cập nhật tiến độ, blocker và actual effort
- tổng hợp summary để nhìn nhanh sức khỏe công việc
- xác định next actions cho PM hoặc team

## Dùng khi nào

Dùng skill này khi:
- đã có WBS, schedule hoặc action items
- cần tạo task board ban đầu cho execution
- cần cập nhật task board theo trạng thái thực tế
- cần tổng hợp việc đang làm / bị chặn / đã xong

## Không dùng khi nào

Không dùng skill này khi:
- chưa có đầu vào đủ rõ để xác định task
- mục tiêu là lập kế hoạch phase-level, không phải execution-level
- chỉ cần issue log hoặc change log
- cần theo dõi lesson learned sau dự án

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- WBS
- action items
- schedule
- trạng thái task thực tế từ chat / notes / report

## Input tùy chọn

- owner/assigned person
- estimate / actual effort
- priority
- blocker information
- completed date
- current phase

## Output

Output là file `task-board.md` với 6 phần chính:

1. **Status Legend**
2. **Backlog**
3. **In Progress**
4. **Done**
5. **Blocked**
6. **Summary**

Có thể bổ sung:
7. **Cancelled**
8. **Next Actions**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/task-board-template.md`.

## Quy tắc xử lý

### 1. Mỗi task chỉ được nằm ở một trạng thái chính
Một task không được xuất hiện đồng thời ở nhiều cột/nhóm trạng thái. Nếu task đang bị block thì ưu tiên đưa vào **Blocked** thay vì **In Progress**.

### 2. Phân biệt rõ các trạng thái
- **Backlog / Not Started:** chưa bắt đầu
- **In Progress:** đang thực hiện
- **Done:** đã hoàn thành
- **Blocked:** đang bị chặn bởi blocker cụ thể
- **Cancelled:** đã hủy, không làm nữa

### 3. Backlog phải ưu tiên được
Nếu có priority, task trong backlog cần thể hiện rõ mức ưu tiên để biết nên kéo việc nào lên trước.

### 4. In Progress phải có thông tin tiến độ
Task đang làm nên có tối thiểu:
- estimate
- actual effort
- % done
- blocker (nếu có)

### 5. Done phải ghi nhận completion rõ ràng
Task hoàn thành nên có:
- actual effort
- completed date

### 6. Blocked phải có blocker và hành động tiếp theo
Nếu task bị chặn, phải ghi:
- blocker cụ thể là gì
- bị chặn từ khi nào
- action hoặc escalation tiếp theo

### 7. Summary phải phản ánh thực trạng execution
Summary nên có:
- total tasks
- completed / in progress / blocked / not started / cancelled
- completion % hoặc on-time % nếu đủ dữ liệu
- current phase nếu xác định được

### 8. Next Actions phải có owner và ưu tiên
Nếu có phần Next Actions, mỗi action nên có:
- action cụ thể
- owner
- priority
- deadline (nếu biết)

Không viết kiểu quá chung chung như “tiếp tục làm tiếp”.

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Task nào đã bắt đầu thật sự?
- Task nào đã xong?
- Task nào đang bị chặn? chặn bởi gì?
- Task nào ưu tiên cao nhưng chưa bắt đầu?
- Có task nào không còn phù hợp và nên cancel không?
- Current phase là gì?
- Next action hợp lý nhất là gì?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `wbs-generator`
- `schedule-generator`
- `action-items-extractor`

Và là đầu vào cho:
- `status-dashboard-updater`
- `issue-log-updater`
- daily/weekly status reporting

Task board là trung tâm vận hành của execution.

## Liên hệ với cấu trúc dự án

Skill này tạo hoặc cập nhật file:
```
projects/[project-name]/03-execution/task-board.md
```

File này là nơi phản ánh tình trạng công việc sống của dự án.

## Tiêu chí hoàn thành tốt

Một task board tốt khi:
- task được phân loại đúng trạng thái
- nhìn vào là biết ngay dự án đang ở đâu
- backlog có thứ tự ưu tiên rõ
- blocked tasks có thông tin để xử lý
- summary giúp PM ra quyết định nhanh
- next actions ngắn gọn, hữu ích
- next actions có owner/priority rõ ràng

## Lỗi thường gặp cần tránh

- cùng một task xuất hiện ở nhiều trạng thái
- in progress nhưng không có tiến độ
- blocked nhưng không ghi blocker
- done nhưng không có completed date
- summary sai số lượng
- next actions quá chung chung, thiếu owner/priority
- task board chỉ là bản sao của WBS mà không phản ánh execution thật

## Cách dùng ngắn gọn

1. Đọc WBS / action items / trạng thái thực tế
2. Phân loại task theo trạng thái
3. Ghi progress/actual/blocker nếu có
4. Tạo summary execution
5. Đề xuất next actions
6. Xuất/cập nhật `task-board.md`

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ task board thực tế
- Tham khảo: `systems/pm-agent/templates/task-board-template.md`
- Tham khảo: `projects/active/web-ban-hang/03-execution/task-board.md`
