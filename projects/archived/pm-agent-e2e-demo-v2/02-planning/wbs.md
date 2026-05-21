# Work Breakdown Structure: Hệ thống quản lý công việc nội bộ

## Level 1: Hệ thống quản lý công việc nội bộ MVP

### Level 2: Backend Foundation
#### Level 3: Authentication
##### Level 4: TASK-001 - Implement auth module
- **ID:** TASK-001
- **Description:** Xây đăng ký/đăng nhập và xác thực JWT.
- **Estimated effort:** 12h
- **Dependencies:** None
- **Assigned to:** Backend dev
- **Status:** Done
- **Input:** Charter, requirements, spec
- **Output:** Auth endpoints

#### Level 3: Task API
##### Level 4: TASK-002 - Implement task CRUD + contract
- **ID:** TASK-002
- **Description:** Xây API CRUD cho task và khóa response schema để frontend có thể dùng ổn định.
- **Estimated effort:** 14h
- **Dependencies:** TASK-001
- **Assigned to:** Backend dev
- **Status:** In Progress
- **Input:** Requirements, spec
- **Output:** Task API + example payloads

##### Level 4: TASK-003 - Add dashboard summary API
- **ID:** TASK-003
- **Description:** Tạo API aggregate tổng số task theo trạng thái cho dashboard MVP.
- **Estimated effort:** 6h
- **Dependencies:** TASK-002
- **Assigned to:** Backend dev
- **Status:** Not Started
- **Input:** Spec, task data model
- **Output:** Dashboard summary API

### Level 2: Frontend Core
#### Level 3: Task UI
##### Level 4: TASK-004 - Build task list UI
- **ID:** TASK-004
- **Description:** Tạo màn hình danh sách task với filter cơ bản.
- **Estimated effort:** 12h
- **Dependencies:** TASK-002
- **Assigned to:** Frontend dev
- **Status:** Blocked
- **Input:** Stable task list API contract
- **Output:** Task list page

##### Level 4: TASK-005 - Build task form UI
- **ID:** TASK-005
- **Description:** Tạo form create/edit task với validation cơ bản.
- **Estimated effort:** 10h
- **Dependencies:** TASK-004
- **Assigned to:** Frontend dev
- **Status:** Not Started
- **Input:** Task list UI, create/update API
- **Output:** Task form

##### Level 4: TASK-006 - Build task detail + comments UI
- **ID:** TASK-006
- **Description:** Tạo task detail view và comment flow cơ bản.
- **Estimated effort:** 14h
- **Dependencies:** TASK-005
- **Assigned to:** Frontend dev
- **Status:** Not Started
- **Input:** Task detail API, comment API
- **Output:** Task detail + comments

### Level 2: Monitoring & Release
#### Level 3: Dashboard + QA
##### Level 4: TASK-007 - Build dashboard UI
- **ID:** TASK-007
- **Description:** Tạo dashboard MVP hiển thị tổng số task và phân bổ theo trạng thái.
- **Estimated effort:** 8h
- **Dependencies:** TASK-003, TASK-004
- **Assigned to:** Frontend dev
- **Status:** Not Started
- **Input:** Dashboard summary API
- **Output:** Dashboard page

##### Level 4: TASK-008 - Run smoke test and internal rollout prep
- **ID:** TASK-008
- **Description:** Chạy smoke test cho auth, task flow, comments và dashboard trước internal rollout.
- **Estimated effort:** 10h
- **Dependencies:** TASK-006, TASK-007
- **Assigned to:** Tester part-time
- **Status:** Not Started
- **Input:** Built MVP
- **Output:** Test checklist + release readiness

## Summary
- **Total tasks:** 8
- **Estimated total time:** 86h
- **Critical path:** TASK-001 → TASK-002 → TASK-004 → TASK-005 → TASK-006 → TASK-008
