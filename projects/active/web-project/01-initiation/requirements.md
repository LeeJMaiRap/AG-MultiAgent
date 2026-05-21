Để bắt đầu xây dựng **ứng dụng thanh toán nhanh**, mình cần thêm một số thông tin từ PM Orchestrator trước khi tạo/sửa file PRD trong thư mục dự án.

## 1. Thông tin cần xác nhận

Vui lòng cung cấp:

1. **Tên dự án**
   - Ví dụ: `quickpay`, `fast-payment-app`, `paynow`

2. **Đường dẫn thư mục dự án**
   - Ví dụ: `projects/active/quickpay/01-initiation/requirements.md`

3. **Loại ứng dụng**
   - Web app?
   - Mobile app?
   - Cả web và mobile?
   - Mini app trong hệ sinh thái khác?

4. **Đối tượng người dùng chính**
   - Người dùng cá nhân?
   - Chủ cửa hàng?
   - Nhân viên thu ngân?
   - Doanh nghiệp?

5. **Phạm vi thanh toán**
   - Thanh toán nội bộ giữa người dùng trong app?
   - Thanh toán qua QR?
   - Thanh toán hóa đơn?
   - Nạp/rút tiền?
   - Liên kết ngân hàng/ví điện tử?
   - Thanh toán tại cửa hàng?

6. **Khu vực triển khai**
   - Việt Nam?
   - Quốc tế?
   - Có yêu cầu tiền tệ cụ thể không? Ví dụ: VND, USD

7. **Yêu cầu bảo mật/xác thực**
   - OTP?
   - PIN giao dịch?
   - Face ID/Touch ID?
   - 2FA?
   - KYC?

8. **Vai trò người dùng**
   - Người dùng thường
   - Merchant/cửa hàng
   - Admin vận hành
   - Nhân viên hỗ trợ

---

## 2. Bản PRD nháp ban đầu

Trong lúc chờ xác nhận, dưới đây là bản yêu cầu sản phẩm khởi tạo cho ứng dụng thanh toán nhanh.

# PRD — Ứng dụng Thanh toán Nhanh

## 2.1. Mục tiêu sản phẩm

Xây dựng một ứng dụng cho phép người dùng thực hiện thanh toán nhanh, an toàn và dễ sử dụng thông qua các phương thức như mã QR, chuyển tiền đến người dùng khác, thanh toán đơn hàng và theo dõi lịch sử giao dịch.

## 2.2. Vấn đề cần giải quyết

Người dùng thường gặp các vấn đề khi thanh toán:

- Quy trình thanh toán nhiều bước.
- Khó kiểm tra trạng thái giao dịch.
- Không có lịch sử giao dịch rõ ràng.
- Không có xác thực giao dịch đủ an toàn.
- Khó thanh toán nhanh tại cửa hàng hoặc cho người khác.

## 2.3. Mục tiêu kinh doanh

- Giảm thời gian hoàn tất một giao dịch thanh toán.
- Tăng tỷ lệ giao dịch thành công.
- Cung cấp trải nghiệm thanh toán đơn giản, an toàn.
- Tạo nền tảng có thể mở rộng cho merchant, hóa đơn, khuyến mãi và loyalty.

## 2.4. Đối tượng người dùng

### Người dùng cá nhân

Người dùng muốn thanh toán nhanh cho hàng hóa, dịch vụ hoặc chuyển tiền cho người khác.

### Merchant/cửa hàng

Đơn vị chấp nhận thanh toán qua ứng dụng.

### Admin vận hành

Nhân sự quản trị hệ thống, theo dõi giao dịch, xử lý khiếu nại và quản lý người dùng.

---

# 3. Phạm vi chức năng MVP

## 3.1. Đăng ký và đăng nhập

Người dùng có thể tạo tài khoản và đăng nhập vào ứng dụng bằng số điện thoại/email.

### User Story

Là người dùng mới, tôi muốn đăng ký tài khoản để có thể sử dụng dịch vụ thanh toán.

### Acceptance Criteria

- Người dùng có thể đăng ký bằng số điện thoại hoặc email.
- Hệ thống yêu cầu nhập:
  - Họ tên
  - Số điện thoại hoặc email
  - Mật khẩu
- Mật khẩu phải có tối thiểu 8 ký tự.
- Nếu số điện thoại/email đã tồn tại, hệ thống hiển thị lỗi: `Tài khoản đã tồn tại`.
- Sau khi đăng ký thành công, người dùng được chuyển đến màn hình xác thực OTP hoặc màn hình chính tùy cấu hình xác thực.
- Hệ thống không cho phép tạo tài khoản nếu thiếu trường bắt buộc.

