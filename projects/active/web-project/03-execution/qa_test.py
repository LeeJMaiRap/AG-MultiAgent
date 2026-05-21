## QA Status — Chưa thể nghiệm thu tính năng

Mình đã nhận PRD cho **ứng dụng thanh toán nhanh / QuickPay** và các ghi chú từ FE/BE. Tuy nhiên hiện tại **chưa thể thực hiện kiểm thử hoặc xác nhận Acceptance Criteria** vì chưa có thông tin triển khai thực tế và chưa có môi trường/source code để chạy test.

Theo vai trò QA/Test Agent, mình **không sửa code**, chỉ kiểm thử và lập báo cáo nghiệm thu khi có hệ thống để kiểm tra.

---

## Thông tin QA cần để bắt đầu kiểm thử

Vui lòng cung cấp:

```text
Tên dự án:
Đường dẫn repository/project:
Đường dẫn frontend:
Đường dẫn backend:
Stack frontend:
Stack backend:
Package manager:
Database/dev storage:
Có source code chưa: Có / Không
Có backend API chạy được chưa: Có / Không
Có frontend chạy được chưa: Có / Không
URL local frontend:
URL local backend/API:
Tài khoản test user:
Tài khoản test admin:
Có seed data không:
Command cài đặt:
Command chạy dev:
Command chạy test:
Command build:
```

Ví dụ:

```text
Tên dự án: quickpay
Đường dẫn project: D:\projects\quickpay
Frontend: D:\projects\quickpay\frontend
Backend: D:\projects\quickpay\backend
Frontend stack: React + Vite + TypeScript
Backend stack: Node.js + Express + Prisma + SQLite
Package manager: npm
URL frontend: http://localhost:5173
URL backend: http://localhost:3000
Test user: user@test.com / Password123
Test admin: admin@test.com / Admin123
Command:
- npm install
- npm run dev
- npm test
```

---

## Phạm vi kiểm thử QA dự kiến theo PRD

Sau khi có source code/môi trường, mình sẽ kiểm thử các nhóm sau:

### 1. Auth người dùng

- Đăng ký bằng email/số điện thoại.
- Kiểm tra trường bắt buộc.
- Password tối thiểu 8 ký tự.
- Tài khoản trùng hiển thị: `Tài khoản đã tồn tại`.
- Đăng nhập thành công/thất bại.
- Không rò rỉ password/token trong log/response.

### 2. OTP

- OTP đúng 6 chữ số.
- OTP hết hạn sau 5 phút.
- Sai quá 5 lần bị khóa 10 phút.
- Gửi lại OTP chỉ sau tối thiểu 60 giây.
- Message lỗi: `Mã OTP đã hết hạn`.

### 3. PIN giao dịch

- PIN đúng 6 chữ số.
- Nhập lại PIN phải khớp.
- Chặn PIN yếu:
  - `000000`
  - `111111`
  - `123456`
  - `654321`
- Nếu chưa thiết lập PIN thì không thể thanh toán.
- PIN không được trả về trong API response/log.

### 4. Trang chủ ví

- Hiển thị số dư.
- Format VND đúng dạng `1.000.000 ₫`.
- Hiển thị 5 giao dịch gần nhất.
- Trạng thái rỗng: `Bạn chưa có giao dịch nào`.
- Ẩn/hiện số dư.
- Khi ẩn hiển thị `******`.

### 5. QR Payment

- Quét/decode QR hợp lệ.
- QR không hợp lệ hiển thị: `Mã QR không hợp lệ`.
- QR có số tiền cố định thì không cho sửa số tiền.
- QR không có số tiền thì bắt buộc nhập số tiền.
- Min amount: `1.000 ₫`.
- Max amount mặc định: `50.000.000 ₫`.
- Màn hình xác nhận có đủ:
  - Người nhận/merchant
  - Số tiền
  - Phí nếu có
  - Tổng tiền
- Bắt buộc nhập PIN.
- Thành công hiển thị biên nhận.
- Thất bại hiển thị lý do.

### 6. Chuyển tiền nội bộ

- Nhập số điện thoại/email/ID người nhận.
- Người nhận không tồn tại hiển thị: `Không tìm thấy người nhận`.
- Không được chuyển cho chính mình.
- Kiểm tra số dư không đủ: `Số dư không đủ`.
- Thành công:
  - Trừ tiền người gửi.
  - Cộng tiền người nhận.
  - Tạo lịch sử cho cả hai bên.
  - Có mã tham chiếu duy nhất.
- Kiểm tra idempotency/chống giao dịch trùng.

### 7. Lịch sử giao dịch

- Sắp xếp mới nhất trước.
- Hiển thị đủ:
  - Mã giao dịch
  - Loại
  - Số tiền
  - Trạng thái
  - Thời gian
  - Đối tác
- Lọc theo:
  - Thời gian
  - Trạng thái
  - Loại giao dịch
- Không có kết quả hiển thị: `Không tìm thấy giao dịch phù hợp`.
- Kiểm tra phân trang mặc định tối đa 20 bản ghi/trang.

### 8. Chi tiết giao dịch

- Hiển thị đầy đủ thông tin giao dịch.
- User chỉ xem được giao dịch liên quan tới mình.
- Truy cập giao dịch không thuộc quyền phải bị từ chối.
- Biên nhận không chứa thông tin nhạy cảm.

### 9. Notification

- Người gửi nhận thông báo khi giao dịch thành công/thất bại/processing quá thời gian.
- Người nhận nhận thông báo khi nhận tiền.
- Notification không chứa PIN/token/thông tin bảo mật.
- Danh sách notification trong app hoạt động.

### 10. Admin Portal/API

- Admin login.
- Sai thông tin hiển thị: `Email hoặc mật khẩu không đúng`.
- Khóa admin sau 5 lần đăng nhập sai liên tiếp.
- Admin có role hợp lệ mới truy cập dashboard.
- Danh sách user.
- Tìm/lọc user.
- Không hiển thị PIN/password.
- Danh sách transaction.
- Tìm/lọc transaction.
- Không chỉnh sửa trực tiếp số tiền giao dịch đã hoàn tất.
- Hành động admin có audit log.

### 11. Non-functional/Security

- Password/PIN/OTP không lưu plain text.
- API nhạy cảm yêu cầu authentication.
- Payment API yêu cầu PIN.
- Token có thời hạn.
- Không log dữ liệu nhạy cảm:
  - Password
  - PIN
  - OTP
  - Access token
  - Refresh token
- Chống replay/idempotency cho API thanh toán.
- Kiểm tra response time cơ bản nếu có môi trường phù hợp.

---

## Báo cáo nghiệm thu sẽ tạo sau khi kiểm thử

Khi có source/môi trường, mình sẽ lập báo cáo theo template:

`verification-report-template.md`

Nội dung sẽ gồm:

```text
1. Thông tin build/môi trường
2. Danh sách test đã chạy
3. Kết quả Pass/Fail theo từng Acceptance Criteria
4. Log command:
   - install
   - build
   - test
   - dev
5. API response evidence
6. Console/browser errors nếu có
7. Bug list kèm repro steps
8. Kết luận nghiệm thu:
   - Accepted
   - Accepted with Issues
   - Rejected
```

---

## Kết luận hiện tại

**Trạng thái QA:** Blocked — chưa có source code, môi trường chạy, endpoint/API hoặc tài khoản test.

**Không thể xác nhận Acceptance Criteria tại thời điểm này.**

Vui lòng cung cấp repository/project path và hướng dẫn chạy local để mình bắt đầu kiểm thử và lập verification report.