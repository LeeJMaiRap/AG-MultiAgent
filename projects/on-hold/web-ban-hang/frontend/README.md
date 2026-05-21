# Web Bán Hàng - Frontend

React + Vite + Tailwind CSS + Axios

## Cài đặt

```bash
npm install
```

## Chạy development server

```bash
npm run dev
```

Server sẽ chạy tại http://localhost:3000

## Build production

```bash
npm run build
```

## Cấu trúc thư mục

```
frontend/
├── public/          # Static assets
├── src/
│   ├── main.jsx    # Entry point
│   ├── App.jsx     # Root component
│   └── index.css   # Tailwind imports
├── index.html
├── vite.config.js
├── tailwind.config.js
└── package.json
```

## API Proxy

Vite đã được cấu hình để proxy `/api` requests tới `http://localhost:5000`
