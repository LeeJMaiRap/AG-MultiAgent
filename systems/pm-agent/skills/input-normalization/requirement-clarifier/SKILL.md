---
name: requirement-clarifier
description: Làm rõ yêu cầu thô từ chat, brief, ghi chú hoặc mô tả ban đầu thành bản yêu cầu có cấu trúc; dùng khi đầu vào còn mơ hồ, thiếu chi tiết, lẫn nhiều ý, hoặc cần bóc tách để chuẩn bị tạo tài liệu PM như charter, requirements, spec, plan.
---

# Requirement Clarifier

## Mục tiêu

Biến yêu cầu thô thành một bản yêu cầu đã được làm rõ, có cấu trúc, dễ dùng tiếp cho các skill/tài liệu PM phía sau.

Skill này giúp:
- bóc tách yêu cầu chính
- phát hiện điểm mơ hồ, thiếu thông tin, xung đột hoặc chưa chốt
- đề xuất câu hỏi cần hỏi lại anh
- chuẩn hóa đầu vào trước khi tạo tài liệu PM

## Dùng khi nào

Dùng skill này khi đầu vào là:
- tin nhắn chat mô tả nhu cầu dự án
- brief ngắn
- ghi chú họp thô
- danh sách ý tưởng chưa sắp xếp
- yêu cầu có nhiều phần nhưng chưa rõ ranh giới
- mô tả có thể hiểu theo nhiều cách

## Không dùng khi nào

Không dùng skill này khi:
- đầu vào đã là tài liệu yêu cầu hoàn chỉnh, rõ ràng và có cấu trúc tốt
- mục tiêu là cập nhật trạng thái dự án, không phải làm rõ yêu cầu
- mục tiêu là xuất PDF hoặc định dạng trình bày

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- đoạn chat yêu cầu
- brief dự án
- ghi chú họp
- mô tả yêu cầu tự do

## Input tùy chọn

- tên dự án
- bối cảnh khách hàng / tổ chức
- ràng buộc thời gian
- ràng buộc ngân sách
- ràng buộc kỹ thuật
- file/tài liệu liên quan đã có
- quyết định đã chốt trước đó

## Output

Output chuẩn là một bản Markdown có 7 phần sau:

1. **Tóm tắt yêu cầu gốc**
2. **Mục tiêu chính**
3. **Phạm vi sơ bộ**
4. **Danh sách yêu cầu đã bóc tách**
5. **Điểm còn mơ hồ / chưa đủ dữ liệu**
6. **Câu hỏi cần xác nhận**
7. **Đề xuất bước tiếp theo**

## Format output chuẩn

```md
# Requirement Clarification

## 1. Tóm tắt yêu cầu gốc
...

## 2. Mục tiêu chính
- ...

## 3. Phạm vi sơ bộ
### Bao gồm
- ...

### Chưa rõ / chưa chốt
- ...

### Ngoài phạm vi (nếu suy ra được)
- ...

## 4. Danh sách yêu cầu đã bóc tách
### Yêu cầu nghiệp vụ
- ...

### Yêu cầu chức năng
- ...

### Yêu cầu phi chức năng
- ...

### Ràng buộc / giả định
- ...

## 5. Điểm còn mơ hồ / chưa đủ dữ liệu
- ...

## 6. Câu hỏi cần xác nhận
1. ...?
2. ...?

## 7. Đề xuất bước tiếp theo
- ...
```

## Quy tắc xử lý

### 1. Không được tự bịa thông tin
Nếu đầu vào không nói rõ, phải ghi là:
- chưa rõ
- chưa được xác nhận
- cần hỏi lại
- chỉ là giả định tạm thời

### 2. Tách yêu cầu theo đúng bản chất
Ưu tiên tách thành:
- yêu cầu nghiệp vụ
- yêu cầu chức năng
- yêu cầu phi chức năng
- ràng buộc
- giả định

### 3. Phân biệt rõ “đã có” và “suy ra”
Nếu một ý là suy luận hợp lý từ ngữ cảnh, phải thể hiện đó là suy luận tạm thời, không được viết như fact đã chốt.

### 4. Khi yêu cầu quá rộng, phải bóc nhỏ
Nếu đầu vào có nhiều ý chồng lên nhau, cần nhóm lại theo các mảng công việc riêng.

### 5. Câu hỏi xác nhận phải thật sự hữu ích và cụ thể
Chỉ hỏi các câu có ảnh hưởng tới:
- phạm vi
- ưu tiên
- cách triển khai
- tài liệu sẽ sinh ra sau đó

Không hỏi lan man các câu nhỏ không giúp quyết định.

