# PHẦN 7: Ví dụ thực tế cho PM Agent

## Tổng quan
Phần này đưa ra ví dụ cụ thể để minh họa cách PM Agent vận hành với một dự án thật.

## Bối cảnh ví dụ

### Yêu cầu đầu vào từ user
```text
Anh muốn làm một Project Manager Agent bằng OpenClaw.
Agent này phải có khả năng nhận yêu cầu dự án, phân tích yêu cầu,
tạo tài liệu PM, chia task, điều phối thực thi, theo dõi tiến độ,
và tạo báo cáo tổng kết.
```

Đây là yêu cầu tự nhiên, còn khá rộng.
PM Agent không được nhảy vào code ngay.

## Giai đoạn 1 — PM Agent tiếp nhận yêu cầu

### PM Agent phân tích nội dung
Nó rút ra được:

**Mục tiêu chính**
- Xây một PM Agent bằng OpenClaw

**Kết quả mong muốn**
- Một prototype PM Agent
- Có thể nhận yêu cầu dự án
- Tạo tài liệu PM
- Điều phối thực thi
- Cập nhật trạng thái
- Tạo final report

**Điểm còn mơ hồ**
- Chỉ làm tài liệu hay có thực thi thật?
- Có dùng sub-agent không?
- Sản phẩm cuối là file docs, skill, hay demo chạy được?
- Phạm vi MVP là gì?

### PM Agent hỏi lại user
Ví dụ PM Agent hỏi:
1. PM Agent cần dừng ở mức tài liệu hay phải thực thi task thật?
2. Có cần dùng sub-agent/worker trong OpenClaw không?
3. Kết quả cuối cùng anh muốn là:
   - bộ tài liệu nghiệp vụ,
   - prototype chạy được,
   - hay cả hai?
4. Anh ưu tiên demo nhanh hay kiến trúc đẹp, đầy đủ?
5. Có giới hạn thời gian hoặc phạm vi không?

## Giai đoạn 2 — PM Agent tạo charter nháp

Sau khi có câu trả lời, PM Agent tạo `charter.md`:

```markdown
# Project Charter: OpenClaw PM Agent

## Mục tiêu
Xây dựng một PM Agent prototype trên OpenClaw có khả năng:
- nhận yêu cầu dự án
- phân tích và chuẩn hóa yêu cầu
- tạo bộ tài liệu PM
- chia task
- điều phối task execution
- theo dõi tiến độ
- tổng kết dự án

## In-scope
- Nghiệp vụ PM Agent
- Bộ tài liệu chuẩn
- Workflow thực thi
- Prototype gọi worker/sub-agent
- Status tracking và final report

## Out-of-scope
- Tích hợp Jira/Trello
- Giao diện dashboard web hoàn chỉnh
- Multi-user enterprise deployment

## Success Criteria
- Agent tạo được charter, plan, rules, task-board
- Agent điều phối được ít nhất 1 worker
- Agent cập nhật trạng thái dự án
- Agent tạo được final report
```

## Giai đoạn 3 — PM Agent lập kế hoạch

Sau khi charter được xác nhận, PM Agent tạo bộ tài liệu planning.

### `spec.md`
Trả lời: **PM Agent phải làm được gì?**

```markdown
# Specification

## Core Features
1. Receive project request
2. Analyze requirements
3. Generate PM documents
4. Build project plan
5. Create task board
6. Assign tasks to worker agent
7. Review worker output
8. Update project state
9. Generate reports
10. Close project
```

### `plan.md`
Ví dụ chia phase:

```markdown
# Plan

## Phase 1 - Business Analysis
- Define PM workflow
- Define required artifacts

## Phase 2 - Architecture
- Define PM Agent + Worker model
- Define project state structure

## Phase 3 - Prototype
- Implement PM workflow in OpenClaw
- Test sub-agent task delegation

## Phase 4 - Validation
- Run end-to-end example
- Produce final report
```

### `rules.md`
Ví dụ:

```markdown
# Rules

1. Every project must start with charter
2. Every task must have ID and status
3. Every scope change must be logged
4. Every blocker must be added to issue-log
5. Every execution cycle must update task-board
6. Project cannot be closed without final-report
```

### `wbs.md`
Ví dụ:

```markdown
1. Project Analysis
   1.1 Analyze PM responsibilities
   1.2 Define PM Agent scope

2. Documentation Design
   2.1 Define charter template
   2.2 Define plan template
   2.3 Define task-board template

3. Execution Workflow
   3.1 Define task lifecycle
   3.2 Define worker prompt format
   3.3 Define review process

4. Prototype Implementation
   4.1 Create docs structure
   4.2 Implement PM workflow
   4.3 Test with sample project

5. Closure
   5.1 Final report
   5.2 Lessons learned
```

## Giai đoạn 4 — PM Agent tạo task board

Sau planning, PM Agent chuyển WBS thành task cụ thể.

### `task-board.md`
Ví dụ:

```markdown
## Backlog
- TASK-001: Create charter template
- TASK-002: Create requirements template
- TASK-003: Create planning docs structure
- TASK-004: Define worker execution prompt
- TASK-005: Build example project workflow
- TASK-006: Test end-to-end flow
- TASK-007: Create final report

## In Progress
- None

## Done
- None

## Blocked
- None
```

### Phân loại task
**PM Agent tự làm**
- TASK-001: Create charter template
- TASK-002: Create requirements template
- TASK-003: Create planning docs structure
- TASK-004: Define worker execution prompt

