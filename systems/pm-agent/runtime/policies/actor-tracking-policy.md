# Actor Tracking Policy

Quy định chuẩn để PM Agent xác định và ghi nhận **ai đã thực hiện thay đổi** trong workflow dự án.

## Mục tiêu

Actor tracking giúp:
- truy được ai đã làm thay đổi nào
- tăng độ tin cậy cho daily report
- hỗ trợ audit / handoff / lessons learned
- giảm mơ hồ giữa human, main agent và subagent

## Actor format chuẩn

Chỉ dùng các format sau:

- `human:[name]`
- `agent:main`
- `subagent:[label-or-session]`
- `unknown`

## Ý nghĩa từng loại actor

### `human:[name]`
Dùng khi thay đổi được thực hiện bởi người thật và có thể xác định tên đủ chắc chắn.

Ví dụ:
- `human:Doanh`
- `human:Nguyen Van A`

### `agent:main`
Dùng khi thay đổi được thực hiện bởi main OpenClaw agent trong session chính.

Ví dụ:
- cập nhật file PM
- tái cấu trúc workspace
- tạo report
- chuẩn hóa runtime

### `subagent:[label-or-session]`
Dùng khi thay đổi được thực hiện bởi subagent / child session có danh tính riêng.

Ưu tiên:
1. label dễ đọc nếu có
2. session key rút gọn nếu không có label

Ví dụ:
- `subagent:sa-fix-runtime`
- `subagent:child-abc123`

### `unknown`
Dùng khi **không đủ bằng chứng chắc chắn** để xác định actor.

**Không được thay `unknown` bằng phỏng đoán.**

## Thứ tự ưu tiên xác định actor

Khi cần gán actor cho một thay đổi, dùng thứ tự sau:

1. **Explicit actor trong chính artifact**
   - ví dụ field `Actor:` trong handoff / change / issue / decision

2. **Handoff records**
   - nếu task được giao cho subagent/worker và có kết quả rõ ràng

3. **Change log / decision log / issue log / approvals**
   - nếu đã ghi rõ requested by / approved by / resolved by / owner

4. **Git author / git commit context**
   - chỉ dùng như tín hiệu hỗ trợ, không phải lúc nào cũng đủ để xác định actor logic trong workflow

5. **Session context đáng tin cậy**
   - ví dụ main session vừa tạo subagent và ghi rõ đầu ra thuộc subagent nào

6. **`unknown`**
   - nếu các nguồn trên không đủ chắc chắn

## Khi nào KHÔNG được bịa actor

Không được tự gán actor cụ thể nếu:
- chỉ có suy luận mơ hồ từ ngữ cảnh chat
- git author không phản ánh đúng actor workflow
- file bị sửa qua nhiều bước nhưng không có attribution rõ
- không có handoff / log / decision / explicit field

Khi đó phải ghi:
- `unknown`
- và nếu cần, thêm note ngắn giải thích nguồn chưa đủ

## Quy tắc ghi actor vào artifact

### Task board
Nếu một task được cập nhật trạng thái quan trọng, nên có actor trong dòng note hoặc cột phụ.

Ví dụ:
- `Updated by: agent:main`
- `Completed by: subagent:sa-build-api`

### Change log
Mỗi change entry nên có:
- `Requested by:`
- `Implemented by:`
- `Approved by:` (nếu có)

### Issue log
Mỗi issue nên có thể hiện:
- `Reported by:`
- `Resolved by:`
- `Verified by:`

### Handoffs
Mỗi handoff phải có:
- `Assigned by:`
- `Assigned to:`
- `Result returned by:`

### Decisions
Mỗi decision nên có:
- `Made by:`
- `Approved by:` nếu applicable

### Approvals
Mỗi approval phải có:
- `Approver:`
- `Requested by:` nếu có flow request riêng

## Quy tắc cho daily reports

Daily report phải:
- ưu tiên actor có bằng chứng
- tách rõ human / main agent / subagent / unknown
- không trộn actor hành chính với actor thực thi nếu chưa rõ
- ghi limitation nếu attribution còn yếu

## Quy tắc cho PM Agent framework reports

Khi report cho chính `systems/pm-agent/`:
- thay đổi do em trực tiếp làm → `agent:main`
- yêu cầu / quyết định do anh đưa ra → `human:Doanh`
- subagent chỉ được ghi khi có session evidence rõ
- nếu không có session evidence → không được tự nhận là subagent

## Mức độ tin cậy attribution

Có thể dùng 3 mức nội bộ khi suy nghĩ trước khi ghi:
- **High confidence** - có explicit actor trong artifact
- **Medium confidence** - có handoff / session / git + context khớp rõ
- **Low confidence** - chỉ có suy luận yếu

Chỉ nên ghi actor cụ thể khi confidence ở mức High hoặc Medium rõ ràng.
Nếu Low → dùng `unknown`.

## Kết luận ngắn

Nguyên tắc cứng:
- **Có bằng chứng thì gán actor**
- **Không đủ bằng chứng thì dùng `unknown`**
- **Không bịa actor để làm report đẹp hơn**
