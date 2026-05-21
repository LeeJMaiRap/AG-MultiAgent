---
name: daily-project-report-generator
description: Tạo file báo cáo hằng ngày cho một project hoặc cho chính PM Agent framework vào cuối ngày hoặc theo lịch định kỳ; dùng khi cần snapshot thay đổi trong ngày, ai đã làm gì (human / agent / subagent), tiến độ, issue/risk chính và next actions. Output mặc định vào `projects/active/[project-name]/reports/daily/YYYY-MM-DD.md` hoặc `systems/pm-agent/reports/daily/YYYY-MM-DD.md` tùy mode.
---

# Daily Project Report Generator

## Mục tiêu

Tạo báo cáo hằng ngày ngắn gọn nhưng đủ giá trị vận hành để:
- nhìn lại thay đổi của dự án trong ngày
- truy được ai đã thực hiện thay đổi
- tổng hợp task progress / issues / changes
- chuẩn bị handoff cho ngày hôm sau

## Dùng khi nào

Dùng skill này khi:
- cần report định kỳ mỗi ngày (ví dụ 19:00)
- cần daily digest cho owner / PM
- cần snapshot thay đổi dự án theo từng ngày
- cần log hoạt động human / agent / subagent

## Không dùng khi nào

Không dùng skill này khi:
- cần final report khi closure
- cần status dashboard điều hành tổng thể nhiều ngày
- chưa có đủ dữ liệu tối thiểu từ project files

## Reporting modes

### 1. Project report mode
Dùng cho project cụ thể.

Đọc tối thiểu các nguồn sau nếu có:
- `project.yaml`
- `03-execution/task-board.md`
- `03-execution/change-log.md`
- `03-execution/issue-log.md`
- `04-monitoring/status-dashboard.md`
- `05-closure/final-report.md`
- `decisions/decision-log.md`
- `approvals/`
- `handoffs/`
- git log trong thư mục project (bao gồm commits trong ngày report)
- file evidence có tên hoặc mtime khớp ngày report

Output mặc định:
`projects/active/[project-name]/reports/daily/YYYY-MM-DD.md`

### 2. Framework report mode
Dùng cho chính `systems/pm-agent/`.

Đọc tối thiểu các nguồn sau nếu có:
- `systems/pm-agent/STATUS.md`
- `systems/pm-agent/runtime/`
- `systems/pm-agent/eval/`
- `systems/pm-agent/skills/`
- git log liên quan PM Agent
- các report/checklist/policy liên quan

Output mặc định:
`systems/pm-agent/reports/daily/YYYY-MM-DD.md`

## Output

Format chuẩn xem ở `template-output.md` và phải tuân theo policy trong:
`systems/pm-agent/runtime/policies/daily-reporting-structure-policy.md`

## Nội dung bắt buộc

### Với project report
1. Project info + reporting date
2. Summary ngắn trong ngày
3. Thay đổi trong ngày
4. Actor attribution
5. Task progress snapshot
6. Issues / risks cần chú ý
7. Decisions / approvals mới (nếu có)
8. Next actions cho ngày sau

### Với framework report
1. Framework info + reporting date
2. Summary ngắn trong ngày
3. Thay đổi trong ngày
4. Capability / readiness snapshot
5. Issues / risks cần chú ý
6. Decisions / approvals mới (nếu có)
7. Actor attribution
8. Next actions cho ngày sau

## Quy tắc quan trọng

### 1. Phân biệt rõ nguồn thay đổi
Dùng các nhãn actor sau khi có thể xác định:
- `human:[name]`
- `agent:main`
- `subagent:[label-or-session]`
- `unknown`

### 2. Không bịa actor
Nếu không xác định chắc chắn ai làm, ghi `unknown` và nêu lý do ngắn.

### 3. Report là snapshot, không thay thế logs chi tiết
Daily report chỉ tóm tắt thông tin quan trọng nhất. Không chép nguyên task board hay change log vào report.

### 4. Luôn có next actions
Ngay cả khi ngày đó ít thay đổi, vẫn phải chốt ngày mai cần làm gì.

### 5. Nếu không có thay đổi đáng kể
Vẫn có thể tạo report, nhưng ghi rõ:
- không có thay đổi lớn
- đang chờ gì / bị chặn gì
- framework/project đang active hay on-hold
- phải detect no-change tự động từ: git commits today, change log, decisions, approvals, handoffs
- nếu no-change và project active → cần xem xét stale risk

### 6. Nếu project stopped / on-hold
Không được viết report như thể dự án vẫn đang active progress.
Phải nêu đúng trạng thái thật và lý do tại sao vẫn tạo report (nếu có).

## Heuristic gợi ý

Khi tổng hợp, rà theo câu hỏi:
- Hôm nay dự án có tiến lên không?
- Có deliverable nào thay đổi?
- Ai tạo thay đổi đó?
- Có blocker nào mới?
- Có quyết định/approval nào phát sinh?
- Ngày mai phải làm gì ngay?
- Có git commits trong ngày report không?
- Có file evidence mới trong ngày không?
- Có source conflict giữa các artifact không?
- Project có đang stale không (active nhưng no meaningful change)?

## Nguồn xác định actor

Ưu tiên theo thứ tự:
1. explicit actor trong project docs (approvals, decisions, handoffs, change log, issue log)
2. decision/change log
3. handoff notes
4. git commit author (chỉ dùng như tín hiệu hỗ trợ)
5. session knowledge nếu có

**Actor attribution được tổng hợp tự động:**
- Đếm frequency của từng actor từ các artifact
- Tách rõ human / agent:main / subagent / unknown
- Không bịa actor nếu không có evidence

## Liên hệ với workflow PM

Skill này thuộc monitoring/operations định kỳ.

Nó thường chạy sau:
- `task-board-builder`
- `change-log-updater`
- `issue-log-updater`
- `status-dashboard-updater`

## Cấu trúc output

- `template-output.md` - mẫu đầu ra
- `examples/` - ví dụ report mẫu
- `scripts/generate_daily_report.py` - script dựng khung report từ project files
- `systems/pm-agent/runtime/policies/daily-reporting-structure-policy.md` - policy cấu trúc daily reporting

## Cách dùng ngắn gọn

1. Xác định report mode: project hay framework
2. Xác định target path
3. Xác định ngày report
4. Đọc source-of-truth phù hợp với mode
5. Tóm tắt thay đổi trong ngày
6. Gán actor attribution khi có thể
7. Ghi next actions
8. Xuất file vào `reports/daily/`
