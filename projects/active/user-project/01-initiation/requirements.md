Dưới đây là bản đặc tả yêu cầu ban đầu cho **MVP bán hàng trực tuyến**. Vì bạn chưa cung cấp tên dự án/thư mục làm việc cụ thể, tôi chưa tạo file. Khi có project path, có thể lưu tài liệu này tại:

`projects/active/[project-name]/01-initiation/requirements.md`

---

# PRD — MVP Bán Hàng Trực Tuyến

## 1. Tổng quan sản phẩm

### 1.1 Mục tiêu

Xây dựng một nền tảng bán hàng trực tuyến phiên bản MVP cho phép:

- Khách hàng xem danh sách sản phẩm.
- Khách hàng xem chi tiết sản phẩm.
- Khách hàng thêm sản phẩm vào giỏ hàng.
- Khách hàng đặt hàng.
- Quản trị viên quản lý sản phẩm và đơn hàng ở mức cơ bản.

### 1.2 Phạm vi MVP

MVP tập trung vào quy trình mua hàng cơ bản:

```text
Xem sản phẩm → Xem chi tiết → Thêm vào giỏ → Đặt hàng → Admin xử lý đơn
```

### 1.3 Đối tượng người dùng

#### Khách hàng

Người truy cập website để xem sản phẩm và đặt mua hàng.

#### Quản trị viên

Người quản lý danh sách sản phẩm và theo dõi đơn hàng.

---

## 2. Mục tiêu kinh doanh

### 2.1 Mục tiêu chính

- Cho phép doanh nghiệp bắt đầu bán hàng online nhanh chóng.
- Kiểm chứng nhu cầu thị trường với chi phí phát triển thấp.
- Thu thập dữ liệu đơn hàng và hành vi mua hàng cơ bản.

### 2.2 Chỉ số thành công MVP

| Chỉ số | Mục tiêu |
|---|---|
| Khách hàng có thể hoàn tất đơn hàng | 100% flow đặt hàng hoạt động |
| Thời gian tạo sản phẩm mới bởi admin | Dưới 2 phút |
| Đơn hàng được lưu lại đầy đủ | 100% đơn hàng có thông tin khách + sản phẩm |
| Website hoạt động trên mobile và desktop | Có responsive layout cơ bản |

---

## 3. Phạm vi chức năng

## 3.1 Chức năng cho khách hàng

### F-001: Xem danh sách sản phẩm

Khách hàng có thể xem danh sách sản phẩm đang được bán.

#### Yêu cầu chi tiết

- Hiển thị danh sách sản phẩm.
- Mỗi sản phẩm hiển thị:
  - Hình ảnh sản phẩm.
  - Tên sản phẩm.
  - Giá bán.
  - Trạng thái còn hàng hoặc hết hàng.
  - Nút xem chi tiết.
- Chỉ hiển thị sản phẩm đang được bật trạng thái hiển thị.

#### Acceptance Criteria

```gherkin
Given khách hàng truy cập trang danh sách sản phẩm
When hệ thống có sản phẩm đang được hiển thị
Then khách hàng thấy danh sách sản phẩm gồm hình ảnh, tên, giá và trạng thái tồn kho

Given sản phẩm bị admin tắt hiển thị
When khách hàng truy cập trang danh sách sản phẩm
Then sản phẩm đó không xuất hiện trong danh sách

Given sản phẩm hết hàng
When khách hàng xem danh sách sản phẩm
Then sản phẩm hiển thị trạng thái "Hết hàng"
And khách hàng không thể thêm sản phẩm đó vào giỏ từ danh sách
```

---

### F-002: Xem chi tiết sản phẩm

Khách hàng có thể xem thông tin chi tiết của một sản phẩm.

#### Yêu cầu chi tiết

Trang chi tiết sản phẩm cần hiển thị:

- Hình ảnh sản phẩm.
- Tên sản phẩm.
- Giá bán.
- Mô tả sản phẩm.
- Trạng thái tồn kho.
- Số lượng còn lại nếu có.
- Nút thêm vào giỏ hàng nếu sản phẩm còn hàng.

#### Acceptance Criteria

