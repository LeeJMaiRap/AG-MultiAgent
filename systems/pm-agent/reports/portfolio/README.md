# Portfolio Dashboard Foundation

## Mục đích
Cung cấp visibility tổng thể về tất cả projects được PM Agent quản lý, không chỉ active projects.

## Phạm vi
- Active projects
- On-hold projects
- Stopped projects
- Archived projects

## Dashboard Structure

### 1. Active Projects
Path: `projects/active/`

**Metrics:**
- Số lượng projects active
- Tổng tasks across active projects
- Completion % trung bình
- Projects có stale risk
- Projects có source conflict

**Output location:**
- `systems/pm-agent/reports/portfolio/active-projects-dashboard.md`

---

### 2. On-Hold Projects
Path: `projects/on-hold/`

**Metrics:**
- Số lượng projects on-hold
- Lý do on-hold (nếu có trong metadata)
- Thời gian on-hold
- Điều kiện để resume (nếu có)

**Output location:**
- `systems/pm-agent/reports/portfolio/on-hold-projects-dashboard.md`

---

### 3. Stopped Projects
Path: `projects/stopped/`

**Metrics:**
- Số lượng projects stopped
- Lý do stopped
- Lessons learned có được capture chưa

**Output location:**
- `systems/pm-agent/reports/portfolio/stopped-projects-dashboard.md`

---

### 4. Archived Projects
Path: `projects/archived/`

**Metrics:**
- Số lượng projects archived
- Completion status khi archive
- Lessons learned availability
- Reference value

**Output location:**
- `systems/pm-agent/reports/portfolio/archived-projects-dashboard.md`

---

## Portfolio Summary

**Output location:**
`systems/pm-agent/reports/portfolio/portfolio-summary.md`

**Content:**
- Total projects across all lifecycles
- Breakdown by lifecycle status
- Health indicators:
  - Active projects with stale risk
  - On-hold projects quá lâu
  - Path/metadata mismatches
  - Source conflicts unresolved
- Recent transitions (active → on-hold, etc.)

---

## Update Frequency

### Active projects dashboard
- Daily (via cron hoặc on-demand)

### On-hold/stopped/archived dashboards
- Weekly hoặc on-demand
- Hoặc khi có lifecycle transition

### Portfolio summary
- Daily hoặc on-demand

---

## Data Sources

### Per-project
- `project.yaml` - metadata, status, metrics
- `03-execution/task-board.md` - task progress
- `04-monitoring/status-dashboard.md` - current status
- `03-execution/issue-log.md` - open issues
- `lessons-learned.md` - lessons (nếu có)

### Cross-project
- Scan `projects/*/project.yaml`
- Aggregate metrics
- Detect mismatches (path vs metadata)
- Detect stale projects

---

## Foundation Rules

### 1. Lifecycle folder structure
```
projects/
├── active/
├── on-hold/
├── stopped/
└── archived/
```

### 2. Metadata priority
- Metadata `status` field thắng folder path khi conflict
- Dashboard phải log mismatch nếu có

### 3. Stale detection integration
- Active projects: check stale theo policy
- On-hold projects: track thời gian on-hold
- Stopped projects: không check stale
- Archived projects: không check stale

### 4. Actor attribution
- Dashboard không bịa actor
- Dùng actor từ project artifacts nếu có
- Dùng `unknown` nếu không rõ

---

## Implementation Notes

### Phase 1 (foundation)
- Tạo folder structure cho portfolio reports
- Tạo template cho từng dashboard type
- Định nghĩa data schema

### Phase 2 (automation)
- Script/skill để generate dashboards
- Integration với daily cron
- Notification khi có anomaly

### Phase 3 (enhancement)
- Trend analysis
- Predictive stale detection
- Cross-project dependency tracking

---

## Current Status
**Foundation established:** 2026-05-15
**Implementation level:** Phase 1 (foundation only)
**Next step:** Create templates and initial dashboards
