---
name: rules-generator
description: Tạo file `02-planning/rules.md` - bộ nguyên tắc làm việc cho dự án từ charter, requirements, spec hoặc bối cảnh team; dùng khi cần chuẩn hóa coding standards, git workflow, testing standards, documentation standards, quality gates và change management trước khi execution.
---

# Rules Generator

## Mục tiêu

Tạo tài liệu Project Rules để thống nhất cách làm việc trong dự án trước khi bước vào execution, giúp giảm lỗi, giảm mâu thuẫn cách làm và tăng tính nhất quán.

Skill này giúp:
- chốt coding standards theo công nghệ của dự án
- xác định git workflow và commit/branch convention
- đặt ra testing standards và documentation standards
- tạo quality gates trước khi merge hoặc release
- xác định quy trình change management và các rule vận hành quan trọng khác

## Dùng khi nào

Dùng skill này khi:
- đã có spec hoặc ít nhất đã rõ stack và cách triển khai
- cần chuẩn hóa cách làm việc trước khi bắt đầu execution
- team/agent cần một bộ rule thống nhất để làm theo
- cần giới hạn sai lệch về coding style, workflow và quality

## Không dùng khi nào

Không dùng skill này khi:
- đầu vào chưa rõ stack hoặc chưa rõ loại dự án
- mục tiêu là lập kế hoạch phase/task (dùng `project-plan-generator`)
- mục tiêu là tạo task board hằng ngày
- chỉ cần một vài ghi chú kỹ thuật nhỏ, không cần bộ rules hoàn chỉnh

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- project spec
- project plan
- charter + yêu cầu về stack/cách làm việc

## Input tùy chọn

- stack công nghệ cụ thể
- team size / vai trò
- quy trình git hiện tại
- yêu cầu testing
- yêu cầu security/performance/accessibility
- deployment flow

## Output

Output là file `rules.md` theo cấu trúc chuẩn với tối thiểu 6 phần:

1. **Coding Standards**
2. **Git Workflow**
3. **Testing Standards**
4. **Documentation Standards**
5. **Quality Gates**
6. **Change Management**

Tùy dự án có thể bổ sung:
7. **Security Standards**
8. **Performance Standards**
9. **Accessibility Standards**
10. **Deployment Standards**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/rules-template.md`, và được phép mở rộng khi dự án cần rule cụ thể hơn.

## Quy tắc xử lý

### 1. Rules phải bám sát stack thực tế
Nếu dự án dùng React + Node.js thì rules phải phản ánh đúng stack đó, ví dụ:
- React hooks / component conventions
- Node.js async/await
- naming conventions phù hợp JS ecosystem

Không được viết rules chung chung không dùng được.

### 2. Chỉ tạo rule có tính vận hành
Rules phải là thứ team/agent có thể áp dụng được trong thực tế, không nên là các câu khẩu hiệu mơ hồ như:
- “code thật đẹp”
- “làm cẩn thận”
- “viết chuẩn”

### 3. Quality gates phải kiểm tra được
Mỗi quality gate phải là điều kiện có thể xác minh, ví dụ:
- [ ] tests passed
- [ ] code review passed
- [ ] no critical bugs
- [ ] documentation complete

### 4. Git workflow phải đủ rõ để tránh hỗn loạn
Ít nhất cần có:
- branch naming
- commit message format
- yêu cầu trước khi merge / PR

### 5. Testing standards phải tương ứng với mức độ dự án
Nếu là MVP, có thể ưu tiên manual testing + smoke test.
Nếu là production-grade, nên bổ sung unit/integration/e2e expectations.

Không áp tiêu chuẩn quá nặng nếu không phù hợp thực tế.

### 6. Change management phải giúp kiểm soát scope
Phần này cần nêu rõ:
- thay đổi được yêu cầu như thế nào
- ai phê duyệt
- cần đánh giá ảnh hưởng gì

### 7. Phần mở rộng chỉ thêm khi có giá trị
Security / performance / accessibility / deployment standards chỉ nên bổ sung khi:
- đầu vào có nhu cầu thật
- dự án có rủi ro tương ứng
- team cần rule đó để tránh lỗi lặp lại

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Dự án đang dùng stack gì?
- Team hiện tại cần kiểm soát lỗi ở đâu nhiều nhất: code style, git, testing hay deployment?
- Có yêu cầu bảo mật hoặc hiệu năng nào đáng chú ý không?
- Có cần accessibility standards không?
- Đây là MVP nhanh hay dự án cần kỷ luật chặt hơn?
- Những rule nào là “must-have” và những rule nào là “nice-to-have”?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `project-spec-generator`
- `project-plan-generator`

Và hỗ trợ cho:
- `task-board-builder`
- execution workflow
- code review / QA / release process

Đây là tài liệu định chuẩn cách làm, không phải tài liệu mô tả yêu cầu hay kỹ thuật thuần túy.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/02-planning/rules.md
```

File này là bộ nguyên tắc nền cho toàn bộ quá trình implementation.

## Tiêu chí hoàn thành tốt

Một rules document tốt khi:
- bám sát stack và cách làm việc thực tế
- có thể dùng trực tiếp để hướng dẫn người/agent thực thi
- quality gates rõ ràng, kiểm tra được
- git workflow đủ để tránh rối
- testing/documentation standards đủ dùng, không quá hình thức
- có kiểm soát thay đổi hợp lý

## Lỗi thường gặp cần tránh

- viết rules quá chung chung
- copy nguyên rule template mà không tùy biến theo dự án
- quality gates không đo được
- testing standards quá nặng hoặc quá nhẹ so với dự án
- không có change management
- thêm quá nhiều rule phụ mà không có giá trị thực tế

## Cách dùng ngắn gọn

1. Đọc spec / plan / stack hiện có
2. Xác định những rule bắt buộc cho coding, git, test, docs
3. Viết quality gates có thể kiểm tra
4. Xác định change management
5. Bổ sung security / performance / deployment rules nếu cần
6. Xuất file `rules.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ rules thực tế
- Tham khảo: `systems/pm-agent/templates/rules-template.md`
- Tham khảo: `projects/active/web-ban-hang/02-planning/rules.md`
