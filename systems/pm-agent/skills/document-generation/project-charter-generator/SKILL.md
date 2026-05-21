---
name: project-charter-generator
description: Tạo file `01-initiation/charter.md` - tài liệu khởi tạo dự án chính thức từ requirement clarification, meeting notes hoặc brief dự án; dùng khi cần tạo charter cho dự án mới, định nghĩa mục tiêu SMART, phạm vi, success criteria, stakeholders, constraints và rủi ro sơ bộ theo chuẩn PM.
---

# Project Charter Generator

## Mục tiêu

Tạo tài liệu Project Charter chính thức để khởi tạo dự án, làm cơ sở cho toàn bộ giai đoạn planning và execution sau này.

Skill này giúp:
- chuyển yêu cầu đã làm rõ thành tài liệu charter có cấu trúc chuẩn PM
- định nghĩa rõ mục tiêu SMART
- xác định phạm vi in-scope / out-of-scope
- liệt kê stakeholders và trách nhiệm
- ghi nhận constraints, assumptions và rủi ro sơ bộ
- tạo mốc phê duyệt chính thức trước khi chuyển sang planning

## Dùng khi nào

Dùng skill này khi:
- đã có requirement clarification hoặc meeting notes đủ rõ
- cần tạo tài liệu khởi tạo dự án chính thức
- cần định nghĩa phạm vi và mục tiêu trước khi lập kế hoạch chi tiết
- cần có tài liệu để owner/sponsor phê duyệt

## Không dùng khi nào

Không dùng skill này khi:
- yêu cầu còn quá mơ hồ, chưa qua requirement clarification
- mục tiêu là tạo tài liệu kỹ thuật chi tiết (dùng `project-spec-generator`)
- mục tiêu là tạo kế hoạch triển khai (dùng `project-plan-generator`)
- dự án đã có charter và chỉ cần cập nhật

## Input bắt buộc

Ít nhất phải có:
- tên dự án
- mục tiêu chính của dự án
- phạm vi sơ bộ (in-scope)

## Input tùy chọn

- requirement clarification đã hoàn chỉnh
- meeting notes
- owner/sponsor name
- timeline/deadline
- budget
- constraints kỹ thuật
- stakeholders đã biết
- rủi ro đã nhận diện

## Output

Output là file `charter.md` theo cấu trúc chuẩn với 9 phần:

1. **Thông tin cơ bản**
2. **Mục tiêu dự án (SMART)**
3. **Phạm vi dự án**
4. **Success Criteria**
5. **Stakeholders**
6. **Constraints**
7. **Assumptions**
8. **Rủi ro sơ bộ**
9. **Phê duyệt**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải tuân thủ template có sẵn trong `systems/pm-agent/templates/charter-template.md`.

## Quy tắc xử lý

### 1. Mục tiêu phải theo chuẩn SMART
Mỗi mục tiêu phải có đủ 5 yếu tố:
- **Specific:** cụ thể, rõ ràng
- **Measurable:** đo lường được
- **Achievable:** khả thi
- **Relevant:** liên quan, có ý nghĩa
- **Time-bound:** có mốc thời gian

Nếu đầu vào thiếu yếu tố nào, phải ghi chú rõ và đề xuất làm rõ.

### 2. Phân biệt rõ in-scope và out-of-scope
- **In-scope:** những gì dự án sẽ làm
- **Out-of-scope:** những gì dự án **không** làm (nhưng có thể bị nhầm lẫn)

Phần out-of-scope rất quan trọng để tránh scope creep.

### 3. Success criteria phải đo lường được
Mỗi tiêu chí thành công phải:
- rõ ràng
- có thể kiểm chứng
- không mơ hồ

Tránh các tiêu chí kiểu "làm tốt", "chất lượng cao" mà không định nghĩa rõ.

### 4. Constraints phải thực tế
Ghi nhận đúng các ràng buộc:
- timeline
- budget
- technology
- resources
- legal/compliance

Nếu không rõ, ghi "Chưa xác định" thay vì bịa số liệu.

### 5. Assumptions phải ghi rõ
Mọi giả định quan trọng phải được liệt kê, ví dụ:
- "Giả định có đủ nguồn lực"
- "Giả định API bên thứ 3 hoạt động ổn định"
- "Giả định không có thay đổi scope lớn"

### 6. Rủi ro sơ bộ chỉ cần mức high-level
Không cần phân tích rủi ro chi tiết ở giai đoạn này. Chỉ cần liệt kê các rủi ro lớn, rõ ràng.

### 7. Phê duyệt phải có checklist
Phần phê duyệt phải có ít nhất:
- [ ] Đã được owner xác nhận
- [ ] Đã được PM Agent phân tích
- [ ] Sẵn sàng chuyển sang giai đoạn Planning

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Mục tiêu thật sự của dự án là gì? (không phải tính năng)
- Làm sao biết dự án thành công?
- Phạm vi nào dễ bị hiểu nhầm hoặc mở rộng không kiểm soát?
- Ai là người quyết định cuối cùng?
- Ràng buộc nào có thể làm dự án thất bại?
- Giả định nào nếu sai sẽ ảnh hưởng lớn?
- Rủi ro nào cần theo dõi ngay từ đầu?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `requirement-clarifier`
- `meeting-notes-normalizer`

Và là đầu vào cho:
- `requirements-document-generator`
- `project-spec-generator`
- `project-plan-generator`

Charter là tài liệu đầu tiên và quan trọng nhất trong giai đoạn Initiation.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/01-initiation/charter.md
```

File này là tài liệu nền cho toàn bộ dự án.

## Tiêu chí hoàn thành tốt

Một charter tốt khi:
- đọc xong là hiểu rõ dự án làm gì, tại sao, cho ai
- mục tiêu SMART đầy đủ và rõ ràng
- phạm vi in/out-scope không gây nhầm lẫn
- success criteria có thể kiểm chứng
- stakeholders và trách nhiệm rõ ràng
- constraints và assumptions được ghi nhận đầy đủ
- có thể dùng làm cơ sở để lập kế hoạch chi tiết

## Lỗi thường gặp cần tránh

- viết mục tiêu không theo SMART
- không ghi rõ out-of-scope
- success criteria quá mơ hồ
- bỏ sót constraints quan trọng
- không ghi assumptions
- rủi ro quá chi tiết hoặc quá chung chung
- thiếu phần phê duyệt
- trộn lẫn charter với spec kỹ thuật

## Cách dùng ngắn gọn

1. Đọc requirement clarification hoặc meeting notes
2. Xác định mục tiêu chính và chuyển thành SMART
3. Tách rõ in-scope và out-of-scope
4. Định nghĩa success criteria đo lường được
5. Liệt kê stakeholders
6. Ghi nhận constraints, assumptions, rủi ro
7. Tạo checklist phê duyệt
8. Xuất file `charter.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ charter thực tế
- Tham khảo: `systems/pm-agent/templates/charter-template.md`
- Tham khảo: `projects/active/web-ban-hang/01-initiation/charter.md`
