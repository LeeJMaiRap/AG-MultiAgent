# Project Plan: Web Bán Acc Game

## Timeline: 2 Days (2026-05-16 to 2026-05-18)

## Day 1: 2026-05-16 (Today)

### Morning (3h) - Initiation & Planning ✅
- [x] Charter created
- [x] Requirements documented
- [x] Tech stack decided
- [x] Task board created
- [x] Project registered

### Afternoon (4h) - Foundation & Backend
- [ ] **TASK-001:** Setup Next.js project (1h)
  - Init Next.js 14 with App Router
  - Install dependencies (Prisma, Tailwind, Zod, bcrypt)
  - Setup folder structure
  
- [ ] **TASK-002:** Database setup (1h)
  - Prisma schema for Acc & Admin
  - SQLite database init
  - Migrations
  
- [ ] **TASK-003:** Backend API - CRUD acc (2h)
  - GET /api/accs (list with filters)
  - GET /api/accs/:id (detail)
  - POST /api/accs (admin)
  - PUT /api/accs/:id (admin)
  - DELETE /api/accs/:id (admin)

### Evening (3h) - Frontend Public
- [ ] **TASK-005:** Public listing page (2h)
  - Homepage with acc grid
  - Filter by game
  - Search basic
  - Responsive layout
  
- [ ] **TASK-006:** Acc detail page (1h)
  - Detail view
  - Image gallery
  - Contact CTA (phone/FB)

## Day 2: 2026-05-17

### Morning (4h) - Admin Panel
- [ ] **TASK-004:** Admin authentication (1.5h)
  - Login page
  - JWT/session
  - Middleware protection
  
- [ ] **TASK-007:** Admin dashboard (1.5h)
  - Dashboard layout
  - Acc list table
  - Navigation
  
- [ ] **TASK-008:** Admin CRUD UI (1h)
  - Create acc form
  - Edit acc form
  - Image upload UI

### Afternoon (3h) - Polish & Testing
- [ ] **TASK-010:** Image upload implementation (1.5h)
  - Cloudinary integration or local storage
  - Upload endpoint
  - Image preview
  
- [ ] **TASK-011:** Responsive polish (1h)
  - Mobile optimization
  - UI/UX improvements
  
- [ ] **TASK-014:** Seed data (0.5h)
  - Create 10-20 sample accs

### Evening (2h) - Deploy & Closure
- [ ] **TASK-012:** Testing & bug fixes (1h)
  - End-to-end testing
  - Fix critical bugs
  
- [ ] **TASK-013:** Deploy (1h)
  - Deploy to Vercel
  - Environment setup
  - Production testing
  - Final verification

## Risk Mitigation

### R-001: Timeline too tight
- **Mitigation:** Use simple stack (Next.js + SQLite), skip non-essential features
- **Contingency:** Extend to 2.5 days if needed

### R-002: Image upload complexity
- **Mitigation:** Start with local storage, upgrade to Cloudinary if time permits
- **Contingency:** Use placeholder images for demo

### R-003: Admin auth security
- **Mitigation:** Use proven patterns (NextAuth or simple JWT)
- **Contingency:** Basic auth with strong password for MVP

### R-004: Responsive design time
- **Mitigation:** Use Tailwind responsive utilities from start
- **Contingency:** Focus on mobile-first, desktop as enhancement

## Success Metrics
- [ ] Website deployed and accessible
- [ ] Public can view acc list
- [ ] Public can filter by game
- [ ] Public can view acc detail with contact info
- [ ] Admin can login
- [ ] Admin can CRUD accs
- [ ] Images display correctly
- [ ] Responsive on mobile + desktop
- [ ] No critical bugs

## Approval
- [ ] Owner confirms plan
- [ ] Ready to start execution

---

**Total estimated time:** 19h
**Available time:** 2 days × 10h = 20h
**Buffer:** 1h
**Status:** Feasible ✅