```gherkin
Given khách hàng chọn một sản phẩm còn hàng
When trang chi tiết sản phẩm được mở
Then hệ thống hiển thị tên, hình ảnh, giá, mô tả và trạng thái còn hàng
And nút "Thêm vào giỏ hàng" được bật

Given khách hàng chọn một sản phẩm hết hàng
When trang chi tiết sản phẩm được mở
Then hệ thống hiển thị trạng thái "Hết hàng"
And nút "Thêm vào giỏ hàng" bị vô hiệu hóa

Given khách hàng truy cập URL sản phẩm không tồn tại
When hệ thống xử lý request
Then hiển thị trang thông báo "Không tìm thấy sản phẩm"
```

---

### F-003: Giỏ hàng

Khách hàng có thể thêm, cập nhật và xóa sản phẩm trong giỏ hàng.

#### Yêu cầu chi tiết

- Thêm sản phẩm vào giỏ hàng.
- Cập nhật số lượng sản phẩm.
- Xóa sản phẩm khỏi giỏ hàng.
- Hiển thị tổng tiền.
- Không cho phép đặt số lượng lớn hơn tồn kho.
- Giỏ hàng có thể lưu trong session/local storage đối với MVP.

#### Acceptance Criteria

```gherkin
Given sản phẩm còn hàng
When khách hàng bấm "Thêm vào giỏ hàng"
Then sản phẩm được thêm vào giỏ
And số lượng mặc định là 1

Given sản phẩm đã có trong giỏ
When khách hàng thêm lại cùng sản phẩm
Then số lượng sản phẩm trong giỏ tăng thêm 1
And không tạo dòng sản phẩm trùng lặp

Given khách hàng cập nhật số lượng sản phẩm trong giỏ
When số lượng mới nhỏ hơn hoặc bằng tồn kho
Then hệ thống cập nhật số lượng thành công
And tổng tiền được tính lại chính xác

Given khách hàng cập nhật số lượng lớn hơn tồn kho
When khách hàng xác nhận cập nhật
Then hệ thống không cho phép cập nhật
And hiển thị thông báo "Số lượng vượt quá tồn kho"

Given khách hàng xóa sản phẩm khỏi giỏ
When thao tác xóa thành công
Then sản phẩm không còn xuất hiện trong giỏ
And tổng tiền được tính lại chính xác

Given giỏ hàng không có sản phẩm
When khách hàng mở trang giỏ hàng
Then hệ thống hiển thị thông báo "Giỏ hàng của bạn đang trống"
And nút đặt hàng không được hiển thị hoặc bị vô hiệu hóa
```

---

### F-004: Đặt hàng

Khách hàng có thể tạo đơn hàng từ giỏ hàng.

#### Yêu cầu chi tiết

Khách hàng cần nhập thông tin:

- Họ tên.
- Số điện thoại.
- Email, tùy chọn ở MVP.
- Địa chỉ giao hàng.
- Ghi chú đơn hàng, tùy chọn.

Hệ thống cần lưu:

- Thông tin khách hàng.
- Danh sách sản phẩm.
- Số lượng từng sản phẩm.
- Đơn giá tại thời điểm đặt hàng.
- Tổng tiền.
- Trạng thái đơn hàng mặc định: `Mới`.

#### Phạm vi thanh toán MVP

MVP chưa tích hợp thanh toán online.

Phương thức thanh toán mặc định:

- Thanh toán khi nhận hàng, COD.

#### Acceptance Criteria

```gherkin
Given khách hàng có ít nhất một sản phẩm trong giỏ
When khách hàng mở trang checkout
Then hệ thống hiển thị form nhập họ tên, số điện thoại, email, địa chỉ và ghi chú
And hệ thống hiển thị danh sách sản phẩm, số lượng và tổng tiền

Given khách hàng bỏ trống họ tên
When khách hàng bấm "Đặt hàng"
Then hệ thống không tạo đơn hàng
And hiển thị lỗi "Vui lòng nhập họ tên"

Given khách hàng nhập số điện thoại không hợp lệ
When khách hàng bấm "Đặt hàng"
Then hệ thống không tạo đơn hàng
And hiển thị lỗi "Số điện thoại không hợp lệ"

Given khách hàng bỏ trống địa chỉ giao hàng
When khách hàng bấm "Đặt hàng"
Then hệ thống không tạo đơn hàng
And hiển thị lỗi "Vui lòng nhập địa chỉ giao hàng"

Given thông tin checkout hợp lệ
And sản phẩm trong giỏ còn đủ tồn kho
When khách hàng bấm "Đặt hàng"
Then hệ thống tạo đơn hàng thành công
And trạng thái đơn hàng là "Mới"
And hệ thống trừ tồn kho tương ứng
And giỏ hàng được xóa
And khách hàng thấy màn hình xác nhận đặt hàng thành công

Given sản phẩm trong giỏ không còn đủ tồn kho tại thời điểm đặt hàng
When khách hàng bấm "Đặt hàng"
Then hệ thống không tạo đơn hàng
And hiển thị danh sách sản phẩm không đủ tồn kho
```

