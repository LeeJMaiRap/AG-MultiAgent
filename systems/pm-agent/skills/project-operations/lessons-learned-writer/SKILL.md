---
name: lessons-learned-writer
description: Tạo hoặc cập nhật file `lessons-learned.md` từ retrospective notes, issue log, change log, testing results hoặc trải nghiệm thực thi; dùng khi cần tổng hợp bài học rút ra, insight, khuyến nghị và tri thức có thể tái sử dụng cho dự án hiện tại hoặc dự án tương lai.
---

# Lessons Learned Writer

## Mục tiêu

Tạo và duy trì tài liệu Lessons Learned để lưu lại những gì dự án làm tốt, những gì chưa tốt, insight quan trọng và khuyến nghị cải tiến cho các lần sau.

Skill này giúp:
- tổng hợp bài học từ execution, testing, issue resolution và thay đổi phạm vi
- phân biệt phần làm tốt và phần cần cải thiện
- rút ra insight có thể tái sử dụng
- tạo recommendations cho team, PM Agent và dự án tương lai
- biến kinh nghiệm thành tri thức có thể dùng lại thay vì để trôi mất

## Dùng khi nào

Dùng skill này khi:
- kết thúc một phase quan trọng hoặc kết thúc dự án
- vừa giải quyết một sự cố/lỗi đáng nhớ
- vừa hoàn thành demo / MVP / handover
- cần tổng hợp retrospective có cấu trúc

## Không dùng khi nào

Không dùng skill này khi:
- dự án còn quá sớm, chưa có dữ liệu học được gì đáng kể
- chỉ cần ghi issue, risk hay change riêng lẻ
- chỉ cần status update ngắn hạn

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- retrospective notes
- issue log
- change log
- testing results
- execution observations
- post-demo / post-delivery notes

## Input tùy chọn

- metrics summary
- team feedback
- owner feedback
- links tới tài liệu liên quan
- knowledge transfer notes

## Output

Output là file `lessons-learned.md` với các phần chính:

1. **What Went Well**
2. **What Could Be Improved**
3. **Key Insights**
4. **Recommendations**
5. **Metrics Summary**
6. **Knowledge Transfer**
7. **Action Items**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/lessons-learned-template.md`.

## Quy tắc xử lý

### 1. Bài học phải xuất phát từ trải nghiệm thực tế
Không viết lessons learned kiểu chung chung hoặc sáo rỗng. Mỗi bài học nên gắn với:
- sự kiện thực tế
- vấn đề đã gặp
- điều đã thử
- kết quả quan sát được

### 2. Phân biệt rõ “what went well” và “what could be improved”
- **What went well:** điểm mạnh thật sự cần giữ lại
- **What could be improved:** điểm yếu, sai lệch, thiếu sót cần sửa

Không nên biến phần cải thiện thành lời tự khen hoặc ngược lại.

### 3. Key insights phải có khả năng tái sử dụng
Insight tốt là insight có thể áp dụng lại cho dự án khác, ví dụ:
- pattern kỹ thuật
- pattern quản lý
- cách phối hợp
- quyết định kiến trúc / workflow hữu ích

### 4. Recommendations phải hành động được
Khuyến nghị nên cụ thể và có ích, ví dụ:
- cập nhật template nào
- đổi workflow nào
- thêm checklist gì
- test phần nào sớm hơn

### 5. Metrics summary chỉ dùng khi có dữ liệu đủ tin cậy
Không bịa số. Nếu chưa có metric chắc chắn, có thể ghi “chưa đủ dữ liệu” hoặc bỏ gọn phần đó.

### 6. Knowledge transfer phải giúp người sau dùng lại được
Nên chỉ rõ:
- tài liệu ở đâu
- ai / thành phần nào liên quan
- dự án liên quan
- repo / thư mục bài học nếu có

### 7. Action items phải chuyển bài học thành việc cụ thể với owner và deadline
Ví dụ:
- Cập nhật template X
  - Owner: PM Agent
  - Deadline: 2026-05-20
- Thêm checklist test Y
  - Owner: QA lead
  - Deadline: 2026-05-18
- Sửa skill instruction Z
  - Owner: PM Agent
  - Deadline: 2026-05-25
- Tài liệu hóa pattern tái sử dụng
  - Owner: Tech lead
  - Deadline: End of phase

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Điều gì đã thực sự làm tốt và nên giữ lại?
- Điều gì gây chậm trễ, bug, hiểu nhầm hoặc lặp việc?
- Có pattern kỹ thuật/quản lý nào đáng tái sử dụng?
- Nếu làm lại từ đầu, nên thay đổi điều gì?
- Có tài liệu hoặc template nào nên cập nhật không?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- execution milestone complete
- demo complete
- handover
- retrospective / postmortem

Và hỗ trợ cho:
- cập nhật memory / knowledge base
- cải thiện templates, workflow, skills
- các dự án PM tiếp theo

Lessons learned là nơi biến kinh nghiệm thành tài sản tái sử dụng.

## Liên hệ với cấu trúc dự án

Skill này tạo hoặc cập nhật file:
```
projects/[project-name]/lessons-learned.md
```

Hoặc có thể dùng như tài liệu closure / retrospective ở cuối dự án.

## Tiêu chí hoàn thành tốt

Một lessons learned document tốt khi:
- không sáo rỗng
- có bài học thực tế, cụ thể
- có insight tái sử dụng được
- có recommendations rõ ràng
- có action items biến bài học thành cải tiến thực sự
- giúp dự án sau làm tốt hơn dự án trước

## Lỗi thường gặp cần tránh

- viết quá chung chung
- chỉ liệt kê sự kiện mà không rút ra bài học
- không có recommendations cụ thể
- không có action items theo sau
- trộn lẫn issue log với lessons learned
- tô hồng hoặc bi quan quá mức

## Cách dùng ngắn gọn

1. Đọc issue log / change log / testing results / notes thực tế
2. Tách phần làm tốt và phần cần cải thiện
3. Rút ra key insights có thể tái sử dụng
4. Viết recommendations cụ thể
5. Tổng hợp metrics nếu có
6. Chốt action items cải tiến
7. Xuất/cập nhật `lessons-learned.md`

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ lessons learned thực tế
- Tham khảo: `systems/pm-agent/templates/lessons-learned-template.md`
- Tham khảo: `projects/active/web-ban-hang/lessons-learned.md`
