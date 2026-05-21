# Acceptance Criteria — e-commerce-web MVP

## 1. Tổng quan

Tài liệu này định nghĩa tiêu chí nghiệm thu cho MVP website bán hàng `e-commerce-web`.

Các nhóm chức năng chính:

- Customer site
- Auth
- Cart
- Checkout COD
- Order history
- Admin site
- Backend API
- Authorization
- Database/seed

---

## 2. Acceptance Criteria — Customer Site

### AC-HOME-001

Given người dùng truy cập trang chủ  
When trang được tải thành công  
Then hệ thống hiển thị giao diện trang chủ có điều hướng đến danh sách sản phẩm.

### AC-HOME-002

Given hệ thống có dữ liệu sản phẩm active  
When người dùng truy cập trang chủ  
Then hệ thống có thể hiển thị một số sản phẩm nổi bật hoặc sản phẩm mới.

### AC-PRODUCT-LIST-001

Given người dùng truy cập trang danh sách sản phẩm  
When backend trả về danh sách sản phẩm active  
Then frontend hiển thị danh sách sản phẩm gồm tên, giá, ảnh và nút xem chi tiết.

### AC-PRODUCT-LIST-002

Given có sản phẩm inactive trong database  
When customer hoặc guest xem danh sách sản phẩm  
Then sản phẩm inactive không được hiển thị.

### AC-PRODUCT-LIST-003

Given không có sản phẩm phù hợp  
When người dùng truy cập danh sách sản phẩm  
Then hệ thống hiển thị trạng thái rỗng dễ hiểu.

### AC-PRODUCT-DETAIL-001

Given người dùng chọn một sản phẩm active  
When trang chi tiết sản phẩm được mở  
Then hệ thống hiển thị tên, mô tả, giá, tồn kho, ảnh và nút thêm vào giỏ hàng.

### AC-PRODUCT-DETAIL-002

Given sản phẩm không tồn tại hoặc inactive  
When người dùng truy cập URL chi tiết sản phẩm  
Then hệ thống hiển thị thông báo không tìm thấy hoặc không khả dụng.

### AC-PRODUCT-DETAIL-003

Given sản phẩm còn tồn kho  
When người dùng bấm thêm vào giỏ hàng  
Then sản phẩm được thêm vào giỏ hàng.

### AC-PRODUCT-DETAIL-004

Given sản phẩm hết hàng  
When người dùng xem chi tiết sản phẩm  
Then nút thêm vào giỏ hàng bị vô hiệu hóa hoặc hiển thị trạng thái hết hàng.

---

## 3. Acceptance Criteria — Auth

### AC-AUTH-REGISTER-001

Given guest nhập tên, email và mật khẩu hợp lệ  
When guest submit form đăng ký  
Then hệ thống tạo tài khoản customer mới.

### AC-AUTH-REGISTER-002

Given email đã tồn tại  
When guest submit form đăng ký với email đó  
Then hệ thống từ chối và hiển thị lỗi phù hợp.

### AC-AUTH-REGISTER-003

Given dữ liệu đăng ký thiếu hoặc sai định dạng  
When guest submit form  
Then hệ thống không tạo tài khoản và trả lỗi validation.

### AC-AUTH-REGISTER-004

Given tài khoản được tạo thành công  
When hệ thống trả response  
Then response không chứa password hash.

### AC-AUTH-LOGIN-001

Given user nhập đúng email và mật khẩu  
When user submit form đăng nhập  
Then hệ thống trả JWT token và thông tin user cơ bản.

### AC-AUTH-LOGIN-002

Given user nhập sai email hoặc mật khẩu  
When user submit form đăng nhập  
Then hệ thống từ chối đăng nhập và trả lỗi xác thực.

### AC-AUTH-LOGIN-003

Given user đăng nhập thành công  
When frontend nhận token  
Then frontend lưu token để gọi API cần xác thực.

### AC-AUTH-LOGIN-004

Given response đăng nhập thành công  
When kiểm tra dữ liệu trả về  
Then response không chứa password hash.

---

## 4. Acceptance Criteria — Cart

### AC-CART-ADD-001

Given sản phẩm active và còn hàng  
When người dùng bấm thêm vào giỏ hàng  
Then sản phẩm xuất hiện trong giỏ hàng.

### AC-CART-ADD-002

Given sản phẩm đã có trong giỏ hàng  
When người dùng thêm lại cùng sản phẩm  
Then số lượng sản phẩm trong giỏ hàng tăng lên.

### AC-CART-ADD-003

Given sản phẩm hết hàng  
When người dùng bấm thêm vào giỏ hàng  
Then hệ thống không thêm sản phẩm và hiển thị thông báo phù hợp.

### AC-CART-UPDATE-001

Given giỏ hàng có sản phẩm  
When người dùng thay đổi số lượng hợp lệ  
Then tổng tiền giỏ hàng được cập nhật.

### AC-CART-UPDATE-002

Given người dùng đặt số lượng về 0 hoặc bấm xóa  
When thao tác được xác nhận  
Then sản phẩm bị xóa khỏi giỏ hàng.

### AC-CART-UPDATE-003