---

## 3.2 Chức năng cho quản trị viên

### F-005: Đăng nhập admin

Quản trị viên có thể đăng nhập vào khu vực quản trị.

#### Yêu cầu chi tiết

- Admin đăng nhập bằng email và mật khẩu.
- Chỉ tài khoản có quyền admin mới truy cập được trang quản trị.
- MVP có thể tạo sẵn tài khoản admin ban đầu.

#### Acceptance Criteria

```gherkin
Given admin nhập đúng email và mật khẩu
When admin bấm "Đăng nhập"
Then hệ thống cho phép truy cập dashboard quản trị

Given người dùng nhập sai email hoặc mật khẩu
When bấm "Đăng nhập"
Then hệ thống không cho đăng nhập
And hiển thị lỗi "Thông tin đăng nhập không chính xác"

Given người chưa đăng nhập truy cập URL quản trị
When hệ thống kiểm tra quyền truy cập
Then chuyển người dùng về trang đăng nhập admin

Given người dùng không có quyền admin truy cập URL quản trị
When hệ thống kiểm tra quyền truy cập
Then hệ thống từ chối truy cập
```

---

### F-006: Quản lý sản phẩm

Admin có thể tạo, xem, sửa và ẩn/hiện sản phẩm.

#### Yêu cầu chi tiết

Thông tin sản phẩm gồm:

- Tên sản phẩm.
- Mô tả.
- Giá bán.
- Hình ảnh.
- Số lượng tồn kho.
- Trạng thái hiển thị: bật/tắt.

#### Acceptance Criteria

```gherkin
Given admin đã đăng nhập
When admin mở trang quản lý sản phẩm
Then hệ thống hiển thị danh sách sản phẩm gồm tên, giá, tồn kho và trạng thái hiển thị

Given admin nhập đầy đủ thông tin sản phẩm hợp lệ
When admin bấm "Tạo sản phẩm"
Then hệ thống tạo sản phẩm mới
And sản phẩm xuất hiện trong danh sách quản lý

Given admin bỏ trống tên sản phẩm
When admin bấm "Tạo sản phẩm"
Then hệ thống không tạo sản phẩm
And hiển thị lỗi "Vui lòng nhập tên sản phẩm"

Given admin nhập giá bán nhỏ hơn hoặc bằng 0
When admin bấm "Tạo sản phẩm"
Then hệ thống không tạo sản phẩm
And hiển thị lỗi "Giá bán phải lớn hơn 0"

Given admin nhập tồn kho nhỏ hơn 0
When admin bấm "Tạo sản phẩm"
Then hệ thống không tạo sản phẩm
And hiển thị lỗi "Tồn kho không được nhỏ hơn 0"

Given admin chỉnh sửa thông tin sản phẩm hợp lệ
When admin bấm "Lưu thay đổi"
Then hệ thống cập nhật sản phẩm thành công
And dữ liệu mới được hiển thị trong danh sách

Given admin tắt trạng thái hiển thị của sản phẩm
When khách hàng truy cập trang danh sách sản phẩm
Then sản phẩm đó không xuất hiện trên website bán hàng
```

---

### F-007: Quản lý đơn hàng

Admin có thể xem danh sách và chi tiết đơn hàng.

#### Yêu cầu chi tiết

Danh sách đơn hàng hiển thị:

- Mã đơn hàng.
- Tên khách hàng.
- Số điện thoại.
- Tổng tiền.
- Trạng thái đơn hàng.
- Ngày tạo.

