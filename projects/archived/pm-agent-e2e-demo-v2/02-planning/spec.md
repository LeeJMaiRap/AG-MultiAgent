# Specification: Hệ thống quản lý công việc nội bộ

## 1. Overview
Xây dựng một hệ thống web nội bộ cho team nhỏ để tạo task, giao người phụ trách, đặt deadline, comment và theo dõi trạng thái. Dashboard chỉ ở mức cơ bản cho MVP: tổng số task và phân bổ theo trạng thái.

## 2. Architecture

### System Architecture
```
Browser (React SPA)
    ↓ HTTPS
Backend API (Node.js/Express)
    ↓
Database (MongoDB)
```

### Components
- **Frontend:** React SPA với Tailwind CSS
- **Backend:** REST API Node.js/Express
- **Database:** MongoDB
- **Authentication:** JWT Bearer token

### Data Architecture
Hệ thống có 3 entities chính: User, Task, Comment. User tạo và được assign Task. Task có nhiều Comment.

## 3. API Specification

### POST /api/auth/register
- **Description:** Đăng ký user mới
- **Auth required:** No
- **Request body:**
  ```json
  {
    "email": "string (required, email format, max 255 chars)",
    "password": "string (required, min 8 chars)",
    "name": "string (required, max 100 chars)"
  }
  ```
- **Success response (201):**
  ```json
  {
    "id": "user-abc123",
    "email": "john@example.com",
    "name": "John Doe",
    "role": "member",
    "createdAt": "2026-05-14T01:00:00Z"
  }
  ```
- **Error responses:**
  - 400: Invalid input (email format, password too short)
  - 409: Email already exists

### POST /api/auth/login
- **Description:** Đăng nhập
- **Auth required:** No
- **Request body:**
  ```json
  {
    "email": "string (required)",
    "password": "string (required)"
  }
  ```
- **Success response (200):**
  ```json
  {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": "user-abc123",
      "email": "john@example.com",
      "name": "John Doe",
      "role": "member"
    }
  }
  ```
- **Error responses:**
  - 401: Invalid credentials

### GET /api/auth/me
- **Description:** Lấy thông tin user hiện tại
- **Auth required:** Yes (JWT Bearer token)
- **Success response (200):**
  ```json
  {
    "id": "user-abc123",
    "email": "john@example.com",
    "name": "John Doe",
    "role": "member"
  }
  ```
- **Error responses:**
  - 401: Unauthorized (token invalid/expired)

### POST /api/tasks
- **Description:** Tạo task mới
- **Auth required:** Yes (JWT)
- **Request body:**
  ```json
  {
    "title": "string (required, max 200 chars)",
    "description": "string (optional, max 2000 chars)",
    "ownerId": "string (optional, valid user ID)",
    "deadline": "ISO 8601 date (optional)",
    "status": "string (optional, default: 'todo', enum: todo/in-progress/done/blocked)"
  }
  ```
- **Success response (201):**
  ```json
  {
    "id": "task-xyz789",
    "title": "Implement login feature",
    "description": "Add JWT authentication",
    "ownerId": "user-abc123",
    "ownerName": "John Doe",
    "deadline": "2026-05-20T00:00:00Z",
    "status": "todo",
    "createdBy": "user-def456",
    "createdAt": "2026-05-14T01:00:00Z",
    "updatedAt": "2026-05-14T01:00:00Z"
  }
  ```
- **Error responses:**
  - 400: Invalid input
  - 401: Unauthorized
  - 404: Owner user not found

### GET /api/tasks
- **Description:** Lấy danh sách tasks với filter và pagination
- **Auth required:** Yes (JWT)
- **Request parameters:**
  - `page` (number, optional, default: 1): Page number
  - `limit` (number, optional, default: 20, max: 100): Items per page
  - `status` (string, optional): Filter by status
  - `ownerId` (string, optional): Filter by owner
  - `search` (string, optional): Search in title/description
- **Success response (200):**
  ```json
  {
    "data": [
      {
        "id": "task-xyz789",
        "title": "Implement login feature",
        "status": "in-progress",
        "ownerId": "user-abc123",
        "ownerName": "John Doe",
        "deadline": "2026-05-20T00:00:00Z",
        "createdAt": "2026-05-14T01:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 45,
      "totalPages": 3
    }
  }
  ```
- **Error responses:**
  - 400: Invalid query parameters
  - 401: Unauthorized

