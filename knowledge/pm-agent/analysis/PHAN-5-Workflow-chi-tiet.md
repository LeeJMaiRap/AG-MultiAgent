# PHẦN 5: Workflow chi tiết từng bước cho PM Agent

## Tổng quan
Phần này mô tả chi tiết cách PM Agent vận hành theo từng giai đoạn.

## Workflow tổng thể end-to-end

```
User đưa yêu cầu dự án
    ↓
PM Agent phân tích yêu cầu
    ↓
PM Agent tạo tài liệu khởi tạo
    ↓
PM Agent hỏi lại nếu thiếu thông tin
    ↓
PM Agent lập kế hoạch + chia task
    ↓
PM Agent quyết định task nào tự làm, task nào giao sub-agent
    ↓
Worker/Sub-agent thực hiện task
    ↓
PM Agent nhận kết quả, cập nhật trạng thái
    ↓
PM Agent giám sát tiến độ / issue / risk / change
    ↓
PM Agent lặp lại chu trình execution cho đến khi hoàn tất
    ↓
PM Agent tổng kết, nghiệm thu, đóng dự án
    ↓
PM Agent lưu lessons learned và memory
```

## GIAI ĐOẠN 1 — TIẾP NHẬN & PHÂN TÍCH YÊU CẦU

### Mục tiêu
Biến một yêu cầu tự nhiên của người dùng thành một bài toán dự án rõ ràng.

### Input
Ví dụ user nói:
> "Làm cho anh một PM Agent bằng OpenClaw"

### PM Agent phải làm gì?

#### Bước 1: Tiếp nhận yêu cầu
- Đọc yêu cầu gốc
- Xác định đây là:
  - yêu cầu tạo sản phẩm?
  - yêu cầu nghiên cứu?
  - yêu cầu triển khai?
  - hay cả ba?

#### Bước 2: Trích xuất thông tin cốt lõi
PM Agent cần cố gắng rút ra:
- Mục tiêu chính
- Đầu ra mong muốn
- Phạm vi sơ bộ
- Bối cảnh sử dụng
- Người dùng mục tiêu
- Ràng buộc kỹ thuật
- Ràng buộc thời gian
- Tiêu chí thành công

#### Bước 3: Phát hiện khoảng trống thông tin
Ví dụ thiếu:
- Output cuối cùng là gì?
- Cần demo hay cần chạy thật?
- Có giới hạn công nghệ không?
- Thời hạn bao lâu?
- Có cần UI không?
- Có cần báo cáo học thuật không?

#### Bước 4: Tạo danh sách câu hỏi làm rõ
PM Agent không nên hỏi lan man.
Chỉ hỏi các câu ảnh hưởng trực tiếp đến scope, timeline, kiến trúc, hoặc tiêu chí nghiệm thu.

Ví dụ:
- Dự án này ưu tiên nghiên cứu hay ưu tiên sản phẩm chạy được?
- Anh cần PM Agent ở mức tạo tài liệu hay điều phối task thực sự?
- Có cần demo bằng OpenClaw session/sub-agent không?
- Kết quả cuối cùng là báo cáo, skill, hay prototype chạy được?

#### Bước 5: Tạo tài liệu khởi tạo ban đầu
PM Agent tạo:
- `charter.md`
- `requirements.md`

### Output của giai đoạn này
- Yêu cầu đã được chuẩn hóa
- Các câu hỏi mở đã được ghi nhận
- Đã có charter nháp
- Đã có requirements bản đầu

## GIAI ĐOẠN 2 — XÁC NHẬN PHẠM VI & MỤC TIÊU

### Mục tiêu
Đảm bảo PM Agent và user hiểu cùng một thứ.

### PM Agent phải làm gì?

#### Bước 1: Tóm tắt hiểu biết hiện tại
PM Agent cần phản hồi kiểu:
- Đây là mục tiêu dự án
- Đây là phạm vi em hiểu
- Đây là đầu ra em dự kiến
- Đây là thứ em chưa chắc

#### Bước 2: Đưa ra đề xuất scope
Chia thành:
- **In-scope**
- **Out-of-scope**
- **Future enhancements**

#### Bước 3: Xác nhận success criteria
Ví dụ:
- PM Agent nhận yêu cầu dự án và phân tích được
- PM Agent tạo bộ tài liệu PM chuẩn
- PM Agent chia task và điều phối được ít nhất 1 worker
- PM Agent cập nhật trạng thái dự án
- PM Agent tạo final report

#### Bước 4: Chốt baseline ban đầu
Sau khi user xác nhận, PM Agent đánh dấu:
- Charter approved
- Scope baseline established
- Project ready for planning

