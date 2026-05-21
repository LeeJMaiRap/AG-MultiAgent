# Product Requirements Document — e-commerce-web

## 1. Tổng quan sản phẩm

`e-commerce-web` là website bán hàng MVP phục vụ hai nhóm người dùng chính:

- Khách hàng mua hàng trực tuyến
- Quản trị viên vận hành sản phẩm, danh mục, đơn hàng và khách hàng

Mục tiêu của MVP là xây dựng một hệ thống bán hàng cơ bản, chạy local trên môi trường Windows Native, có đầy đủ luồng mua hàng từ xem sản phẩm đến đặt hàng COD, đồng thời có khu vực admin để quản lý dữ liệu.

---

## 2. Product Vision

Xây dựng một nền tảng e-commerce đơn giản, dễ mở rộng, phục vụ việc:

- Hiển thị sản phẩm cho khách hàng
- Cho phép khách hàng đăng ký, đăng nhập, thêm sản phẩm vào giỏ hàng và đặt hàng
- Cho phép admin quản lý danh mục, sản phẩm, đơn hàng và khách hàng
- Cung cấp backend API rõ ràng để frontend và backend phát triển song song

---

## 3. Đối tượng người dùng

### 3.1 Guest

Guest có thể:

- Xem trang chủ
- Xem danh sách sản phẩm
- Xem chi tiết sản phẩm
- Thêm sản phẩm vào giỏ hàng local
- Đăng ký tài khoản
- Đăng nhập

Guest không thể:

- Checkout
- Xem lịch sử đơn hàng
- Truy cập trang admin

### 3.2 Customer

Customer có thể:

- Xem sản phẩm
- Thêm, cập nhật, xóa sản phẩm trong giỏ hàng
- Checkout COD
- Xem lịch sử đơn hàng
- Xem chi tiết đơn hàng của mình

Customer không thể:

- Truy cập trang admin
- Quản lý sản phẩm hoặc danh mục
- Quản lý đơn hàng của người khác
- Cập nhật trạng thái đơn hàng

### 3.3 Admin

Admin có thể:

- Đăng nhập trang admin
- Xem dashboard
- Quản lý danh mục
- Quản lý sản phẩm
- Quản lý đơn hàng
- Cập nhật trạng thái đơn hàng
- Xem danh sách khách hàng

---

## 4. Phạm vi MVP

### 4.1 Customer Site

- Trang chủ
- Trang danh sách sản phẩm
- Trang chi tiết sản phẩm
- Giỏ hàng
- Đăng ký
- Đăng nhập
- Checkout COD
- Lịch sử đơn hàng
- Chi tiết đơn hàng

### 4.2 Admin Site

- Admin login
- Dashboard tổng quan
- Quản lý danh mục
- Quản lý sản phẩm
- Quản lý đơn hàng
- Quản lý khách hàng

### 4.3 Backend API

- Auth API cho customer/admin
- Category API
- Product API
- Order API
- Admin API
- Authorization theo role
- Validate dữ liệu đầu vào
- Seed dữ liệu mẫu

---

## 5. Ngoài phạm vi MVP

Các tính năng sau chưa nằm trong MVP:

- Thanh toán online qua VNPay, Momo, Stripe hoặc PayPal
- Tích hợp vận chuyển bên thứ ba
- Voucher/coupon nâng cao
- Wishlist
- Đánh giá sản phẩm
- Chat hỗ trợ khách hàng
- Email/SMS notification
- Multi-vendor marketplace
- Multi-language
- Multi-currency
- Báo cáo doanh thu nâng cao
- Quản lý tồn kho nhiều kho

---

## 6. User Stories

### US-GUEST-001 — Xem trang chủ

Là guest, tôi muốn xem trang chủ để nhìn thấy sản phẩm nổi bật và điều hướng đến danh sách sản phẩm.

### US-GUEST-002 — Xem danh sách sản phẩm

Là guest, tôi muốn xem danh sách sản phẩm để lựa chọn sản phẩm cần mua.

### US-GUEST-003 — Xem chi tiết sản phẩm

Là guest, tôi muốn xem thông tin chi tiết sản phẩm để quyết định có mua hay không.

### US-GUEST-004 — Đăng ký tài khoản

Là guest, tôi muốn đăng ký tài khoản để có thể đặt hàng.

### US-GUEST-005 — Đăng nhập

Là guest, tôi muốn đăng nhập để checkout và xem đơn hàng của mình.

### US-CUS-001 — Thêm sản phẩm vào giỏ hàng

Là customer, tôi muốn thêm sản phẩm vào giỏ hàng để chuẩn bị mua.

### US-CUS-002 — Cập nhật giỏ hàng

Là customer, tôi muốn thay đổi số lượng hoặc xóa sản phẩm khỏi giỏ hàng.

### US-CUS-003 — Checkout COD

Là customer, tôi muốn đặt hàng bằng phương thức thanh toán khi nhận hàng.

### US-CUS-004 — Xem lịch sử đơn hàng

Là customer, tôi muốn xem các đơn hàng đã đặt.

### US-CUS-005 — Xem chi tiết đơn hàng

Là customer, tôi muốn xem chi tiết từng đơn hàng bao gồm sản phẩm, số lượng, giá và trạng thái.

### US-ADM-001 — Đăng nhập admin

Là admin, tôi muốn đăng nhập vào trang quản trị để vận hành hệ thống.

### US-ADM-002 — Xem dashboard

Là admin, tôi muốn xem số lượng sản phẩm, khách hàng, đơn hàng và doanh thu cơ bản.

### US-ADM-003 — Quản lý danh mục

Là admin, tôi muốn tạo, sửa, xóa và xem danh mục sản phẩm.

