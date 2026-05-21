# Project Charter: Hệ thống quản lý task nội bộ

## 1. Thông tin cơ bản
- **Tên dự án:** Hệ thống quản lý task nội bộ
- **Mã dự án:** TMS-2026-05-11
- **Ngày khởi tạo:** 2026-05-11
- **PM Agent:** Lệ
- **Sponsor/Owner:** Nguyễn Thành Doanh

## 2. Mục tiêu dự án (SMART)
- **Specific:** Xây dựng một hệ thống web nội bộ giúp team quản lý task, phân công người thực hiện, theo dõi tiến độ và cộng tác hiệu quả hơn công cụ hiện tại
- **Measurable:** Hệ thống cho phép tạo task, assign người thực hiện, comment, đính kèm file, đặt deadline và theo dõi trạng thái task cho team 5 người
- **Achievable:** Phạm vi MVP tập trung vào nhu cầu nội bộ cốt lõi, không bao gồm import dữ liệu Trello hoặc tích hợp phức tạp bên ngoài
- **Relevant:** Giải quyết nhu cầu quản lý công việc nội bộ và thay thế công cụ hiện tại chưa đáp ứng đủ tính năng
- **Time-bound:** Hoàn thành phiên bản MVP trong khoảng 2 tháng

## 3. Phạm vi dự án
### In-scope (Trong phạm vi)
- Hệ thống web quản lý task nội bộ
- Tạo task
- Phân công người thực hiện
- Theo dõi trạng thái/tiến độ task
- Comment trong task
- Đính kèm file
- Đặt deadline
- Phân quyền admin / member

### Out-of-scope (Ngoài phạm vi)
- Import dữ liệu từ Trello
- Tích hợp công cụ bên ngoài phức tạp
- Ứng dụng mobile native
- Dashboard phân tích nâng cao ở giai đoạn đầu

## 4. Success Criteria (Tiêu chí thành công)
- Team 5 người có thể dùng hệ thống để tạo và quản lý task nội bộ
- Có thể assign người phụ trách và deadline cho task
- Có thể trao đổi qua comment và đính kèm file trong task
- Hệ thống phân quyền được ít nhất 2 vai trò: admin và member
- MVP được hoàn thành trong khoảng 2 tháng

## 5. Stakeholders
| Vai trò | Tên | Trách nhiệm |
|---------|-----|-------------|
| Owner | Nguyễn Thành Doanh | Phê duyệt phạm vi, xác nhận yêu cầu, nghiệm thu |
| PM Agent | Lệ | Quản lý dự án, chuẩn hóa tài liệu, điều phối workflow |
| End Users | Team nội bộ 5 người | Sử dụng hệ thống, phản hồi trong quá trình hoàn thiện |

## 6. Constraints (Ràng buộc)
- **Timeline:** Khoảng 2 tháng cho MVP
- **Budget:** Không quá cao, chưa chốt số cụ thể
- **Technology:** Hệ thống web nội bộ
- **Resources:** Team nội bộ 5 người, PM Agent hỗ trợ phân tích và điều phối

## 7. Assumptions (Giả định)
- Team chỉ cần hệ thống dùng nội bộ ở giai đoạn đầu
- Không cần import dữ liệu từ Trello
- Phạm vi MVP giữ tập trung vào task management cốt lõi
- Team có thể dành đủ thời gian tham gia phản hồi trong quá trình triển khai

## 8. Rủi ro sơ bộ
- **R-001:** Budget chưa được chốt rõ có thể ảnh hưởng phạm vi triển khai
- **R-002:** Nếu phạm vi mở rộng thêm dashboard nâng cao hoặc tích hợp ngoài, timeline 2 tháng có thể bị ảnh hưởng
- **R-003:** Nếu người dùng nội bộ không phản hồi kịp, việc tinh chỉnh yêu cầu có thể chậm

## 9. Phê duyệt
- [ ] Đã được owner xác nhận
- [x] Đã được PM Agent phân tích
- [ ] Sẵn sàng chuyển sang giai đoạn Planning
