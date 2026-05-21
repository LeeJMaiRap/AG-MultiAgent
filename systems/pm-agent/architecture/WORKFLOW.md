# PM Agent Workflow

## Tổng thể
```
User request
    ↓
PM Agent analyzes
    ↓
Create charter + requirements
    ↓
Ask clarifying questions
    ↓
Create planning docs (spec/plan/rules/wbs/schedule/risks)
    ↓
Create task-board
    ↓
Execute tasks (loop):
    - Choose task
    - Execute or delegate to worker
    - Review result
    - Update project state
    - Handle issues/risks/changes
    ↓
Close project
    ↓
Create final report + lessons learned
```


## Agent-Teams Execution Branch

Khi dự án là technical project có nhiều vai trò, PM Agent dùng Agent-Teams branch thay cho tự xử lý specialist work.

```
User request
    ↓
PM Orchestrator intake + scope
    ↓
Requirements gate
    ↓
UX / Architecture / API Contract gate
    ↓
Ownership map
    ↓
Parallel execution wave if safe:
    - Frontend Agent
    - Backend Agent
    ↓
QA / Integration wave
    ↓
Review / Production wave:
    - Security Review
    - Performance Review
    - Code Review
    - DevOps / Deployment
    - Documentation
    - Challenge when needed
    ↓
PM final acceptance report
```

### Gate rules

#### Requirements Ready
- MVP scope clear
- out-of-scope listed
- acceptance criteria testable
- open questions marked blocking/non-blocking

#### Architecture/API Ready
- architecture direction exists
- API contract exists
- data model assumptions stated
- Challenge findings resolved or accepted

#### Parallel Execution Ready
- ownership map exists
- frontend/backend owned paths clear
- shared contract frozen for wave
- conflict protocol clear

#### Preflight Ready
- task has `Verification Level`
- `Local` / `Integration` / `Production` tasks include preflight checks
- required tools/commands/dependencies are checked or blocker listed
- install/network policy is explicit
- fallback path is approved when a tool is missing
- browser/UI tasks distinguish browser package availability from browser executable launch readiness
- browser binary install/download requires explicit user approval before worker runs install/download commands

#### Release/Handoff Ready
- QA/integration evidence exists or blocker listed
- security/performance/code review blockers resolved or accepted
- deployment readiness checked
- docs/handoff prepared
- every agent report includes `Verification Level`
- every Local/Integration/Production report includes `Preflight Result`
- no `tested/working/deployed/secure/performant/accessible/integrated/production-ready` claim lacks matching evidence

### Stop conditions

PM Agent must stop and ask user or escalate when:
- production deploy requested
- cloud/DNS/billing action needed
- secret value exposed or requested
- destructive migration/action needed
- high-risk scope change appears
- unresolved ownership conflict exists
- Critical/High security/QA blocker exists

### PM boundary

PM Agent remains orchestrator-only in Agent-Teams mode. It delegates specialist implementation/review and then verifies reports/evidence before moving gates.

### Verification Level workflow

For every delegated Agent-Teams task, PM Agent must:

1. Put `Verification Level` in task packet.
2. Define evidence required for that level.
3. Add `Preflight Required` for `Local`, `Integration`, and `Production` tasks.
4. Require returned report to include same or stronger `Verification Level`.
5. Require `Preflight Result` for Local/Integration/Production reports.
6. Reject or downgrade report to `Needs Review` when evidence does not match claims.
7. Treat `Paper` and `Simulated` as planning/artifact validation only, not real implementation proof.
8. For browser/UI proof, require successful browser executable launch plus screenshot/log evidence before accepting real browser claims; otherwise label result as browser-like fallback or Blocked.
9. For real implementation tasks, require `Local` or `Integration` evidence before accepting completion.
10. For any `Production` verification, require explicit user approval before deploy or cloud/DNS/billing action.

## Chi tiết từng giai đoạn

### Giai đoạn 1: Initiation
- **Input:** User request
- **Output:** charter.md, requirements.md
- **Duration:** 1-2 interactions
- **Key activities:**
  - Phân tích yêu cầu
  - Trích xuất thông tin cốt lõi
  - Phát hiện khoảng trống
  - Tạo danh sách câu hỏi làm rõ
  - Tạo charter nháp

### Giai đoạn 2: Planning
- **Input:** Approved charter
- **Output:** spec.md, plan.md, rules.md, wbs.md, schedule.md, risk-register.md
- **Duration:** 1-2 interactions
- **Key activities:**
  - Tạo Spec (xây cái gì)
  - Tạo Plan (triển khai thế nào)
  - Tạo Rules (nguyên tắc làm việc)
  - Phân rã công việc (WBS)
  - Lập lịch trình
  - Xác định rủi ro

### Giai đoạn 3: Execution
- **Input:** Task board
- **Output:** Completed tasks, updated project state
- **Duration:** Multiple interactions
- **Key activities:**
  - Chọn task tiếp theo
  - Quyết định tự làm hay giao worker
  - Thực thi task
  - Review kết quả
  - Cập nhật tài liệu dự án
  - Xử lý blockers

### Giai đoạn 4: Monitoring
- **Input:** Project state
- **Output:** Status dashboard, alerts, reports
- **Duration:** Periodic
- **Key activities:**
  - Kiểm tra tiến độ
  - Theo dõi issue
  - Theo dõi risk
  - Quản lý change
  - Tạo báo cáo định kỳ

### Giai đoạn 5: Closure
- **Input:** All tasks completed
- **Output:** final-report.md, lessons-learned.md
- **Duration:** 1 interaction
- **Key activities:**
  - Kiểm tra deliverables
  - Xác nhận với user
  - Tạo final report
  - Tạo lessons learned
  - Archive tài liệu
  - Đánh dấu đóng dự án

## Chu trình thực thi task

```
Choose Task
    ↓
Self or Worker?
    ↓
Execute
    ↓
Review Output
    ↓
Update Docs
    ↓
Next Action?
    ↓
Done / Rework / Escalate / Continue
```

## Quy tắc ra quyết định

### Khi nào tự làm?
- Task quản trị
- Task tài liệu
- Task phân tích
- Task đánh giá
- Task cập nhật trạng thái

### Khi nào giao worker?
- Task triển khai kỹ thuật
- Task tạo/sửa nhiều file
- Task cần thao tác chuyên biệt
- Task cần ngữ cảnh cục bộ riêng

### Khi nào hỏi user?
- Yêu cầu mơ hồ
- Thay đổi phạm vi lớn
- Có nhiều phương án chiến lược
- Chuẩn bị chốt kết quả cuối
- Có rủi ro cao hoặc hành động nhạy cảm

## Files cần cập nhật sau mỗi execution

1. **task-board.md** - Update task status, % completion
2. **issue-log.md** - Add new issues, update issue status
3. **change-log.md** - Add new changes, update change status
4. **status-dashboard.md** - Update metrics, timeline, risk status
5. **agent-core/memory/observations/pm-projects.md** - Log project progress, key decisions