### GET /api/tasks/:id
- **Description:** Lấy chi tiết một task
- **Auth required:** Yes (JWT)
- **Request parameters:**
  - `id` (path param, required): Task ID
- **Success response (200):**
  ```json
  {
    "id": "task-xyz789",
    "title": "Implement login feature",
    "description": "Add JWT authentication with refresh token",
    "ownerId": "user-abc123",
    "ownerName": "John Doe",
    "deadline": "2026-05-20T00:00:00Z",
    "status": "in-progress",
    "createdBy": "user-def456",
    "createdAt": "2026-05-14T01:00:00Z",
    "updatedAt": "2026-05-14T10:00:00Z",
    "comments": [
      {
        "id": "comment-123",
        "userId": "user-abc123",
        "userName": "John Doe",
        "content": "Started working on this",
        "createdAt": "2026-05-14T09:00:00Z"
      }
    ]
  }
  ```
- **Error responses:**
  - 401: Unauthorized
  - 404: Task not found

### PATCH /api/tasks/:id
- **Description:** Cập nhật task (partial update)
- **Auth required:** Yes (JWT)
- **Request parameters:**
  - `id` (path param, required): Task ID
- **Request body:** (tất cả fields đều optional)
  ```json
  {
    "title": "string (optional)",
    "description": "string (optional)",
    "ownerId": "string (optional)",
    "deadline": "ISO 8601 date (optional)",
    "status": "string (optional, enum: todo/in-progress/done/blocked)"
  }
  ```
- **Success response (200):**
  ```json
  {
    "id": "task-xyz789",
    "title": "Updated title",
    "status": "done",
    "updatedAt": "2026-05-14T12:00:00Z"
  }
  ```
- **Error responses:**
  - 400: Invalid input
  - 401: Unauthorized
  - 403: Forbidden (không có quyền sửa task này)
  - 404: Task not found

### POST /api/tasks/:id/comments
- **Description:** Thêm comment vào task
- **Auth required:** Yes (JWT)
- **Request parameters:**
  - `id` (path param, required): Task ID
- **Request body:**
  ```json
  {
    "content": "string (required, max 1000 chars)"
  }
  ```
- **Success response (201):**
  ```json
  {
    "id": "comment-456",
    "taskId": "task-xyz789",
    "userId": "user-abc123",
    "userName": "John Doe",
    "content": "This is a comment",
    "createdAt": "2026-05-14T13:00:00Z"
  }
  ```
- **Error responses:**
  - 400: Invalid input
  - 401: Unauthorized
  - 404: Task not found

### GET /api/dashboard/summary
- **Description:** Lấy tổng quan dashboard
- **Auth required:** Yes (JWT)
- **Success response (200):**
  ```json
  {
    "totalTasks": 45,
    "byStatus": {
      "todo": 15,
      "in-progress": 10,
      "done": 18,
      "blocked": 2
    }
  }
  ```
- **Error responses:**
  - 401: Unauthorized

## 4. Data Model

### Entity: User

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | ObjectId | Primary key, auto-generated | Unique user identifier |
| email | String | Required, unique, email format, max 255 chars | User email address |
| password | String | Required, min 8 chars, hashed (bcrypt) | User password (never store plain text) |
| name | String | Required, max 100 chars | User full name |
| role | Enum | Required, default: 'member', values: ['member', 'admin'] | User role |
| createdAt | Date | Auto-generated | Account creation timestamp |
| updatedAt | Date | Auto-updated | Last update timestamp |

**Relationships:**
- User has many Tasks as owner (one-to-many via Task.ownerId)
- User has many Tasks as creator (one-to-many via Task.createdBy)
- User has many Comments (one-to-many)

**Indexes:**
- email (unique)
- role
- createdAt

**Sample data:**
```json
{
  "id": "user-abc123",
  "email": "john.doe@example.com",
  "password": "$2b$10$...",
  "name": "John Doe",
  "role": "member",
  "createdAt": "2026-05-14T01:00:00Z",
  "updatedAt": "2026-05-14T01:00:00Z"
}
```

### Entity: Task

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | ObjectId | Primary key, auto-generated | Unique task identifier |
| title | String | Required, max 200 chars | Task title |
| description | String | Optional, max 2000 chars | Task detailed description |
| ownerId | ObjectId | Optional, foreign key to User | Task owner/assignee |
| status | Enum | Required, default: 'todo', values: ['todo', 'in-progress', 'done', 'blocked'] | Current task status |
| deadline | Date | Optional | Task deadline |
| createdBy | ObjectId | Required, foreign key to User | User who created this task |
| createdAt | Date | Auto-generated | Task creation timestamp |
| updatedAt | Date | Auto-updated | Last update timestamp |

