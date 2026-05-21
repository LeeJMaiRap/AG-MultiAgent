# 🚀 Hướng Dẫn Chạy Demo - Web Bán Hàng

## Chuẩn Bị

### 1. Backend Setup
```bash
cd projects/active/web-ban-hang/backend

# Copy .env từ .env.example
cp .env.example .env

# Cài dependencies
npm install

# Khởi chạy server
npm run dev
```
Server sẽ chạy tại `http://localhost:5000`

**Lưu ý:** Backend sử dụng mock data (không cần MongoDB thực). Health check: `curl http://localhost:5000/health`

### 2. Frontend Setup
```bash
cd projects/active/web-ban-hang/frontend

# Copy .env từ .env.example
cp .env.example .env

# Cài dependencies
npm install

# Khởi chạy dev server
npm run dev
```
Frontend sẽ chạy tại `http://localhost:3000`

## Kiểm Tra Build

### Build Frontend
```bash
cd projects/active/web-ban-hang/frontend
npm run build
```
Output: `dist/` folder (4.4 KB HTML + assets)

### Verify Backend
```bash
cd projects/active/web-ban-hang/backend
node --check server.js
```

## Tính Năng Demo

- ✅ Responsive design (mobile + desktop)
- ✅ Tailwind CSS styling
- ✅ Mock data integration
- ✅ API routes: `/api/auth`, `/api/products`, `/api/cart`, `/api/orders`
- ✅ Health check endpoint: `/health`

## Troubleshooting

| Vấn đề | Giải pháp |
|--------|----------|
| Port 5000 đã dùng | Thay `PORT` trong `.env` backend |
| Port 3000 đã dùng | Vite sẽ tự chọn port khác |
| Module not found | Chạy `npm install` lại |
| CORS error | Kiểm tra `CLIENT_URL` trong backend `.env` |

## Cấu Trúc Dự Án

```
web-ban-hang/
├── backend/
│   ├── config/          # Database config
│   ├── controllers/      # Business logic
│   ├── models/          # Data models
│   ├── routes/          # API routes
│   ├── middleware/      # Auth, validation
│   ├── seed/            # Mock data
│   └── server.js        # Entry point
├── frontend/
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── pages/       # Page components
│   │   ├── App.jsx      # Root component
│   │   └── main.jsx     # Entry point
│   ├── dist/            # Build output
│   └── vite.config.js   # Vite config
└── DEMO_GUIDE.md        # This file
```

## Chạy Cùng Lúc (Terminal Riêng)

**Terminal 1 - Backend:**
```bash
cd projects/active/web-ban-hang/backend && npm run dev
```

**Terminal 2 - Frontend:**
```bash
cd projects/active/web-ban-hang/frontend && npm run dev
```

Mở browser: `http://localhost:3000`
