Tôi sẽ kiểm tra cấu trúc project hiện tại để xác định frontend stack/thư mục được phép sửa, sau đó triển khai các route/UI và tích hợp API theo contract.Mình chưa nhận được **project path/thư mục làm việc cụ thể** nên hiện tại chưa thể tạo/sửa file frontend hoặc chạy build/dev server để cung cấp bằng chứng kiểm tra.

Vui lòng gửi thêm một trong các thông tin sau:

1. **Đường dẫn project frontend trên máy Windows**, ví dụ:
   ```text
   C:\Users\...\projects\online-shop\frontend
   ```
2. Hoặc cấu trúc thư mục hiện tại của repo, ví dụ:
   ```text
   online-shop/
     frontend/
     backend/
     docs/
   ```
3. Stack frontend đang dùng:
   - React/Vite?
   - Next.js?
   - Vue/Nuxt?
   - Angular?
   - Hay cần tạo mới frontend từ đầu?

Sau khi có project path, mình sẽ triển khai trong frontend:

- Public routes:
  - `/`
  - `/products/:id`
  - `/cart`
  - `/checkout`
  - `/order-success/:id`

- Admin routes:
  - `/admin/login`
  - `/admin`
  - `/admin/products`
  - `/admin/products/new`
  - `/admin/products/:id/edit`
  - `/admin/orders`
  - `/admin/orders/:id`

- Tích hợp API đúng contract:
  - `GET /api/products`
  - `GET /api/products/:id`
  - `POST /api/orders`
  - `POST /api/admin/login`
  - `POST /api/admin/logout`
  - `GET /api/admin/me`
  - `GET/POST/PATCH /api/admin/products`
  - `GET/PATCH /api/admin/orders`

- Giỏ hàng dùng `localStorage` key:
  ```text
  mvp_shop_cart
  ```

- Sau khi xong sẽ cung cấp bằng chứng:
  - Lệnh install/build đã chạy.
  - Kết quả build OK.
  - Dev server live.
  - Ghi chú các flow đã kiểm tra thủ công.