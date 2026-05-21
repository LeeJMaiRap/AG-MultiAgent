# Task Board: Web Bán Acc Game

## Backlog

### TASK-001: Setup project structure
- **Description:** Khởi tạo Next.js project, cấu trúc folder, cài dependencies
- **Priority:** Critical
- **Estimate:** 1h
- **Status:** todo
- **Dependencies:** None

### TASK-002: Setup database & schema
- **Description:** Tạo database (SQLite/MongoDB), định nghĩa schema acc game
- **Priority:** Critical
- **Estimate:** 1h
- **Status:** todo
- **Dependencies:** TASK-001

### TASK-003: Backend API - CRUD acc
- **Description:** API endpoints: GET /api/accs, GET /api/accs/:id, POST/PUT/DELETE (admin only)
- **Priority:** High
- **Estimate:** 2h
- **Status:** todo
- **Dependencies:** TASK-002

### TASK-004: Admin authentication
- **Description:** Login page, JWT/session, protect admin routes
- **Priority:** High
- **Estimate:** 1.5h
- **Status:** todo
- **Dependencies:** TASK-002

### TASK-005: Frontend - Danh sách acc (public)
- **Description:** Trang chủ hiển thị grid acc, filter theo game, search cơ bản
- **Priority:** High
- **Estimate:** 2h
- **Status:** todo
- **Dependencies:** TASK-003

### TASK-006: Frontend - Chi tiết acc (public)
- **Description:** Trang chi tiết 1 acc, hiển thị ảnh, thông tin, CTA liên hệ
- **Priority:** High
- **Estimate:** 1.5h
- **Status:** todo
- **Dependencies:** TASK-003

### TASK-007: Admin panel - Dashboard & list
- **Description:** Trang admin dashboard, bảng danh sách acc
- **Priority:** High
- **Estimate:** 1.5h
- **Status:** todo
- **Dependencies:** TASK-004

### TASK-008: Admin panel - Create/Edit acc
- **Description:** Form thêm/sửa acc, upload ảnh
- **Priority:** High
- **Estimate:** 2h
- **Status:** todo
- **Dependencies:** TASK-007

### TASK-009: Admin panel - Delete acc
- **Description:** Nút xóa acc, confirm dialog
- **Priority:** Medium
- **Estimate:** 0.5h
- **Status:** todo
- **Dependencies:** TASK-007

### TASK-010: Image upload & storage
- **Description:** Tích hợp Cloudinary hoặc local storage cho ảnh acc
- **Priority:** High
- **Estimate:** 1.5h
- **Status:** todo
- **Dependencies:** TASK-002

### TASK-011: Responsive UI polish
- **Description:** Đảm bảo responsive mobile + desktop, polish UI/UX
- **Priority:** Medium
- **Estimate:** 2h
- **Status:** todo
- **Dependencies:** TASK-005, TASK-006, TASK-008

### TASK-012: Testing & bug fixes
- **Description:** Test toàn bộ flow khách + admin, fix bugs
- **Priority:** High
- **Estimate:** 2h
- **Status:** todo
- **Dependencies:** All above

### TASK-013: Deploy to hosting
- **Description:** Deploy lên Vercel/Netlify, config domain/env
- **Priority:** High
- **Estimate:** 1h
- **Status:** todo
- **Dependencies:** TASK-012

### TASK-014: Seed data mẫu
- **Description:** Tạo 10-20 acc mẫu để demo
- **Priority:** Medium
- **Estimate:** 0.5h
- **Status:** todo
- **Dependencies:** TASK-003

## In Progress
_(empty)_

## Done
_(empty)_

## Blocked
_(empty)_

---

**Total estimate:** ~19h
**Timeline:** 2 days (Day 1: ~10h, Day 2: ~9h)
**Critical path:** TASK-001 → TASK-002 → TASK-003 → TASK-005/006 → TASK-012 → TASK-013
