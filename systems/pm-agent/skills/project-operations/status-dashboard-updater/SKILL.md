---
name: status-dashboard-updater
description: Tạo hoặc cập nhật file `04-monitoring/status-dashboard.md` từ task board, issue log, change log, schedule và risk register; dùng khi cần tổng hợp sức khỏe dự án, metrics, timeline, budget, scope, top risks/issues, upcoming milestones và recommended actions trong một dashboard ngắn gọn.
---

# Status Dashboard Updater

## Mục tiêu

Tạo và duy trì tài liệu Status Dashboard để tổng hợp nhanh tình trạng dự án, giúp owner hoặc PM nhìn một lượt là biết dự án đang ổn, có rủi ro hay đang lệch kế hoạch.

Skill này giúp:
- tổng hợp project health ở mức điều hành
- hiển thị key metrics ngắn gọn, dễ đọc
- phản ánh tình trạng timeline, budget, scope
- nêu top risks, top issues và upcoming milestones
- đề xuất recommended actions để xử lý ngay

## Dùng khi nào

Dùng skill này khi:
- cần báo cáo tiến độ dự án ngắn gọn
- cần tổng hợp nhiều nguồn thành một dashboard điều hành
- cần cập nhật trạng thái định kỳ (daily/weekly)
- owner cần nhìn nhanh sức khỏe dự án

## Không dùng khi nào

Không dùng skill này khi:
- chưa có dữ liệu thực tế từ task board / issues / schedule
- mục tiêu là ghi log chi tiết task, issue hoặc change riêng lẻ
- chỉ cần một tài liệu planning, không phải monitoring

## Input bắt buộc

Ít nhất phải có một hoặc nhiều nguồn sau:
- task board
- schedule
- issue log
- risk register
- change log

## Input tùy chọn

- actual hours spent
- forecast updates
- owner feedback
- reporting date
- milestone review notes

## Output

Output là file `status-dashboard.md` với các phần chính:

1. **Project Health**
2. **Key Metrics**
3. **Timeline Status**
4. **Budget Status**
5. **Scope Status**
6. **Top Risks**
7. **Top Issues**
8. **Upcoming Milestones**
9. **Recommended Actions**

Có thể bổ sung:
- **Current Phase**
- **Last Updated**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/status-dashboard-template.md`.

## Quy tắc xử lý

### 1. Dashboard phải ngắn gọn nhưng có giá trị điều hành
Không được biến dashboard thành bản sao dài dòng của task board hay issue log. Chỉ lấy các thông tin quan trọng nhất.

### 2. Project health phải phản ánh đúng tình hình thực tế
Chỉ dùng 3 mức:
- 🟢 On Track
- 🟡 At Risk
- 🔴 Off Track

Đánh giá phải dựa trên timeline, blockers, risk score, scope completion và issue severity - không được tô hồng tình hình.

### 3. Key metrics phải có căn cứ và giải thích
Nếu có dữ liệu thì dùng metrics như:
- SPI (Schedule Performance Index)
- CPI (Cost Performance Index)
- Scope Completion
- Defect rate

**Quan trọng:** Nếu dùng SPI/CPI, phải giải thích công thức hoặc nghĩa của chúng ở cuối dashboard (hoặc trong reference file).

Nếu chưa đủ dữ liệu tính chính xác, có thể dùng metric gần đúng nhưng phải nhất quán và không giả vờ "chính xác tuyệt đối".

### 4. Timeline / Budget / Scope phải tách riêng
Ba phần này phải được trình bày độc lập để tránh đánh giá mơ hồ:
- timeline có bị trễ không?
- budget/effort có bị vượt không?
- scope completion đang ở mức nào?

### 5. Top risks và top issues phải được chọn lọc
Chỉ đưa ra những risk/issue quan trọng nhất, thường là top 2-3 mục có ảnh hưởng lớn nhất.

### 6. Recommended actions phải cụ thể và có owner/deadline
Recommended actions phải là việc có thể hành động ngay.

**Mỗi action phải có:**
- **Owner:** ai chịu trách nhiệm thực hiện
- **Deadline:** khi nào cần hoàn thành
- **Priority:** (nếu có nhiều actions)

Ví dụ action tốt:
```
1. Chốt API contract cho task list trong 24 giờ để gỡ blocker TASK-003
   - Owner: Backend dev
   - Deadline: 2026-05-17
   - Priority: Critical