Chi tiết đơn hàng hiển thị:

- Thông tin khách hàng.
- Địa chỉ giao hàng.
- Ghi chú.
- Danh sách sản phẩm.
- Số lượng.
- Đơn giá.
- Tổng tiền.
- Trạng thái đơn hàng.

Admin có thể cập nhật trạng thái đơn hàng:

- Mới.
- Đang xử lý.
- Đang giao.
- Hoàn tất.
- Đã hủy.

#### Acceptance Criteria

```gherkin
Given admin đã đăng nhập
When admin mở trang quản lý đơn hàng
Then hệ thống hiển thị danh sách đơn hàng gồm mã đơn, khách hàng, số điện thoại, tổng tiền, trạng thái và ngày tạo

Given admin chọn một đơn hàng
When trang chi tiết đơn hàng được mở
Then hệ thống hiển thị đầy đủ thông tin khách hàng, địa chỉ, sản phẩm, số lượng, đơn giá, tổng tiền và trạng thái

Given admin cập nhật trạng thái đơn hàng sang "Đang xử lý"
When admin lưu thay đổi
Then trạng thái đơn hàng được cập nhật thành "Đang xử lý"

Given admin cập nhật trạng thái đơn hàng sang "Đã hủy"
When admin lưu thay đổi
Then trạng thái đơn hàng được cập nhật thành "Đã hủy"

Given đơn hàng đã ở trạng thái "Hoàn tất"
When admin cập nhật trạng thái
Then hệ thống không cho phép chuyển về trạng thái "Mới"
And hiển thị lỗi "Không thể chuyển đơn hoàn tất về trạng thái mới"
```

---

## 4. Ngoài phạm vi MVP

Các chức năng sau **không nằm trong MVP**:

- Đăng ký/đăng nhập tài khoản khách hàng.
- Thanh toán online qua VNPay, MoMo, Stripe, PayPal.
- Mã giảm giá.
- Tính phí vận chuyển tự động.
- Tích hợp đơn vị vận chuyển.
- Đánh giá sản phẩm.
- Yêu thích sản phẩm.
- Chat hỗ trợ.
- Báo cáo doanh thu nâng cao.
- Phân quyền nhiều vai trò admin.
- Quản lý danh mục sản phẩm phức tạp.
- Biến thể sản phẩm như màu sắc, kích thước.
- Email/SMS tự động.
- Đa ngôn ngữ.
- Đa tiền tệ.

---

## 5. Yêu cầu dữ liệu

## 5.1 Product

| Trường | Kiểu dữ liệu | Bắt buộc | Ghi chú |
|---|---:|---:|---|
| id | UUID/Integer | Có | Mã sản phẩm |
| name | String | Có | Tên sản phẩm |
| description | Text | Không | Mô tả sản phẩm |
| price | Decimal | Có | Giá bán, phải > 0 |
| imageUrl | String | Không | URL hình ảnh |
| stockQuantity | Integer | Có | Tồn kho, >= 0 |
| isVisible | Boolean | Có | Có hiển thị ra website không |
| createdAt | DateTime | Có | Ngày tạo |
| updatedAt | DateTime | Có | Ngày cập nhật |

---

## 5.2 Cart Item

Nếu lưu ở client/session:

| Trường | Kiểu dữ liệu | Bắt buộc | Ghi chú |
|---|---:|---:|---|
| productId | UUID/Integer | Có | Mã sản phẩm |
| quantity | Integer | Có | Số lượng, >= 1 |

---

## 5.3 Order

| Trường | Kiểu dữ liệu | Bắt buộc | Ghi chú |
|---|---:|---:|---|
| id | UUID/Integer | Có | Mã đơn hàng |
| customerName | String | Có | Họ tên |
| customerPhone | String | Có | Số điện thoại |
| customerEmail | String | Không | Email |
| shippingAddress | Text | Có | Địa chỉ giao hàng |
| note | Text | Không | Ghi chú |
| totalAmount | Decimal | Có | Tổng tiền |
| status | Enum | Có | Mặc định: Mới |
| paymentMethod | Enum | Có | COD |
| createdAt | DateTime | Có | Ngày tạo |
| updatedAt | DateTime | Có | Ngày cập nhật |

