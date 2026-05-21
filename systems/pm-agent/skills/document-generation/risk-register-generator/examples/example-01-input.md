# Ví dụ 1: Input cho risk register hệ thống quản lý task

## Nguồn: Charter + Project Plan

### Từ Charter - Rủi ro sơ bộ
- R-001: Budget chưa được chốt rõ có thể ảnh hưởng phạm vi triển khai
- R-002: Nếu phạm vi mở rộng thêm dashboard nâng cao hoặc tích hợp ngoài, timeline 2 tháng có thể bị ảnh hưởng
- R-003: Nếu người dùng nội bộ không phản hồi kịp, việc tinh chỉnh yêu cầu có thể chậm

### Từ Project Plan - Risk Mitigation
- Timeline 2 tháng quá ngắn: tập trung MVP, bỏ qua nice-to-have
- File upload phức tạp: dùng thư viện có sẵn, giới hạn file size
- Phân quyền có bug: test kỹ, code review cẩn thận
- Team không có thời gian test: lên lịch test session cụ thể
- Responsive UI tốn thời gian: dùng CSS framework, test sớm

### Bối cảnh
- Team nhỏ (2 developers)
- MVP trong 2 tháng
- Chỉ dùng nội bộ
- Stack: React + Node.js + MongoDB