Given giỏ hàng rỗng  
When người dùng mở trang giỏ hàng  
Then hệ thống hiển thị trạng thái giỏ hàng rỗng.

---

## 5. Acceptance Criteria — Checkout COD

### AC-CHECKOUT-001

Given customer đã đăng nhập và giỏ hàng có sản phẩm hợp lệ  
When customer nhập thông tin nhận hàng và xác nhận checkout COD  
Then backend tạo đơn hàng mới với trạng thái `PENDING`.

### AC-CHECKOUT-002

Given user chưa đăng nhập  
When user cố checkout  
Then hệ thống yêu cầu đăng nhập.

### AC-CHECKOUT-003

Given giỏ hàng rỗng  
When customer cố checkout  
Then hệ thống không tạo đơn hàng và hiển thị lỗi.

### AC-CHECKOUT-004

Given sản phẩm trong giỏ hàng không đủ tồn kho  
When customer checkout  
Then backend từ chối tạo đơn hàng và trả lỗi tồn kho.

### AC-CHECKOUT-005

Given đơn hàng được tạo thành công  
When kiểm tra database  
Then order items được lưu với giá tại thời điểm đặt hàng.

### AC-CHECKOUT-006

Given đơn hàng được tạo thành công  
When kiểm tra tồn kho sản phẩm  
Then tồn kho được trừ theo số lượng đã đặt.

### AC-CHECKOUT-007

Given frontend gửi tổng tiền đơn hàng  
When backend xử lý checkout  
Then backend tự tính lại tổng tiền và không tin tưởng total từ frontend.

---

## 6. Acceptance Criteria — Order History

### AC-ORDER-HISTORY-001

Given customer đã đăng nhập  
When customer mở trang lịch sử đơn hàng  
Then hệ thống hiển thị danh sách đơn hàng của chính customer đó.

### AC-ORDER-HISTORY-002

Given customer A và customer B tồn tại  
When customer A gọi API đơn hàng  
Then customer A không xem được đơn hàng của customer B.

### AC-ORDER-HISTORY-003

Given customer chưa có đơn hàng  
When customer mở lịch sử đơn hàng  
Then hệ thống hiển thị trạng thái rỗng.

### AC-ORDER-DETAIL-001

Given customer đã đăng nhập và có đơn hàng  
When customer mở chi tiết đơn hàng của mình  
Then hệ thống hiển thị sản phẩm, số lượng, đơn giá, tổng tiền, trạng thái và thông tin nhận hàng.

### AC-ORDER-DETAIL-002

Given customer cố truy cập đơn hàng không thuộc về mình  
When backend kiểm tra quyền truy cập  
Then backend trả lỗi không được phép hoặc không tìm thấy.

---

## 7. Acceptance Criteria — Admin Auth

### AC-ADMIN-AUTH-001

Given user có role `ADMIN`  
When user đăng nhập admin thành công  
Then user có thể truy cập admin dashboard.

### AC-ADMIN-AUTH-002

Given user có role `CUSTOMER`  
When user cố truy cập admin dashboard hoặc admin API  
Then hệ thống từ chối truy cập.

### AC-ADMIN-AUTH-003

Given request admin API không có token  
When request được gửi  
Then backend trả lỗi unauthorized.

### AC-ADMIN-AUTH-004

Given request admin API có token hết hạn hoặc không hợp lệ  
When request được gửi  
Then backend trả lỗi unauthorized.

---

## 8. Acceptance Criteria — Admin Dashboard

### AC-ADMIN-DASHBOARD-001

Given admin đã đăng nhập  
When admin mở dashboard  
Then hệ thống hiển thị số liệu tổng quan tối thiểu gồm số sản phẩm, số đơn hàng và số khách hàng.

### AC-ADMIN-DASHBOARD-002

Given customer hoặc guest truy cập dashboard  
When hệ thống kiểm tra quyền  
Then truy cập bị từ chối.

---

## 9. Acceptance Criteria — Admin Category Management

### AC-ADMIN-CATEGORY-001

Given admin đã đăng nhập  
When admin tạo danh mục với tên hợp lệ  
Then danh mục mới được lưu vào database.

### AC-ADMIN-CATEGORY-002

Given admin nhập tên danh mục rỗng  
When submit form  
Then hệ thống từ chối và hiển thị lỗi validation.

### AC-ADMIN-CATEGORY-003

Given admin chỉnh sửa danh mục  
When dữ liệu hợp lệ  
Then hệ thống cập nhật danh mục.

### AC-ADMIN-CATEGORY-004

Given admin xóa danh mục không còn sản phẩm liên quan  
When thao tác xóa được xác nhận  
Then danh mục bị xóa hoặc được đánh dấu inactive.

### AC-ADMIN-CATEGORY-005

Given danh mục còn sản phẩm liên quan  
When admin cố xóa  
Then hệ thống nên từ chối hoặc chuyển sang trạng thái inactive tùy thiết kế backend.

---

## 10. Acceptance Criteria — Admin Product Management

### AC-ADMIN-PRODUCT-001

