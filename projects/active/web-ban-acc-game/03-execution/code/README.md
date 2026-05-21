# Web Bán Acc Game

Vị trí code trong workspace PM Agent:
`projects/active/web-ban-acc-game/03-execution/code/`

Ứng dụng web bán tài khoản game sử dụng Next.js 16 (App Router) và SQLite.

## Tính năng

- **Trang chủ công khai**: Danh sách tài khoản game với bộ lọc theo game và tìm kiếm
- **Trang chi tiết**: Xem thông tin chi tiết tài khoản và liên hệ
- **Quản trị viên**: Đăng nhập và xem danh sách tài khoản (bảo vệ bằng JWT session)

## Công nghệ

- Next.js 16 (App Router)
- TypeScript
- Tailwind CSS 4
- better-sqlite3 (không dùng Prisma)
- bcryptjs (mã hóa mật khẩu)
- jsonwebtoken (xác thực admin)

## Cài đặt và chạy

### 1. Cài đặt dependencies

```bash
npm install
```

### 2. Khởi tạo database

```bash
npm run init-db
```

Script này sẽ:
- Tạo thư mục `data/` và file `app.db`
- Tạo bảng `admins` và `accs`
- Seed 1 admin: `admin` / `admin123`
- Seed 6 tài khoản game mẫu (Kingdom Story, Liên Minh Huyền Thoại, PUBG)

### 3. Chạy development server

```bash
npm run dev
```

Mở [http://localhost:3000](http://localhost:3000) để xem trang chủ.

### 4. Đăng nhập quản trị

Truy cập [http://localhost:3000/admin/login](http://localhost:3000/admin/login)

- **Username**: `admin`
- **Password**: `admin123`

## Cấu trúc thư mục

```
├── app/
│   ├── page.tsx              # Trang chủ (danh sách acc)
│   ├── acc/[id]/page.tsx     # Trang chi tiết acc
│   ├── admin/
│   │   ├── login/page.tsx    # Trang đăng nhập admin
│   │   └── page.tsx          # Dashboard admin
│   ├── layout.tsx            # Root layout
│   └── globals.css           # Global styles
├── lib/
│   ├── db.ts                 # SQLite helper
│   └── auth.ts               # JWT authentication
├── scripts/
│   └── init-db.ts            # Database initialization script
└── data/
    └── app.db                # SQLite database (tạo sau khi chạy init-db)
```

## Database Schema

### Table: admins
- `id` INTEGER PRIMARY KEY
- `username` TEXT UNIQUE
- `password_hash` TEXT
- `created_at` DATETIME

### Table: accs
- `id` INTEGER PRIMARY KEY
- `game` TEXT
- `title` TEXT
- `description` TEXT
- `price` REAL
- `contact_phone` TEXT
- `contact_facebook` TEXT
- `image_url` TEXT
- `status` TEXT (available/sold)
- `created_at` DATETIME

## Thông tin liên hệ mẫu

Tất cả tài khoản mẫu sử dụng:
- **Điện thoại**: 0705460062
- **Facebook**: https://www.facebook.com/doanhnt.274

## Build cho production

```bash
npm run build
npm start
```

## Lưu ý bảo mật

- Đổi `JWT_SECRET` trong file `.env` cho production
- Đổi mật khẩu admin mặc định sau khi triển khai
- File `data/app.db` chứa dữ liệu thực, cần backup định kỳ
