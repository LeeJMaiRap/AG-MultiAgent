# Task Board: Hệ thống quản lý task nội bộ

## Status Legend
- 🔴 Not Started
- 🟡 In Progress
- 🟢 Done
- ⚫ Blocked
- ⚪ Cancelled

## Backlog (Chưa bắt đầu)
| ID | Task | Assigned | Estimate | Priority | Status |
|----|------|----------|----------|----------|--------|
| TASK-004 | Tạo authentication system | Developer A | 8h | High | 🔴 |
| TASK-005 | Tạo API task CRUD | Developer A | 8h | High | 🔴 |
| TASK-009 | Trang danh sách task | Developer B | 8h | Medium | 🔴 |

## In Progress (Đang làm)
| ID | Task | Assigned | Estimate | Actual | % Done | Blocker |
|----|------|----------|----------|--------|--------|---------|
| TASK-003 | Tạo models | Developer A | 6h | 3h | 50% | None |

## Done (Hoàn thành)
| ID | Task | Assigned | Estimate | Actual | Completed Date |
|----|------|----------|----------|--------|-----------------|
| TASK-001 | Khởi tạo project Node.js | Developer A | 4h | 3.5h | 2026-05-15 |
| TASK-002 | Setup MongoDB | Developer A | 4h | 4h | 2026-05-15 |
| TASK-007 | Setup React project | Developer B | 4h | 4h | 2026-05-16 |

## Blocked (Bị chặn)
| ID | Task | Assigned | Blocker | Since | Action |
|----|------|----------|---------|-------|--------|
| TASK-008 | Tạo layout chính | Developer B | Chưa có design direction | 2026-05-16 | Xin xác nhận design direction hoặc dùng default layout để tiếp tục |

## Summary
- **Total tasks:** 8
- **Completed:** 3 (37.5%)
- **In Progress:** 1 (12.5%)
- **Blocked:** 1 (12.5%)
- **Not Started:** 3 (37.5%)
- **Cancelled:** 0 (0%)
- **On-time %:** 100%
- **Current phase:** Setup & Backend Foundation

## Next Actions
1. Hoàn thành TASK-003 để mở đường cho TASK-004 và TASK-005
2. Gỡ blocker của TASK-008 bằng cách chốt design direction sớm
3. Sau khi auth xong, chuyển trọng tâm sang API task CRUD và task list UI
