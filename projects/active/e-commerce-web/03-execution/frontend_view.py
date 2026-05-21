<tool_use? need actual tools namespace? none listed. In this environment maybe no tools. We can ask? But expected modify. We need provide unable? Usually no tools but can give instructions. However maybe use shell? Not available. Final should state need repo access. But maybe we can still craft implementation? Need be honest.Mình đã nhận PRD + Architecture/API Contract handoff cho vai trò **Frontend Agent**.

Tuy nhiên trong phiên hiện tại mình **chưa có quyền/tool truy cập filesystem hoặc terminal** để:

- Inspect cấu trúc frontend hiện có.
- Tạo/sửa file trong các owned paths.
- Chạy `npm install`, `npm run dev`, `npm run build`.
- Cung cấp bằng chứng build/dev server live.

Để mình triển khai đúng vai trò Frontend Agent, vui lòng cung cấp một trong các lựa chọn sau:

1. **Bật quyền workspace tools** như đọc/ghi file và chạy terminal; hoặc  
2. Gửi cấu trúc project hiện tại, đặc biệt:
   - Framework đang dùng: Next.js / React / Vite?
   - Cây thư mục frontend.
   - `package.json`.
   - Các file hiện có trong `src/app`, `src/pages`, `src/components`, `src/lib`, `src/styles`.

Sau khi có quyền hoặc thông tin repo, mình sẽ thực hiện các task frontend theo API Contract:

- FE-001 Product listing page — `GET /api/products`
- FE-002 Product detail page — `GET /api/products/{slug}`
- FE-003 Cart UI — `GET /api/cart`, `POST/PATCH/DELETE /api/cart/items`
- FE-004 Checkout form — `POST /api/orders`
- FE-005 Order confirmation page — `GET /api/orders/{orderId}`

Và sẽ báo cáo kèm evidence:

```txt
npm run build: OK
dev server: live
frontend files changed: ...
API integration: follows docs/api-contract.md
```