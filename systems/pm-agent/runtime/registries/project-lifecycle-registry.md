# Project Lifecycle Registry

Registry chuẩn cho vòng đời project trong PM Agent.

## Lifecycle states

| Phase | Entry Criteria | Exit Criteria | Key Artifacts |
|-------|----------------|---------------|---------------|
| Initiation | User request received | Charter + requirements approved | charter.md, requirements.md |
| Planning | Initiation approved | Plan docs complete + approved | spec.md, plan.md, rules.md, wbs.md, schedule.md, risk-register.md |
| Execution | Planning approved | Core deliverables built | task-board.md, issue-log.md, change-log.md |
| Monitoring | Project active | Project ready for closure | status-dashboard.md |
| Closure | All major tasks done | Closure approved + archived | final-report.md, lessons-learned.md |

## Phase transition rules

### Initiation → Planning
Required:
- Charter exists
- Requirements exists
- Scope approved

### Planning → Execution
Required:
- Spec, plan, rules, wbs, schedule, risk register exist
- Plan approved
- Task board created

### Execution → Monitoring
Required:
- Minimum 1 execution cycle completed
- Status dashboard initialized

### Monitoring → Closure
Required:
- All critical tasks done
- Open issues accepted or resolved
- Final deliverables verified
- Closure approval ready

## Archive rules

Project được archive khi:
- Closure approved, hoặc
- Demo/validation complete và không còn active work
- Owner quyết định dừng project

Project archive path:
- `projects/archived/[project-name]/`
