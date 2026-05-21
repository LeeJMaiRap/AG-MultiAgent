# Stale Project Detection Policy

Quy định chuẩn để PM Agent phát hiện project, task, approval hoặc workflow đang bị `stale` (chết mềm / nằm im quá lâu mà không được xử lý đúng mức).

## Mục tiêu

Policy này giúp:
- phát hiện project không còn tiến triển nhưng chưa được đánh dấu rõ
- phát hiện approval/task/issue nằm im quá lâu
- hỗ trợ escalation đúng lúc
- giảm tình trạng owner tưởng dự án còn active nhưng thực tế đã đứng yên

---

# 1. Định nghĩa `stale`

`Stale` nghĩa là:
- vẫn còn mở / active trên giấy tờ
- nhưng không có tiến triển đủ ý nghĩa trong một khoảng thời gian đã định
- hoặc có dependency/approval đang treo quá lâu mà chưa được escalate

---

# 2. Các loại stale cần phát hiện

## A. Stale Task
Một task bị coi là stale khi:
- status là `In Progress` nhưng không có update đáng kể quá lâu
- status là `Blocked` nhưng không có escalation/action tiếp theo
- task được assign nhưng không có output/evidence mới

## B. Stale Approval
Một approval bị coi là stale khi:
- đã request nhưng quá timeout mà chưa có quyết định
- không có follow-up hoặc escalation

## C. Stale Issue
Một issue bị coi là stale khi:
- vẫn open nhưng không có update/resolution attempt trong một khoảng thời gian đáng kể
- severity cao nhưng không có owner action rõ

## D. Stale Project
Một project bị coi là stale khi:
- `status: active` nhưng không có thay đổi meaningful trong nhiều ngày
- source-of-truth không được cập nhật
- không có decision mới, task progress mới, approval mới, issue update mới
- project thực tế đã dừng nhưng metadata vẫn ghi active

---

# 3. Ngưỡng stale đề xuất

## Task stale
- `In Progress` không update quá **3 ngày** → stale
- `Blocked` không có action/escalation quá **2 ngày** → stale

## Approval stale
- scope/change approval quá **24 giờ** không phản hồi → stale nhẹ
- plan/closure approval quá **48 giờ** không phản hồi → stale
- quá timeout nhiều lần → stale nặng

## Issue stale
- issue severity High không update quá **2 ngày** → stale
- issue Medium/Low không update quá **5 ngày** → stale

## Project stale
- project active không có update meaningful quá **3 ngày** → stale nhẹ
- quá **7 ngày** → stale rõ ràng
- quá **14 ngày** mà vẫn `active` → phải xem lại status hoặc escalate

**Lưu ý:** Đây là default heuristic. Có thể tinh chỉnh theo loại project sau này.

---

# 4. Tín hiệu để xét có update meaningful hay không

Các tín hiệu được tính là meaningful update:
- task status thay đổi có bằng chứng
- issue được update/resolved
- change log có mục mới
- approval mới hoặc approval được giải quyết
- decision mới
- handoff mới có result
- report mới phản ánh tiến triển thật
- git/change evidence gắn với project có giá trị thực

Không tính là meaningful update nếu chỉ có:
- chào hỏi
- note ngắn vô nghĩa
- rename nhẹ không ảnh hưởng trạng thái thật
- report auto tạo nhưng không có thay đổi nội dung thực tế

---

# 5. Severity levels và cách xử lý khi phát hiện stale

## Severity levels chuẩn

### `warning`
Dùng khi:
- có tín hiệu stale nhẹ
- chưa đủ để coi là blocked
- vẫn còn khả năng tự hồi phục nếu follow-up sớm

**Ví dụ:**
- task `In Progress` không update quá 3 ngày
- project active không có meaningful update quá 3 ngày
- approval scope/change quá 24h chưa phản hồi

**Cách xử lý:**
- ghi vào report
- thêm next action
- gắn nhãn cần follow-up

---

### `needs-review`
Dùng khi:
- stale đã rõ hơn
- cần người quản lý/owner xem lại trạng thái thật
- có nguy cơ metadata/status hiện tại không còn phản ánh đúng thực tế

**Ví dụ:**
- project active không có meaningful update quá 7 ngày
- issue severity cao không có update quá 2 ngày
- approval plan/closure quá 48h chưa phản hồi

**Cách xử lý:**
- escalate trong status dashboard hoặc daily report
- yêu cầu review lại owner action
- kiểm tra lại có nên giữ `active` không

---

### `blocked`
Dùng khi:
- stale gắn với blocker trực tiếp
- task/approval/issue không thể tiến tiếp nếu không có hành động rõ
- workflow bị nghẽn chứ không chỉ chậm

**Ví dụ:**
- task `Blocked` không có escalation/action quá 2 ngày
- approval critical bị treo làm chặn task downstream
- issue severity cao chặn milestone nhưng không có owner action

**Cách xử lý:**
- đánh dấu blocked rõ trong dashboard/report
- nêu blocker cụ thể
- yêu cầu action để mở chặn
- không viết như thể tiến độ vẫn bình thường

---

### `owner-attention`
Dùng khi:
- stale đã nặng
- cần owner xác nhận tiếp tục, dừng, hoặc đổi status
- không nên để PM Agent tự coi project là active bình thường nữa

**Ví dụ:**
- project active không có meaningful update quá 14 ngày
- mismatch giữa trạng thái thật và metadata kéo dài
- stale nhiều lớp cùng lúc: task + approval + project

**Cách xử lý:**
- đề xuất đổi status thành `on-hold` / `stopped`
- yêu cầu owner xác nhận tiếp tục hay dừng
- escalate trực tiếp thay vì chỉ log nội bộ

---

## Mapping từ stale level cũ sang severity mới
- stale nhẹ → `warning`
- stale rõ → `needs-review`
- stale nặng → `owner-attention`
- stale có blocker trực tiếp → `blocked`

## Quy tắc chọn severity
1. Có blocker trực tiếp → ưu tiên `blocked`
2. Không blocker nhưng cần owner xác nhận tiếp tục/dừng → `owner-attention`
3. Không đến mức owner-attention nhưng cần xem lại trạng thái thật → `needs-review`
4. Mới là tín hiệu sớm → `warning`

---

# 6. Rule cứng

1. Không để project `active` quá lâu nếu không có tiến triển meaningful
2. Không để approval pending quá timeout mà không log stale
3. Không để blocked task đứng yên quá lâu mà không escalation
4. Khi stale nặng, phải xem lại metadata status chứ không chỉ viết report cho có

---

# 7. Output mong muốn khi stale được phát hiện

Khi phát hiện stale, PM Agent nên tạo ít nhất một trong các dấu vết sau:
- section trong daily report
- note trong status dashboard
- next action rõ ràng
- đề xuất đổi status project
- escalation message cho owner (nếu policy notify cho phép)
- severity label rõ: `warning` / `needs-review` / `blocked` / `owner-attention`

## Output format gợi ý

```markdown
## Stale Detection
- Target: [task / approval / project]
- Severity: [warning / needs-review / blocked / owner-attention]
- Reason: [vì sao bị coi là stale]
- Since: [từ thời điểm nào]
- Next action: [hành động tiếp theo]
- Escalation: [có/không, escalate cho ai]
```

---

# 8. Kết luận ngắn

Nguyên tắc cứng:
- `active` mà không tiến triển đủ lâu → phải bị coi là stale
- stale không chỉ để quan sát, mà phải dẫn tới follow-up / escalation / status change
