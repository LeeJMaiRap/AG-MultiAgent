# Data Model Guide

Hướng dẫn viết Data Model chi tiết trong spec.md.

## Tại sao cần Data Model chi tiết?

Data model rõ ràng giúp:
- Backend developer biết chính xác cần tạo table/collection nào
- Tránh thiếu field hoặc constraint khi implement
- Dễ dàng thiết kế database migration
- Frontend developer hiểu được data structure để xử lý
- Giảm rework do phát hiện thiếu field sau khi đã code

## Format chuẩn cho mỗi entity

```markdown
### Entity: [EntityName]

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID/ObjectId | Primary key, auto-generated | Unique identifier |
| [field1] | String/Number/Date/Boolean | Required/Optional, Unique, Min/Max, Default | Mô tả field |
| [field2] | String/Number/Date/Boolean | Required/Optional, Unique, Min/Max, Default | Mô tả field |

**Relationships:**
- [EntityName] has many [OtherEntity] (one-to-many)
- [EntityName] belongs to [ParentEntity] (many-to-one)

**Indexes:**
- [field1] (unique)
- [field2]
- [field1, field2] (compound index)

**Sample data:**
```json
{
  "id": "example-id-123",
  "field1": "example value",
  "field2": 42
}
```
```

## Ví dụ cụ thể

### Entity: User

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary key, auto-generated | Unique user identifier |
| email | String | Required, unique, email format, max 255 chars | User email address |
| password | String | Required, min 8 chars, hashed (bcrypt) | User password (never store plain text) |
| name | String | Required, max 100 chars | User full name |
| role | Enum | Required, default: 'customer', values: ['customer', 'admin'] | User role |
| createdAt | Date | Auto-generated | Account creation timestamp |
| updatedAt | Date | Auto-updated | Last update timestamp |

**Relationships:**
- User has many Orders (one-to-many)
- User has one Cart (one-to-one)

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
  "role": "customer",
  "createdAt": "2026-05-14T01:00:00Z",
  "updatedAt": "2026-05-14T01:00:00Z"
}
```

---

### Entity: Task

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | ObjectId | Primary key, auto-generated | Unique task identifier |
| title | String | Required, max 200 chars | Task title |
| description | String | Optional, max 2000 chars | Task detailed description |
| ownerId | ObjectId | Required, foreign key to User | Task owner/assignee |
| status | Enum | Required, default: 'todo', values: ['todo', 'in-progress', 'done', 'blocked'] | Current task status |
| priority | Enum | Optional, default: 'medium', values: ['low', 'medium', 'high'] | Task priority |
| deadline | Date | Optional | Task deadline |
| createdAt | Date | Auto-generated | Task creation timestamp |
| updatedAt | Date | Auto-updated | Last update timestamp |

**Relationships:**
- Task belongs to User (many-to-one via ownerId)
- Task has many Comments (one-to-many)

**Indexes:**
- ownerId
- status
- deadline
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
  "priority": "high",
  "deadline": "2026-05-20T00:00:00Z",
  "createdAt": "2026-05-14T01:00:00Z",
  "updatedAt": "2026-05-14T10:00:00Z"
}
```

---

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

---

### Entity: Order

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary key, auto-generated | Unique order identifier |
| userId | UUID | Required, foreign key to User | Customer who placed the order |
| items | Array | Required, min 1 item | Array of order items |
| items[].productId | UUID | Required | Product ID |
| items[].quantity | Number | Required, min 1 | Quantity ordered |
| items[].price | Number | Required, min 0 | Price at time of order |
| totalAmount | Number | Required, min 0 | Total order amount |
| shippingAddress | Object | Required | Shipping address details |
| shippingAddress.street | String | Required | Street address |
| shippingAddress.city | String | Required | City |
| shippingAddress.zipCode | String | Required | Zip/postal code |
| paymentMethod | Enum | Required, values: ['cod', 'card', 'bank_transfer'] | Payment method |
| status | Enum | Required, default: 'pending', values: ['pending', 'processing', 'shipped', 'delivered', 'cancelled'] | Order status |
| createdAt | Date | Auto-generated | Order creation timestamp |
| updatedAt | Date | Auto-updated | Last update timestamp |

**Relationships:**
- Order belongs to User (many-to-one via userId)
- Order references many Products (via items array)

**Indexes:**
- userId
- status
- createdAt
- (userId, status) - compound index for user's orders by status

**Sample data:**
```json
{
  "id": "order-def456",
  "userId": "user-abc123",
  "items": [
    {
      "productId": "prod-111",
      "quantity": 2,
      "price": 299000
    },
    {
      "productId": "prod-222",
      "quantity": 1,
      "price": 599000
    }
  ],
  "totalAmount": 1197000,
  "shippingAddress": {
    "street": "123 Main St",
    "city": "Hanoi",
    "zipCode": "100000"
  },
  "paymentMethod": "cod",
  "status": "processing",
  "createdAt": "2026-05-14T08:00:00Z",
  "updatedAt": "2026-05-14T09:00:00Z"
}
```

