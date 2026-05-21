# PM Projects - Quan sát về các dự án PM Agent

## 2026-04-24 - Khởi tạo dự án PM Agent
- **Owner:** Nguyễn Thành Doanh
- **Bối cảnh:** Bài tập thực tập tại HUECIT
- **Mục tiêu:** Nghiên cứu và xây dựng Project Manager Agent bằng OpenClaw
- **Loại dự án:** Dự án cá nhân, Vibe Code / No Code
- **Kết quả mong muốn:** PM Agent có thể nhận yêu cầu dự án, tạo tài liệu PM, chia task, điều phối thực thi, theo dõi tiến độ, và tạo báo cáo tổng kết

## 2026-04-24 - Dự án Web Bán Hàng (PROJECT TEST CỦA PM AGENT)
- **Owner:** Nguyễn Thành Doanh
- **Mục tiêu:** Xây dựng trang web bán hàng MVP hoàn chỉnh trong 1 ngày
- **Vai trò trong hệ thống:** Đây là **dự án test / validation project** để kiểm chứng PM Agent
- **Scope:** Trang chủ, danh sách sản phẩm, chi tiết sản phẩm, giỏ hàng, checkout, auth, admin dashboard, 1000+ sản phẩm mẫu
- **Timeline:** 1 ngày (24 giờ)
- **Trạng thái hiện tại:** Demo-ready / late execution stabilization
- **Tiến độ task board đúng:** 19/33 task (~58%)
- **Đánh giá thực tế:** Mức hoàn thiện demo cao hơn tỷ lệ task do WBS có nhiều task nâng cao chưa cần cho MVP
- **Kết quả nổi bật:**
  - Backend foundation hoàn thành
  - MongoDB chạy được và seed thành công 1050 sản phẩm
  - Frontend MVP hoàn thành
  - Kết nối frontend-backend cơ bản hoàn thành
  - Demo prep hoàn thành
  - Báo cáo cuối cùng đã xuất
- **Quyết định quan trọng:** Đã chuyển từ full scope sang MVP scope để đảm bảo khả thi
- **Bài học chính:** PM Agent hoạt động tốt khi có workflow rõ ràng, externalized state, prompts và templates đầy đủ

## Trạng thái riêng của PM Agent
- **PM Agent không phải là Web Bán Hàng**
- PM Agent là framework/agent quản lý dự án
- PM Agent hiện ở giai đoạn: **đánh giá và hoàn thiện sau lần kiểm chứng thực tế đầu tiên**
- Tiến độ PM Agent nên hiểu theo framework maturity, không theo task board của Web Bán Hàng
- Mức hoàn thành PM Agent framework + validation: ~85%

## Kiến trúc đề xuất
- 1 PM Agent chính
- 1 hoặc nhiều Worker Agent
- Project state lưu bằng file
- Human-in-the-loop ở các quyết định quan trọng

## Các artifacts cốt lõi
- charter.md
- requirements.md
- spec.md
- plan.md
- rules.md
- wbs.md
- schedule.md
- risk-register.md
- task-board.md
- issue-log.md
- change-log.md
- status-dashboard.md
- final-report.md
- lessons-learned.md

## Ghi chú
- Mô hình được xây dựng qua 8 phần phân tích
- Dùng OpenClaw làm nền tảng triển khai
- Có thể mở rộng thành skill hoặc SOP trong tương lai
- Đã chứng minh được PM Agent có thể quản lý một dự án demo thực tế end-to-end
