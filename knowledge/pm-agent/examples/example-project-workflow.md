# Example Project Workflow - OpenClaw PM Agent Prototype

## User Request
"Hãy xây dựng một PM Agent bằng OpenClaw có khả năng nhận yêu cầu dự án, tạo tài liệu PM, chia task, điều phối thực thi, theo dõi tiến độ, và tạo báo cáo tổng kết."

## Phase 1 - Initiation
PM Agent thực hiện:
1. Phân tích yêu cầu
2. Trích xuất mục tiêu, scope, ràng buộc
3. Phát hiện khoảng trống thông tin
4. Hỏi người dùng các câu hỏi làm rõ
5. Tạo `charter.md` và `requirements.md`

## Phase 2 - Planning
PM Agent tạo:
- `spec.md`
- `plan.md`
- `rules.md`
- `wbs.md`
- `schedule.md`
- `risk-register.md`

Ví dụ phase:
- Business Analysis
- Architecture Design
- Prototype Implementation
- Validation
- Closure

## Phase 3 - Task Board
PM Agent chuyển WBS thành task cụ thể:
- TASK-001: Create charter template
- TASK-002: Create requirements template
- TASK-003: Create planning docs structure
- TASK-004: Define worker execution prompt
- TASK-005: Build example project workflow
- TASK-006: Test end-to-end flow
- TASK-007: Create final report

## Phase 4 - Execution
Ví dụ task thực thi:
- PM Agent chọn TASK-005
- PM Agent quyết định giao worker
- Worker nhận prompt rõ ràng
- Worker tạo file output
- PM Agent review kết quả
- PM Agent cập nhật task-board, status-dashboard, issue-log

## Phase 5 - Monitoring
PM Agent tạo `status-dashboard.md` với:
- overall status
- completion %
- top issues
- top risks
- recommended actions

## Phase 6 - Closure
PM Agent tạo:
- `final-report.md`
- `lessons-learned.md`

## End-to-End Loop
```text
Analyze → Plan → Create Tasks → Execute/Delegate → Review → Update → Close
```

## Key Insight
PM Agent không chỉ tạo tài liệu. Nó phải:
- hiểu yêu cầu
- lập kế hoạch
- điều phối thực thi
- cập nhật project state
- xử lý issue/risk/change
- tổng kết dự án