---

## 3.2. Xác thực OTP

Người dùng xác thực số điện thoại/email thông qua mã OTP.

### User Story

Là người dùng, tôi muốn xác thực OTP để đảm bảo tài khoản thuộc về tôi.

### Acceptance Criteria

- Hệ thống gửi OTP gồm 6 chữ số.
- OTP có hiệu lực trong 5 phút.
- Người dùng nhập sai OTP quá 5 lần sẽ bị khóa xác thực trong 10 phút.
- Nếu OTP hết hạn, hệ thống hiển thị: `Mã OTP đã hết hạn`.
- Nếu OTP đúng, tài khoản được đánh dấu là đã xác thực.
- Người dùng có thể yêu cầu gửi lại OTP sau tối thiểu 60 giây.

---

## 3.3. Thiết lập PIN giao dịch

Người dùng thiết lập PIN để xác nhận các giao dịch thanh toán.

### User Story

Là người dùng, tôi muốn tạo PIN giao dịch để bảo vệ các khoản thanh toán của mình.

### Acceptance Criteria

- PIN gồm đúng 6 chữ số.
- Người dùng phải nhập PIN hai lần để xác nhận.
- Nếu hai lần nhập không khớp, hệ thống hiển thị: `PIN xác nhận không khớp`.
- Không cho phép PIN là chuỗi dễ đoán:
  - `000000`
  - `111111`
  - `123456`
  - `654321`
- Người dùng không thể thực hiện thanh toán nếu chưa thiết lập PIN.

---

## 3.4. Trang chủ ví/thanh toán

Người dùng xem tổng quan số dư, nút thanh toán nhanh và lịch sử gần đây.

### User Story

Là người dùng, tôi muốn xem thông tin ví và các thao tác thanh toán chính để sử dụng nhanh.

### Acceptance Criteria

- Trang chủ hiển thị:
  - Số dư hiện tại
  - Nút quét QR
  - Nút chuyển tiền
  - Nút lịch sử giao dịch
  - 5 giao dịch gần nhất
- Số dư được hiển thị theo định dạng tiền tệ, ví dụ: `1.000.000 ₫`.
- Nếu không có giao dịch, hiển thị trạng thái rỗng: `Bạn chưa có giao dịch nào`.
- Người dùng có thể ẩn/hiện số dư.
- Khi số dư bị ẩn, hiển thị dạng `******`.

---

## 3.5. Quét mã QR thanh toán

Người dùng quét mã QR để thanh toán cho merchant hoặc người dùng khác.

### User Story

Là người dùng, tôi muốn quét mã QR để thanh toán nhanh mà không cần nhập thông tin thủ công.

### Acceptance Criteria

- Người dùng có thể mở camera để quét QR.
- Nếu chưa cấp quyền camera, hệ thống yêu cầu cấp quyền.
- Nếu QR không hợp lệ, hiển thị: `Mã QR không hợp lệ`.
- QR hợp lệ phải chứa tối thiểu:
  - ID người nhận hoặc merchant
  - Loại giao dịch
  - Số tiền hoặc trạng thái cho phép nhập số tiền
- Nếu QR có số tiền cố định, trường số tiền không được chỉnh sửa.
- Nếu QR không có số tiền, người dùng phải nhập số tiền.
- Số tiền thanh toán tối thiểu là `1.000 ₫`.
- Số tiền thanh toán tối đa mặc định là `50.000.000 ₫/giao dịch`, trừ khi cấu hình khác.
- Trước khi thanh toán, hệ thống hiển thị màn hình xác nhận gồm:
  - Tên người nhận/merchant
  - Số tiền
  - Phí giao dịch nếu có
  - Tổng tiền
- Người dùng phải nhập PIN để xác nhận giao dịch.
- Sau khi giao dịch thành công, hiển thị biên nhận thanh toán.
- Nếu giao dịch thất bại, hiển thị lý do thất bại nếu có.

---

## 3.6. Chuyển tiền đến người dùng khác

Người dùng chuyển tiền đến số điện thoại, email hoặc ID người nhận.

### User Story

Là người dùng, tôi muốn chuyển tiền cho người khác trong ứng dụng.

### Acceptance Criteria

