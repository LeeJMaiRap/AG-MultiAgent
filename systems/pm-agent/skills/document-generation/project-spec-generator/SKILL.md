---
name: project-spec-generator
description: Tạo file `02-planning/spec.md` - đặc tả kỹ thuật chi tiết từ requirements document, charter hoặc requirement clarification; dùng khi cần tạo tài liệu spec với architecture, features, technical stack, data model và quality standards để làm cơ sở cho implementation.
---

# Project Spec Generator

## Mục tiêu

Tạo tài liệu Specification (đặc tả kỹ thuật) chi tiết để định nghĩa rõ kiến trúc hệ thống, các tính năng, công nghệ sử dụng và tiêu chuẩn chất lượng, làm cơ sở cho giai đoạn execution.

Skill này giúp:
- chuyển requirements document thành đặc tả kỹ thuật có cấu trúc
- định nghĩa kiến trúc hệ thống (system architecture, data architecture)
- mô tả chi tiết từng feature với user flow và technical approach
- xác định technical stack cụ thể
- đặt ra quality standards cho implementation

## Dùng khi nào

Dùng skill này khi:
- đã có requirements document hoặc charter
- cần tạo đặc tả kỹ thuật chi tiết trước khi bắt đầu code
- cần định nghĩa kiến trúc và công nghệ sử dụng
- cần làm rõ cách triển khai từng feature

## Không dùng khi nào

Không dùng skill này khi:
- yêu cầu còn quá mơ hồ, chưa có requirements document
- mục tiêu là tạo kế hoạch triển khai (dùng `project-plan-generator`)
- mục tiêu là tạo WBS hoặc schedule (dùng `wbs-generator`, `schedule-generator`)
- chỉ cần cập nhật một vài chi tiết kỹ thuật, không cần tạo spec mới

## Input bắt buộc

Ít nhất phải có:
- requirements document hoặc charter
- danh sách features chính
- phạm vi MVP đã được xác định

## Input tùy chọn

- technical stack đã được chọn
- architecture diagram nếu đã có
- data model nếu đã được thiết kế
- quality standards đã được thảo luận
- constraints kỹ thuật

## Output

Output là file `spec.md` theo cấu trúc chuẩn với 6-9 phần:

1. **Overview**
2. **Architecture**
3. **API Specification** (bắt buộc cho backend/API projects)
4. **Data Model** (bắt buộc nếu có database)
5. **Features**
6. **Technical Stack**
7. **Quality Standards**
8. **Data Requirements** (tùy chọn)
9. **MVP Scope Confirmation** (tùy chọn)

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải tuân thủ template có sẵn trong `systems/pm-agent/templates/spec-template.md`.

## Quy tắc xử lý

### 1. Architecture phải rõ ràng và đầy đủ
Architecture cần bao gồm:
- **System Architecture:** components, modules, integrations
- **Data Architecture:** entities, relationships, storage

Nếu có thể, nên có diagram đơn giản (ASCII art hoặc mô tả text).

### 1a. API Specification phải chi tiết (bắt buộc cho backend/API projects)
API Specification cần bao gồm:
- **Endpoint list:** method + path cho mỗi API
- **Request schema:** parameters, body, headers
- **Response schema:** success response + error response
- **Status codes:** 200, 201, 400, 401, 404, 500...
- **Authentication requirements:** endpoints nào cần auth

Ví dụ format:
```
### POST /api/tasks
- **Description:** Tạo task mới
- **Auth required:** Yes (JWT)
- **Request body:**
  ```json
  {
    "title": "string (required)",
    "description": "string (optional)",
    "ownerId": "string (required)",
    "deadline": "ISO date (optional)"
  }
  ```
- **Success response (201):**
  ```json
  {
    "id": "task-123",
    "title": "...",
    "status": "todo",
    "createdAt": "2026-05-14T00:00:00Z"
  }
  ```
- **Error responses:**
  - 400: Invalid input
  - 401: Unauthorized
```

**Tại sao quan trọng:** API contract rõ ràng giúp frontend và backend làm việc song song mà không bị block.

### 1b. Data Model phải có schema chi tiết (bắt buộc nếu có database)
Data Model cần bao gồm:
- **Entity name**
- **Fields với type và constraints:**
  - field name
  - data type (string, number, boolean, date...)
  - constraints (required, unique, min/max length...)
  - default value (nếu có)
- **Relationships:** one-to-one, one-to-many, many-to-many
- **Indexes:** fields nào cần index để tối ưu query

Ví dụ format:
```
#### User
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | ObjectId/UUID | Primary key, auto-generated | Unique identifier |
| email | String | Required, unique, email format | User email |
| password | String | Required, min 8 chars, hashed | Hashed password |
| name | String | Required | User full name |
| role | Enum | Required, default: 'customer' | customer/admin |
| createdAt | Date | Auto-generated | Account creation time |

**Relationships:**
- User has many Orders (one-to-many)

**Indexes:**
- email (unique)
- role
```

**Tại sao quan trọng:** Schema rõ ràng giúp tránh rework khi phát hiện thiếu field hoặc constraint.