2. Không mở rộng thêm dashboard ngoài mức cơ bản của MVP
   - Owner: PM Agent
   - Deadline: Ongoing
   - Priority: High
```

Ví dụ action không tốt (quá chung chung, thiếu owner/deadline):
```
❌ Tiếp tục cố gắng
❌ Theo dõi tiến độ
❌ Cải thiện chất lượng
```

### 7. Dashboard phải có dấu mốc thời gian
Nên có phần `Last Updated` hoặc reporting date để biết dashboard này còn mới hay đã cũ.

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Dự án đang on track, at risk hay off track?
- Mốc nào sắp tới quan trọng nhất?
- Có blocker hoặc issue nào đang đe dọa critical path không?
- Risk nào đáng lo nhất lúc này?
- Completion % có phù hợp với timeline hiện tại không?
- Hành động điều phối nào cần làm ngay?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `task-board-builder`
- `issue-log-updater`
- `change-log-updater`
- `risk-register-generator`
- `schedule-generator`

Và là đầu ra monitoring quan trọng cho:
- owner updates
- weekly reviews
- execution steering

Status dashboard là góc nhìn điều hành ở mức cao.

## Liên hệ với cấu trúc dự án

Skill này tạo hoặc cập nhật file:
```
projects/[project-name]/04-monitoring/status-dashboard.md
```

File này là bản snapshot sức khỏe dự án ở thời điểm báo cáo.

## Tiêu chí hoàn thành tốt

Một status dashboard tốt khi:
- nhìn nhanh là hiểu sức khỏe dự án
- số liệu không mâu thuẫn nhau
- **metrics có giải thích (SPI/CPI là gì, tính thế nào)**
- top risks/issues thật sự đáng quan tâm
- **recommended actions hữu ích, có owner và deadline**
- có thể dùng để báo cáo nhanh cho owner

## Lỗi thường gặp cần tránh

- dashboard quá dài và lặp lại log chi tiết
- overall status không khớp dữ liệu thực tế
- **metrics thiếu căn cứ hoặc không giải thích (SPI/CPI xuất hiện mà không nói là gì)**
- risks/issues chọn không đúng trọng tâm
- **actions quá mơ hồ, thiếu owner và deadline**
- không có timestamp cập nhật

## Cách dùng ngắn gọn

1. Đọc task board / issue log / schedule / risk register / change log
2. Đánh giá overall health
3. Tính/tổng hợp key metrics
4. Tóm tắt timeline, budget, scope
5. Chọn top risks, top issues, milestones
6. Viết recommended actions
7. Ghi thời điểm cập nhật
8. Xuất/cập nhật `status-dashboard.md`

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `references/recommended-actions-guide.md` - hướng dẫn viết recommended actions hiệu quả
- `references/metrics-notes-guide.md` - hướng dẫn giải thích metrics (SPI/CPI/etc.)
- `examples/` - ví dụ status dashboard thực tế
- Tham khảo: `systems/pm-agent/templates/status-dashboard-template.md`
- Tham khảo: `projects/active/web-ban-hang/04-monitoring/status-dashboard.md`

## Khi nào nên đọc thêm tài liệu tham chiếu

- Nếu cần viết recommended actions: đọc `references/recommended-actions-guide.md`
- Nếu dùng SPI/CPI hoặc metrics khác: đọc `references/metrics-notes-guide.md`
- Nếu đang phân vân action nào nên đề xuất: đọc `references/recommended-actions-guide.md`
- Nếu không chắc có nên dùng SPI/CPI hay không: đọc `references/metrics-notes-guide.md`
