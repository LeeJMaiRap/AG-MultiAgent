# Ví dụ 1: Input cho issue log hệ thống quản lý task

## Nguồn: Task board + feedback thực tế

### Blocked task từ task board
- TASK-008: Tạo layout chính bị chặn vì chưa có design direction
- Since: 2026-05-16
- Action: Xin xác nhận design direction hoặc dùng default layout để tiếp tục

### Lỗi đã xảy ra và đã xử lý
- jsonwebtoken version trong package.json không hợp lệ
- npm install fail
- Worker Agent báo lỗi lúc 2026-05-15 10:30
- PM Agent đã sửa version và cài lại thành công lúc 2026-05-15 10:35

### Feedback test
- Form create task không validate deadline
- Ảnh hưởng: user có thể tạo task thiếu thông tin quan trọng
- Chưa fix
- Reported by: Tester nội bộ
- Reported date: 2026-05-16 14:00
