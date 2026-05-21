---
name: requirements-document-generator
description: Tạo file `01-initiation/requirements.md` - tài liệu tổng hợp yêu cầu chi tiết từ requirement clarification, charter hoặc meeting notes; dùng khi cần tạo tài liệu yêu cầu chính thức với business requirements, functional requirements, non-functional requirements, user stories và traceability matrix theo chuẩn PM.
---

# Requirements Document Generator

## Mục tiêu

Tạo tài liệu Requirements chính thức để ghi nhận đầy đủ yêu cầu nghiệp vụ, chức năng và phi chức năng của dự án, làm cơ sở cho giai đoạn planning và execution.

Skill này giúp:
- chuyển requirement clarification thành tài liệu yêu cầu có cấu trúc chuẩn PM
- phân loại rõ business requirements, functional requirements, non-functional requirements
- định nghĩa acceptance criteria cho từng yêu cầu chức năng
- tạo user stories nếu dự án theo Agile
- xây dựng traceability matrix để liên kết yêu cầu với task

## Dùng khi nào

Dùng skill này khi:
- đã có requirement clarification hoặc charter
- cần tạo tài liệu yêu cầu chi tiết chính thức
- cần phân loại và cấu trúc hóa yêu cầu trước khi thiết kế kỹ thuật
- cần có tài liệu để làm cơ sở cho spec và plan

## Không dùng khi nào

Không dùng skill này khi:
- yêu cầu còn quá mơ hồ, chưa qua requirement clarification
- mục tiêu là tạo đặc tả kỹ thuật chi tiết (dùng `project-spec-generator`)
- mục tiêu là tạo kế hoạch triển khai (dùng `project-plan-generator`)
- chỉ cần cập nhật một vài yêu cầu, không cần tạo tài liệu mới

## Input bắt buộc

Ít nhất phải có:
- requirement clarification đã hoàn chỉnh
- hoặc charter + meeting notes chi tiết
- danh sách yêu cầu chính đã được làm rõ

## Input tùy chọn

- charter đã có
- user stories nếu đã được định nghĩa
- acceptance criteria đã được thảo luận
- non-functional requirements đã biết
- traceability với task nếu đã có

## Output

Output là file `requirements.md` theo cấu trúc chuẩn với 5 phần:

1. **Business Requirements**
2. **Functional Requirements**
3. **Non-Functional Requirements**
4. **User Stories** (nếu dùng Agile)
5. **Traceability Matrix**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải tuân thủ template có sẵn trong `systems/pm-agent/templates/requirements-template.md`.

## Quy tắc xử lý

### 1. Phân loại yêu cầu đúng bản chất
- **Business Requirements (BR):** yêu cầu nghiệp vụ, mục tiêu kinh doanh
- **Functional Requirements (FR):** yêu cầu chức năng cụ thể
- **Non-Functional Requirements (NFR):** yêu cầu về hiệu năng, bảo mật, usability, v.v.

Không được trộn lẫn các loại yêu cầu.

### 2. Mỗi functional requirement phải có acceptance criteria
Acceptance criteria phải:
- rõ ràng, đo lường được
- có thể kiểm chứng
- dạng checklist

Ví dụ tốt:
- [ ] Hiển thị ít nhất 12 sản phẩm mỗi trang
- [ ] Có phân trang
- [ ] Responsive trên mobile và desktop

Ví dụ xấu:
- Hiển thị sản phẩm đẹp
- Phân trang tốt

### 3. Functional requirement phải có Input-Process-Output
Mỗi FR nên mô tả:
- **Input:** đầu vào từ người dùng hoặc hệ thống
- **Process:** xử lý logic
- **Output:** kết quả trả về

### 4. Non-functional requirements phải có metric
Mỗi NFR phải có chỉ số đo lường cụ thể:
- Performance: "Trang chủ load < 3 giây"
- Security: "Password được hash bằng bcrypt"
- Usability: "Responsive trên mobile (375px), tablet (768px), desktop (1024px+)"

### 5. User stories theo format chuẩn
Nếu dự án dùng Agile, user stories phải theo format:
```
Là [vai trò], tôi muốn [hành động] để [mục đích]
```

Mỗi user story phải có:
- acceptance criteria
- priority
- estimate (nếu có)

### 6. Traceability matrix phải liên kết đầy đủ
Mỗi requirement phải được liên kết với:
- type (Business/Functional/Non-Functional)
- priority
- status
- linked tasks (nếu đã có)

### 7. Đánh số ID rõ ràng
- Business Requirements: BR-001, BR-002, ...
- Functional Requirements: FR-001, FR-002, ...
- Non-Functional Requirements: NFR-001, NFR-002, ...
- User Stories: US-001, US-002, ...

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Yêu cầu nào là nghiệp vụ (business), yêu cầu nào là chức năng (functional)?
- Mỗi chức năng có input/process/output rõ ràng không?
- Acceptance criteria có thể kiểm chứng được không?
- Có yêu cầu phi chức năng nào về performance, security, usability không?
- Nếu dùng Agile, có thể viết thành user stories không?
- Yêu cầu nào liên kết với task nào?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `requirement-clarifier`
- `project-charter-generator`

Và là đầu vào cho:
- `project-spec-generator`
- `project-plan-generator`
- `wbs-generator`

Requirements document là tài liệu quan trọng thứ 2 trong giai đoạn Initiation (sau charter).

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/01-initiation/requirements.md
```

File này là cơ sở cho toàn bộ tài liệu planning và execution.

## Tiêu chí hoàn thành tốt

Một requirements document tốt khi:
- phân loại yêu cầu rõ ràng (BR/FR/NFR)
- mỗi functional requirement có acceptance criteria đầy đủ
- non-functional requirements có metric cụ thể
- user stories (nếu có) theo format chuẩn
- traceability matrix liên kết đầy đủ
- có thể dùng làm cơ sở để tạo spec và plan

## Lỗi thường gặp cần tránh

- trộn lẫn business requirements với functional requirements
- functional requirements thiếu acceptance criteria
- acceptance criteria quá mơ hồ, không đo lường được
- non-functional requirements không có metric
- user stories không theo format chuẩn
- thiếu traceability matrix
- đánh số ID không nhất quán

## Cách dùng ngắn gọn

1. Đọc requirement clarification hoặc charter
2. Phân loại yêu cầu thành BR/FR/NFR
3. Viết acceptance criteria cho mỗi FR
4. Định nghĩa metric cho mỗi NFR
5. Tạo user stories nếu dự án dùng Agile
6. Xây dựng traceability matrix
7. Xuất file `requirements.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ requirements document thực tế
- Tham khảo: `systems/pm-agent/templates/requirements-template.md`
- Tham khảo: `projects/active/web-ban-hang/01-initiation/requirements.md`
