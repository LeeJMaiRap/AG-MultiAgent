# Requirement Clarification

## 1. Tóm tắt yêu cầu gốc
Người dùng muốn xây dựng một hệ thống quản lý dự án dạng web cho team nội bộ, nhằm hỗ trợ tạo task, phân công người thực hiện và theo dõi tiến độ. Hệ thống cần truy cập được từ nhiều nơi, có giới hạn thời gian triển khai khoảng 2 tháng, và chi phí nên ở mức hợp lý.

## 2. Mục tiêu chính
- Tạo một hệ thống quản lý dự án phù hợp với team hiện tại
- Hỗ trợ quản lý task, phân công và theo dõi tiến độ tốt hơn Trello đang dùng
- Có thể truy cập qua web từ nhiều nơi

## 3. Phạm vi sơ bộ

### Bao gồm
- Hệ thống web quản lý dự án
- Tạo task
- Assign người thực hiện
- Theo dõi tiến độ

### Chưa rõ / chưa chốt
- Có cần phân quyền theo vai trò hay không
- Có cần thông báo real-time hay email notification không
- Có cần báo cáo/dashboards nâng cao hay không
- Có cần import dữ liệu từ Trello hay không

### Ngoài phạm vi (nếu suy ra được)
- Chưa có dấu hiệu cho thấy cần mobile app native

## 4. Danh sách yêu cầu đã bóc tách

### Yêu cầu nghiệp vụ
- Team cần một công cụ quản lý dự án phù hợp hơn công cụ hiện tại
- Hệ thống phải hỗ trợ cộng tác trong team 5 người

### Yêu cầu chức năng
- Tạo task
- Gán người phụ trách cho task
- Theo dõi trạng thái/tiến độ task
- Truy cập qua nền tảng web

### Yêu cầu phi chức năng
- Có thể truy cập từ nhiều nơi
- Cần hoàn thành trong khoảng 2 tháng
- Chi phí triển khai không nên cao

### Ràng buộc / giả định
- Team hiện đang dùng Trello
- Dự án có thể là công cụ nội bộ trước tiên
- Budget chưa được chốt chính thức

## 5. Điểm còn mơ hồ / chưa đủ dữ liệu
- Chưa rõ phạm vi tính năng chi tiết ngoài task/assign/progress
- Chưa rõ mức độ phân quyền người dùng
- Chưa rõ có cần lưu lịch sử thay đổi không
- Chưa rõ có cần tích hợp công cụ hiện tại hay không
- Chưa rõ định nghĩa "không quá cao" về ngân sách là bao nhiêu

## 6. Câu hỏi cần xác nhận
1. Hệ thống này chỉ dùng nội bộ hay có cần hỗ trợ khách hàng/bên ngoài cùng truy cập?
2. Ngoài tạo task, assign và theo dõi tiến độ, anh có cần thêm tính năng như comment, file đính kèm, deadline, notification hay report không?
3. Có cần import dữ liệu cũ từ Trello sang hệ thống mới không?
4. Có cần phân quyền như admin / manager / member không?
5. Mức ngân sách hoặc giới hạn công nghệ chấp nhận được là gì?

## 7. Đề xuất bước tiếp theo
- Xác nhận phạm vi tính năng MVP
- Làm rõ yêu cầu phân quyền và báo cáo
- Sau khi chốt câu trả lời, chuyển sang tạo `charter.md` và `requirements.md`