- Người dùng có thể nhập số điện thoại/email/ID người nhận.
- Hệ thống kiểm tra người nhận có tồn tại.
- Nếu người nhận không tồn tại, hiển thị: `Không tìm thấy người nhận`.
- Người dùng không thể chuyển tiền cho chính mình.
- Người dùng nhập số tiền chuyển.
- Số tiền tối thiểu là `1.000 ₫`.
- Hệ thống hiển thị màn hình xác nhận trước khi chuyển.
- Người dùng phải nhập PIN giao dịch.
- Nếu số dư không đủ, hiển thị: `Số dư không đủ`.
- Nếu giao dịch thành công:
  - Trừ tiền người gửi
  - Cộng tiền người nhận
  - Tạo lịch sử giao dịch cho cả hai bên
- Giao dịch phải có mã tham chiếu duy nhất.

---

## 3.7. Lịch sử giao dịch

Người dùng xem danh sách giao dịch đã thực hiện.

### User Story

Là người dùng, tôi muốn xem lịch sử giao dịch để kiểm tra các khoản thanh toán của mình.

### Acceptance Criteria

- Danh sách hiển thị các giao dịch theo thứ tự mới nhất trước.
- Mỗi giao dịch hiển thị:
  - Mã giao dịch
  - Loại giao dịch
  - Số tiền
  - Trạng thái
  - Thời gian
  - Đối tác giao dịch
- Trạng thái giao dịch gồm:
  - `Thành công`
  - `Đang xử lý`
  - `Thất bại`
  - `Đã hoàn tiền`
- Người dùng có thể lọc theo:
  - Khoảng thời gian
  - Trạng thái
  - Loại giao dịch
- Người dùng có thể bấm vào một giao dịch để xem chi tiết.
- Nếu không có kết quả, hiển thị: `Không tìm thấy giao dịch phù hợp`.

---

## 3.8. Chi tiết giao dịch

Người dùng xem thông tin đầy đủ của một giao dịch.

### User Story

Là người dùng, tôi muốn xem chi tiết giao dịch để đối soát khi cần.

### Acceptance Criteria

- Màn hình chi tiết giao dịch hiển thị:
  - Mã giao dịch
  - Mã tham chiếu
  - Trạng thái
  - Số tiền
  - Phí giao dịch nếu có
  - Tổng tiền
  - Người gửi
  - Người nhận
  - Thời gian tạo
  - Thời gian hoàn tất nếu có
  - Nội dung giao dịch nếu có
- Người dùng chỉ xem được giao dịch liên quan đến tài khoản của mình.
- Nếu truy cập giao dịch không thuộc quyền, hệ thống trả lỗi không có quyền truy cập.
- Người dùng có thể tải/chia sẻ biên nhận nếu tính năng được bật.

---

## 3.9. Biên nhận thanh toán

Sau khi thanh toán thành công, người dùng xem biên nhận.

### User Story

Là người dùng, tôi muốn có biên nhận sau giao dịch để lưu lại bằng chứng thanh toán.

### Acceptance Criteria

- Biên nhận hiển thị:
  - Logo/tên ứng dụng
  - Trạng thái thanh toán
  - Số tiền
  - Người nhận
  - Mã giao dịch
  - Thời gian
- Biên nhận chỉ được tạo cho giao dịch thành công hoặc đang xử lý.
- Người dùng có thể chia sẻ biên nhận dưới dạng ảnh hoặc PDF nếu được hỗ trợ.
- Biên nhận không hiển thị thông tin nhạy cảm như PIN, token, dữ liệu xác thực.

---

## 3.10. Thông báo giao dịch

Người dùng nhận thông báo khi có giao dịch.

### User Story

Là người dùng, tôi muốn nhận thông báo khi giao dịch thành công hoặc thất bại.

### Acceptance Criteria

- Người gửi nhận thông báo khi giao dịch:
  - Thành công
  - Thất bại
  - Đang xử lý quá thời gian cấu hình
- Người nhận nhận thông báo khi nhận được tiền.
- Nội dung thông báo gồm:
  - Loại giao dịch
  - Số tiền
  - Trạng thái
  - Thời gian
- Thông báo không chứa PIN, token hoặc thông tin bảo mật.
- Người dùng có thể xem danh sách thông báo trong ứng dụng.

---

# 4. Chức năng Admin MVP

## 4.1. Đăng nhập admin

Admin đăng nhập vào hệ thống quản trị.

### Acceptance Criteria

- Admin đăng nhập bằng email và mật khẩu.
- Nếu thông tin sai, hiển thị: `Email hoặc mật khẩu không đúng`.
- Tài khoản admin bị khóa sau 5 lần đăng nhập sai liên tiếp.
- Admin phải có vai trò hợp lệ mới truy cập được dashboard.
- Hệ thống ghi nhận thời gian đăng nhập gần nhất.