**Relationships:**
- Task belongs to User as owner (many-to-one via ownerId)
- Task belongs to User as creator (many-to-one via createdBy)
- Task has many Comments (one-to-many)

**Indexes:**
- ownerId
- status
- deadline
- createdBy
- createdAt
- (status, ownerId) - compound index for filtering tasks by status and owner

**Sample data:**
```json
{
  "id": "task-xyz789",
  "title": "Implement login feature",
  "description": "Add JWT authentication with refresh token support",
  "ownerId": "user-abc123",
  "status": "in-progress",
  "deadline": "2026-05-20T00:00:00Z",
  "createdBy": "user-def456",
  "createdAt": "2026-05-14T01:00:00Z",
  "updatedAt": "2026-05-14T10:00:00Z"
}
```

### Entity: Comment

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | ObjectId | Primary key, auto-generated | Unique comment identifier |
| taskId | ObjectId | Required, foreign key to Task | Parent task |
| userId | ObjectId | Required, foreign key to User | Comment author |
| content | String | Required, max 1000 chars | Comment text content |
| createdAt | Date | Auto-generated | Comment creation timestamp |

**Relationships:**
- Comment belongs to Task (many-to-one via taskId)
- Comment belongs to User (many-to-one via userId)

**Indexes:**
- taskId
- userId
- createdAt

**Sample data:**
```json
{
  "id": "comment-123",
  "taskId": "task-xyz789",
  "userId": "user-abc123",
  "content": "Started working on this task",
  "createdAt": "2026-05-14T09:00:00Z"
}
```

## 5. Features

### Feature 1: Authentication
- **Description:** Đăng ký, đăng nhập, xác thực JWT
- **User Flow:** Register → Login → Nhận token → Dùng token cho các API khác
- **Technical Approach:** bcrypt hash password, JWT token với expiry 7 days
- **Dependencies:** None

### Feature 2: Task management
- **Description:** Tạo, sửa, xóa, theo dõi task
- **User Flow:** Tạo task → Assign owner → Cập nhật trạng thái → Xem danh sách
- **Technical Approach:** CRUD API + React forms + status dropdown
- **Dependencies:** Feature 1 (Auth)

### Feature 3: Comment system
- **Description:** Comment trong task
- **User Flow:** Mở task detail → Nhập comment → Submit → Hiển thị trong task
- **Technical Approach:** Task detail page + comment list + comment form
- **Dependencies:** Feature 2 (Task management)

### Feature 4: Basic dashboard
- **Description:** Tổng hợp task theo trạng thái
- **User Flow:** Mở dashboard → Xem tổng số task và phân bổ theo trạng thái
- **Technical Approach:** Aggregate query MongoDB + simple card UI
- **Dependencies:** Feature 2 (Task management)

## 6. Technical Stack

### Frontend
- **Framework:** React.js
- **State Management:** Context API hoặc Zustand
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios
- **Routing:** React Router

### Backend
- **Runtime:** Node.js
- **Framework:** Express.js
- **Authentication:** JWT (jsonwebtoken)
- **Password Hashing:** bcrypt
- **Validation:** express-validator
- **CORS:** cors middleware

### Database
- **Database:** MongoDB
- **ODM:** Mongoose

### Development Tools
- **Package Manager:** npm
- **Build Tool:** Vite
- **Version Control:** Git

## 7. Quality Standards

### Code Quality
- Clean code principles
- Component-based architecture
- Reusable components
- Proper error handling
- Input validation on both frontend and backend

### Testing Requirements
- Manual testing cho MVP
- Test form validation
- Test authentication flow
- Test task CRUD operations

### Documentation Requirements
- README với hướng dẫn cài đặt
- API documentation (đã có trong spec này)
- Code comments cho logic phức tạp

## 8. MVP Scope Confirmation

### Included in MVP
✅ Authentication (register/login)  
✅ Task CRUD  
✅ Assign owner  
✅ Deadline  
✅ Status tracking (todo/in-progress/done/blocked)  
✅ Comment trong task  
✅ Dashboard cơ bản (tổng số task + theo trạng thái)  

### Not Included in MVP
❌ Attachment management  
❌ Analytics nâng cao  
❌ Mobile app native  
❌ Activity history / audit trail  
❌ Advanced dashboard (charts, trends)  
❌ Email notifications  
❌ Real-time updates (WebSocket)