### US-ADM-004 — Quản lý sản phẩm

Là admin, tôi muốn tạo, sửa, xóa và xem sản phẩm.

### US-ADM-005 — Quản lý đơn hàng

Là admin, tôi muốn xem danh sách đơn hàng, xem chi tiết và cập nhật trạng thái đơn hàng.

### US-ADM-006 — Quản lý khách hàng

Là admin, tôi muốn xem danh sách khách hàng đã đăng ký.

---

## 7. User Flows

### 7.1 Luồng mua hàng

```txt
Guest/Customer
→ Truy cập trang chủ
→ Xem danh sách sản phẩm
→ Mở chi tiết sản phẩm
→ Thêm vào giỏ hàng
→ Mở giỏ hàng
→ Nếu chưa đăng nhập: chuyển tới đăng nhập/đăng ký
→ Checkout
→ Nhập thông tin nhận hàng
→ Xác nhận COD
→ Tạo đơn hàng
→ Hiển thị đặt hàng thành công
```

### 7.2 Luồng đăng ký

```txt
Guest
→ Mở trang đăng ký
→ Nhập tên, email, mật khẩu
→ Submit
→ Hệ thống validate dữ liệu
→ Tạo tài khoản customer
→ Chuyển tới trang đăng nhập hoặc tự động đăng nhập
```

### 7.3 Luồng đăng nhập

```txt
Guest
→ Mở trang đăng nhập
→ Nhập email và mật khẩu
→ Submit
→ Hệ thống xác thực
→ Trả JWT token
→ Frontend lưu token
→ Điều hướng về trang trước đó hoặc trang chủ
```

### 7.4 Luồng xem lịch sử đơn hàng

```txt
Customer
→ Đăng nhập
→ Mở trang đơn hàng của tôi
→ Hệ thống lấy danh sách đơn hàng theo user hiện tại
→ Customer chọn một đơn hàng
→ Hệ thống hiển thị chi tiết đơn hàng
```

### 7.5 Luồng admin quản lý sản phẩm

```txt
Admin
→ Đăng nhập admin
→ Mở trang quản lý sản phẩm
→ Xem danh sách sản phẩm
→ Tạo/sửa/xóa sản phẩm
→ Backend validate dữ liệu
→ Lưu thay đổi vào database
→ Frontend refresh danh sách
```

### 7.6 Luồng admin xử lý đơn hàng

```txt
Admin
→ Đăng nhập admin
→ Mở trang quản lý đơn hàng
→ Xem danh sách đơn hàng
→ Mở chi tiết đơn hàng
→ Cập nhật trạng thái đơn hàng
→ Hệ thống lưu trạng thái mới
```

---

## 8. Business Rules

### 8.1 User/Auth

- Email người dùng phải là duy nhất.
- Mật khẩu phải được hash trước khi lưu.
- User có role `CUSTOMER` hoặc `ADMIN`.
- Customer không được truy cập API admin.
- Không trả password hash trong response.
- JWT secret không được hardcode trong source public.

### 8.2 Product

- Sản phẩm phải thuộc một danh mục hợp lệ.
- Sản phẩm có tối thiểu: tên, mô tả, giá, tồn kho, ảnh đại diện, trạng thái active/inactive.
- Giá sản phẩm phải >= 0.
- Tồn kho phải >= 0.
- Sản phẩm inactive không hiển thị ở customer site.
- Admin có thể xem cả sản phẩm active và inactive.

### 8.3 Category

- Danh mục có tên không được rỗng.
- Không nên xóa cứng danh mục nếu vẫn còn sản phẩm liên quan.
- Danh mục inactive không hiển thị ở customer site.

### 8.4 Cart

- Giỏ hàng MVP có thể lưu ở frontend local state/localStorage.
- Mỗi dòng giỏ hàng gồm Product ID, tên, giá, số lượng và ảnh.
- Số lượng sản phẩm trong giỏ hàng phải > 0.
- Không cho checkout nếu giỏ hàng rỗng.
- Không cho checkout nếu số lượng vượt tồn kho hiện tại.

### 8.5 Checkout

- Chỉ customer đã đăng nhập mới checkout.
- MVP chỉ hỗ trợ COD.
- Checkout cần tên người nhận, số điện thoại, địa chỉ và ghi chú tùy chọn.
- Backend phải tự tính tổng tiền, không tin total từ frontend.
- Backend kiểm tra user, sản phẩm, active status, số lượng và tồn kho trước khi tạo đơn.
- Sau khi tạo đơn thành công, tồn kho được trừ tương ứng.

### 8.6 Order

Trạng thái đơn hàng:

```txt
PENDING
CONFIRMED
SHIPPING
COMPLETED
CANCELLED
```

- Đơn mới mặc định `PENDING`.
- Customer chỉ xem đơn của chính mình.
- Admin xem được tất cả đơn hàng.
- Admin có thể cập nhật trạng thái đơn hàng.
- Không cho sửa sản phẩm trong đơn sau khi đã tạo.

---

## 9. Yêu cầu phi chức năng

- Chạy native trên Windows.
- Không dùng Docker path `/root` hoặc `/workspace`.
- Dùng path Windows hoặc relative path.
- Không cài package ngoài nếu chưa có preflight approval.
- Validate input ở backend.
- API admin phải kiểm tra role.
- Không trả thông tin nhạy cảm trong response.
- Thiết kế đủ đơn giản để mở rộng sau này cho payment, coupon, review, wishlist.

---

## 10. Deliverables Product Scope

Tài liệu Product gồm:

- `docs/prd.md`
- `docs/acceptance-criteria.md`

Hai tài liệu này là đầu vào cho:

- Architecture Agent
- Frontend Agent
- Backend Agent
- QA Agent
