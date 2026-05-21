# Work Breakdown Structure: Trang Web Bán Hàng

## Level 1: Trang Web Bán Hàng MVP

### Level 2: Setup & Backend Foundation
#### Level 3: Project Setup
##### Level 4: TASK-001 - Khởi tạo project Node.js
- **ID:** TASK-001
- **Description:** Tạo cấu trúc project Node.js với Express
- **Estimated effort:** 30 phút
- **Dependencies:** None
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Project structure với package.json, server.js, routes/

#### Level 3: Database Setup
##### Level 4: TASK-002 - Setup MongoDB/MySQL
- **ID:** TASK-002
- **Description:** Cấu hình database connection
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-001
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Database credentials
- **Output:** Database connection file

##### Level 4: TASK-003 - Tạo models
- **ID:** TASK-003
- **Description:** Tạo User, Product, Order, Cart models
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-002
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Database schema
- **Output:** Model files

#### Level 3: Authentication
##### Level 4: TASK-004 - Tạo authentication system
- **ID:** TASK-004
- **Description:** Implement JWT authentication
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-003
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** User model
- **Output:** Auth endpoints (register, login)

#### Level 3: API Endpoints
##### Level 4: TASK-005 - Tạo API endpoints cơ bản
- **ID:** TASK-005
- **Description:** Tạo endpoints cho products, cart, orders
- **Estimated effort:** 2 giờ
- **Dependencies:** TASK-003, TASK-004
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Models
- **Output:** API endpoints

### Level 2: Frontend - Trang chủ & Danh sách sản phẩm
#### Level 3: Project Setup
##### Level 4: TASK-006 - Setup React/Vue project
- **ID:** TASK-006
- **Description:** Tạo React/Vue project với Vite
- **Estimated effort:** 30 phút
- **Dependencies:** None
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Frontend project structure

#### Level 3: Layout & Navigation
##### Level 4: TASK-007 - Tạo layout chính
- **ID:** TASK-007
- **Description:** Header, footer, sidebar, navigation
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-006
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Design mockup
- **Output:** Layout components

#### Level 3: Trang chủ
##### Level 4: TASK-008 - Trang chủ với slider
- **ID:** TASK-008
- **Description:** Hero slider, featured products, categories
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-007
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** API endpoints
- **Output:** Home page component

#### Level 3: Danh sách sản phẩm
##### Level 4: TASK-009 - Danh sách sản phẩm
- **ID:** TASK-009
- **Description:** Product grid, pagination
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-008
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** API endpoints
- **Output:** Product list component

#### Level 3: Tìm kiếm & Lọc
##### Level 4: TASK-010 - Tìm kiếm sản phẩm
- **ID:** TASK-010
- **Description:** Search bar, real-time search
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-009
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** API endpoints
- **Output:** Search component

##### Level 4: TASK-011 - Lọc sản phẩm
- **ID:** TASK-011
- **Description:** Filter by category, price
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-010
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** API endpoints
- **Output:** Filter sidebar

### Level 2: Frontend - Chi tiết & Giỏ hàng
#### Level 3: Chi tiết sản phẩm
##### Level 4: TASK-012 - Trang chi tiết sản phẩm
- **ID:** TASK-012
- **Description:** Product detail page với hình ảnh, mô tả, giá
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-009
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** API endpoints
- **Output:** Product detail component

#### Level 3: Giỏ hàng
##### Level 4: TASK-013 - Giỏ hàng
- **ID:** TASK-013
- **Description:** Cart component với thêm/xóa/sửa số lượng
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-012
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** API endpoints
- **Output:** Cart component

### Level 2: Frontend - Checkout & Auth
#### Level 3: Thanh toán
##### Level 4: TASK-014 - Form thanh toán
- **ID:** TASK-014
- **Description:** Checkout form với thông tin giao hàng
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-013
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** API endpoints
- **Output:** Checkout component

#### Level 3: Authentication
##### Level 4: TASK-015 - Form đăng ký
- **ID:** TASK-015
- **Description:** Registration form với validation
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-004
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Auth API
- **Output:** Register component

