# Tech Stack & Architecture: Web Bán Acc Game

## Tech Stack (Simple & Fast)

### Frontend
- **Framework:** Next.js 14 (App Router)
- **Styling:** Tailwind CSS
- **UI Components:** shadcn/ui (optional, hoặc custom)
- **Image:** Next/Image với Cloudinary hoặc local

### Backend
- **API:** Next.js API Routes
- **Auth:** NextAuth.js hoặc simple JWT
- **Validation:** Zod

### Database
- **Option 1 (Recommended):** SQLite + Prisma
  - Pros: Zero config, fast setup, portable
  - Cons: Single file, không scale lớn (OK cho MVP)
  
- **Option 2:** MongoDB + Mongoose
  - Pros: Flexible schema, cloud-ready
  - Cons: Cần MongoDB Atlas hoặc local instance

**Decision:** SQLite + Prisma (nhanh nhất cho 2 ngày)

### Storage
- **Images:** Cloudinary (free tier) hoặc Vercel Blob
- **Fallback:** Local public folder (đơn giản nhất)

### Deployment
- **Hosting:** Vercel (zero-config, auto CI/CD)
- **Domain:** Vercel subdomain hoặc custom

## Architecture

```
web-ban-acc-game/
├── app/
│   ├── (public)/
│   │   ├── page.tsx              # Trang chủ - danh sách acc
│   │   ├── acc/[id]/page.tsx     # Chi tiết acc
│   │   └── layout.tsx            # Public layout
│   ├── admin/
│   │   ├── login/page.tsx        # Admin login
│   │   ├── dashboard/page.tsx    # Admin dashboard
│   │   ├── accs/page.tsx         # Quản lý acc list
│   │   ├── accs/new/page.tsx     # Thêm acc mới
│   │   ├── accs/[id]/edit/page.tsx # Sửa acc
│   │   └── layout.tsx            # Admin layout (protected)
│   ├── api/
│   │   ├── accs/route.ts         # GET /api/accs, POST /api/accs
│   │   ├── accs/[id]/route.ts    # GET/PUT/DELETE /api/accs/:id
│   │   ├── auth/login/route.ts   # POST /api/auth/login
│   │   └── upload/route.ts       # POST /api/upload (image)
│   └── layout.tsx                # Root layout
├── components/
│   ├── AccCard.tsx               # Card hiển thị acc
│   ├── AccFilter.tsx             # Bộ lọc game
│   ├── AdminNav.tsx              # Admin navigation
│   └── ...
├── lib/
│   ├── db.ts                     # Prisma client
│   ├── auth.ts                   # Auth helpers
│   └── utils.ts                  # Utilities
├── prisma/
│   ├── schema.prisma             # Database schema
│   └── seed.ts                   # Seed data
├── public/
│   └── uploads/                  # Local images (nếu không dùng Cloudinary)
└── package.json
```

## Database Schema (Prisma)

```prisma
model Acc {
  id          String   @id @default(cuid())
  game        String   // Tên game
  title       String   // Tiêu đề acc
  rank        String?  // Rank/level
  description String?  // Mô tả chi tiết
  price       Int      // Giá (VND)
  images      String[] // Array URL ảnh
  status      String   @default("available") // available | sold
  contactPhone String? // SĐT liên hệ
  contactFB    String? // Facebook link
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

model Admin {
  id       String @id @default(cuid())
  username String @unique
  password String // Hashed
}
```

## API Endpoints

### Public
- `GET /api/accs` - Lấy danh sách acc (query: game, search)
- `GET /api/accs/:id` - Chi tiết 1 acc

### Admin (Protected)
- `POST /api/auth/login` - Đăng nhập admin
- `POST /api/accs` - Tạo acc mới
- `PUT /api/accs/:id` - Cập nhật acc
- `DELETE /api/accs/:id` - Xóa acc
- `POST /api/upload` - Upload ảnh

## Security
- Admin routes protected bằng middleware
- Password hashed với bcrypt
- Input validation với Zod
- CSRF protection (Next.js built-in)
- Rate limiting (optional, nếu có thời gian)

## Performance
- Next.js Image optimization
- Static generation cho public pages (ISR)
- API caching cơ bản
- Lazy loading images

## Deployment Checklist
- [ ] Environment variables (.env.local → Vercel env)
- [ ] Database migration (Prisma migrate)
- [ ] Seed admin account
- [ ] Test production build locally
- [ ] Deploy to Vercel
- [ ] Verify all routes work
- [ ] Test admin login production
- [ ] Test image upload production

---

**Estimated setup time:** 1-2h
**Estimated total dev time:** 16-18h
**Buffer:** 2-4h for bugs/polish
**Total:** Fits in 2 days
