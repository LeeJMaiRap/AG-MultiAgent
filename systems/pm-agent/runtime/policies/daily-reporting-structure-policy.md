# Daily Reporting Structure Policy

Quy định cấu trúc chuẩn cho báo cáo hằng ngày của PM Agent, áp dụng cho cả:
- **PM Agent framework reports**
- **project-level daily reports**

## Mục tiêu

Daily reporting phải:
- nhất quán về vị trí lưu
- nhất quán về naming
- tách rõ framework vs project
- xử lý đúng trạng thái active / on-hold / stopped / archived
- tránh làm report sai ngữ cảnh

## 1. Hai mode báo cáo

### A. Framework report mode
Dùng khi report cho chính hệ `systems/pm-agent/`.

**Output path:**
`systems/pm-agent/reports/daily/YYYY-MM-DD.md`

**Dùng khi:**
- theo dõi tiến độ nâng cấp PM Agent
- log thay đổi runtime / skill / architecture / readiness
- snapshot trạng thái framework theo ngày

### B. Project report mode
Dùng khi report cho một project cụ thể.

**Output path:**
`projects/active/[project-name]/reports/daily/YYYY-MM-DD.md`

**Dùng khi:**
- theo dõi tiến độ project theo từng ngày
- log thay đổi task / issue / change / approval / decision
- tổng hợp hoạt động human / agent / subagent trên project đó

## 2. Naming rule

Tên file mặc định:
`YYYY-MM-DD.md`

Ví dụ:
- `2026-05-14.md`
- `2026-05-15.md`

Không thêm timestamp vào tên file daily chính thức nếu chỉ có 1 report/ngày.

Nếu cùng ngày cần report bổ sung hiếm gặp:
- `YYYY-MM-DD-update-2.md`
- nhưng mặc định vẫn ưu tiên **1 file/ngày**

## 3. Folder rule

### Framework
- `systems/pm-agent/reports/daily/`

### Project active
- `projects/active/[project-name]/reports/daily/`

### Project archived
Thông thường **không tạo daily report mới** cho archived project.
Nếu cần backfill hoặc audit đặc biệt, phải ghi rõ lý do.

### Project stopped / on-hold
Vẫn có thể tạo report, nhưng report phải ghi rõ:
- project status = stopped/on-hold
- không có tiến triển active
- đang chờ điều gì / đang đóng băng vì sao

## 4. Status handling rule

### Active
Tạo report bình thường nếu project/framework còn đang vận hành.

### On-hold
Có thể tạo report định kỳ thưa hơn hoặc tạo theo sự kiện.
Nếu vẫn tạo daily, phải nói rõ dự án đang tạm dừng.

### Stopped
Không nên tiếp tục tạo daily report mặc định.
Chỉ tạo nếu:
- cần snapshot đóng trạng thái
- cần audit ngày cuối
- owner yêu cầu rõ

### Archived
Không chạy daily reporting mặc định.

## 5. Source of truth rule

### Framework report source of truth
Ưu tiên đọc:
1. `systems/pm-agent/STATUS.md`
2. `systems/pm-agent/runtime/`
3. `systems/pm-agent/eval/`
4. `systems/pm-agent/skills/`
5. git log liên quan PM Agent
6. các policy/checklist/reports liên quan

### Project report source of truth
Ưu tiên đọc:
1. `project.yaml`
2. `03-execution/task-board.md`
3. `03-execution/change-log.md`
4. `03-execution/issue-log.md`
5. `04-monitoring/status-dashboard.md`
6. `decisions/`
7. `approvals/`
8. `handoffs/`
9. git log trong thư mục project

## 6. Required sections rule

### Framework report bắt buộc có
- Summary
- Changes Today
- Capability/Readiness Snapshot
- Issues / Risks Needing Attention
- Decisions / Approvals Today
- Actor Attribution Summary
- Next Actions
- Evidence / References

### Project report bắt buộc có
- Summary
- Changes Today
- Task Progress Snapshot
- Issues / Risks Needing Attention
- Decisions / Approvals Today
- Actor Attribution Summary
- Next Actions
- Evidence / References

## 7. No-change rule

Nếu ngày đó không có thay đổi đáng kể:
- vẫn có thể tạo report nếu đang ở chế độ daily bắt buộc
- phải ghi rõ `No significant change today`
- phải nêu project/framework đang chờ gì
- vẫn phải có next actions hoặc trạng thái chờ

## 8. Stopped/on-hold wording rule

Nếu project stopped/on-hold:
- không được viết như thể project đang active progress
- phải nêu rõ trạng thái hiện tại
- không dùng language gây hiểu nhầm như `ongoing momentum` nếu thực tế đã dừng
- nếu project active nhưng không có meaningful update quá lâu, phải xem xét stale detection theo `systems/pm-agent/runtime/policies/stale-project-detection-policy.md`

## 9. Audit rule

Daily report là snapshot điều hành, không thay thế:
- task board
- change log
- issue log
- handoff notes
- git history

Report phải dẫn được về source of truth tương ứng.

## 10. Source conflict handling rule

Nếu các source-of-truth lệch nhau, report **không được chọn bừa** một nguồn mà không nói rõ.

### Ví dụ conflict thường gặp
- `project.yaml` nói completion = 58% nhưng `task-board.md` lại phản ánh completion thấp hơn
- status dashboard nói on track nhưng issue/change data cho thấy trạng thái rủi ro hơn

### Quy tắc xử lý
1. Ưu tiên phát hiện conflict
2. Ghi conflict vào report
3. Nêu rõ source nào đang lệch source nào
4. Không tự “hòa giải” nếu không có policy rõ hoặc bằng chứng đủ mạnh
5. Đưa conflict đó vào next actions nếu ảnh hưởng điều hành

### Rule cứng
- Có conflict → report phải nói có conflict
- Không đủ căn cứ → không được tự chọn một con số “đẹp hơn”

## Kết luận ngắn

Nguyên tắc cứng:
- framework report và project report phải tách rõ
- chỉ active project/framework mới chạy daily mặc định
- stopped/on-hold phải ghi đúng trạng thái
- report phải bám source of truth, không được viết sai ngữ cảnh