##### Level 4: TASK-016 - Form đăng nhập
- **ID:** TASK-016
- **Description:** Login form với JWT
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-004
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Auth API
- **Output:** Login component

### Level 2: Admin Dashboard
#### Level 3: Admin Panel
##### Level 4: TASK-017 - Trang admin
- **ID:** TASK-017
- **Description:** Protected admin page
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-016
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Auth API
- **Output:** Admin layout

#### Level 3: Quản lý sản phẩm
##### Level 4: TASK-018 - Danh sách sản phẩm admin
- **ID:** TASK-018
- **Description:** Admin product list
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-017
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Admin API
- **Output:** Admin product list

##### Level 4: TASK-019 - Form thêm/sửa sản phẩm
- **ID:** TASK-019
- **Description:** Product CRUD forms
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-018
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Admin API
- **Output:** Product form

#### Level 3: Quản lý đơn hàng
##### Level 4: TASK-020 - Danh sách đơn hàng
- **ID:** TASK-020
- **Description:** Admin order list
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-017
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Admin API
- **Output:** Admin order list

##### Level 4: TASK-021 - Cập nhật trạng thái đơn hàng
- **ID:** TASK-021
- **Description:** Update order status
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-020
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Admin API
- **Output:** Order status update

### Level 2: Data & Testing
#### Level 3: Seed Data
##### Level 4: TASK-022 - Tạo 1000+ sản phẩm mẫu
- **ID:** TASK-022
- **Description:** Generate sample products data
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-003
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Seed data file

#### Level 3: Testing
##### Level 4: TASK-023 - Testing trang chủ
- **ID:** TASK-023
- **Description:** Test home page functionality
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-008
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Test report

##### Level 4: TASK-024 - Testing danh sách sản phẩm
- **ID:** TASK-024
- **Description:** Test product list functionality
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-009
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Test report

##### Level 4: TASK-025 - Testing giỏ hàng
- **ID:** TASK-025
- **Description:** Test cart functionality
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-013
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Test report

##### Level 4: TASK-026 - Testing checkout
- **ID:** TASK-026
- **Description:** Test checkout functionality
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-014
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Test report

##### Level 4: TASK-027 - Testing auth
- **ID:** TASK-027
- **Description:** Test authentication
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-015, TASK-016
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Test report

##### Level 4: TASK-028 - Testing admin
- **ID:** TASK-028
- **Description:** Test admin functionality
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-018, TASK-020
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Test report

##### Level 4: TASK-029 - Responsive testing
- **ID:** TASK-029
- **Description:** Test on mobile, tablet, desktop
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-023 to TASK-028
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Responsive test report

### Level 2: Deployment & Final
#### Level 3: Deployment
##### Level 4: TASK-030 - Deploy backend
- **ID:** TASK-030
- **Description:** Deploy backend to server
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-005, TASK-022
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** Server access
- **Output:** Deployed backend

##### Level 4: TASK-031 - Deploy frontend
- **ID:** TASK-031
- **Description:** Deploy frontend to server
- **Estimated effort:** 30 phút
- **Dependencies:** TASK-012 to TASK-021
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Deployed frontend

#### Level 3: Final
##### Level 4: TASK-032 - Final check
- **ID:** TASK-032
- **Description:** Smoke test, bug fixes
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-030, TASK-031
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Final test report

##### Level 4: TASK-033 - Documentation
- **ID:** TASK-033
- **Description:** Create README, API docs
- **Estimated effort:** 1 giờ
- **Dependencies:** TASK-032
- **Assigned to:** Worker Agent
- **Status:** Not Started
- **Input:** None
- **Output:** Documentation files

## Summary
- **Total tasks:** 33
- **Estimated total time:** 24 giờ
- **Critical path:** TASK-001 → TASK-002 → TASK-003 → TASK-004 → TASK-005 → TASK-006 → TASK-007 → TASK-008 → TASK-009 → TASK-012 → TASK-013 → TASK-014 → TASK-015 → TASK-016 → TASK-017 → TASK-018 → TASK-020 → TASK-022 → TASK-030 → TASK-031 → TASK-032 → TASK-033