**Giao Worker Agent**
- TASK-005: Build example project workflow
- TASK-006: Test end-to-end flow

**Cần user approval**
- Approve final scope
- Approve final deliverables

## Giai đoạn 5 — PM Agent thực thi một task mẫu

Giả sử PM Agent chọn:
> **TASK-005: Build example project workflow**

Task này phù hợp để giao Worker Agent.

### PM Agent tạo prompt cho Worker
Ví dụ prompt:

```markdown
Bạn là Worker Agent.

## Task
Build an example project workflow for the OpenClaw PM Agent.

## Input
Read:
- systems/pm-agent/charter.md
- systems/pm-agent/plan.md
- systems/pm-agent/rules.md

## Output
Create:
- systems/pm-agent/example-workflow.md

## Requirements
- Show end-to-end flow
- Include user input, PM Agent actions, worker actions
- Keep structure clear
- Do not change project scope
- If blocked, report blocker instead of guessing
```

### Worker Agent trả kết quả
Ví dụ Worker tạo được `example-workflow.md`.

PM Agent sau đó review:
- File có được tạo đúng không?
- Nội dung có bám charter không?
- Có vi phạm scope không?
- Có cần chỉnh sửa không?

### PM Agent cập nhật project state
Sau khi review xong, PM Agent cập nhật:

**`task-board.md`**
- TASK-005 từ `In Progress` → `Done`

**`status-dashboard.md`**
- Completion tăng từ 40% → 55%

**`issue-log.md`**
- Nếu có lỗi thì ghi vào

**`risk-register.md`**
- Nếu worker làm lệch scope thì thêm risk mới

## Giai đoạn 6 — Tình huống có blocker

Giả sử đến TASK-006:
> Test end-to-end flow

Worker Agent báo:
- Chưa có prompt chuẩn cho closure phase
- Chưa có file `final-report` template

Lúc này PM Agent không được giả vờ mọi thứ ổn.

Nó phải:
1. Ghi blocker vào `issue-log.md`
2. Cập nhật TASK-006 = Blocked
3. Phân tích nguyên nhân
4. Tạo action tiếp theo:
   - Thêm task mới: `TASK-006A Create final-report template`
5. Cập nhật `change-log.md` nếu plan thay đổi

Đây là điểm phân biệt giữa:
- agent biết "làm"
và
- agent biết "quản lý dự án"

## Giai đoạn 7 — PM Agent giám sát

Sau vài task, PM Agent phải tạo báo cáo kiểu như:

### `status-dashboard.md`
Ví dụ:

```markdown
# Project Status Dashboard

## Overall Status
🟡 At Risk

## Progress
- Total tasks: 8
- Done: 4
- In Progress: 1
- Blocked: 1
- Not Started: 2
- Completion: 50%

## Top Issues
- Missing closure template
- Worker output inconsistent in task review

## Top Risks
- Scope drift
- Context overflow

## Recommended Actions
1. Create closure templates
2. Tighten worker prompt
3. Review scope before continuing
```

## Giai đoạn 8 — PM Agent đóng dự án

Khi prototype hoàn tất, PM Agent tạo:

### `final-report.md`
Ví dụ nội dung tóm tắt:

```markdown
# Final Report

## Project
OpenClaw PM Agent Prototype

## Objectives achieved
- PM workflow defined
- Standard PM docs created
- Task delegation model validated
- Reporting workflow demonstrated

## Deliverables
- Business process docs
- PM Agent instructions
- Example workflow
- Prototype structure

## Remaining work
- Convert docs into runnable skill
- Add automated monitoring
- Improve worker orchestration
```

### `lessons-learned.md`
Ví dụ:

```markdown
# Lessons Learned

## What went well
- Documentation-first approach kept scope clear
- PM + Worker model was practical
- Externalized project state reduced confusion

## What could be improved
- Need better worker prompt templates
- Need stronger handoff pattern
- Need more compact reporting format

## Key insights
- PM Agent must update docs after every execution
- Worker prompts must be very specific
- Human approval needed at scope changes only

## Recommendations
- Use this workflow for future projects
- Build skill/SOP from these docs
- Test with more complex projects
```

## Một ví dụ mini khác để dễ demo

Nếu cần demo ngắn trước giảng viên/người hướng dẫn, có thể dùng ví dụ nhỏ hơn:
> **"Hãy quản lý dự án tạo landing page giới thiệu HUECIT Internship"**

PM Agent sẽ:
1. Tạo charter
2. Tạo requirements
3. Tạo spec/plan
4. Chia task:
   - Viết nội dung landing page
   - Tạo cấu trúc HTML/CSS
   - Review nội dung
   - Tạo final report
5. Giao 1 task cho worker
6. Cập nhật trạng thái
7. Tạo báo cáo cuối

Ví dụ này dễ demo vì:
- Nhỏ
- Rõ
- Có thể thấy ngay PM Agent quản lý thế nào
- Không quá nặng

## Kết luận

Điểm quan trọng nhất cần nhớ:
**PM Agent không chỉ tạo tài liệu**.
Nó phải:
- Hiểu yêu cầu
- Chuẩn hóa yêu cầu
- Lập kế hoạch
- Chia task
- Điều phối thực thi
- Cập nhật trạng thái
- Xử lý issue/risk/change
- Tổng kết dự án

Nếu thiếu phần **assign → execute → review → update**, thì nó chưa thật sự là PM Agent.

---

**Ngày phân tích:** 2026-04-24
**Người phân tích:** Lệ (PM Agent)
