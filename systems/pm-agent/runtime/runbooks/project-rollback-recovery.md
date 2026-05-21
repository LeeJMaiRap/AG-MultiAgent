# Runbook: Project Rollback / Recovery

Áp dụng khi một thay đổi trong project gây lỗi, làm sai trạng thái hệ, hoặc khiến deliverable không còn tin cậy và cần rollback/recovery có kiểm soát.

## Mục tiêu

Runbook này giúp PM Agent:
- không hoảng loạn rollback bừa
- phân biệt rollback logic vs recovery logic
- giữ source-of-truth nhất quán
- log rõ lý do, phạm vi và hậu quả của rollback

---

# 1. Khi nào dùng rollback / recovery

Dùng khi:
- thay đổi mới gây hỏng chức năng chính
- output mới làm lệch deliverable quan trọng
- task bị mark done sai và cần quay lại trạng thái trước
- config/runtime/docs bị cập nhật sai và ảnh hưởng workflow
- có source conflict nghiêm trọng cần trả về baseline gần nhất

Không dùng khi:
- chỉ là thay đổi nhỏ có thể sửa tiến tiếp ngay
- chưa xác định rõ cái gì thật sự bị hỏng
- rollback sẽ gây mất dữ liệu hoặc làm tình hình xấu hơn mà chưa đánh giá impact

---

# 2. Phân biệt rollback và recovery

## Rollback
Quay về trạng thái trước đó đã biết là ổn hơn.

Ví dụ:
- revert file/doc/config về commit trước
- trả task từ `Done` về `In Progress`
- restore baseline plan trước scope change

## Recovery
Không nhất thiết quay ngược, mà đưa hệ về trạng thái dùng được.

Ví dụ:
- giữ phần tốt của thay đổi mới nhưng sửa phần hỏng
- tạo hotfix thay vì revert toàn bộ
- giữ artifact mới nhưng sửa status / evidence / docs cho đúng

---

# 3. Bước xử lý chuẩn

## Bước 1 — Xác định phạm vi hỏng
Trả lời rõ:
- hỏng ở đâu?
- ảnh hưởng artifact nào?
- ảnh hưởng task, issue, approval hay project state?
- có ảnh hưởng user-facing hay chỉ internal?

## Bước 2 — Thu thập baseline an toàn
Tìm trạng thái gần nhất đủ tin cậy:
- git commit tốt gần nhất
- version tài liệu trước đó
- status/project metadata trước thay đổi lỗi
- report hoặc dashboard trước khi lỗi phát sinh

## Bước 3 — Chọn rollback hay recovery
Chọn **rollback** nếu:
- baseline cũ rõ ràng
- thay đổi mới hỏng nhiều hơn lợi
- revert an toàn hơn sửa nóng

Chọn **recovery** nếu:
- chỉ một phần bị lỗi
- rollback toàn phần gây mất tiến triển giá trị
- có thể sửa tại chỗ mà ít rủi ro hơn

## Bước 4 — Ghi log trước khi thao tác
Trước khi rollback/recovery, phải ghi tối thiểu:
- lý do
- phạm vi
- actor quyết định
- baseline được chọn
- rủi ro của thao tác

## Bước 5 — Thực hiện rollback/recovery
Sau khi làm xong, cập nhật:
- task board
- issue log
- change log
- status dashboard
- decision log nếu cần

## Bước 6 — Verify sau recovery
Không được coi là xong chỉ vì đã revert/sửa.
Phải kiểm tra:
- trạng thái mới có ổn hơn không
- source-of-truth đã nhất quán chưa
- cần follow-up gì nữa không

---

# 4. Tối thiểu phải log gì

Khi có rollback/recovery, nên tạo entry kiểu:

```markdown
## RB-001 - [Rollback/Recovery title]
- **Date:** YYYY-MM-DD
- **Type:** Rollback / Recovery
- **Triggered by:** [Issue / conflict / failure]
- **Actor:** [human:... / agent:main / subagent:... / unknown]
- **Scope:** [Files / tasks / project state affected]
- **Baseline chosen:** [commit / file version / prior state]
- **Action taken:** [what was reverted/recovered]
- **Verification:** [how checked afterward]
- **Follow-up:** [what still remains]
```

---

# 5. Rule cứng

1. Không rollback bừa khi chưa xác định baseline tốt hơn
2. Không gọi recovery là thành công nếu chưa verify
3. Không quên cập nhật source-of-truth sau rollback/recovery
4. Nếu rollback/recovery làm thay đổi project status hoặc scope, phải log rõ
5. Nếu có owner-impact lớn, phải escalate/notify theo policy

---

# 6. Khi nào phải escalate owner

Escalate nếu:
- rollback làm mất deliverable đáng kể
- rollback ảnh hưởng scope/timeline lớn
- conflict quá lớn không tự xử lý chắc chắn được
- cần quyết định giữa revert toàn phần và recovery chọn lọc

---

# 7. Kết luận ngắn

Nguyên tắc cứng:
- **Rollback/recovery phải có baseline, lý do, verification và source-of-truth update**
- **Không revert chỉ để “trông sạch hơn” nếu trạng thái mới không thật sự an toàn hơn**
