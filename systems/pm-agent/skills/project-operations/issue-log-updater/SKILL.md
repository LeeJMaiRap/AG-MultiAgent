---
name: issue-log-updater
description: Tạo hoặc cập nhật file `03-execution/issue-log.md` từ blocker, lỗi phát sinh, feedback test hoặc trạng thái thực tế; dùng khi cần ghi nhận, theo dõi và cập nhật các vấn đề đang mở hoặc đã giải quyết trong quá trình execution.
---

# Issue Log Updater

## Mục tiêu

Tạo và duy trì tài liệu Issue Log để ghi nhận các vấn đề phát sinh trong execution, giúp team/PM biết vấn đề nào đang mở, mức độ nghiêm trọng ra sao, nguyên nhân là gì và cần xử lý thế nào.

Skill này giúp:
- ghi nhận issue mới phát sinh từ task execution, testing hoặc deployment
- phân loại issue theo severity và status
- theo dõi root cause, impact, resolution và owner
- tách rõ issue đang mở và issue đã giải quyết
- tổng hợp statistics để nhìn nhanh sức khỏe vận hành

## Dùng khi nào

Dùng skill này khi:
- xuất hiện lỗi, blocker, bug hoặc vấn đề thực tế trong execution
- cần cập nhật trạng thái xử lý issue
- cần lưu lại issue đã giải quyết để tránh lặp lại
- cần tổng hợp issue cho status report hoặc dashboard

## Không dùng khi nào

Không dùng skill này khi:
- thông tin chỉ là rủi ro tương lai, chưa xảy ra (dùng `risk-register-generator`)
- chỉ là thay đổi phạm vi/yêu cầu (dùng `change-log-updater`)
- chỉ là task chưa bắt đầu hoặc đang làm bình thường, không có vấn đề

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- task board với blocked tasks
- testing feedback
- lỗi phát sinh từ execution/deployment
- chat/note mô tả issue thực tế

## Input tùy chọn

- severity
- reported by
- root cause phân tích sơ bộ
- assigned to
- target resolution date
- resolved date

## Output

Output là file `issue-log.md` với 3 phần chính:

1. **Active Issues**
2. **Resolved Issues**
3. **Issue Statistics**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/issue-log-template.md`.

## Quy tắc xử lý

### 1. Phân biệt issue với risk và task
- **Issue:** vấn đề đã xảy ra thật
- **Risk:** điều có thể xảy ra trong tương lai
- **Task:** việc cần làm bình thường

Không được trộn lẫn ba loại này.

### 2. Mỗi issue phải có ID duy nhất
Format:
- `ISS-001`
- `ISS-002`
- ...

ID phải tuần tự, không trùng lặp.

### 3. Severity phải phản ánh đúng mức độ ảnh hưởng
- **High:** chặn luồng chính, ảnh hưởng lớn tới timeline/scope/chất lượng
- **Medium:** ảnh hưởng đáng kể nhưng có workaround hoặc không chặn toàn bộ
- **Low:** ảnh hưởng nhỏ, không chặn tiến độ chính

### 4. Active issue phải đủ thông tin để xử lý
Issue đang mở nên có tối thiểu:
- severity
- status
- reported by
- reported date
- description
- impact
- assigned to
- target resolution

### 5. Root cause và resolution phải thực tế và sâu hơn
- **Root cause:** nguyên nhân thật hoặc phân tích sơ bộ hợp lý
  - Nên dùng 5 Whys hoặc Fishbone nếu có thể
  - Không chỉ ghi 1 câu chung chung
- **Resolution:** hướng sửa hoặc cách khắc phục cụ thể
- **Prevention action:** làm gì để không lặp lại (cho resolved issues)

Không ghi kiểu quá mơ hồ như "sẽ kiểm tra sau" nếu có thể mô tả rõ hơn.

### 6. Issue đã giải quyết phải giữ lịch sử ngắn gọn
Resolved issue nên ghi:
- resolved by
- resolved date
- resolution thực tế

Mục đích là để tra cứu và tránh lặp lỗi.

### 7. Statistics phải khớp với nội dung log
Issue statistics phải tính đúng:
- total issues
- open
- resolved
- average resolution time (nếu đủ dữ liệu)

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Vấn đề này đã xảy ra thật chưa?
- Nó ảnh hưởng đến phần nào của dự án?
- Có chặn critical path không?
- Nguyên nhân sơ bộ là gì?
- Có workaround hoặc cách giải quyết rõ ràng chưa?
- Issue này đang mở hay đã được xử lý xong?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `task-board-builder` (khi có blocked tasks)
- testing / QA feedback
- deployment incidents

Và hỗ trợ cho:
- `status-dashboard-updater`
- daily/weekly reporting
- retrospective / lessons learned

Issue log là nơi ghi lại sự cố thật trong execution.

## Liên hệ với cấu trúc dự án

Skill này tạo hoặc cập nhật file:
```
projects/[project-name]/03-execution/issue-log.md
```

File này là sổ theo dõi vấn đề vận hành của dự án.

## Tiêu chí hoàn thành tốt

Một issue log tốt khi:
- issue được ghi nhận rõ ràng, không mơ hồ
- phân biệt đúng active vs resolved
- severity hợp lý
- root cause và resolution hữu ích
- statistics chính xác
- giúp team/PM nhìn ra vấn đề nào cần ưu tiên xử lý

## Lỗi thường gặp cần tránh

- ghi risk thành issue
- ghi task bình thường thành issue
- thiếu severity hoặc thiếu impact
- root cause quá cảm tính
- resolved issue không có resolution rõ ràng
- statistics sai số lượng

## Cách dùng ngắn gọn

1. Đọc task board / feedback / logs / notes
2. Xác định vấn đề nào là issue thật
3. Phân loại active hoặc resolved
4. Gán severity, impact, root cause, owner
5. Cập nhật statistics
6. Xuất/cập nhật `issue-log.md`

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ issue log thực tế
- Tham khảo: `systems/pm-agent/templates/issue-log-template.md`
- Tham khảo: `projects/active/web-ban-hang/03-execution/issue-log.md`
