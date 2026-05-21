# Task Board: Trang Web Bán Hàng

## Status Legend
- 🔴 Not Started
- 🟡 In Progress
- 🟢 Done
- ⚫ Blocked
- ⚪ Cancelled

## Project Status Note
**Current lifecycle:** `on-hold`  
**Current mode:** `demo`  
**Project state:** Demo-ready reference, không còn active delivery project.

**Important:** Task board này đã được reconcile vào 2026-05-15 theo `conflict-resolution-2026-05-15.md` vì bản cũ không còn phản ánh đúng deliverables thực tế.

---

## Done (Hoàn thành / Demo-ready deliverables)

| ID | Task | Assigned | Status | Evidence |
|----|------|----------|--------|----------|
| TASK-001 | Charter creation | PM Agent | 🟢 | `01-initiation/charter.md` |
| TASK-002 | Requirements creation | PM Agent | 🟢 | `01-initiation/requirements.md` |
| TASK-003 | Planning docs creation | PM Agent | 🟢 | `02-planning/plan.md`, `spec.md`, `wbs.md`, `schedule.md`, `risk-register.md`, `rules.md` |
| TASK-004 | Setup backend foundation | Worker Agent | 🟢 | `backend/server.js`, `backend/package.json` |
| TASK-005 | Database/config foundation | Worker Agent | 🟢 | `backend/config/database.js`, `.env.example` |
| TASK-006 | Models implementation | Worker Agent | 🟢 | `backend/models/` |
| TASK-007 | Auth API foundation | Worker Agent | 🟢 | `backend/controllers/auth.js`, `backend/routes/auth.js`, `backend/middleware/auth.js` |
| TASK-008 | Product API foundation | Worker Agent | 🟢 | `backend/controllers/products.js`, `backend/routes/products.js` |
| TASK-009 | Cart API foundation | Worker Agent | 🟢 | `backend/controllers/cart.js`, `backend/routes/cart.js` |
| TASK-010 | Orders API foundation | Worker Agent | 🟢 | `backend/controllers/orders.js`, `backend/routes/orders.js` |
| TASK-011 | Seed/mock data foundation | Worker Agent | 🟢 | `backend/seed/products.js` |
| TASK-012 | Setup frontend foundation | Worker Agent | 🟢 | `frontend/package.json`, `vite.config.js`, `src/main.jsx` |
| TASK-013 | Home/storefront UI | Worker Agent | 🟢 | `frontend/src/pages/Home.jsx`, layout components |
| TASK-014 | Product listing/detail UI | Worker Agent | 🟢 | `frontend/src/pages/Products.jsx`, `ProductDetail.jsx`, related components |
| TASK-015 | Cart/checkout UI flow | Worker Agent | 🟢 | `frontend/src/pages/Cart.jsx`, `Checkout.jsx`, related components |
| TASK-016 | Auth UI flow | Worker Agent | 🟢 | `frontend/src/pages/Login.jsx`, `Register.jsx`, `components/AuthForm.jsx` |
| TASK-017 | Admin foundation UI | Worker Agent | 🟢 | `frontend/src/pages/Admin.jsx`, admin components |
| TASK-018 | Build/demo verification artifacts | PM Agent | 🟢 | `frontend/dist/`, `DEMO_GUIDE.md` |
| TASK-019 | Final report / validation snapshot | PM Agent | 🟢 | `05-closure/final-report.md` |

## In Progress / Partial

| ID | Task | Assigned | Status | Note |
|----|------|----------|--------|------|
| TASK-020 | Production hardening | PM Agent | 🟡 Partial | Chưa production-ready |
| TASK-021 | Full verification / exhaustive testing | PM Agent | 🟡 Partial | Mới đủ cho demo/validation |
| TASK-022 | Final polish admin/deployment/monitoring | PM Agent | 🟡 Partial | Nêu rõ trong final report |

## Not Completed / Deferred

| ID | Task | Reason |
|----|------|--------|
| TASK-023 | Production deployment readiness | Bị cắt khỏi scope demo/MVP |
| TASK-024 | Full monitoring/operations hardening | Bị cắt khỏi scope demo/MVP |
| TASK-025 | Full production QA pass | Chưa nằm trong mức validation này |
| TASK-026 | Real payment/shipping/email flows | Scope reduction sang MVP demo |
| TASK-027 | Advanced analytics | Scope reduction sang MVP demo |
| TASK-028 | Production security hardening | Chưa làm trong validation này |
| TASK-029 | Large-scale performance validation | Chưa làm trong validation này |
| TASK-030 | Full deployment automation | Chưa làm trong validation này |
| TASK-031 | Extended responsive/polish pass | Partial only |
| TASK-032 | Comprehensive final acceptance | Chưa đủ production criteria |
| TASK-033 | Full operational handoff pack | Chưa cần cho demo reference |

## Summary
- **Total tasks:** 33
- **Completed:** 19 (58%)
- **In Progress / Partial:** 3 (9%)
- **Deferred / Not completed:** 11 (33%)
- **Current state:** Demo-ready, on-hold reference
- **Completion basis:** Reconciled to match evidence + `project.yaml`

## Current Phase
**Validation complete / Demo-ready reference**
- Lifecycle: `on-hold`
- Delivery mode: `demo`
- Not an active execution board anymore

## Next Actions
1. Không tiếp tục dùng board này như active delivery board
2. Nếu tái sử dụng project này làm reference, dùng `final-report.md` + `DEMO_GUIDE.md` + conflict resolution note làm source chính
3. Nếu muốn revive project, cần lập active task board mới hoặc reopen board với scope mới
