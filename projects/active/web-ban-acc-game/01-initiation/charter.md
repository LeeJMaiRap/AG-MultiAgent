# Project Charter: Web Bán Acc Game

## 1. Thông tin cơ bản
- **Tên dự án:** Web Bán Acc Game
- **Mã dự án:** WBAG-2026-05-16
- **Ngày khởi tạo:** 2026-05-16
- **PM Agent:** Lệ
- **Sponsor/Owner:** Nguyễn Thành Doanh

## 2. Mục tiêu dự án (SMART)
- **Specific:** Xây dựng trang web bán tài khoản game đa dạng với tính năng xem danh sách, mua acc, và admin CRUD
- **Measurable:** Website chạy được, khách xem acc → chọn → liên hệ mua, admin quản lý được acc
- **Achievable:** Trong 2 ngày với stack đơn giản
- **Relevant:** Đáp ứng nhu cầu kinh doanh acc game của anh
- **Time-bound:** Hoàn thành trong 2 ngày (deadline: 2026-05-18)

## 3. Phạm vi dự án
### In-scope (Trong phạm vi)
- **Frontend khách:**
  - Trang chủ hiển thị danh sách acc game
  - Lọc theo loại game
  - Xem chi tiết acc (rank, skin, giá, thông tin liên hệ)
  - Không cần đăng ký/đăng nhập
  - Hiển thị thông tin liên hệ (SĐT / Facebook) để mua
  - Responsive (mobile + desktop)

- **Admin panel:**
  - Đăng nhập admin
  - CRUD acc game (Create, Read, Update, Delete)
  - Upload hình ảnh acc
  - Quản lý thông tin: loại game, rank, skin, giá, mô tả, trạng thái (còn/hết)

- **Backend:**
  - API CRUD acc
  - Authentication admin
  - Database lưu trữ acc

- **Tech stack đơn giản:**
  - Frontend: Next.js (React) hoặc HTML/CSS/JS thuần
  - Backend: Node.js + Express hoặc Next.js API routes
  - Database: SQLite hoặc MongoDB
  - Hosting: Vercel/Netlify (deploy nhanh)

### Out-of-scope (Ngoài phạm vi)
- Hệ thống thanh toán tự động
- Đăng ký/đăng nhập khách hàng
- Chat trực tuyến
- Hệ thống đánh giá/review
- Quản lý đơn hàng phức tạp
- Email marketing

## 4. Success Criteria (Tiêu chí thành công)
- Website chạy được trên trình duyệt
- Khách xem được danh sách acc game
- Khách lọc được theo loại game
- Khách xem chi tiết acc và thông tin liên hệ
- Admin đăng nhập được
- Admin CRUD được acc (thêm/sửa/xóa/xem)
- Giao diện đơn giản, sạch sẽ, responsive
- Deploy lên hosting public
- Không có lỗi critical

## 5. Stakeholders
| Vai trò | Tên | Trách nhiệm |
|---------|-----|-------------|
| Owner | Nguyễn Thành Doanh | Xác nhận yêu cầu, phê duyệt scope, nghiệm thu |
| PM Agent | Lệ | Quản lý dự án, lập kế hoạch, điều phối |
| Developer | Lệ (hoặc worker agent) | Thực thi code, deploy |

## 6. Constraints (Ràng buộc)
- **Timeline:** 2 ngày (48 giờ)
- **Budget:** Không xác định (dự án cá nhân)
- **Technology:** Stack đơn giản, dễ deploy
- **Resources:** 1 developer (PM Agent hoặc worker)

## 7. Assumptions (Giả định)
- Anh sẽ cung cấp thông tin acc mẫu để test
- Không cần tích hợp thanh toán tự động
- Khách liên hệ trực tiếp qua SĐT/Facebook
- Hosting miễn phí hoặc chi phí thấp (Vercel/Netlify)

## 8. Rủi ro sơ bộ
- **R-001:** Timeline 2 ngày có thể chặt nếu gặp vấn đề kỹ thuật
- **R-002:** Upload hình ảnh có thể cần storage service (Cloudinary/S3)
- **R-003:** Admin authentication cần bảo mật tốt
- **R-004:** Responsive design có thể tốn thời gian

## 9. High-level Timeline
- **Day 1 (2026-05-16):**
  - Morning: Initiation + Planning (requirements, spec, plan)
  - Afternoon: Execution start (setup project, database, basic CRUD)
  - Evening: Frontend khách (danh sách acc, chi tiết)
  
- **Day 2 (2026-05-17):**
  - Morning: Admin panel (CRUD UI)
  - Afternoon: Polish UI, responsive, testing
  - Evening: Deploy, final testing, closure

## 10. Phê duyệt
- [ ] Đã được owner xác nhận scope
- [ ] Đã được PM Agent phân tích
- [ ] Sẵn sàng chuyển sang giai đoạn Planning

---

**Next steps:**
1. Owner xác nhận charter này
2. PM Agent tạo requirements chi tiết
3. Bắt đầu planning phase