---

## 5.4 Order Item

| Trường | Kiểu dữ liệu | Bắt buộc | Ghi chú |
|---|---:|---:|---|
| id | UUID/Integer | Có | Mã dòng đơn hàng |
| orderId | UUID/Integer | Có | Mã đơn hàng |
| productId | UUID/Integer | Có | Mã sản phẩm |
| productName | String | Có | Snapshot tên sản phẩm |
| unitPrice | Decimal | Có | Snapshot giá tại thời điểm mua |
| quantity | Integer | Có | Số lượng |
| lineTotal | Decimal | Có | unitPrice x quantity |

---

## 5.5 Admin User

| Trường | Kiểu dữ liệu | Bắt buộc | Ghi chú |
|---|---:|---:|---|
| id | UUID/Integer | Có | Mã admin |
| email | String | Có | Duy nhất |
| passwordHash | String | Có | Không lưu plain text |
| role | String/Enum | Có | admin |
| createdAt | DateTime | Có | Ngày tạo |

---

## 6. Quy tắc nghiệp vụ

### BR-001: Giá sản phẩm

- Giá sản phẩm phải lớn hơn 0.
- Giá trong đơn hàng phải là giá tại thời điểm đặt hàng.
- Nếu admin thay đổi giá sau khi đơn đã tạo, đơn hàng cũ không bị thay đổi giá.

### BR-002: Tồn kho

- Tồn kho sản phẩm không được nhỏ hơn 0.
- Khi đặt hàng thành công, hệ thống trừ tồn kho.
- Nếu tồn kho không đủ tại thời điểm checkout, hệ thống không tạo đơn hàng.
- Sản phẩm có tồn kho bằng 0 được xem là hết hàng.

### BR-003: Trạng thái sản phẩm

- Chỉ sản phẩm `isVisible = true` mới hiển thị cho khách hàng.
- Admin vẫn xem được cả sản phẩm đang ẩn.

### BR-004: Trạng thái đơn hàng

Trạng thái đơn hàng hợp lệ:

```text
Mới → Đang xử lý → Đang giao → Hoàn tất
Mới → Đã hủy
Đang xử lý → Đã hủy
```

Không cho phép:

- Chuyển đơn `Hoàn tất` về `Mới`.
- Chuyển đơn `Đã hủy` sang `Hoàn tất`.

### BR-005: Thanh toán

- MVP chỉ hỗ trợ COD.
- Không yêu cầu tích hợp cổng thanh toán online.

---

## 7. Yêu cầu giao diện

## 7.1 Trang khách hàng

### Trang danh sách sản phẩm

Các thành phần chính:

- Header với tên cửa hàng.
- Link giỏ hàng.
- Grid/list sản phẩm.
- Card sản phẩm gồm ảnh, tên, giá, trạng thái.
- Nút xem chi tiết.

### Trang chi tiết sản phẩm

Các thành phần chính:

- Ảnh sản phẩm.
- Tên sản phẩm.
- Giá.
- Mô tả.
- Tồn kho/trạng thái.
- Nút thêm vào giỏ.

### Trang giỏ hàng

Các thành phần chính:

- Danh sách sản phẩm trong giỏ.
- Số lượng có thể chỉnh sửa.
- Nút xóa sản phẩm.
- Tổng tiền.
- Nút đi đến checkout.

### Trang checkout

Các thành phần chính:

- Form thông tin khách hàng.
- Tóm tắt đơn hàng.
- Tổng tiền.
- Phương thức thanh toán COD.
- Nút đặt hàng.

### Trang xác nhận đặt hàng

Các thành phần chính:

- Thông báo đặt hàng thành công.
- Mã đơn hàng.
- Tổng tiền.
- Thông tin liên hệ/giao hàng.
- Link quay lại trang sản phẩm.

---

## 7.2 Trang quản trị

### Trang đăng nhập

- Email.
- Mật khẩu.
- Nút đăng nhập.
- Hiển thị lỗi đăng nhập.

### Dashboard admin

MVP có thể chỉ gồm navigation:

- Quản lý sản phẩm.
- Quản lý đơn hàng.
- Đăng xuất.

### Trang quản lý sản phẩm