**Mỗi câu hỏi phải có:**
- **Priority:** (Critical/High/Medium/Low) - mức độ quan trọng
- **Context:** tại sao câu hỏi này quan trọng
- **Options:** (nếu có thể) gợi ý các lựa chọn cụ thể

Ví dụ câu hỏi tốt:
```
1. Dashboard MVP cần hiển thị những chỉ số nào?
   - **Priority:** High
   - **Context:** Ảnh hưởng trực tiếp đến effort frontend và timeline
   - **Options:**
     - A. Chỉ số task theo status (todo/in-progress/done)
     - B. Thêm số task theo owner
     - C. Thêm số task theo deadline (overdue/upcoming)
     - D. Tất cả các trên + biểu đồ

2. Có cần attachment trong MVP hay để phase sau?
   - **Priority:** Medium
   - **Context:** Nếu cần thì phải thêm file storage và upload logic
   - **Options:**
     - A. Cần ngay trong MVP
     - B. Để phase 2
```

Ví dụ câu hỏi không tốt (quá chung chung):
```
❌ Dashboard cần những gì?
❌ Có cần thêm tính năng gì không?
```

### 6. Ưu tiên phục vụ bước tiếp theo trong workflow PM
Output phải giúp dùng tiếp cho một trong các việc sau:
- tạo `charter.md`
- tạo `requirements.md`
- tạo `spec.md`
- tạo `plan.md`
- tạo action items

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Mục tiêu thật sự của dự án là gì?
- Người dùng đang muốn kết quả cuối cùng nào?
- Phạm vi nào đã rõ, phạm vi nào chưa rõ?
- Có bao nhiêu nhóm yêu cầu khác nhau?
- Có xung đột nào trong mô tả không?
- Có phụ thuộc nào vào người, hệ thống, nền tảng, công cụ khác không?
- Có tiêu chí thành công nào đã được nói ra hoặc ngầm hiểu không?
- **Những câu hỏi nào ảnh hưởng mạnh nhất đến scope/timeline/architecture?**
- **Có thể gợi ý options cụ thể nào để stakeholder dễ trả lời?**
- **Câu hỏi nào là Critical/High, câu nào có thể để sau?**

## Liên hệ với workflow PM

Skill này nên chạy trước các skill:
- `project-charter-generator`
- `requirements-document-generator`
- `project-spec-generator`
- `project-plan-generator`

Đây là skill nền giúp làm sạch đầu vào cho toàn bộ nhóm skill tạo tài liệu.

## Liên hệ với cấu trúc dự án

Skill này không tạo trực tiếp file trong `projects/[project-name]/`, nhưng output của nó là đầu vào quan trọng để tạo:
- `01-initiation/charter.md`
- `01-initiation/requirements.md`
- `02-planning/spec.md`
- `02-planning/plan.md`

## Tiêu chí hoàn thành tốt

Một output tốt khi:
- đọc xong là hiểu dự án đang cần gì
- nhìn ra rõ phần nào đã rõ, phần nào chưa rõ
- **có danh sách câu hỏi xác nhận ngắn, sắc, dùng được ngay**
- **mỗi câu hỏi có priority, context, và options cụ thể**
- có thể dùng trực tiếp để chuyển sang bước viết tài liệu PM

## Lỗi thường gặp cần tránh

- trộn lẫn fact với suy đoán
- viết lại nguyên văn đầu vào nhưng không bóc tách gì thêm
- **hỏi quá nhiều câu nhỏ không quan trọng**
- **câu hỏi quá chung chung, không có options cụ thể**
- **câu hỏi thiếu priority và context**
- bỏ sót ràng buộc quan trọng
- không chỉ ra phần nào còn mơ hồ
- biến output thành tài liệu yêu cầu hoàn chỉnh quá sớm

## Cách dùng ngắn gọn

1. Đọc đầu vào thô
2. Tóm tắt lại ý chính
3. Tách yêu cầu theo nhóm
4. Đánh dấu phần chưa rõ
5. Sinh câu hỏi xác nhận
6. Đề xuất bước tiếp theo phù hợp

## Tài nguyên đi kèm

- `template-input.md` - mẫu đầu vào tham khảo
- `template-output.md` - mẫu đầu ra chuẩn
- `references/clarification-questions-guide.md` - hướng dẫn viết câu hỏi xác nhận hiệu quả
- `examples/` - ví dụ test thực tế

## Khi nào nên đọc thêm tài liệu tham chiếu

- Nếu đầu vào còn mơ hồ và cần đặt câu hỏi làm rõ: đọc `references/clarification-questions-guide.md`
- Nếu đang phân vân câu hỏi nào nên hỏi trước: đọc `references/clarification-questions-guide.md`
- Nếu cần ví dụ câu hỏi tốt vs không tốt: đọc `references/clarification-questions-guide.md`
