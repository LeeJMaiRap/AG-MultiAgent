# Specification: Trang Web Bán Hàng

## 1. Overview
Xây dựng một trang web bán hàng MVP hoàn chỉnh với đầy đủ tính năng cơ bản: hiển thị sản phẩm, giỏ hàng, thanh toán, quản lý admin. Giao diện đẹp, responsive, phục vụ 1000+ sản phẩm và 500 người dùng.

## 2. Architecture

### System Architecture
```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTP/HTTPS
┌──────▼──────────────┐
│   Frontend (SPA)    │
│   React/Vue.js      │
└──────┬──────────────┘
       │ REST API
┌──────▼──────────────┐
│   Backend API       │
│   Node.js/Express   │
└──────┬──────────────┘
       │
┌──────▼──────────────┐
│   Database          │
│   MongoDB/MySQL     │
└─────────────────────┘
```

### Components
- **Frontend:** Single Page Application (React hoặc Vue.js)
- **Backend:** RESTful API (Node.js + Express)
- **Database:** MongoDB hoặc MySQL
- **Authentication:** JWT hoặc Session-based
- **File Storage:** Local storage hoặc cloud (cho hình ảnh sản phẩm)

### Data Architecture

#### Entities
1. **User**
   - id
   - email
   - password (hashed)
   - name
   - role (customer/admin)
   - createdAt

2. **Product**
   - id
   - name
   - description
   - price
   - category
   - image
   - stock
   - createdAt

3. **Order**
   - id
   - userId
   - items (array of {productId, quantity, price})
   - totalAmount
   - shippingAddress
   - paymentMethod
   - status (pending/processing/shipped/delivered/cancelled)
   - createdAt

4. **Cart** (session-based hoặc database)
   - userId/sessionId
   - items (array of {productId, quantity})

## 3. Features

### Feature 1: Trang chủ
- **Description:** Landing page với slider, sản phẩm nổi bật, danh mục
- **User Flow:**
  1. User truy cập website
  2. Xem slider hình ảnh
  3. Xem sản phẩm nổi bật
  4. Click vào danh mục hoặc sản phẩm
- **Technical Approach:** 
  - Frontend: Component-based UI
  - Backend: API endpoint `/api/products/featured`
- **Dependencies:** None

### Feature 2: Danh sách sản phẩm
- **Description:** Hiển thị tất cả sản phẩm với tìm kiếm, lọc, phân trang
- **User Flow:**
  1. User truy cập trang sản phẩm
  2. Xem danh sách sản phẩm (grid view)
  3. Sử dụng tìm kiếm/lọc
  4. Click vào sản phẩm để xem chi tiết
- **Technical Approach:**
  - Frontend: Product grid component, search bar, filter sidebar
  - Backend: API endpoint `/api/products?page=1&limit=12&search=&category=&minPrice=&maxPrice=`
- **Dependencies:** Database với 1000+ sản phẩm mẫu

### Feature 3: Chi tiết sản phẩm
- **Description:** Trang chi tiết với hình ảnh lớn, mô tả, giá, nút mua
- **User Flow:**
  1. User click vào sản phẩm
  2. Xem thông tin chi tiết
  3. Chọn số lượng
  4. Click "Thêm vào giỏ hàng"
- **Technical Approach:**
  - Frontend: Product detail component
  - Backend: API endpoint `/api/products/:id`
- **Dependencies:** Feature 2

### Feature 4: Giỏ hàng
- **Description:** Quản lý sản phẩm trong giỏ hàng
- **User Flow:**
  1. User thêm sản phẩm vào giỏ
  2. Xem giỏ hàng
  3. Thay đổi số lượng hoặc xóa sản phẩm
  4. Click "Thanh toán"
- **Technical Approach:**
  - Frontend: Cart component, localStorage hoặc state management
  - Backend: API endpoint `/api/cart` (nếu dùng database)
- **Dependencies:** Feature 3

### Feature 5: Thanh toán
- **Description:** Form nhập thông tin giao hàng và đặt hàng
- **User Flow:**
  1. User click "Thanh toán" từ giỏ hàng
  2. Điền thông tin giao hàng
  3. Chọn phương thức thanh toán
  4. Xác nhận đơn hàng
  5. Nhận thông báo thành công