- Danh sách sản phẩm.
- Nút tạo sản phẩm.
- Form tạo/sửa sản phẩm.
- Công tắc bật/tắt hiển thị.

### Trang quản lý đơn hàng

- Danh sách đơn hàng.
- Bộ lọc trạng thái, nếu kịp trong MVP.
- Trang chi tiết đơn hàng.
- Dropdown cập nhật trạng thái.

---

## 8. Yêu cầu phi chức năng

## 8.1 Hiệu năng

- Trang danh sách sản phẩm tải trong vòng tối đa 3 giây với 100 sản phẩm trên kết nối mạng thông thường.
- Thao tác thêm vào giỏ hàng phản hồi trong vòng tối đa 1 giây.
- Tạo đơn hàng phản hồi trong vòng tối đa 3 giây nếu không có lỗi hệ thống.

## 8.2 Bảo mật

- Mật khẩu admin phải được hash.
- Không lưu mật khẩu dạng plain text.
- Trang admin bắt buộc yêu cầu đăng nhập.
- API admin phải kiểm tra quyền truy cập.
- Validate dữ liệu đầu vào ở cả frontend và backend.
- Không cho phép khách hàng gửi tổng tiền từ client làm nguồn dữ liệu tin cậy; backend phải tự tính tổng tiền.

## 8.3 Khả dụng

- Website hỗ trợ responsive cơ bản cho:
  - Mobile: từ 360px trở lên.
  - Tablet.
  - Desktop.
- Các lỗi form phải hiển thị rõ cạnh trường liên quan hoặc trong khu vực thông báo lỗi.

## 8.4 Khả năng kiểm thử

- Mỗi flow chính phải có thể kiểm thử thủ công.
- Các rule quan trọng như tồn kho, giá, trạng thái đơn hàng cần có test case.

---

## 9. User Stories

## Epic 1: Mua hàng

### US-001: Xem danh sách sản phẩm

Là khách hàng, tôi muốn xem danh sách sản phẩm để lựa chọn sản phẩm cần mua.

#### Acceptance Criteria

- Hiển thị các sản phẩm đang bật trạng thái hiển thị.
- Mỗi sản phẩm có ảnh, tên, giá, trạng thái tồn kho.
- Sản phẩm ẩn không xuất hiện.

---

### US-002: Xem chi tiết sản phẩm

Là khách hàng, tôi muốn xem chi tiết sản phẩm để quyết định có mua hay không.

#### Acceptance Criteria

- Hiển thị đầy đủ tên, ảnh, giá, mô tả.
- Nếu còn hàng, có thể thêm vào giỏ.
- Nếu hết hàng, không thể thêm vào giỏ.

---

### US-003: Quản lý giỏ hàng

Là khách hàng, tôi muốn thêm, sửa, xóa sản phẩm trong giỏ để chuẩn bị đặt hàng.

#### Acceptance Criteria

- Có thể thêm sản phẩm còn hàng vào giỏ.
- Có thể thay đổi số lượng.
- Không thể nhập số lượng lớn hơn tồn kho.
- Có thể xóa sản phẩm khỏi giỏ.
- Tổng tiền được cập nhật đúng.

---

### US-004: Đặt hàng COD

Là khách hàng, tôi muốn nhập thông tin giao hàng và đặt hàng để mua sản phẩm.

#### Acceptance Criteria

- Form yêu cầu họ tên, số điện thoại, địa chỉ.
- Email và ghi chú là tùy chọn.
- Đơn hàng được tạo khi dữ liệu hợp lệ và tồn kho đủ.
- Hệ thống trừ tồn kho sau khi đặt hàng thành công.
- Giỏ hàng được xóa sau khi đặt hàng thành công.

---

## Epic 2: Quản trị sản phẩm

### US-005: Đăng nhập admin

Là admin, tôi muốn đăng nhập vào hệ thống để quản lý cửa hàng.

#### Acceptance Criteria

- Đăng nhập thành công với thông tin hợp lệ.
- Không đăng nhập được với thông tin sai.
- Người chưa đăng nhập không truy cập được trang admin.

---

### US-006: Tạo sản phẩm

Là admin, tôi muốn tạo sản phẩm mới để bán trên website.

#### Acceptance Criteria

