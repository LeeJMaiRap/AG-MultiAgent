# Issue Log: Hệ thống quản lý task nội bộ

## Active Issues (Vấn đề đang mở)

### ISS-001: Thiếu design direction cho layout chính
- **Severity:** Medium
- **Status:** Open
- **Reported by:** Task Board / PM Agent
- **Reported date:** 2026-05-16
- **Description:** TASK-008 bị chặn vì chưa có định hướng layout đủ rõ để tiếp tục implement UI chính.
- **Impact:** Chậm tiến độ phần frontend core và có thể ảnh hưởng các task UI phụ thuộc phía sau.
- **Root cause:** Chưa chốt design direction trước khi bắt đầu task layout.
- **Resolution:** Xin xác nhận design direction hoặc dùng default layout tạm thời để tiếp tục.
- **Assigned to:** PM Agent
- **Target resolution:** 2026-05-17

### ISS-002: Form create task chưa validate deadline
- **Severity:** Medium
- **Status:** Open
- **Reported by:** Tester nội bộ
- **Reported date:** 2026-05-16 14:00
- **Description:** Form tạo task hiện chưa kiểm tra deadline bắt buộc, khiến user có thể tạo task thiếu thông tin quan trọng.
- **Impact:** Chất lượng dữ liệu task giảm, có thể ảnh hưởng việc theo dõi tiến độ và phân công.
- **Root cause:** Validation rule cho trường deadline chưa được implement ở frontend hoặc backend.
- **Resolution:** Bổ sung validation deadline ở form và kiểm tra lại ở API nếu cần.
- **Assigned to:** Developer B
- **Target resolution:** 2026-05-17

## Resolved Issues (Vấn đề đã giải quyết)

### ISS-003: Lỗi version jsonwebtoken trong package.json
- **Severity:** Medium
- **Status:** Resolved
- **Reported by:** Worker Agent
- **Reported date:** 2026-05-15 10:30
- **Resolved by:** PM Agent
- **Resolved date:** 2026-05-15 10:35
- **Resolution:** Sửa version `jsonwebtoken` trong package.json về version hợp lệ và chạy lại `npm install` thành công.

## Issue Statistics
- **Total issues:** 3
- **Open:** 2
- **Resolved:** 1
- **Average resolution time:** ~5 phút (đối với issue đã đóng)
