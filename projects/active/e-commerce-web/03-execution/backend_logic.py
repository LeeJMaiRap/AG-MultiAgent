Tôi sẽ kiểm tra cấu trúc dự án/backend hiện có, sau đó triển khai các API theo contract trong phạm vi backend và chạy kiểm thử cục bộ để cung cấp evidence.Không thể tiếp tục triển khai trực tiếp vì trong phiên này không có quyền truy cập công cụ đọc/ghi/chạy lệnh trên filesystem ngoài nội dung tài liệu bạn đã cung cấp.

Theo vai trò **Backend Agent**, bước tiếp theo khi có quyền repo sẽ là:

1. Kiểm tra cấu trúc dự án:
   - `backend/**`
   - hoặc các path backend được task-board cho phép như:
     - `src/api/**`
     - `src/server/**`
     - `src/modules/**`
     - `src/lib/db/**`
     - `prisma/**`
     - `database/**`

2. Triển khai các nhóm API theo contract:

   ```txt
   GET    /api/products
   GET    /api/products/:slug

   GET    /api/cart
   POST   /api/cart/items
   PATCH  /api/cart/items/:itemId
   DELETE /api/cart/items/:itemId

   POST   /api/orders
   GET    /api/orders/:orderId
   ```

3. Triển khai database/migration/seed:
   - `categories`
   - `products`
   - `carts`
   - `cart_items`
   - `orders`
   - `order_items`

4. Bảo mật và validation:
   - Validate `X-Session-Id`.
   - Validate `quantity > 0`.
   - Không nhận giá từ client.
   - Chỉ lấy giá từ product DB.
   - Kiểm tra product active.
   - Kiểm tra cart thuộc session hiện tại.
   - Error response theo contract:

   ```json
   {
     "error": {
       "code": "VALIDATION_ERROR",
       "message": "Invalid request payload",
       "details": []
     }
   }
   ```

5. Evidence cần cung cấp sau khi có quyền chạy:
   - Log server start thành công.
   - Kết quả gọi API bằng curl/Postman/test runner, ví dụ:
     - list products trả `200`
     - add cart item trả `200`
     - checkout trả `201`
     - invalid quantity trả `422`

Hiện trạng:

```txt
Backend Implementation Status: BLOCKED
Reason: No filesystem/tool access available in this chat turn
Required Next Step: Provide repository access/tools or paste backend project structure/files
```