- Có thể nhập tên, mô tả, giá, ảnh, tồn kho, trạng thái hiển thị.
- Không tạo được sản phẩm nếu thiếu tên.
- Không tạo được sản phẩm nếu giá <= 0.
- Không tạo được sản phẩm nếu tồn kho < 0.

---

### US-007: Chỉnh sửa sản phẩm

Là admin, tôi muốn chỉnh sửa thông tin sản phẩm để cập nhật nội dung bán hàng.

#### Acceptance Criteria

- Có thể sửa tên, mô tả, giá, ảnh, tồn kho, trạng thái.
- Thay đổi được lưu thành công khi dữ liệu hợp lệ.
- Sản phẩm bị tắt hiển thị không xuất hiện ở trang khách hàng.

---

## Epic 3: Quản trị đơn hàng

### US-008: Xem danh sách đơn hàng

Là admin, tôi muốn xem danh sách đơn hàng để theo dõi tình hình bán hàng.

#### Acceptance Criteria

- Danh sách hiển thị mã đơn, khách hàng, số điện thoại, tổng tiền, trạng thái, ngày tạo.
- Đơn hàng mới tạo từ checkout xuất hiện trong danh sách admin.

---

### US-009: Xem chi tiết đơn hàng

Là admin, tôi muốn xem chi tiết đơn hàng để xử lý giao hàng.

#### Acceptance Criteria

- Hiển thị thông tin khách hàng.
- Hiển thị địa chỉ giao hàng.
- Hiển thị danh sách sản phẩm, số lượng, đơn giá, tổng tiền.
- Hiển thị trạng thái đơn hàng.

---

### US-010: Cập nhật trạng thái đơn hàng

Là admin, tôi muốn cập nhật trạng thái đơn hàng để phản ánh tiến trình xử lý.

#### Acceptance Criteria

- Có thể chuyển đơn từ `Mới` sang `Đang xử lý`.
- Có thể chuyển đơn từ `Đang xử lý` sang `Đang giao`.
- Có thể chuyển đơn từ `Đang giao` sang `Hoàn tất`.
- Có thể hủy đơn ở trạng thái `Mới` hoặc `Đang xử lý`.
- Không thể chuyển đơn `Hoàn tất` về `Mới`.
- Không thể chuyển đơn `Đã hủy` sang `Hoàn tất`.

---

## 10. API/Backend Handoff Requirements

Gợi ý các nhóm endpoint cần có cho Backend Agent.

### Public Product APIs

| Method | Endpoint | Mục đích |
|---|---|---|
| GET | `/api/products` | Lấy danh sách sản phẩm visible |
| GET | `/api/products/:id` | Lấy chi tiết sản phẩm visible |

### Cart

Nếu giỏ hàng lưu client-side thì không cần API riêng cho cart ở MVP.

### Order APIs

| Method | Endpoint | Mục đích |
|---|---|---|
| POST | `/api/orders` | Tạo đơn hàng |

### Admin Auth APIs

| Method | Endpoint | Mục đích |
|---|---|---|
| POST | `/api/admin/login` | Đăng nhập admin |
| POST | `/api/admin/logout` | Đăng xuất admin |
| GET | `/api/admin/me` | Kiểm tra phiên đăng nhập |

### Admin Product APIs

| Method | Endpoint | Mục đích |
|---|---|---|
| GET | `/api/admin/products` | Lấy tất cả sản phẩm |
| POST | `/api/admin/products` | Tạo sản phẩm |
| GET | `/api/admin/products/:id` | Lấy chi tiết sản phẩm |
| PUT/PATCH | `/api/admin/products/:id` | Cập nhật sản phẩm |

### Admin Order APIs

| Method | Endpoint | Mục đích |
|---|---|---|
| GET | `/api/admin/orders` | Lấy danh sách đơn hàng |
| GET | `/api/admin/orders/:id` | Lấy chi tiết đơn hàng |
| PATCH | `/api/admin/orders/:id/status` | Cập nhật trạng thái đơn hàng |

---

## 11. Frontend Handoff Requirements

Frontend cần xây dựng các route/trang sau.

### Public routes

