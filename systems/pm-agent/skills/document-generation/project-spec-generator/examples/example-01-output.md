# Specification: Hệ thống quản lý task nội bộ

## 1. Overview
Xây dựng một hệ thống web nội bộ giúp team 5 người quản lý task, phân công người thực hiện, theo dõi tiến độ và cộng tác trực tiếp trong từng task. Hệ thống tập trung vào phạm vi MVP cốt lõi, không bao gồm import dữ liệu từ Trello hoặc tích hợp phức tạp bên ngoài.

## 2. Architecture

### System Architecture
```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTP/HTTPS
┌──────▼──────────────┐
│   Frontend (SPA)    │
│   React.js          │
└──────┬──────────────┘
       │ REST API
┌──────▼──────────────┐
│   Backend API       │
│   Node.js/Express   │
└──────┬──────────────┘
       │
┌──────▼──────────────┐
│   Database          │
│   MongoDB           │
└─────────────────────┘
```

### Components
- **Frontend:** Single Page Application cho giao diện quản lý task
- **Backend:** RESTful API xử lý business logic và phân quyền
- **Database:** MongoDB lưu users, tasks, comments, attachments metadata
- **Authentication:** JWT-based authentication
- **Integrations:** Không có tích hợp bên ngoài trong MVP

### Data Architecture
#### Entities
1. **User**
   - id
   - email
   - password (hashed)
   - name
   - role (admin/member)
   - createdAt

2. **Task**
   - id
   - title
   - description
   - deadline
   - status (todo/in-progress/done)
   - ownerId
   - createdBy
   - createdAt

3. **Comment**
   - id
   - taskId
   - userId
   - content
   - createdAt

4. **Attachment**
   - id
   - taskId
   - fileName
   - fileUrl
   - uploadedBy
   - createdAt

## 3. Features

### Feature 1: Tạo task
- **Description:** Người dùng có thể tạo task mới với thông tin cơ bản
- **User Flow:**
  1. User mở form tạo task
  2. Nhập tiêu đề, mô tả, deadline
  3. Chọn người phụ trách
  4. Submit form
  5. Task xuất hiện trong danh sách
- **Technical Approach:** Frontend dùng form component; backend cung cấp API POST `/api/tasks`; dữ liệu lưu trong MongoDB
- **Dependencies:** User authentication

### Feature 2: Phân công người thực hiện
- **Description:** Người dùng có quyền có thể gán owner cho task
- **User Flow:**
  1. User chọn task
  2. Chọn người phụ trách từ danh sách
  3. Xác nhận thay đổi
  4. Hệ thống cập nhật owner
- **Technical Approach:** API PATCH `/api/tasks/:id/assign`; kiểm tra quyền trước khi cập nhật
- **Dependencies:** Feature 1

### Feature 3: Theo dõi trạng thái task
- **Description:** Cập nhật và hiển thị trạng thái task theo vòng đời công việc
- **User Flow:**
  1. User mở task hoặc board
  2. Chọn trạng thái mới
  3. Hệ thống cập nhật trạng thái
  4. Board/list hiển thị trạng thái mới
- **Technical Approach:** API PATCH `/api/tasks/:id/status`; frontend dùng list hoặc board view
- **Dependencies:** Feature 1

### Feature 4: Comment trong task
- **Description:** Người dùng có thể trao đổi trực tiếp trong từng task
- **User Flow:**
  1. User mở task detail
  2. Nhập comment
  3. Submit comment
  4. Comment hiển thị trong luồng thảo luận
- **Technical Approach:** API POST `/api/tasks/:id/comments`; comment lưu trong collection riêng
- **Dependencies:** Feature 1, User authentication

### Feature 5: Đính kèm file
- **Description:** Người dùng có thể upload file liên quan vào task
- **User Flow:**
  1. User mở task
  2. Chọn file cần upload
  3. Hệ thống upload file
  4. File hiển thị trong task
- **Technical Approach:** API upload file + lưu metadata attachment trong database
- **Dependencies:** Feature 1

### Feature 6: Phân quyền người dùng
- **Description:** Hệ thống hỗ trợ role admin và member
- **User Flow:**
  1. User đăng nhập
  2. Hệ thống xác định role
  3. UI và API chỉ cho phép thao tác phù hợp với quyền
- **Technical Approach:** JWT chứa role; middleware backend kiểm tra role; frontend ẩn/hiện chức năng theo quyền
- **Dependencies:** Authentication system

## 4. Technical Stack

### Frontend
- **Framework:** React.js
- **State Management:** Context API hoặc Zustand
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios
- **Routing:** React Router

### Backend
- **Runtime:** Node.js
- **Framework:** Express.js
- **Authentication:** JWT
- **Validation:** express-validator hoặc zod

### Database
- **Option:** MongoDB + Mongoose

### Development Tools
- **Package Manager:** npm
- **Build Tool:** Vite
- **Version Control:** Git

## 5. Quality Standards

### Code Quality
- Component-based architecture
- Clean code principles
- Proper error handling
- Reusable UI components

### Testing Requirements
- Manual testing cho các luồng chính của MVP
- Test responsive trên mobile và desktop
- Test quyền truy cập giữa admin và member

### Documentation Requirements
- README hướng dẫn cài đặt và chạy dự án
- API documentation cho các endpoint chính
- Comment cho logic phân quyền hoặc xử lý phức tạp

## 6. Data Requirements
- Có dữ liệu mẫu cho users và tasks để test luồng chính
- Có ít nhất 2 role người dùng: admin, member
- Có dữ liệu task với nhiều trạng thái để test board/list

## 7. MVP Scope Confirmation

### Included in MVP
✅ Tạo task
✅ Phân công người thực hiện
✅ Theo dõi trạng thái task
✅ Comment trong task
✅ Đính kèm file
✅ Phân quyền admin/member
✅ Responsive UI

### Not Included in MVP
❌ Import dữ liệu từ Trello
❌ Tích hợp công cụ bên ngoài
❌ Realtime collaboration nâng cao
❌ Mobile app native
❌ Dashboard analytics nâng cao