Given admin đã đăng nhập  
When admin tạo sản phẩm với dữ liệu hợp lệ  
Then sản phẩm mới được lưu vào database.

### AC-ADMIN-PRODUCT-002

Given sản phẩm thiếu tên, giá, danh mục hoặc tồn kho không hợp lệ  
When admin submit form  
Then backend trả lỗi validation.

### AC-ADMIN-PRODUCT-003

Given admin chỉnh sửa sản phẩm  
When dữ liệu hợp lệ  
Then sản phẩm được cập nhật.

### AC-ADMIN-PRODUCT-004

Given admin xóa sản phẩm  
When thao tác được xác nhận  
Then sản phẩm bị xóa mềm hoặc chuyển inactive.

### AC-ADMIN-PRODUCT-005

Given sản phẩm inactive  
When customer xem danh sách sản phẩm  
Then sản phẩm đó không hiển thị.

### AC-ADMIN-PRODUCT-006

Given admin xem danh sách sản phẩm  
When danh sách được tải  
Then admin có thể thấy cả sản phẩm active và inactive nếu backend hỗ trợ.

---

## 11. Acceptance Criteria — Admin Order Management

### AC-ADMIN-ORDER-001

Given admin đã đăng nhập  
When admin mở trang quản lý đơn hàng  
Then hệ thống hiển thị danh sách tất cả đơn hàng.

### AC-ADMIN-ORDER-002

Given admin mở chi tiết đơn hàng  
When dữ liệu tồn tại  
Then hệ thống hiển thị thông tin customer, sản phẩm, số lượng, tổng tiền, trạng thái và thông tin nhận hàng.

### AC-ADMIN-ORDER-003

Given đơn hàng có trạng thái hợp lệ  
When admin cập nhật trạng thái sang trạng thái hợp lệ khác  
Then hệ thống lưu trạng thái mới.

### AC-ADMIN-ORDER-004

Given admin gửi trạng thái không hợp lệ  
When backend validate request  
Then backend từ chối cập nhật.

### AC-ADMIN-ORDER-005

Given customer cố gọi API cập nhật trạng thái đơn hàng  
When backend kiểm tra role  
Then backend trả lỗi forbidden.

---

## 12. Acceptance Criteria — Admin Customer Management

### AC-ADMIN-CUSTOMER-001

Given admin đã đăng nhập  
When admin mở trang quản lý khách hàng  
Then hệ thống hiển thị danh sách customer.

### AC-ADMIN-CUSTOMER-002

Given danh sách customer được trả về  
When kiểm tra response  
Then response không chứa password hash.

### AC-ADMIN-CUSTOMER-003

Given customer hoặc guest gọi API danh sách khách hàng  
When backend kiểm tra quyền  
Then backend từ chối truy cập.

---

## 13. Acceptance Criteria — Backend API

### AC-API-001

Given API nhận request sai định dạng  
When backend validate input  
Then backend trả lỗi validation có format nhất quán.

### AC-API-002

Given API xử lý lỗi server  
When lỗi phát sinh  
Then backend trả lỗi phù hợp và không lộ thông tin nhạy cảm.

### AC-API-003

Given request thành công  
When backend trả response  
Then response có dữ liệu cần thiết cho frontend và không chứa password hash.

### AC-API-004

Given endpoint cần xác thực  
When request không có JWT token  
Then backend trả unauthorized.

### AC-API-005

Given endpoint cần quyền admin  
When request có token customer  
Then backend trả forbidden.

---

## 14. Acceptance Criteria — Database & Seed

### AC-DB-001

Given project được setup thành công  
When chạy migration hoặc schema setup  
Then database SQLite được tạo.

### AC-DB-002

Given seed script được chạy  
When kiểm tra database  
Then có dữ liệu mẫu tối thiểu:

- 1 admin user
- 1 customer user
- 1 locked customer nếu có tính năng khóa
- Nhiều category active/inactive
- Nhiều product active/inactive/in-stock/out-of-stock
- Một số order mẫu nếu cần QA

### AC-DB-003

Given password user seed  
When lưu vào database  
Then password phải được hash.

---

## 15. Definition of Done

Một module được xem là hoàn tất khi:

- Có UI hoặc API tương ứng hoạt động theo scope MVP.
- Có validation cơ bản.
- Có xử lý lỗi cơ bản.
- Có kiểm tra phân quyền với chức năng cần auth.
- Không trả password hash về frontend.
- Có thể chạy local trên Windows Native.
- QA có thể kiểm thử theo acceptance criteria trong tài liệu này.

---

## 16. Điều kiện nghiệm thu MVP tổng thể

MVP được xem là đạt yêu cầu khi:

- Guest có thể xem sản phẩm.
- Customer có thể đăng ký, đăng nhập, thêm giỏ hàng và đặt hàng COD.
- Customer có thể xem lịch sử và chi tiết đơn hàng của mình.
- Admin có thể đăng nhập và quản lý danh mục, sản phẩm, đơn hàng, khách hàng.
- Backend có phân quyền customer/admin.
- Database SQLite có schema và seed dữ liệu mẫu.
- Hệ thống chạy được local theo hướng dẫn Windows Native.