- **Technical Approach:**
  - Frontend: Checkout form component
  - Backend: API endpoint `/api/orders` (POST)
- **Dependencies:** Feature 4

### Feature 6: Đăng ký / Đăng nhập
- **Description:** Authentication system
- **User Flow:**
  1. User click "Đăng ký" hoặc "Đăng nhập"
  2. Điền form
  3. Submit
  4. Nhận token/session
  5. Redirect về trang chủ
- **Technical Approach:**
  - Frontend: Auth forms
  - Backend: API endpoints `/api/auth/register`, `/api/auth/login`
  - Security: bcrypt for password hashing, JWT for tokens
- **Dependencies:** None

### Feature 7: Admin Dashboard
- **Description:** Trang quản lý sản phẩm và đơn hàng
- **User Flow:**
  1. Admin đăng nhập
  2. Truy cập dashboard
  3. Quản lý sản phẩm (CRUD)
  4. Quản lý đơn hàng (view, update status)
- **Technical Approach:**
  - Frontend: Admin panel components
  - Backend: API endpoints `/api/admin/products`, `/api/admin/orders`
  - Security: Role-based access control
- **Dependencies:** Feature 6

### Feature 8: Responsive UI
- **Description:** Giao diện đẹp, responsive trên mọi thiết bị
- **User Flow:** User truy cập từ bất kỳ thiết bị nào
- **Technical Approach:**
  - CSS Framework: Tailwind CSS hoặc Bootstrap
  - Mobile-first design
  - Breakpoints: 375px, 768px, 1024px, 1440px
- **Dependencies:** All features

## 4. Technical Stack

### Frontend
- **Framework:** React.js hoặc Vue.js
- **State Management:** Redux/Vuex hoặc Context API
- **Styling:** Tailwind CSS hoặc Bootstrap 5
- **HTTP Client:** Axios
- **Routing:** React Router hoặc Vue Router

### Backend
- **Runtime:** Node.js
- **Framework:** Express.js
- **Authentication:** JWT (jsonwebtoken)
- **Password Hashing:** bcrypt
- **Validation:** express-validator
- **CORS:** cors middleware

### Database
- **Option 1:** MongoDB + Mongoose
- **Option 2:** MySQL + Sequelize

### Development Tools
- **Package Manager:** npm hoặc yarn
- **Build Tool:** Vite hoặc Webpack
- **Code Editor:** VS Code
- **Version Control:** Git

## 5. Quality Standards

### Code Quality
- Clean code principles
- Component-based architecture
- Reusable components
- Proper error handling
- Input validation

### Testing Requirements (MVP - optional)
- Manual testing cho các luồng chính
- Test trên Chrome, Firefox, Safari
- Test trên mobile và desktop

### Documentation Requirements
- README với hướng dẫn cài đặt
- API documentation (endpoints, request/response)
- Code comments cho logic phức tạp

## 6. Data Requirements

### Sample Data
- **Products:** 1000+ sản phẩm mẫu
  - Đa dạng danh mục (Điện tử, Thời trang, Gia dụng, Thực phẩm, v.v.)
  - Hình ảnh placeholder hoặc từ nguồn miễn phí
  - Giá từ 10,000đ đến 50,000,000đ
  - Mô tả ngắn gọn

- **Users:** 1 admin account + có thể tạo thêm user
  - Admin: admin@example.com / admin123
  - Customer: có thể đăng ký mới

## 7. MVP Scope Confirmation

### Included in MVP
✅ Trang chủ đẹp  
✅ Danh sách sản phẩm với tìm kiếm/lọc  
✅ Chi tiết sản phẩm  
✅ Giỏ hàng  
✅ Checkout cơ bản  
✅ Đăng ký/đăng nhập  
✅ Admin dashboard  
✅ Responsive UI  
✅ 1000+ sản phẩm mẫu  

### Not Included in MVP
❌ Thanh toán thật (PayPal, Stripe)  
❌ Email notifications  
❌ SMS notifications  
❌ Advanced analytics  
❌ Product reviews/ratings  
❌ Wishlist  
❌ Social login  
❌ Multi-language  
❌ Advanced search (filters by brand, rating, etc.)  
❌ Product recommendations  
