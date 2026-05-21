# Quy Trình Nghiệp Vụ của PM Agent (AI Project Manager)

## Tổng Quan

**PM Agent** là một Agent AI đóng vai trò tương tự như Project Manager truyền thống, nhưng có khả năng **tự động hóa** và **thực hiện chủ động** các công việc quản lý dự án. PM Agent kết hợp **AI automation** với **human-in-the-loop** để hoàn thành dự án hiệu quả và chính xác.

### Nguyên tắc hoạt động
- **Tự động hóa tối đa:** Tự động thực hiện các tác vụ có thể xử lý bằng AI
- **Human-in-the-loop:** Yêu cầu xác nhận từ người dùng khi cần quyết định hoặc hành động bên ngoài
- **Minh bạch:** Báo cáo rõ ràng những gì đã làm, đang làm, và cần con người can thiệp
- **Chủ động:** Không chỉ phản ứng mà còn tự đề xuất, phát hiện rủi ro, và tối ưu quy trình

---

## 1. Khởi Tạo Dự Án (Project Initiation)

### Mục tiêu
Hiểu rõ bối cảnh dự án, xác định mục tiêu, phạm vi, và các bên liên quan

### Công việc PM Agent tự động thực hiện
- [ ] Thu thập thông tin ban đầu từ người dùng
- [ ] Phân tích yêu cầu và tạo bản nháp Project Charter
- [ ] Xác định stakeholders tiềm năng dựa trên mô tả dự án
- [ ] Đề xuất mục tiêu SMART
- [ ] Xây dựng scope, timeline, budget sơ bộ
- [ ] Tạo danh sách câu hỏi còn thiếu để làm rõ dự án

### Công việc cần human-in-the-loop
- [ ] Xác nhận mục tiêu dự án cuối cùng
- [ ] Xác nhận scope chính thức
- [ ] Phê duyệt stakeholders quan trọng
- [ ] Xác nhận budget hoặc giới hạn nguồn lực

### Output
- Draft/Final Project Charter
- Stakeholder Register
- Danh sách assumptions & constraints
- Câu hỏi cần làm rõ

---

## 2. Lập Kế Hoạch (Planning)

### Mục tiêu
Chuyển yêu cầu thành kế hoạch hành động chi tiết, khả thi, có thể theo dõi được

### Công việc PM Agent tự động thực hiện
- [ ] Phân rã công việc thành WBS (Work Breakdown Structure)
- [ ] Tạo backlog hoặc task list chi tiết
- [ ] Ước lượng effort, duration, dependencies
- [ ] Xây dựng timeline, milestone, deadline đề xuất
- [ ] Tạo Risk Register với xác suất, mức độ ảnh hưởng, cách giảm thiểu
- [ ] Đề xuất Communication Plan
- [ ] Đề xuất Resource Plan
- [ ] Tạo template cho status report, meeting notes, issue log

### Công việc cần human-in-the-loop
- [ ] Xác nhận mức ưu tiên công việc
- [ ] Phê duyệt timeline/milestones cuối cùng
- [ ] Xác nhận resource allocation nếu liên quan đến con người thật
- [ ] Chốt phạm vi các hạng mục bắt buộc và tùy chọn

### Output
- Project Management Plan
- WBS / Backlog
- Schedule Plan
- Risk Register
- Communication Plan
- Resource Plan
- Status Report Template

---

## 3. Thực Thi Dự Án (Execution)

### Mục tiêu
Điều phối và thúc đẩy tiến độ dự án bằng cả tự động hóa và phối hợp với con người

### Công việc PM Agent tự động thực hiện
- [ ] Theo dõi task progress dựa trên dữ liệu cập nhật
- [ ] Nhắc việc và đôn đốc các mốc quan trọng
- [ ] Tự động cập nhật trạng thái công việc vào tài liệu dự án
- [ ] Tạo báo cáo tiến độ định kỳ
- [ ] Phát hiện blockers, dependencies, bottlenecks
- [ ] Đề xuất phương án xử lý khi có chậm tiến độ
- [ ] Tự động chuẩn bị agenda cho meeting
- [ ] Tóm tắt thông tin từ các cuộc trao đổi để cập nhật dự án

### Công việc cần human-in-the-loop
- [ ] Xác nhận thay đổi lớn về phạm vi hoặc ưu tiên
- [ ] Ra quyết định liên quan đến nhân sự thật
- [ ] Phê duyệt thông điệp gửi cho khách hàng/stakeholder bên ngoài
- [ ] Can thiệp khi cần thương lượng, xử lý xung đột, hoặc quyết định chiến lược

### Output
- Updated Task Tracker
- Weekly / Daily Status Report
- Issue Log
- Meeting Agenda / Notes
- Action Items

---

## 4. Giám Sát & Kiểm Soát (Monitoring & Controlling)

### Mục tiêu
Phát hiện lệch hướng, quản lý rủi ro, và điều chỉnh kịp thời để đảm bảo dự án thành công

### Công việc PM Agent tự động thực hiện
- [ ] So sánh actual vs plan (tiến độ, nguồn lực, chất lượng)
- [ ] Cảnh báo khi milestone có nguy cơ trễ
- [ ] Phân tích xu hướng issue/risk để phát hiện vấn đề hệ thống
- [ ] Tự động cập nhật dashboard / status summary
- [ ] Theo dõi change requests và tác động của thay đổi
- [ ] Đề xuất corrective actions và preventive actions
- [ ] Theo dõi các KPI dự án (on-time %, open issues, risk severity, workload)

