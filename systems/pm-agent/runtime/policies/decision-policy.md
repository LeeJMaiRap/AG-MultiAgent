# Decision Policy

Quy định về việc ra quyết định trong PM Agent workflow.

## Nguyên tắc chung

1. **Mọi quyết định quan trọng phải được ghi lại**
2. **Quyết định phải có lý do rõ ràng**
3. **Quyết định phải có người chịu trách nhiệm**
4. **Quyết định có thể được rollback nếu cần**

## Phân loại quyết định

### Level 1: Auto-decision (PM Agent tự quyết)
- Chọn task tiếp theo từ task board
- Cập nhật trạng thái task
- Tạo tài liệu theo template
- Phát hiện và log risk/issue
- Cập nhật metrics

**Không cần approval, nhưng phải log.**

### Level 2: Confirm-before-proceed (Xác nhận trước khi làm)
- Thay đổi scope nhỏ
- Thêm/bớt task không ảnh hưởng timeline
- Thay đổi priority task
- Giao task cho worker
- Đóng issue/risk

**Cần thông báo user, user có thể veto.**

### Level 3: Explicit approval required (Phải có approval)
- Thay đổi scope lớn
- Thay đổi timeline/budget
- Thay đổi success criteria
- Đóng project
- Hủy project
- Thay đổi stakeholder

**Phải có approval rõ ràng từ owner trước khi thực hiện.**

## Decision log format

Mỗi quyết định quan trọng phải ghi vào `decisions/decision-log.md`:

```markdown
## [DECISION-ID] - [Title]
- **Date:** YYYY-MM-DD
- **Level:** 1/2/3
- **Made by:** PM Agent / Owner
- **Context:** Tại sao cần quyết định này?
- **Options considered:**
  1. Option A - pros/cons
  2. Option B - pros/cons
- **Decision:** Chọn option X
- **Rationale:** Lý do
- **Impact:** Ảnh hưởng gì
- **Rollback plan:** Nếu cần rollback thì làm thế nào
- **Status:** active / superseded / rolled-back
```

## Khi nào cần escalate?

Escalate lên owner khi:
- Không chắc chắn về quyết định
- Có conflict giữa các stakeholder
- Quyết định ảnh hưởng lớn đến timeline/budget/scope
- Có rủi ro cao
- Cần thay đổi success criteria

## Review cycle

- Decision log phải được review trong closure phase
- Quyết định sai phải được ghi nhận trong lessons learned
- Quyết định tốt phải được ghi nhận để tái sử dụng