## Các loại data types thường dùng

### Primitive types
- **String:** text data
- **Number:** integer hoặc float
- **Boolean:** true/false
- **Date:** timestamp (ISO 8601 format)

### Complex types
- **UUID:** universally unique identifier (e.g., "550e8400-e29b-41d4-a716-446655440000")
- **ObjectId:** MongoDB object ID (e.g., "507f1f77bcf86cd799439011")
- **Enum:** giới hạn giá trị cụ thể (e.g., ['todo', 'in-progress', 'done'])
- **Array:** danh sách các items
- **Object:** nested structure

### Special types
- **Email:** string với email format validation
- **URL:** string với URL format validation
- **Hashed:** string đã được hash (password, sensitive data)

## Constraints thường dùng

### Basic constraints
- **Required:** field bắt buộc phải có
- **Optional:** field có thể null/undefined
- **Unique:** giá trị không được trùng
- **Default:** giá trị mặc định nếu không cung cấp

### String constraints
- **Min length:** độ dài tối thiểu
- **Max length:** độ dài tối đa
- **Pattern/Regex:** format cụ thể (email, phone, etc.)
- **Enum:** chỉ chấp nhận các giá trị cụ thể

### Number constraints
- **Min:** giá trị tối thiểu
- **Max:** giá trị tối đa
- **Integer:** chỉ chấp nhận số nguyên
- **Positive:** chỉ chấp nhận số dương

### Date constraints
- **Min date:** ngày sớm nhất
- **Max date:** ngày muộn nhất
- **Future only:** chỉ chấp nhận ngày trong tương lai
- **Past only:** chỉ chấp nhận ngày trong quá khứ

## Relationships

### One-to-One (1:1)
Một entity chỉ liên kết với một entity khác.
- User has one Profile
- Profile belongs to User

### One-to-Many (1:N)
Một entity liên kết với nhiều entities khác.
- User has many Orders
- Order belongs to User

### Many-to-Many (N:M)
Nhiều entities liên kết với nhiều entities khác (thường cần junction table).
- Student has many Courses
- Course has many Students
- (Cần StudentCourse junction table)

## Indexes

Indexes giúp tối ưu query performance.

### Khi nào cần index?
- Fields thường dùng trong WHERE clause
- Fields dùng để JOIN
- Fields dùng để sort (ORDER BY)
- Foreign keys
- Unique constraints

### Loại indexes
- **Single field index:** index trên 1 field
- **Compound index:** index trên nhiều fields (thứ tự quan trọng)
- **Unique index:** đảm bảo giá trị không trùng
- **Text index:** cho full-text search

### Ví dụ
```
Indexes:
- email (unique) - để login nhanh và đảm bảo unique
- (status, ownerId) - để filter tasks by status and owner
- createdAt - để sort by creation date
```

## Checklist khi viết Data Model

- [ ] Mỗi entity có bảng fields đầy đủ
- [ ] Mỗi field có type rõ ràng (String, Number, Date, Boolean, UUID, ObjectId, Enum, Array, Object)
- [ ] Mỗi field có constraints (Required/Optional, Unique, Min/Max, Default, Enum values)
- [ ] Mỗi field có description ngắn gọn
- [ ] Primary key được định nghĩa rõ (id field)
- [ ] Foreign keys được ghi rõ (userId, taskId, etc.)
- [ ] Relationships được liệt kê đầy đủ (one-to-one, one-to-many, many-to-many)
- [ ] Indexes được xác định cho fields thường query
- [ ] Sample data có ví dụ cụ thể
- [ ] Nested objects (nếu có) được mô tả chi tiết
- [ ] Enum values được liệt kê đầy đủ
- [ ] Password fields được đánh dấu "hashed"
- [ ] Timestamp fields (createdAt, updatedAt) được ghi rõ auto-generated/auto-updated

## Lưu ý quan trọng

1. **Be specific:** Không viết "String" mà phải viết "String (required, max 200 chars)"
2. **Document constraints:** Mỗi field phải có constraints rõ ràng
3. **Show relationships:** Phải ghi rõ entity này liên kết với entity nào
4. **Index wisely:** Chỉ index những fields thật sự cần thiết
5. **Sample data helps:** Ví dụ cụ thể giúp developer hiểu rõ hơn
6. **Think about queries:** Thiết kế data model phải phù hợp với cách query thực tế
7. **Security matters:** Password phải hashed, sensitive data phải được đánh dấu rõ
