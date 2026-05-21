## PM Orchestrator — Tiếp nhận dự án `web-project`

Mình đã nhận brief:

- **Project:** `web-project`
- **Sản phẩm:** Ứng dụng thanh toán nhanh / QuickPay
- **Trạng thái QA hiện tại:** `Blocked`
- **Lý do block:** Chưa có source code, repository path, môi trường chạy, API endpoint, tài khoản test hoặc hướng dẫn cài đặt/chạy.

Hiện tại QA **chưa thể nghiệm thu** là đúng quy trình, vì chưa có bằng chứng thực thi để kiểm thử Acceptance Criteria.

---

# 1. Kết luận điều phối hiện tại

Dự án đang ở trạng thái:

```text
Phase: Pre-Implementation / Environment Discovery
Status: Blocked for QA
Blocking reason: Missing repository/source/runtime information
```

Chưa thể chuyển sang Wave 3 — QA Verification cho đến khi có một trong hai hướng sau:

## Hướng A — Đã có source code

Bạn cung cấp thông tin repository/project path và command chạy local.

## Hướng B — Chưa có source code

Mình sẽ khởi động quy trình xây dựng từ đầu:

1. Product Agent tạo PRD chi tiết.
2. Architecture Agent tạo Technical Spec/API Contract.
3. Backend Agent xây API.
4. Frontend Agent xây UI.
5. QA Agent kiểm thử sau khi có build chạy được.

---

# 2. Thông tin cần bạn xác nhận

Vui lòng chọn một trong hai phương án:

## Phương án A — Đã có source code

Gửi thông tin theo mẫu sau:

```text
Tên dự án:
Đường dẫn repository/project:
Đường dẫn frontend:
Đường dẫn backend:
Stack frontend:
Stack backend:
Package manager:
Database/dev storage:
Có source code chưa: Có
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

Ví dụ Windows Native:

```text
Tên dự án: web-project
Đường dẫn project: D:\Antigravity\LeeJ_MultiAgent\projects\active\web-project
Frontend: D:\Antigravity\LeeJ_MultiAgent\projects\active\web-project\frontend
Backend: D:\Antigravity\LeeJ_MultiAgent\projects\active\web-project\backend
Frontend stack: React + Vite + TypeScript
Backend stack: Node.js + Express + SQLite
Package manager: npm
URL frontend: http://localhost:5173
URL backend: http://localhost:3000
Test user: user@test.com / Password123
Test admin: admin@test.com / Admin123
Command cài đặt:
- npm install
Command chạy dev:
- npm run dev
Command test:
- npm test
Command build:
- npm run build
```

Sau khi có thông tin này, mình sẽ điều phối QA chạy kiểm thử và tạo:

```text
verification-report.md
```

---

## Phương án B — Chưa có source code

Nếu chưa có source code, mình đề xuất tạo mới dự án theo stack mặc định an toàn:

```text
Project name: web-project
Product name: QuickPay
Frontend: React + Vite + TypeScript
Backend: Node.js + Express + TypeScript
Database/dev storage: SQLite
Package manager: npm
Runtime: Windows Native PowerShell/CMD
```

Cấu trúc đề xuất:

```text
web-project/
  docs/
    prd.md
    technical-spec.md
    api-contract.md
    acceptance-criteria.md
    verification-report-template.md
  frontend/
  backend/
  qa/
    test-plan.md
    verification-report.md
  final-report.md
```

---

# 3. Phạm vi sản phẩm QuickPay sẽ được quản lý

Dựa trên QA checklist bạn gửi, phạm vi chức năng chính gồm:

## User App

1. Đăng ký / đăng nhập.
2. OTP.
3. Thiết lập PIN giao dịch.
4. Trang chủ ví.
5. Thanh toán QR.
6. Chuyển tiền nội bộ.
7. Lịch sử giao dịch.
8. Chi tiết giao dịch.
9. Notification.

## Admin Portal/API

1. Admin login.
2. Dashboard.
3. Quản lý user.
4. Quản lý transaction.
5. Audit log.
6. Phân quyền admin.

## Security / Non-functional

1. Không lưu password/PIN/OTP plain text.
2. Không log dữ liệu nhạy cảm.
3. API nhạy cảm yêu cầu authentication.
4. Payment API yêu cầu PIN.
5. Token có thời hạn.
6. Idempotency cho giao dịch.
7. Kiểm tra quyền truy cập transaction.

---

# 4. Quality Gate hiện tại

## Gate QA-01 — Environment Readiness

```text
Status: Failed / Blocked
Reason:
- Chưa có repository path
- Chưa có source code xác nhận
- Chưa có command install/build/test
- Chưa có URL frontend/backend
- Chưa có test account
```

Điều kiện để mở khóa QA:

```text
[ ] Có project path hợp lệ trên Windows
[ ] Có frontend/backend source code
[ ] Có hướng dẫn install
[ ] Có hướng dẫn chạy dev
[ ] Có hướng dẫn build
[ ] Có hướng dẫn test
[ ] Có API base URL
[ ] Có tài khoản test user/admin hoặc seed data
```

---

# 5. Quyết định cần từ bạn

Vui lòng trả lời một trong hai lựa chọn:

## Nếu đã có source

Gửi:

```text
Chọn A — Đã có source code

Tên dự án:
Đường dẫn project:
Frontend path:
Backend path:
Stack:
Package manager:
Commands:
URL local:
Test accounts:
```

## Nếu muốn mình triển khai từ đầu

Gửi:

```text
Chọn B — Tạo mới dự án QuickPay từ đầu

Đồng ý stack mặc định:
- React + Vite + TypeScript
- Node.js + Express + TypeScript
- SQLite
- npm

Hoặc thay stack bằng:
...
```

Sau khi bạn xác nhận, mình sẽ bắt đầu điều phối theo đúng workflow:

```text
Wave 1: Product + Architecture
Wave 2: Frontend + Backend
Wave 3: QA Verification
Wave 4: Final Report
```