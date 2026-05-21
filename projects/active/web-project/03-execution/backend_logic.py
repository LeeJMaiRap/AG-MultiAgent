Tôi sẽ kiểm tra cấu trúc dự án hiện tại để xác định thư mục `backend` và công nghệ đang dùng, sau đó chỉ tạo/sửa file trong phạm vi backend.Mình cần quyền xem cấu trúc repository hoặc bạn cung cấp cây thư mục hiện tại để triển khai đúng trong thư mục `backend`.

Hiện tại bạn mới cung cấp PRD và Technical/API Contract, nhưng chưa có:

- Stack backend hiện có: Node/Nest/Express, Python/FastAPI, Java/Spring, .NET, v.v.
- Cấu trúc thư mục dự án.
- File package/config hiện tại.
- Database đang dùng local/dev.
- Có sẵn thư mục `backend` hay cần tạo mới.

Để tiếp tục đúng vai trò Backend Agent và không sửa ngoài phạm vi, vui lòng cung cấp một trong hai cách sau:

```text
1. Cây thư mục repository hiện tại
2. Nội dung thư mục backend nếu đã có
3. Stack mong muốn nếu chưa có backend
```

Ví dụ:

```text
backend/
  package.json
  src/
  prisma/
```

hoặc xác nhận:

```text
Backend chưa có, hãy tạo mới trong thư mục backend bằng Node.js + Express + Prisma + SQLite/PostgreSQL.
```

Sau khi có thông tin này, mình sẽ triển khai các API MVP theo contract:

- Auth register/login/refresh/logout
- OTP request/verify
- Transaction PIN
- Wallet
- QR decode
- Transfer/QR transaction + confirm PIN + idempotency
- Transaction history/detail/receipt
- Notifications
- Admin users/transactions
- Audit log
- Hash password/PIN/OTP
- Validation + RBAC + error format chuẩn
- Script migrate/seed/test API evidence trong backend.