### Công việc cần human-in-the-loop
- [ ] Phê duyệt corrective actions có ảnh hưởng lớn
- [ ] Xác nhận thay đổi timeline/budget/scope
- [ ] Đưa ra quyết định cuối cùng khi có trade-off giữa thời gian, chi phí, chất lượng

### Output
- Status Dashboard
- Risk & Issue Alerts
- Change Log
- Corrective / Preventive Action Plan
- KPI Reports

---

## 5. Đóng Dự Án (Project Closure)

### Mục tiêu
Tổng kết, xác nhận hoàn thành, bàn giao, và lưu giữ tri thức để tái sử dụng

### Công việc PM Agent tự động thực hiện
- [ ] Kiểm tra checklist hoàn thành deliverables
- [ ] Chuẩn bị báo cáo tổng kết dự án
- [ ] Tổng hợp lessons learned
- [ ] Sắp xếp và archive tài liệu dự án
- [ ] Chuẩn bị handover package
- [ ] Tạo bản tóm tắt kết quả cuối cùng cho stakeholders

### Công việc cần human-in-the-loop
- [ ] Xác nhận deliverables đã đạt yêu cầu
- [ ] Ký duyệt đóng dự án
- [ ] Xác nhận bàn giao cho bên vận hành hoặc khách hàng
- [ ] Đánh giá cuối cùng về hiệu quả dự án

### Output
- Final Project Report
- Lessons Learned Document
- Archived Project Files
- Handover Package
- Closure Confirmation

---

## Cơ Chế Human-in-the-Loop

PM Agent không thay thế hoàn toàn con người trong mọi tình huống. Nó hoạt động theo nguyên tắc:

### 1. Tự động làm trước
PM Agent tự xử lý các công việc có thể chuẩn hóa hoặc tự động hóa:
- Phân tích dữ liệu
- Viết tài liệu
- Cập nhật trạng thái
- Theo dõi tiến độ
- Phát hiện rủi ro
- Tạo báo cáo
- Nhắc việc

### 2. Xin xác nhận khi cần
PM Agent phải yêu cầu xác nhận của con người khi:
- Có quyết định chiến lược
- Cần thay đổi scope/budget/timeline lớn
- Liên quan đến giao tiếp bên ngoài
- Có xung đột lợi ích hoặc rủi ro cao
- Cần phê duyệt chính thức

### 3. Hoàn tất và báo cáo
Sau khi có xác nhận từ người dùng, PM Agent:
- Thực hiện bước tiếp theo
- Cập nhật lại tài liệu dự án
- Đưa ra kết quả cuối cùng rõ ràng, có thể kiểm tra được

---

## Vai Trò Cốt Lõi của PM Agent

| Vai trò | Mô tả |
|--------|------|
| **Planner** | Lập kế hoạch dự án chi tiết |
| **Coordinator** | Điều phối công việc và thông tin |
| **Analyst** | Phân tích tiến độ, rủi ro, hiệu suất |
| **Reporter** | Tạo báo cáo minh bạch, định kỳ |
| **Advisor** | Đề xuất giải pháp, phương án tối ưu |
| **Controller** | Giám sát và kiểm soát thay đổi |
| **Knowledge Keeper** | Lưu giữ tri thức, lessons learned, history |

---

## Workflow Tổng Quát của PM Agent

```text
1. Nhận yêu cầu dự án từ người dùng
2. Phân tích và tạo Project Charter nháp
3. Yêu cầu người dùng xác nhận thông tin quan trọng
4. Tạo kế hoạch chi tiết (WBS, timeline, risks, resources)
5. Theo dõi thực thi và tự động cập nhật trạng thái
6. Phát hiện vấn đề, đề xuất xử lý, xin xác nhận khi cần
7. Tạo báo cáo định kỳ và dashboard
8. Khi hoàn thành, tổng kết, archive, handover
9. Lưu lessons learned vào hệ thống bộ nhớ
```

---

## Checklist Nghiệp Vụ Chuẩn cho PM Agent

### Khởi tạo
- [ ] Đã thu thập yêu cầu ban đầu
- [ ] Đã tạo Project Charter nháp
- [ ] Đã xin xác nhận mục tiêu và phạm vi

### Lập kế hoạch
- [ ] Đã tạo WBS / backlog
- [ ] Đã đề xuất timeline và milestone
- [ ] Đã lập risk register
- [ ] Đã có communication plan

### Thực thi
- [ ] Đã theo dõi tiến độ định kỳ
- [ ] Đã cập nhật issue log
- [ ] Đã nhắc việc các mốc quan trọng

### Giám sát
- [ ] Đã so sánh plan vs actual
- [ ] Đã cảnh báo các rủi ro lớn
- [ ] Đã đề xuất corrective actions khi cần

### Đóng dự án
- [ ] Đã tổng kết deliverables
- [ ] Đã chuẩn bị final report
- [ ] Đã lưu lessons learned
- [ ] Đã được human sign-off

---

## Kết Luận

PM Agent là mô hình Project Manager thế hệ mới: **tự động hóa phần lớn nghiệp vụ quản lý dự án**, nhưng vẫn giữ **con người ở vị trí ra quyết định cuối cùng**. Nhờ đó, PM Agent vừa tăng tốc công việc, vừa đảm bảo tính kiểm soát, an toàn, và thực tế trong môi trường làm việc chuyên nghiệp.
