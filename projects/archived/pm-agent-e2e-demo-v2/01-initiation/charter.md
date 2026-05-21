# Project Charter: Hệ thống quản lý công việc nội bộ

## 1. Thông tin cơ bản
- **Tên dự án:** Hệ thống quản lý công việc nội bộ
- **Mã dự án:** PMD-2026-05-14-V2
- **Ngày khởi tạo:** 2026-05-14
- **PM Agent:** Lệ
- **Sponsor/Owner:** Nguyễn Thành Doanh

## 2. Mục tiêu dự án (SMART)
- **Specific:** Xây dựng một hệ thống web nội bộ giúp team nhỏ quản lý task, giao người phụ trách, deadline, comment và theo dõi trạng thái công việc.
- **Measurable:** MVP cho phép tạo task, assign người, cập nhật trạng thái, comment và xem dashboard cơ bản ở mức tổng hợp task.
- **Achievable:** Giữ scope gọn, ưu tiên task flow lõi; attachment, analytics nâng cao và mobile app để phase sau.
- **Relevant:** Giải quyết tình trạng quản lý công việc rời rạc qua chat và file lẻ.
- **Time-bound:** Hoàn thành MVP trong 6 tuần.

## 3. Phạm vi dự án
### In-scope
- Web app nội bộ
- Task CRUD cơ bản
- Assign owner
- Deadline
- Status tracking
- Comment trong task
- Dashboard cơ bản: tổng số task, theo trạng thái, theo owner hoặc overdue nếu còn đủ năng lực

### Out-of-scope
- Mobile app native
- Analytics nâng cao
- Attachment management đầy đủ
- Tích hợp hệ thống ngoài phức tạp

## 4. Success Criteria
- Team có thể quản lý task tập trung trong một hệ thống duy nhất
- Có thể assign owner, deadline và theo dõi trạng thái task
- Có comment để trao đổi trong task
- MVP usable trong vòng 6 tuần

## 5. Stakeholders
| Vai trò | Tên | Trách nhiệm |
|---------|-----|-------------|
| Owner | Nguyễn Thành Doanh | Xác nhận yêu cầu, phê duyệt scope |
| PM Agent | Lệ | Chuẩn hóa tài liệu, điều phối workflow |
| Backend dev | TBD | Xây API và auth |
| Frontend dev | TBD | Xây UI task flow |
| Tester part-time | TBD | Smoke test, validation, feedback |

## 6. Constraints
- Timeline 6 tuần
- Ngân sách nhỏ
- Nguồn lực: 1 backend, 1 frontend, 1 tester part-time
- Ưu tiên nội bộ, nhanh usable hơn là full-featured

## 7. Assumptions
- Team đồng ý khóa MVP scope sớm
- 2 role cơ bản là đủ cho giai đoạn đầu
- Attachment có thể để phase sau nếu cần bảo vệ timeline

## 8. Rủi ro sơ bộ
- R-001: Scope dashboard nở ra làm chậm MVP
- R-002: Tester part-time phản hồi chậm làm kéo dài vòng feedback
- R-003: Chưa chốt sớm API contract và authorization gây rework frontend

## 9. Phê duyệt
- [x] Đã được owner xác nhận định hướng
- [x] Đã được PM Agent phân tích và khóa scope sơ bộ
- [x] Sẵn sàng chuyển sang Planning
