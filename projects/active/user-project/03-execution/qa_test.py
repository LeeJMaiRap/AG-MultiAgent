## QA Verification Status: BLOCKED

Hiện tại QA **chưa thể tiến hành kiểm thử/ nghiệm thu** các Acceptance Criteria trong PRD vì chưa có đủ thông tin để truy cập và chạy hệ thống local.

### Lý do bị chặn

Chưa có:

1. **Project path / repository path**
2. Thông tin cấu trúc thư mục frontend/backend
3. Hướng dẫn chạy ứng dụng local
4. Thông tin seed data / tài khoản admin mặc định
5. URL dev server hoặc API base URL

Do đó QA chưa thể:

- Chạy frontend/backend
- Thực hiện smoke test
- Gọi API kiểm thử
- Kiểm tra UI flow khách hàng/admin
- Kiểm tra bảo mật admin
- Tạo báo cáo nghiệm thu có bằng chứng log/API response/console error

---

## Thông tin cần cung cấp để QA tiếp tục

Vui lòng gửi các thông tin sau:

### 1. Project path trên Windows

Ví dụ:

```text
D:\Antigravity\projects\online-shop
```

Hoặc:

```text
C:\Users\<user>\Documents\online-shop
```

### 2. Cấu trúc thư mục repo

Ví dụ:

```text
online-shop/
  frontend/
  backend/
  README.md
```

### 3. Lệnh chạy frontend/backend

Ví dụ:

```bash
cd frontend
npm install
npm run dev
```

```bash
cd backend
npm install
npm run dev
```

### 4. Thông tin môi trường

Nếu có file `.env.example`, cần biết:

- Database dùng gì?
- Port backend?
- Port frontend?
- API base URL?
- Có cần migration/seed không?

### 5. Tài khoản admin test

Ví dụ:

```text
Email: admin@example.com
Password: admin123
```

### 6. Dữ liệu seed sản phẩm

Cần có ít nhất:

- 1 sản phẩm còn hàng
- 1 sản phẩm hết hàng
- 1 sản phẩm bị ẩn

Để kiểm thử các flow trong PRD.

---

## Kế hoạch kiểm thử sau khi có project path

QA sẽ kiểm thử theo các nhóm sau:

### Smoke Test

- Khách hàng xem danh sách sản phẩm
- Khách hàng xem chi tiết sản phẩm
- Khách hàng thêm sản phẩm vào giỏ
- Khách hàng checkout thành công
- Admin đăng nhập
- Admin thấy đơn hàng mới
- Admin cập nhật trạng thái đơn hàng

### Functional Test

- F-001: Danh sách sản phẩm
- F-002: Chi tiết sản phẩm
- F-003: Giỏ hàng
- F-004: Đặt hàng
- F-005: Đăng nhập admin
- F-006: Quản lý sản phẩm
- F-007: Quản lý đơn hàng

### Security Test

- Truy cập admin khi chưa đăng nhập
- Gọi API admin không có quyền
- Kiểm tra backend tự tính tổng tiền
- Kiểm tra mật khẩu admin không lưu plain text nếu có quyền xem DB/source config

### Responsive Test

Kiểm tra các viewport:

```text
360px mobile
768px tablet
1366px desktop
```

---

## Trạng thái báo cáo nghiệm thu

Chưa thể tạo báo cáo hoàn chỉnh theo `verification-report-template.md` vì chưa có evidence thực tế.

Trạng thái hiện tại:

```text
Verification Result: BLOCKED
Reason: Missing project path and runnable environment details
```

Vui lòng cung cấp project path và hướng dẫn chạy để QA bắt đầu kiểm thử.