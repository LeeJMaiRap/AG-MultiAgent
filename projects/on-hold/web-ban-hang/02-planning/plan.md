# Project Plan: Trang Web Bán Hàng

## 1. Phases

### Phase 1: Setup & Backend Foundation (2 giờ)
- Khởi tạo project structure
- Setup database
- Tạo API endpoints cơ bản
- Tạo authentication system

### Phase 2: Frontend - Trang chủ & Danh sách sản phẩm (3 giờ)
- Tạo layout chính
- Trang chủ với slider
- Danh sách sản phẩm
- Tìm kiếm & lọc

### Phase 3: Frontend - Chi tiết & Giỏ hàng (2 giờ)
- Trang chi tiết sản phẩm
- Giỏ hàng
- Quản lý giỏ hàng

### Phase 4: Frontend - Checkout & Auth (2 giờ)
- Form thanh toán
- Đăng ký / Đăng nhập
- Xác thực người dùng

### Phase 5: Admin Dashboard (2 giờ)
- Trang quản lý sản phẩm
- Trang quản lý đơn hàng
- CRUD sản phẩm

### Phase 6: Data & Testing (2 giờ)
- Tạo 1000+ sản phẩm mẫu
- Testing toàn bộ luồng
- Fix bugs
- Responsive testing

### Phase 7: Deployment & Final (1 giờ)
- Deploy lên server
- Final check
- Documentation

**Total: 14 giờ (trong 24 giờ)**

## 2. Work Breakdown Structure (WBS)

```
1. Setup & Backend Foundation
   1.1 Khởi tạo project (Node.js + Express)
   1.2 Setup database (MongoDB hoặc MySQL)
   1.3 Tạo models (User, Product, Order, Cart)
   1.4 Tạo authentication (JWT)
   1.5 Tạo API endpoints cơ bản

2. Frontend - Trang chủ & Danh sách sản phẩm
   2.1 Setup React/Vue project
   2.2 Tạo layout chính (header, footer, sidebar)
   2.3 Trang chủ (slider, featured products)
   2.4 Danh sách sản phẩm (grid view)
   2.5 Tìm kiếm sản phẩm
   2.6 Lọc sản phẩm (category, price)
   2.7 Phân trang

3. Frontend - Chi tiết & Giỏ hàng
   3.1 Trang chi tiết sản phẩm
   3.2 Giỏ hàng (view)
   3.3 Thêm/xóa/sửa giỏ hàng
   3.4 Hiển thị tổng tiền

4. Frontend - Checkout & Auth
   4.1 Form thanh toán
   4.2 Form đăng ký
   4.3 Form đăng nhập
   4.4 Xác thực người dùng
   4.5 Lưu đơn hàng

5. Admin Dashboard
   5.1 Trang admin (protected)
   5.2 Danh sách sản phẩm admin
   5.3 Form thêm/sửa sản phẩm
   5.4 Xóa sản phẩm
   5.5 Danh sách đơn hàng
   5.6 Cập nhật trạng thái đơn hàng

6. Data & Testing
   6.1 Tạo seed data (1000+ sản phẩm)
   6.2 Testing trang chủ
   6.3 Testing danh sách sản phẩm
   6.4 Testing chi tiết sản phẩm
   6.5 Testing giỏ hàng
   6.6 Testing checkout
   6.7 Testing auth
   6.8 Testing admin
   6.9 Responsive testing
   6.10 Fix bugs

7. Deployment & Final
   7.1 Deploy backend
   7.2 Deploy frontend
   7.3 Final check
   7.4 Documentation
```

## 3. Dependencies

```
1.1 → 1.2 → 1.3 → 1.4 → 1.5
                    ↓
2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6 → 2.7
                    ↓
3.1 → 3.2 → 3.3 → 3.4
                    ↓
4.1 → 4.2 → 4.3 → 4.4 → 4.5
                    ↓
5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6
                    ↓
6.1 → 6.2 → 6.3 → 6.4 → 6.5 → 6.6 → 6.7 → 6.8 → 6.9 → 6.10
                    ↓
7.1 → 7.2 → 7.3 → 7.4
```

## 4. Resource Allocation

| Task | Assigned To | Estimated Hours | Notes |
|------|-------------|-----------------|-------|
| 1.x (Backend) | Worker Agent | 2h | Node.js + Express + DB |
| 2.x (Frontend - Home & List) | Worker Agent | 3h | React/Vue + API integration |
| 3.x (Frontend - Detail & Cart) | Worker Agent | 2h | Component development |
| 4.x (Frontend - Checkout & Auth) | Worker Agent | 2h | Form handling + Auth |
| 5.x (Admin Dashboard) | Worker Agent | 2h | Admin panel |
| 6.x (Data & Testing) | Worker Agent | 2h | Seed data + QA |
| 7.x (Deployment) | Worker Agent | 1h | Deploy + docs |

## 5. Communication Plan

- **Daily standup:** Every 2 hours (check progress, blockers)
- **Status update:** After each phase completion
- **Final review:** Before deployment
- **Documentation:** Inline comments + README

## 6. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Timeline too tight | High | High | Focus on MVP only, skip nice-to-haves |
| Database performance | Medium | High | Use indexing, optimize queries |
| UI not responsive | Medium | Medium | Test on multiple devices early |
| Authentication bugs | Low | High | Use proven libraries (JWT, bcrypt) |
| Data seed takes too long | Medium | Medium | Use bulk insert, generate data programmatically |

## 7. Success Criteria

- ✅ Website chạy được trên localhost
- ✅ Có thể xem 1000+ sản phẩm
- ✅ Có thể tìm kiếm/lọc sản phẩm
- ✅ Có thể thêm vào giỏ hàng
- ✅ Có thể thanh toán
- ✅ Có thể đăng ký/đăng nhập
- ✅ Admin có thể quản lý sản phẩm
- ✅ Admin có thể quản lý đơn hàng
- ✅ Giao diện đẹp, responsive
- ✅ Không có lỗi critical
