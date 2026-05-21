# Project Plan: Hệ thống quản lý công việc nội bộ

## 1. Phases
### Phase 1: Setup & Backend Foundation
- **Duration:** 1 tuần
- **Deliverables:** Auth + task API contract + task CRUD nền tảng
- **Milestones:** Backend foundation usable

### Phase 2: Frontend Core
- **Duration:** 2 tuần
- **Deliverables:** Task list, task form, task detail cơ bản
- **Milestones:** Core task flow chạy được end-to-end

### Phase 3: Collaboration & Dashboard
- **Duration:** 1 tuần
- **Deliverables:** Comment + dashboard cơ bản
- **Milestones:** MVP feature complete

### Phase 4: Testing & Deployment
- **Duration:** 2 tuần
- **Deliverables:** Stable MVP + internal rollout
- **Milestones:** MVP usable nội bộ

## 2. Work Breakdown Structure (WBS)
1. Backend foundation
   1.1 Auth module
   1.2 Task CRUD + API contract
   1.3 Dashboard summary API
2. Frontend core
   2.1 Task list UI
   2.2 Task create/edit form
   2.3 Task detail view
3. Collaboration & dashboard
   3.1 Comment flow
   3.2 Dashboard UI
4. Testing & deployment
   4.1 Validation + smoke test
   4.2 Deploy nội bộ

## 3. Dependencies
- Auth -> Task CRUD
- Task CRUD + API contract -> Frontend task list / form
- Task detail -> Comment flow
- Task CRUD -> Dashboard summary API -> Dashboard UI
- All core features -> QA -> Deploy

## 4. Resource Allocation
| Task Area | Assigned To | Estimated Hours | Notes |
|-----------|-------------|-----------------|-------|
| Backend foundation | Backend dev | 36h | Auth + CRUD + contract |
| Frontend core | Frontend dev | 44h | Main UI flow |
| QA / validation | Tester part-time | 16h | Smoke + regression |
| PM / coordination | PM Agent | 8h | Scope control + reporting |

## 5. Communication Plan
- Daily sync ngắn trong phase active development
- Weekly review mỗi thứ 6
- Chốt API contract trước khi frontend core mở mạnh

## 6. Risk Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Scope dashboard tăng | Medium | High | Khóa dashboard ở mức tổng hợp cơ bản |
| API contract đổi muộn | High | High | Chốt request/response schema trước frontend |
| Feedback test chậm | Medium | Medium | Lịch review cố định + smoke test checklist |

## 7. Success Criteria
- ✅ MVP dùng được nội bộ
- ✅ Core task flow ổn định
- ✅ Dashboard cơ bản hoạt động
- ✅ Hoàn thành trong 6 tuần hoặc lệch không quá buffer đã chấp nhận