| Route | Mục đích |
|---|---|
| `/` | Trang danh sách sản phẩm |
| `/products/:id` | Trang chi tiết sản phẩm |
| `/cart` | Trang giỏ hàng |
| `/checkout` | Trang checkout |
| `/order-success/:id` | Trang xác nhận đặt hàng |

### Admin routes

| Route | Mục đích |
|---|---|
| `/admin/login` | Đăng nhập admin |
| `/admin` | Dashboard admin |
| `/admin/products` | Quản lý sản phẩm |
| `/admin/products/new` | Tạo sản phẩm |
| `/admin/products/:id/edit` | Sửa sản phẩm |
| `/admin/orders` | Quản lý đơn hàng |
| `/admin/orders/:id` | Chi tiết đơn hàng |

---

## 12. QA Handoff Requirements

QA cần kiểm thử tối thiểu các nhóm sau:

### Smoke Test

- Khách hàng xem được danh sách sản phẩm.
- Khách hàng thêm sản phẩm vào giỏ.
- Khách hàng đặt hàng thành công.
- Admin đăng nhập được.
- Admin thấy đơn hàng mới.
- Admin cập nhật trạng thái đơn hàng.

### Functional Test

- Validate form tạo sản phẩm.
- Validate form checkout.
- Kiểm tra tồn kho khi thêm vào giỏ và đặt hàng.
- Kiểm tra tổng tiền.
- Kiểm tra trạng thái sản phẩm visible/hidden.
- Kiểm tra trạng thái đơn hàng hợp lệ/không hợp lệ.

### Security Test

- Người chưa đăng nhập không truy cập được admin.
- API admin từ chối request không có quyền.
- Không thể tạo đơn hàng với tổng tiền giả từ client.
- Không lưu mật khẩu admin plain text.

### Responsive Test

- Kiểm tra các trang chính ở kích thước:
  - 360px mobile.
  - 768px tablet.
  - 1366px desktop.

---

## 13. Ưu tiên triển khai MVP

### P0 — Bắt buộc

- Danh sách sản phẩm.
- Chi tiết sản phẩm.
- Giỏ hàng.
- Checkout COD.
- Tạo đơn hàng.
- Admin login.
- Admin quản lý sản phẩm.
- Admin xem/cập nhật đơn hàng.

### P1 — Nên có nếu còn thời gian

- Bộ lọc đơn hàng theo trạng thái.
- Tìm kiếm sản phẩm trong admin.
- Phân trang sản phẩm.
- Upload ảnh thay vì nhập URL ảnh.
- Email thông báo đơn hàng.

### P2 — Sau MVP

- Thanh toán online.
- Tài khoản khách hàng.
- Mã giảm giá.
- Phí vận chuyển tự động.
- Báo cáo doanh thu.
- Tích hợp vận chuyển.

---

## 14. Câu hỏi cần xác nhận với PM

1. Tên cửa hàng/dự án là gì?
2. Dùng đơn vị tiền tệ mặc định là VND đúng không?
3. Sản phẩm có cần danh mục ngay trong MVP không?
4. Hình ảnh sản phẩm sẽ upload file hay nhập URL?
5. Có cần email xác nhận đơn hàng trong MVP không?
6. Có cần lọc/tìm kiếm sản phẩm phía khách hàng không?
7. Admin có một tài khoản duy nhất hay nhiều tài khoản?
8. Có cần xuất đơn hàng ra Excel không?
9. Khi hủy đơn hàng có cần hoàn lại tồn kho không?
10. Chính sách chuyển trạng thái đơn hàng có cần chặt như đề xuất không?

---

## 15. Đề xuất quyết định mặc định cho MVP

Nếu không có thêm yêu cầu, đề xuất chốt như sau:

- Tiền tệ: VND.
- Thanh toán: COD.
- Không có tài khoản khách hàng.
- Giỏ hàng lưu local storage.
- Hình ảnh sản phẩm nhập bằng URL.
- Có một tài khoản admin tạo sẵn.
- Không có danh mục sản phẩm trong MVP.
- Không gửi email xác nhận đơn hàng.
- Khi hủy đơn hàng:
  - Nếu đơn đã từng trừ tồn kho lúc đặt hàng, hệ thống cộng lại tồn kho khi hủy.
- Tổng tiền luôn do backend tính lại tại thời điểm tạo đơn.