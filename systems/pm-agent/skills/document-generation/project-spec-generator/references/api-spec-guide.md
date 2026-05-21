# API Specification Guide

Hướng dẫn viết API specification chi tiết trong spec.md.

## Tại sao cần API Specification chi tiết?

API contract rõ ràng giúp:
- Frontend và backend làm việc song song không bị block
- Giảm rework do thay đổi response schema
- Dễ dàng mock API cho frontend development
- Tránh hiểu lầm về data format, status code

## Format chuẩn cho mỗi endpoint

```markdown
### [METHOD] /api/[resource]
- **Description:** Mô tả ngắn gọn endpoint làm gì
- **Auth required:** Yes/No (+ loại auth: JWT, Session, API Key...)
- **Request parameters:** (nếu có query/path params)
  - `param1` (type): description
  - `param2` (type, optional): description
- **Request body:** (nếu có)
  ```json
  {
    "field1": "type (required/optional) - description",
    "field2": "type (required/optional) - description"
  }
  ```
- **Success response (status code):**
  ```json
  {
    "field1": "example value",
    "field2": "example value"
  }
  ```
- **Error responses:**
  - 400: Invalid input (+ chi tiết lỗi gì)
  - 401: Unauthorized
  - 404: Resource not found
  - 500: Internal server error
```

## Ví dụ cụ thể

### POST /api/tasks
- **Description:** Tạo task mới
- **Auth required:** Yes (JWT Bearer token)
- **Request body:**
  ```json
  {
    "title": "string (required, max 200 chars)",
    "description": "string (optional)",
    "ownerId": "string (required, valid user ID)",
    "deadline": "ISO 8601 date (optional)",
    "status": "string (optional, default: 'todo', enum: todo/in-progress/done)"
  }
  ```
- **Success response (201):**
  ```json
  {
    "id": "task-abc123",
    "title": "Implement login feature",
    "description": "Add JWT authentication",
    "ownerId": "user-xyz789",
    "deadline": "2026-05-20T00:00:00Z",
    "status": "todo",
    "createdAt": "2026-05-14T01:00:00Z",
    "updatedAt": "2026-05-14T01:00:00Z"
  }
  ```
- **Error responses:**
  - 400: Invalid input
    ```json
    {
      "error": "Validation failed",
      "details": [
        {"field": "title", "message": "Title is required"},
        {"field": "ownerId", "message": "Invalid user ID"}
      ]
    }
    ```
  - 401: Unauthorized (missing or invalid token)
  - 500: Internal server error

### GET /api/tasks
- **Description:** Lấy danh sách tasks với phân trang và filter
- **Auth required:** Yes (JWT Bearer token)
- **Request parameters:**
  - `page` (number, optional, default: 1): Page number
  - `limit` (number, optional, default: 20, max: 100): Items per page
  - `status` (string, optional): Filter by status (todo/in-progress/done)
  - `ownerId` (string, optional): Filter by owner
  - `search` (string, optional): Search in title/description
- **Success response (200):**
  ```json
  {
    "data": [
      {
        "id": "task-abc123",
        "title": "Implement login feature",
        "status": "in-progress",
        "ownerId": "user-xyz789",
        "deadline": "2026-05-20T00:00:00Z"
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
- **Auth required:** Yes (JWT Bearer token)
- **Request parameters:**
  - `id` (path param, required): Task ID
- **Success response (200):**
  ```json
  {
    "id": "task-abc123",
    "title": "Implement login feature",
    "description": "Add JWT authentication with refresh token",
    "ownerId": "user-xyz789",
    "ownerName": "John Doe",
    "deadline": "2026-05-20T00:00:00Z",
    "status": "in-progress",
    "createdAt": "2026-05-14T01:00:00Z",
    "updatedAt": "2026-05-14T10:00:00Z",
    "comments": [
      {
        "id": "comment-123",
        "userId": "user-abc",
        "userName": "Jane Smith",
        "content": "Started working on this",
        "createdAt": "2026-05-14T09:00:00Z"
      }
    ]
  }
  ```
- **Error responses:**
  - 401: Unauthorized
  - 404: Task not found
  - 500: Internal server error

### PATCH /api/tasks/:id
- **Description:** Cập nhật task (partial update)
- **Auth required:** Yes (JWT Bearer token)
- **Request parameters:**
  - `id` (path param, required): Task ID
- **Request body:** (tất cả fields đều optional)
  ```json
  {
    "title": "string (optional)",
    "description": "string (optional)",
    "ownerId": "string (optional)",
    "deadline": "ISO 8601 date (optional)",
    "status": "string (optional, enum: todo/in-progress/done)"
  }
  ```
- **Success response (200):**
  ```json
  {
    "id": "task-abc123",
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

### DELETE /api/tasks/:id
- **Description:** Xóa task
- **Auth required:** Yes (JWT Bearer token, admin only)
- **Request parameters:**
  - `id` (path param, required): Task ID
- **Success response (204):** No content
- **Error responses:**
  - 401: Unauthorized
  - 403: Forbidden (chỉ admin mới xóa được)
  - 404: Task not found

## Checklist khi viết API Specification

- [ ] Mỗi endpoint có method + path rõ ràng
- [ ] Có mô tả ngắn gọn endpoint làm gì
- [ ] Ghi rõ auth requirement (Yes/No + loại auth)
- [ ] Request parameters/body có type và constraint (required/optional, format, enum...)
- [ ] Response schema có example cụ thể
- [ ] Liệt kê đầy đủ status codes (200, 201, 400, 401, 404, 500...)
- [ ] Error response có format rõ ràng
- [ ] Pagination format nhất quán (nếu có list endpoint)
- [ ] Date format nhất quán (ISO 8601)
- [ ] ID format nhất quán (UUID, ObjectId, hoặc custom format)

## Lưu ý quan trọng

1. **Consistency is key:** Tất cả endpoints phải dùng format nhất quán
2. **Be specific:** Không viết "string" mà phải viết "string (max 200 chars, required)"
3. **Show examples:** Response schema phải có example value cụ thể
4. **Document errors:** Mỗi error code phải giải thích khi nào xảy ra
5. **Think about frontend:** Frontend dev phải đọc spec này và biết chính xác cần gửi gì, nhận gì
