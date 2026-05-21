# Task Board: Hệ thống quản lý công việc nội bộ

## Status Legend
- 🔴 Not Started
- 🟡 In Progress
- 🟢 Done
- ⚫ Blocked
- ⚪ Cancelled

## Backlog (Chưa bắt đầu)
| ID | Task | Assigned | Estimate | Priority | Status |
|----|------|----------|----------|----------|--------|
| TASK-003 | Add dashboard summary API | Backend dev | 6h | Medium | 🔴 |
| TASK-005 | Build task form UI | Frontend dev | 10h | High | 🔴 |
| TASK-006 | Build task detail + comments UI | Frontend dev | 14h | Medium | 🔴 |
| TASK-007 | Build dashboard UI | Frontend dev | 8h | Medium | 🔴 |
| TASK-008 | Run smoke test and rollout prep | Tester part-time | 10h | High | 🔴 |

## In Progress (Đang làm)
| ID | Task | Assigned | Estimate | Actual | % Done | Blocker |
|----|------|----------|----------|--------|--------|---------|
| TASK-002 | Implement task CRUD + contract | Backend dev | 14h | 8h | 60% | None |

## Done (Hoàn thành)
| ID | Task | Assigned | Estimate | Actual | Completed Date |
|----|------|----------|----------|--------|-----------------|
| TASK-001 | Implement auth module | Backend dev | 12h | 10h | 2026-05-15 |

## Blocked (Bị chặn)
| ID | Task | Assigned | Blocker | Since | Action |
|----|------|----------|---------|-------|--------|
| TASK-004 | Build task list UI | Frontend dev | Task list response schema chưa được khóa ổn định | 2026-05-16 | Chốt API contract và publish sample payload |

## Summary
- **Total tasks:** 8
- **Completed:** 1 (12.5%)
- **In Progress:** 1 (12.5%)
- **Blocked:** 1 (12.5%)
- **Not Started:** 5 (62.5%)
- **Cancelled:** 0 (0%)
- **On-time %:** 85%
- **Current phase:** Backend Foundation / Frontend handoff

## Next Actions
1. Chốt API contract cho task list và task detail
   - **Owner:** Backend dev
   - **Priority:** Critical
   - **Deadline:** 2026-05-17
2. Review schema với frontend trước khi gỡ blocker TASK-004
   - **Owner:** PM Agent
   - **Priority:** High
   - **Deadline:** 2026-05-17
3. Chuẩn bị checklist validation cho task form trước khi TASK-005 bắt đầu
   - **Owner:** Frontend dev
   - **Priority:** Medium
   - **Deadline:** 2026-05-23
