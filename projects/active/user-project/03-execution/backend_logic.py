Mình sẽ kiểm tra cấu trúc project hiện tại để xác định stack backend và chỉ chỉnh trong thư mục `backend`.Cần bạn cung cấp **project path / repository hiện tại** hoặc cho phép mình truy cập danh sách file trong workspace để triển khai backend.

Theo PRD/Spec, mình sẽ chỉ thao tác trong thư mục `backend` và triển khai các nhóm chính:

- Public APIs:
  - `GET /api/products`
  - `GET /api/products/:id`
  - `POST /api/orders`
- Admin Auth:
  - `POST /api/admin/login`
  - `POST /api/admin/logout`
  - `GET /api/admin/me`
- Admin Products:
  - `GET /api/admin/products`
  - `POST /api/admin/products`
  - `GET /api/admin/products/:id`
  - `PATCH /api/admin/products/:id`
- Admin Orders:
  - `GET /api/admin/orders`
  - `GET /api/admin/orders/:id`
  - `PATCH /api/admin/orders/:id/status`

Sau khi có project path, mình sẽ:

1. Kiểm tra stack backend hiện có.
2. Thiết kế database schema theo contract.
3. Seed admin mặc định.
4. Implement validation, auth, business rules.
5. Chạy server/test API cục bộ.
6. Trả lại evidence: log server hoặc kết quả gọi API.