### Output
- Charter đã rõ hơn
- Scope rõ ràng
- Success criteria được chốt
- Sẵn sàng sang planning

## GIAI ĐOẠN 3 — LẬP KẾ HOẠCH

### Mục tiêu
Biến mục tiêu dự án thành kế hoạch có thể thực thi.

### PM Agent phải làm gì?

#### Bước 1: Tạo Spec
Spec trả lời câu hỏi: **Phải xây cái gì?**

Nội dung gồm:
- Chức năng
- Đặc tính
- Hành vi mong muốn
- User flow
- Acceptance criteria

#### Bước 2: Tạo Plan
Plan trả lời câu hỏi: **Sẽ triển khai như thế nào?**

Nội dung gồm:
- Phase
- Mốc
- Task groups
- Dependencies
- Thứ tự ưu tiên

#### Bước 3: Tạo Rules
Rules trả lời câu hỏi: **Phải làm theo nguyên tắc nào?**

Ví dụ:
- Tài liệu luôn cập nhật trước/sau execution
- Mọi task phải có status
- Mọi thay đổi scope phải ghi vào change-log
- Mọi blocker phải ghi vào issue-log
- Worker agent không tự ý đổi mục tiêu dự án

#### Bước 4: Tạo WBS
Phân rã từ lớn xuống nhỏ:
1. Phân tích nghiệp vụ PM Agent
2. Thiết kế kiến trúc
3. Thiết kế bộ tài liệu
4. Xây workflow
5. Tạo prototype OpenClaw
6. Kiểm thử
7. Báo cáo tổng kết

#### Bước 5: Tạo lịch trình
Không cần quá phức tạp như PM chuyên nghiệp ngoài đời, nhưng phải có:
- Milestone
- Thứ tự task
- Duration ước lượng
- Dependency
- Critical path nếu có

#### Bước 6: Tạo risk register
PM Agent chủ động nghĩ trước các rủi ro như:
- Yêu cầu mơ hồ
- Scope creep
- Context overflow
- Worker agent làm lệch
- Artifact không cập nhật
- Output không nhất quán

### Output
- `spec.md`
- `plan.md`
- `rules.md`
- `wbs.md`
- `schedule.md`
- `risk-register.md`

## GIAI ĐOẠN 4 — CHUẨN BỊ THỰC THI

### Mục tiêu
Từ plan tổng thể chuyển thành task thực thi được.

### PM Agent phải làm gì?

#### Bước 1: Chuyển WBS thành task board
Mỗi task cần có:
- ID
- Tên
- Mô tả
- Input
- Output
- Priority
- Dependency
- Assignee
- Status
- Estimate

#### Bước 2: Phân loại task
PM Agent cần chia task thành 3 loại:

**Loại A — PM Agent tự làm**
- Viết charter
- Cập nhật risk register
- Tạo status report
- Đánh giá thay đổi

**Loại B — giao Worker Agent**
- Tạo file mẫu
- Code một module
- Refactor tài liệu
- Chạy kiểm tra
- Triển khai prototype

**Loại C — cần human approval**
- Đổi phạm vi lớn
- Bỏ feature
- Thay đổi tiêu chí đầu ra
- Xác nhận nghiệm thu

#### Bước 3: Chuẩn bị task prompt
Nếu giao cho worker, PM Agent phải giao rõ:
- Mục tiêu task
- Input file nào cần đọc
- Output file nào cần tạo/sửa
- Tiêu chí hoàn thành
- Điều gì không được làm
- Khi nào phải báo blocker

#### Bước 4: Chọn thứ tự chạy task
PM Agent không nên chạy task ngẫu nhiên.
Nó phải ưu tiên:
1. Task mở đường
2. Task có dependency thấp
3. Task giảm rủi ro
4. Task tạo ra artifact quan trọng trước

### Output
- `task-board.md`
- Task prompts cho worker
- Execution queue

## GIAI ĐOẠN 5 — THỰC THI TASK

### Mục tiêu
Làm cho công việc thực sự tiến lên.

### PM Agent phải làm gì?

#### Bước 1: Chọn task tiếp theo
Dựa trên:
- Dependency đã thỏa chưa?
- Mức ưu tiên?
- Blocker hiện tại?
- Giá trị tạo ra?

#### Bước 2: Giao task
Nếu task giao sub-agent thì PM Agent phải:
- Spawn sub-agent
- Truyền prompt rõ ràng
- Yêu cầu output cụ thể
- Giới hạn phạm vi task