---

## 4.2. Quản lý người dùng

Admin xem và tìm kiếm người dùng.

### Acceptance Criteria

- Admin có thể xem danh sách người dùng.
- Mỗi người dùng hiển thị:
  - ID
  - Họ tên
  - Số điện thoại/email
  - Trạng thái tài khoản
  - Ngày tạo
- Admin có thể tìm theo ID, số điện thoại, email.
- Admin có thể lọc theo trạng thái:
  - Hoạt động
  - Khóa
  - Chưa xác thực
- Admin có thể xem chi tiết người dùng.
- Admin không được xem PIN hoặc mật khẩu người dùng.

---

## 4.3. Quản lý giao dịch

Admin xem và tra cứu giao dịch.

### Acceptance Criteria

- Admin có thể xem danh sách giao dịch.
- Admin có thể tìm kiếm theo:
  - Mã giao dịch
  - Mã tham chiếu
  - Người gửi
  - Người nhận
- Admin có thể lọc theo:
  - Trạng thái
  - Loại giao dịch
  - Khoảng thời gian
- Admin có thể xem chi tiết giao dịch.
- Admin không thể chỉnh sửa trực tiếp số tiền giao dịch đã hoàn tất.
- Mọi hành động admin trên giao dịch phải được ghi audit log.

---

# 5. Yêu cầu phi chức năng

## 5.1. Bảo mật

- Mật khẩu phải được lưu bằng cơ chế hash an toàn.
- PIN giao dịch không được lưu dạng plain text.
- Tất cả API nhạy cảm phải yêu cầu xác thực.
- Giao dịch thanh toán phải yêu cầu PIN hoặc xác thực tương đương.
- Token phiên đăng nhập phải có thời hạn.
- Hệ thống phải chống replay request cho API thanh toán.
- Không log dữ liệu nhạy cảm:
  - Mật khẩu
  - PIN
  - OTP
  - Access token
  - Refresh token

## 5.2. Hiệu năng

- 95% request thông thường phản hồi dưới 1 giây trong điều kiện tải mục tiêu.
- 95% request tạo giao dịch phản hồi dưới 3 giây, không tính thời gian xử lý từ cổng thanh toán bên thứ ba nếu có.
- Trang lịch sử giao dịch hỗ trợ phân trang.
- Danh sách giao dịch mặc định tải tối đa 20 bản ghi mỗi trang.

## 5.3. Tính nhất quán giao dịch

- Một giao dịch thành công không được trừ tiền hai lần.
- Mỗi yêu cầu thanh toán phải có idempotency key hoặc mã định danh chống xử lý trùng.
- Nếu xảy ra lỗi trong quá trình chuyển tiền nội bộ, hệ thống phải rollback hoặc đánh dấu giao dịch ở trạng thái xử lý để đối soát.
- Số dư hiển thị phải phản ánh trạng thái giao dịch đã hoàn tất.

## 5.4. Khả dụng

- Hệ thống cần có cơ chế xử lý khi dịch vụ OTP, notification hoặc payment gateway tạm thời không khả dụng.
- Người dùng phải nhận được thông báo rõ ràng khi giao dịch đang xử lý.
- Giao dịch không được hiển thị thành công nếu chưa được xác nhận thành công từ hệ thống xử lý chính.

## 5.5. Audit log

- Hệ thống phải ghi log các hành động quan trọng:
  - Đăng nhập
  - Đăng xuất
  - Tạo giao dịch
  - Xác nhận giao dịch
  - Thay đổi trạng thái người dùng
  - Hành động admin trên giao dịch
- Audit log phải có:
  - Actor ID
  - Hành động
  - Thời gian
  - IP/device nếu có
  - Kết quả thành công/thất bại

---

# 6. Các trạng thái giao dịch

## 6.1. Danh sách trạng thái

- `PENDING`: Giao dịch được tạo, chưa hoàn tất.
- `PROCESSING`: Đang xử lý.
- `SUCCESS`: Thành công.
- `FAILED`: Thất bại.
- `REFUNDED`: Đã hoàn tiền.
- `CANCELLED`: Đã hủy.

## 6.2. Quy tắc chuyển trạng thái

- `PENDING` có thể chuyển sang:
  - `PROCESSING`
  - `CANCELLED`
  - `FAILED`
- `PROCESSING` có thể chuyển sang:
  - `SUCCESS`
  - `FAILED`
- `SUCCESS` có thể chuyển sang:
  - `REFUNDED`
- `FAILED`, `REFUNDED`, `CANCELLED` là trạng thái kết thúc.

