# Specification: [PROJECT_NAME]

## 1. Overview
[Tổng quan về những gì sẽ được xây dựng]

## 2. Architecture

### System Architecture
[Diagram hoặc mô tả system architecture]

### Components
- **Frontend:** [Mô tả]
- **Backend:** [Mô tả]
- **Database:** [Mô tả]
- **Authentication:** [Mô tả]
- **Integrations:** [Mô tả nếu có]

### Data Architecture
- [Tóm tắt entities, relationships, storage]

## 3. API Specification

### [METHOD] /api/[resource]
- **Description:** [Mô tả endpoint]
- **Auth required:** [Yes/No + loại auth]
- **Request parameters:** [Query/path params nếu có]
- **Request body:**
  ```json
  {
    "field": "type/constraint"
  }
  ```
- **Success response ([200/201]):**
  ```json
  {
    "field": "value/example"
  }
  ```
- **Error responses:**
  - 400: [Invalid input]
  - 401: [Unauthorized]
  - 404: [Not found]

## 4. Data Model

### Entity: [Entity 1]
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | [UUID/ObjectId] | Primary key | Unique identifier |
| [field_1] | [String/Number/Date] | [Required/Unique/etc.] | [Mô tả] |
| [field_2] | [String/Number/Date] | [Optional/etc.] | [Mô tả] |

**Relationships:**
- [Entity 1] has many [Entity 2]

**Indexes:**
- [field_1]
- [field_2] (unique)

### Entity: [Entity 2]
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | [UUID/ObjectId] | Primary key | Unique identifier |
| [field_1] | [String/Number/Date] | [Required/Unique/etc.] | [Mô tả] |

**Relationships:**
- [Entity 2] belongs to [Entity 1]

**Indexes:**
- [field_1]

## 5. Features

### Feature 1: [Tên feature]
- **Description:** [Mô tả]
- **User Flow:**
  1. [Bước 1]
  2. [Bước 2]
  3. [Bước 3]
- **Technical Approach:** [Cách triển khai kỹ thuật]
- **Dependencies:** [Phụ thuộc]

### Feature 2: [Tên feature]
- **Description:** [Mô tả]
- **User Flow:**
  1. [Bước 1]
  2. [Bước 2]
  3. [Bước 3]
- **Technical Approach:** [Cách triển khai kỹ thuật]
- **Dependencies:** [Phụ thuộc]

## 6. Technical Stack

### Frontend
- **Framework:** [React/Vue/...] 
- **State Management:** [Redux/Context/...]
- **Styling:** [Tailwind/Bootstrap/...]
- **HTTP Client:** [Axios/fetch/...]
- **Routing:** [React Router/Vue Router/...]

### Backend
- **Runtime:** [Node.js/...]
- **Framework:** [Express/Fastify/...]
- **Authentication:** [JWT/Session/...]
- **Validation:** [Library/...]

### Database
- **Option:** [MongoDB/MySQL/PostgreSQL/...]

### Development Tools
- **Package Manager:** [npm/yarn/pnpm]
- **Build Tool:** [Vite/Webpack/...]
- **Version Control:** Git

## 7. Quality Standards

### Code Quality
- [Tiêu chuẩn 1]
- [Tiêu chuẩn 2]
- [Tiêu chuẩn 3]

### Testing Requirements
- [Yêu cầu test 1]
- [Yêu cầu test 2]

### Documentation Requirements
- [Yêu cầu doc 1]
- [Yêu cầu doc 2]

## 8. Data Requirements (nếu cần)
- [Yêu cầu dữ liệu 1]
- [Yêu cầu dữ liệu 2]

## 9. MVP Scope Confirmation (nếu cần)

### Included in MVP
✅ [Nội dung 1]
✅ [Nội dung 2]

### Not Included in MVP
❌ [Nội dung 1]
❌ [Nội dung 2]