#### Bước 3: Theo dõi kết quả
Sau khi worker trả về:
- Kiểm tra output có đ�� không
- Có đúng file cần sửa không
- Có đúng acceptance criteria không
- Có phát sinh issue/risk mới không

#### Bước 4: Cập nhật trạng thái dự án
Ngay sau execution, PM Agent phải cập nhật:
- `task-board.md`
- `issue-log.md` nếu có lỗi
- `change-log.md` nếu có thay đổi
- `status-dashboard.md`
- Có thể cập nhật `risk-register.md`

#### Bước 5: Chọn hành động tiếp theo
- Đánh dấu done
- Yêu cầu rework
- Escalate blocker
- Xin xác nhận từ user
- Chuyển sang task tiếp theo

### Output
- Task completed hoặc escalated
- Tài liệu dự án được cập nhật
- Trạng thái luôn đồng bộ

## GIAI ĐOẠN 6 — GIÁM SÁT & KIỂM SOÁT

### Mục tiêu
Không để dự án "trôi" mà không ai biết.

### PM Agent phải làm gì?

#### Bước 1: Kiểm tra tiến độ
So sánh:
- Planned vs actual
- Estimate vs actual
- Expected deliverables vs actual deliverables

#### Bước 2: Theo dõi issue
Mọi vấn đề phải được phân loại:
- Blocker
- Defect
- Thiếu thông tin
- Phụ thuộc bên ngoài
- Chất lượng thấp

#### Bước 3: Theo dõi risk
PM Agent phải nhìn trước:
- Task nào có nguy cơ trễ
- Scope có phình không
- Context có đang quá tải không
- Worker có drift không

#### Bước 4: Quản lý change
Khi có yêu cầu thay đổi:
1. Ghi vào change-log
2. Phân tích impact:
   - Scope
   - Timeline
   - Chất lượng
   - Tài nguyên
3. Xin phê duyệt nếu cần
4. Cập nhật baseline hoặc ghi chú deviation

#### Bước 5: Tạo báo cáo định kỳ
PM Agent nên có khả năng tạo:
- Daily status
- Weekly summary
- Progress snapshot
- Risk summary
- Issue escalation summary

### Output
- Dự án luôn có tình trạng rõ ràng
- Mọi thay đổi đều có dấu vết
- User không bị "mù" về tiến độ

## GIAI ĐOẠN 7 — NGHIỆM THU & ĐÓNG DỰ ÁN

### Mục tiêu
Kết thúc dự án có kiểm soát, không phải "xong rồi thôi".

### PM Agent phải làm gì?

#### Bước 1: Kiểm tra deliverables
PM Agent cần đối chiếu:
- Success criteria
- Scope đã chốt
- Requirements
- Acceptance criteria

#### Bước 2: Xác nhận với user
PM Agent trình bày:
- Đã làm gì
- Cái gì hoàn thành
- Cái gì chưa làm
- Cái gì là future work

#### Bước 3: Tạo final report
Bao gồm:
- Tổng quan dự án
- Kết quả đạt được
- Timeline thực tế
- Vấn đề chính
- Thay đổi lớn
- Lessons learned

#### Bước 4: Archive tri thức
PM Agent cập nhật:
- `final-report.md`
- `lessons-learned.md`
- Memory / knowledge base nếu cần

#### Bước 5: Đánh dấu đóng dự án
- Task board closed
- Issues unresolved được chuyển sang backlog/future work
- Project status = closed

### Output
- Dự án kết thúc sạch sẽ
- Có báo cáo
- Có tri thức tái sử dụng

## Quy tắc ra quyết định của PM Agent

### Khi nào tự làm?
- Task quản trị
- Task tài liệu
- Task phân tích
- Task đánh giá
- Task cập nhật trạng thái

### Khi nào giao worker?
- Task triển khai kỹ thuật
- Task tạo/sửa nhiều file
- Task cần thao tác chuyên biệt
- Task cần ngữ cảnh cục bộ riêng

### Khi nào hỏi user?
- Yêu cầu mơ hồ
- Thay đổi phạm vi lớn
- Có nhiều phương án chiến lược
- Chuẩn bị chốt kết quả cuối
- Có rủi ro cao hoặc hành động nhạy cảm

## Kết luận

**Workflow chuẩn của PM Agent là:**
- Hiểu yêu cầu
- Chuẩn hóa thành tài liệu
- Lập kế hoạch
- Chia task
- Điều phối thực thi
- Giám sát tiến độ/rủi ro/thay đổi
- Tổng kết và lưu tri thức

---

**Ngày phân tích:** 2026-04-24
**Người phân tích:** Lệ (PM Agent)
