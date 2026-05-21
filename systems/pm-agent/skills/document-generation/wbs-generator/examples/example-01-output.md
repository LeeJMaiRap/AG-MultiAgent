# Work Breakdown Structure: Hệ thống quản lý task nội bộ

## Level 1: Hệ thống quản lý task nội bộ MVP

### Level 2: Setup & Backend Foundation
#### Level 3: Project Setup
##### Level 4: TASK-001 - Khởi tạo project Node.js
- **ID:** TASK-001
- **Description:** Tạo cấu trúc project backend với Node.js và Express
- **Estimated effort:** 4h
- **Dependencies:** None
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** None
- **Output:** Project structure với package.json, server.js, routes/

#### Level 3: Database Setup
##### Level 4: TASK-002 - Setup MongoDB
- **ID:** TASK-002
- **Description:** Cấu hình kết nối MongoDB và tạo database schema cơ bản
- **Estimated effort:** 4h
- **Dependencies:** TASK-001
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** Database credentials
- **Output:** Database connection file và schema setup

##### Level 4: TASK-003 - Tạo models
- **ID:** TASK-003
- **Description:** Tạo models User, Task, Comment, Attachment
- **Estimated effort:** 6h
- **Dependencies:** TASK-002
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** Database schema
- **Output:** Model files

#### Level 3: Authentication
##### Level 4: TASK-004 - Tạo authentication system
- **ID:** TASK-004
- **Description:** Implement JWT authentication với register/login endpoints
- **Estimated effort:** 8h
- **Dependencies:** TASK-003
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** User model
- **Output:** Auth endpoints và middleware xác thực

#### Level 3: API Endpoints
##### Level 4: TASK-005 - Tạo API task CRUD
- **ID:** TASK-005
- **Description:** Tạo API endpoints cho create/read/update/delete task
- **Estimated effort:** 8h
- **Dependencies:** TASK-003, TASK-004
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** Models, auth middleware
- **Output:** Task API endpoints

##### Level 4: TASK-006 - Tạo API comment và attachment
- **ID:** TASK-006
- **Description:** Tạo API cho comment và upload file attachment
- **Estimated effort:** 8h
- **Dependencies:** TASK-005
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** Task API, models
- **Output:** Comment API và upload API

### Level 2: Frontend Core Features
#### Level 3: Frontend Setup
##### Level 4: TASK-007 - Setup React project
- **ID:** TASK-007
- **Description:** Tạo project React với Vite và cấu hình cơ bản
- **Estimated effort:** 4h
- **Dependencies:** None
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** None
- **Output:** Frontend project structure

#### Level 3: Layout & Navigation
##### Level 4: TASK-008 - Tạo layout chính
- **ID:** TASK-008
- **Description:** Tạo header, sidebar, main layout và navigation
- **Estimated effort:** 6h
- **Dependencies:** TASK-007
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** Design direction
- **Output:** Layout components

#### Level 3: Task Management UI
##### Level 4: TASK-009 - Trang danh sách task
- **ID:** TASK-009
- **Description:** Tạo UI hiển thị danh sách task với trạng thái cơ bản
- **Estimated effort:** 8h
- **Dependencies:** TASK-008, TASK-005
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** Task API
- **Output:** Task list component

##### Level 4: TASK-010 - Form tạo và chỉnh sửa task
- **ID:** TASK-010
- **Description:** Tạo form create/edit task với deadline và owner
- **Estimated effort:** 8h
- **Dependencies:** TASK-009
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** Task API
- **Output:** Task form component

##### Level 4: TASK-011 - UI phân công và cập nhật trạng thái
- **ID:** TASK-011
- **Description:** Tạo UI assign owner và update status cho task
- **Estimated effort:** 6h
- **Dependencies:** TASK-010
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** Task API
- **Output:** Assignment/status controls

### Level 2: Collaboration Features
#### Level 3: Comment System
##### Level 4: TASK-012 - UI comment trong task
- **ID:** TASK-012
- **Description:** Tạo giao diện comment trong trang chi tiết task
- **Estimated effort:** 6h
- **Dependencies:** TASK-011, TASK-006
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** Comment API
- **Output:** Comment UI

#### Level 3: File Attachment
##### Level 4: TASK-013 - UI đính kèm file
- **ID:** TASK-013
- **Description:** Tạo giao diện upload và hiển thị file đính kèm
- **Estimated effort:** 6h
- **Dependencies:** TASK-012, TASK-006
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** Upload API
- **Output:** Attachment UI

### Level 2: Admin & Permissions
#### Level 3: Authorization
##### Level 4: TASK-014 - Middleware phân quyền
- **ID:** TASK-014
- **Description:** Implement role-based access control trên backend
- **Estimated effort:** 6h
- **Dependencies:** TASK-004
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** Auth system
- **Output:** Authorization middleware

##### Level 4: TASK-015 - Kiểm tra quyền trên frontend
- **ID:** TASK-015
- **Description:** Ẩn/hiện chức năng theo role admin/member
- **Estimated effort:** 4h
- **Dependencies:** TASK-014, TASK-009
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** User role data
- **Output:** Permission-aware UI

### Level 2: Testing & Refinement
#### Level 3: Core Flow Testing
##### Level 4: TASK-016 - Test luồng task management
- **ID:** TASK-016
- **Description:** Test create, update, assign, status flow
- **Estimated effort:** 6h
- **Dependencies:** TASK-011
- **Assigned to:** Developer A + Developer B
- **Status:** Not Started
- **Input:** Running system
- **Output:** Test report

##### Level 4: TASK-017 - Test collaboration features
- **ID:** TASK-017
- **Description:** Test comment và attachment flow
- **Estimated effort:** 4h
- **Dependencies:** TASK-013
- **Assigned to:** Developer A + Developer B
- **Status:** Not Started
- **Input:** Running system
- **Output:** Test report

##### Level 4: TASK-018 - Responsive testing và bug fixes
- **ID:** TASK-018
- **Description:** Test trên mobile/desktop và fix bug quan trọng
- **Estimated effort:** 8h
- **Dependencies:** TASK-016, TASK-017
- **Assigned to:** Developer B
- **Status:** Not Started
- **Input:** Test results
- **Output:** Stable MVP build

### Level 2: Deployment & Handover
#### Level 3: Deployment
##### Level 4: TASK-019 - Deploy backend và frontend
- **ID:** TASK-019
- **Description:** Deploy hệ thống lên môi trường sử dụng thực tế
- **Estimated effort:** 6h
- **Dependencies:** TASK-018
- **Assigned to:** Developer A
- **Status:** Not Started
- **Input:** Stable MVP build
- **Output:** Deployed system

##### Level 4: TASK-020 - Documentation và handover
- **ID:** TASK-020
- **Description:** Viết README, user guide và bàn giao sử dụng ban đầu
- **Estimated effort:** 6h
- **Dependencies:** TASK-019
- **Assigned to:** Developer A + Developer B
- **Status:** Not Started
- **Input:** Deployed system
- **Output:** Documentation + handover notes

## Summary
- **Total tasks:** 20
- **Estimated total time:** ~118h
- **Critical path:** TASK-001 → TASK-002 → TASK-003 → TASK-004 → TASK-005 → TASK-006 → TASK-009 → TASK-010 → TASK-011 → TASK-012 → TASK-013 → TASK-016 → TASK-017 → TASK-018 → TASK-019 → TASK-020