### 2. Mỗi feature phải có 4 phần
Mỗi feature cần mô tả:
- **Description:** mô tả ngắn gọn
- **User Flow:** các bước người dùng thực hiện
- **Technical Approach:** cách triển khai kỹ thuật
- **Dependencies:** phụ thuộc vào feature nào khác

### 3. Technical stack phải cụ thể
Không viết chung chung như "web framework", mà phải cụ thể:
- Frontend: React.js hoặc Vue.js
- Backend: Node.js + Express
- Database: MongoDB hoặc MySQL

### 4. Quality standards phải đo lường được
Mỗi tiêu chuẩn phải rõ ràng:
- Code quality: clean code principles, component-based
- Testing: manual testing cho MVP, unit tests cho production
- Documentation: README, API docs, code comments

### 5. Phân biệt rõ MVP scope
Nếu dự án có phạm vi MVP, phải liệt kê rõ:
- ✅ Included in MVP
- ❌ Not included in MVP

### 6. Data model phải đầy đủ entities và chi tiết
Data Model (section riêng, không phải Data Requirements) phải có:
- **Tất cả entities** trong hệ thống
- **Mỗi entity phải có bảng fields** với type, constraints, description
- **Relationships** giữa các entities (one-to-one, one-to-many, many-to-many)
- **Indexes** cần thiết cho performance
- **Sample data structure** nếu cần minh họa

Data Requirements (section khác) chỉ dùng cho yêu cầu về dữ liệu mẫu, migration, hoặc data source.

### 7. Spec phải technical nhưng vẫn dễ hiểu
Spec không phải code, nhưng phải đủ chi tiết để developer hiểu và triển khai.

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Kiến trúc hệ thống như thế nào? (client-server, microservices, monolith?)
- Các components chính là gì?
- **API endpoints nào cần có?** (method, path, request/response schema)
- **Data model có những entities nào?** (fields, types, constraints, relationships, indexes)
- Mỗi feature triển khai như thế nào về mặt kỹ thuật?
- Technical stack nào phù hợp với yêu cầu?
- Quality standards nào cần đặt ra?
- Phạm vi MVP bao gồm những gì?
- **API contract giữa frontend và backend rõ chưa?**
- **Database schema đã đủ chi tiết để implement chưa?**

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `requirements-document-generator`
- `project-charter-generator`

Và là đầu vào cho:
- `project-plan-generator`
- `wbs-generator`
- `task-board-builder`

Spec là tài liệu kỹ thuật quan trọng nhất trong giai đoạn Planning.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/02-planning/spec.md
```

File này là cơ sở kỹ thuật cho toàn bộ implementation.

## Tiêu chí hoàn thành tốt

Một spec tốt khi:
- kiến trúc hệ thống rõ ràng, dễ hình dung
- **API specification đầy đủ:** mỗi endpoint có method, path, request/response schema, status codes
- **Data model chi tiết:** mỗi entity có bảng fields với type, constraints, relationships, indexes
- mỗi feature có đủ 4 phần (description, user flow, technical approach, dependencies)
- technical stack cụ thể, không mơ hồ
- quality standards đo lường được
- **frontend và backend có thể làm song song mà không bị block do thiếu contract**
- developer đọc xong có thể bắt đầu code
- phạm vi MVP được xác định rõ ràng

## Lỗi thường gặp cần tránh

- kiến trúc quá chung chung, không cụ thể
- **thiếu API specification hoặc API spec không đủ chi tiết** (chỉ liệt kê endpoint mà không có request/response schema)
- **thiếu data model hoặc data model không có type/constraints** (chỉ liệt kê field name mà không có type, required, unique...)
- **API contract không rõ ràng khiến frontend bị block** (response schema thay đổi, thiếu field, status code không nhất quán)
- feature thiếu user flow hoặc technical approach
- technical stack không rõ ràng
- quality standards quá mơ hồ
- không phân biệt MVP và full scope
- spec quá ngắn, thiếu chi tiết
- spec quá dài, đi vào code implementation

## Cách dùng ngắn gọn

1. Đọc requirements document hoặc charter
2. Thiết kế kiến trúc hệ thống (system + data)
3. Mô tả chi tiết từng feature
4. Xác định technical stack cụ thể
5. Đặt ra quality standards
6. Xác nhận phạm vi MVP
7. Xuất file `spec.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `references/api-spec-guide.md` - hướng dẫn viết API specification chi tiết
- `references/data-model-guide.md` - hướng dẫn viết data model chi tiết
- `examples/` - ví dụ spec thực tế
- Tham khảo: `systems/pm-agent/templates/spec-template.md`
- Tham khảo: `projects/active/web-ban-hang/02-planning/spec.md`

## Khi nào nên đọc thêm tài liệu tham chiếu

- Nếu dự án có backend/API: đọc `references/api-spec-guide.md`
- Nếu dự án có database: đọc `references/data-model-guide.md`
- Nếu đang phân vân mức độ chi tiết của API contract: đọc `references/api-spec-guide.md`
- Nếu đang phân vân cách mô tả field/type/constraint/index: đọc `references/data-model-guide.md`
- Nếu cần ví dụ spec thực tế: xem `examples/` hoặc `projects/active/web-ban-hang/02-planning/spec.md`