---

# 7. Dữ liệu chính cần quản lý

## 7.1. User

- User ID
- Họ tên
- Số điện thoại
- Email
- Trạng thái xác thực
- Trạng thái tài khoản
- Ngày tạo
- Ngày cập nhật

## 7.2. Wallet/Balance

- Wallet ID
- User ID
- Số dư khả dụng
- Số dư bị giữ nếu có
- Tiền tệ
- Ngày cập nhật

## 7.3. Transaction

- Transaction ID
- Reference ID
- Loại giao dịch
- Người gửi
- Người nhận
- Số tiền
- Phí
- Tổng tiền
- Trạng thái
- Nội dung
- Thời gian tạo
- Thời gian cập nhật
- Thời gian hoàn tất

## 7.4. Notification

- Notification ID
- User ID
- Loại thông báo
- Nội dung
- Trạng thái đọc/chưa đọc
- Thời gian tạo

## 7.5. Audit Log

- Audit Log ID
- Actor ID
- Actor type
- Action
- Target entity
- Result
- Metadata
- Created at

---

# 8. Ngoài phạm vi MVP đề xuất

Các chức năng sau nên để giai đoạn sau nếu chưa cần MVP:

- KYC nâng cao.
- Liên kết tài khoản ngân hàng.
- Rút tiền về ngân hàng.
- Thanh toán hóa đơn điện/nước/internet.
- Tích điểm loyalty.
- Hoàn tiền tự động.
- Mã khuyến mãi.
- Merchant portal đầy đủ.
- Đối soát với ngân hàng/cổng thanh toán.
- Hỗ trợ đa tiền tệ.
- Hỗ trợ chargeback/dispute phức tạp.

---

# 9. Handoff cho các Agent

## Cho Architecture Agent

Cần thiết kế hệ thống có các module tối thiểu:

- Authentication & Authorization
- User Management
- Wallet/Balance Service
- Transaction Service
- QR Payment Service
- Notification Service
- Admin Service
- Audit Logging
- Idempotency/Anti-duplicate mechanism

Yêu cầu đặc biệt:

- Giao dịch tiền phải đảm bảo tính nhất quán.
- Cần cơ chế idempotency cho API tạo giao dịch.
- Không lưu PIN/OTP dạng plain text.
- Cần phân quyền user/admin rõ ràng.

## Cho Backend Agent

Cần cung cấp API cho:

- Đăng ký/đăng nhập
- Xác thực OTP
- Thiết lập PIN
- Lấy số dư ví
- Quét/giải mã QR
- Tạo giao dịch
- Xác nhận giao dịch bằng PIN
- Chuyển tiền nội bộ
- Lấy lịch sử giao dịch
- Lấy chi tiết giao dịch
- Lấy thông báo
- Admin quản lý user
- Admin quản lý giao dịch

## Cho Frontend Agent

Cần xây dựng các màn hình:

- Đăng ký
- Đăng nhập
- Xác thực OTP
- Tạo PIN
- Trang chủ ví
- Quét QR
- Nhập số tiền
- Xác nhận thanh toán
- Nhập PIN giao dịch
- Kết quả giao dịch
- Biên nhận
- Lịch sử giao dịch
- Chi tiết giao dịch
- Thông báo
- Admin dashboard nếu nằm trong scope

## Cho QA Agent

Cần kiểm thử:

- Luồng đăng ký/đăng nhập
- Luồng OTP đúng/sai/hết hạn
- Thiết lập PIN hợp lệ/không hợp lệ
- Thanh toán QR hợp lệ/không hợp lệ
- Chuyển tiền thành công
- Chuyển tiền khi số dư không đủ
- Chống chuyển tiền cho chính mình
- Chống giao dịch trùng
- Lịch sử giao dịch và phân quyền xem giao dịch
- Admin xem/tìm/lọc giao dịch
- Không rò rỉ dữ liệu nhạy cảm

---

## 10. Cần PM xác nhận để tiếp tục

Vui lòng trả lời theo mẫu sau:

```text
Tên dự án:
Đường dẫn file requirements:
Nền tảng: Web / Mobile / Cả hai
Người dùng chính:
Phạm vi MVP:
Có ví nội bộ không: Có / Không
Có QR payment không: Có / Không
Có liên kết ngân hàng không: Có / Không
Có admin portal không: Có / Không
Tiền tệ:
Yêu cầu bảo mật:
```

Sau khi có đường dẫn file chính xác, mình có thể chuẩn hóa nội dung thành tài liệu `requirements.md` để handoff cho các agent tiếp theo.