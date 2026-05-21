# PM Agent State Schema

Định nghĩa trạng thái vận hành chuẩn cho PM Agent.

## 1. System-level state

PM Agent có trạng thái ở 2 lớp:

### A. Agent Framework State
Trạng thái của chính PM Agent framework.

```yaml
agent_state:
  version: "1.0"
  status: active
  mode: production-readiness
  current_focus: runtime-standardization
  last_updated: ISO-8601
```

### B. Project Operational State
Trạng thái của từng project mà PM Agent quản lý.

```yaml
project_state:
  project_id: string
  phase: initiation|planning|execution|monitoring|closure
  status: active|on-hold|archived|cancelled
  health: green|yellow|red
  completion_percentage: integer
  current_task: string
  next_action: string
  blockers: []
  pending_approvals: []
  hot_risks: []
  last_updated: ISO-8601
```

## 2. Source of truth

### Không được dùng chat làm source of truth
Mọi state quan trọng phải nằm trong file:

- `project.yaml` → metadata tổng thể
- `03-execution/task-board.md` → trạng thái task
- `03-execution/issue-log.md` → issues
- `03-execution/change-log.md` → changes
- `04-monitoring/status-dashboard.md` → status tổng hợp
- `decisions/decision-log.md` → decisions
- `approvals/*.md` → approvals

## 3. State update rules

### Bắt buộc cập nhật sau mỗi execution cycle
1. Task status
2. Current phase progress
3. Issues / blockers mới
4. Risk escalation nếu có
5. Last updated timestamp

### Không cập nhật nếu chưa có bằng chứng
- Không đánh dấu task done nếu chưa có output/evidence
- Không đóng issue nếu chưa xác minh
- Không update progress % theo cảm tính

## 4. Recovery / resume rules

Khi resume project sau gián đoạn, PM Agent phải đọc theo thứ tự:
1. `project.yaml`
2. `04-monitoring/status-dashboard.md`
3. `03-execution/task-board.md`
4. `03-execution/issue-log.md`
5. `03-execution/change-log.md`
6. `decisions/decision-log.md` (nếu có)
7. `approvals/` folder (nếu có)

## 5. Health scoring

### Green
- Không có blocker critical
- Timeline on track
- Approval không pending quá lâu
- Risks under control

### Yellow
- Có blocker nhưng workaround được
- Có risk cao cần theo dõi sát
- Approval pending nhưng chưa quá timeout

### Red
- Blocker critical
- Scope/timeline lệch lớn
- Approval pending quá timeout
- Deliverable cốt lõi có nguy cơ fail
