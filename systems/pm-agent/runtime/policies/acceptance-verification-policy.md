# Acceptance Verification Policy

Quy định chuẩn để PM Agent xác minh một task, issue hoặc project có thực sự đủ điều kiện được đánh dấu hoàn tất hay chưa.

## Mục tiêu

Policy này giúp:
- tránh `done giả`
- buộc có bằng chứng trước khi đóng task/issue/project
- tăng độ tin cậy cho status dashboard, daily report và closure
- giảm mâu thuẫn giữa task board, project metadata và tình trạng thực tế

## Nguyên tắc cứng

1. **Không có bằng chứng tối thiểu → không đánh dấu done**
2. **Không có tiêu chí chấp nhận rõ → không được kết luận task hoàn tất một cách mạnh**
3. **Issue chỉ được close khi có resolution rõ và đã verify ở mức phù hợp**
4. **Project chỉ được close khi deliverables, approvals và final docs đã đủ**

---

# 1. Task acceptance

## Một task được xem là done khi nào?

Một task chỉ được xem là **Done** khi thỏa tối thiểu các điều kiện sau:

- có output hoặc kết quả cụ thể
- output khớp với mục tiêu của task
- không còn blocker trực tiếp ngăn task đó được xem là xong
- có ít nhất một dạng evidence tối thiểu
- đã cập nhật task board

## Evidence tối thiểu cho task

Tùy loại task, evidence có thể là một hoặc nhiều trong các loại sau:

### Với task tài liệu
- file tài liệu đã tồn tại
- nội dung đủ section chính theo template/rule
- path của tài liệu được ghi rõ

### Với task kỹ thuật/code
- file/code đã được tạo hoặc sửa
- có build/test output, hoặc
- có kiểm tra thực tế tối thiểu, hoặc
- có ghi rõ limitation nếu chưa verify được đầy đủ

### Với task vận hành/PM
- artifact tương ứng đã được cập nhật
- decision/change/issue/task state phản ánh đúng
- next action hoặc status mới đã được log

## Khi nào task chưa được coi là done?

Task **chưa được coi là done** nếu:
- mới chỉ “đã làm một phần”
- output có nhưng chưa khớp acceptance criteria
- còn blocker trực tiếp chưa xử lý
- chưa có bằng chứng tối thiểu
- source-of-truth còn mâu thuẫn rõ ràng

## Trạng thái thay thế

Nếu chưa đủ done, dùng một trong các trạng thái sau:
- `In Progress`
- `Blocked`
- `Pending Verification`
- `Partial`

**Khuyên dùng:** nếu task xong phần chính nhưng thiếu verify, dùng `Pending Verification` thay vì `Done`.

---

# 2. Issue acceptance

## Một issue được close khi nào?

Issue chỉ được xem là resolved/closed khi:
- có root cause hoặc giải thích đủ dùng
- có resolution cụ thể
- có actor chịu trách nhiệm xử lý
- có ít nhất một kiểm tra xác minh phù hợp
- issue log đã được cập nhật

## Evidence tối thiểu cho issue
- resolution note
- resolved by / resolved actor
- resolved date
- nếu có thể: verified by / verified actor

## Không được close issue khi
- chỉ mới “có vẻ ổn”
- chưa có resolution note rõ
- fix có thể đã áp dụng nhưng chưa verify tối thiểu
- issue bị quên cập nhật log

---

# 3. Project acceptance

## Một project chỉ được close khi
- deliverable chính đã hoàn thành hoặc được owner chấp nhận rõ ràng
- không còn blocker critical chưa được chấp nhận
- task board / issue log / change log / status dashboard phản ánh trạng thái cuối
- final report đã có
- lessons learned đã có (nếu policy yêu cầu)
- closure approval đã được ghi lại

## Nếu project chỉ ở mức demo-ready
Không được gọi là production-ready.

Có thể dùng các kết luận như:
- `demo-ready`
- `validation complete`
- `pilot-ready`
- `on-hold after validation`

Nhưng không được tự nâng thành `production complete` nếu chưa đủ bằng chứng.

---

# 4. Verification levels

## Level 0 - No verification
- mới có output thô
- chưa có bằng chứng đủ
- không được mark done

## Level 1 - Basic verification
- có artifact/output rõ
- có review cơ bản
- đủ để mark done có điều kiện với task nhỏ/rủi ro thấp

## Level 2 - Functional verification
- có kiểm tra thực tế / đối chiếu rõ hơn
- đủ để close phần lớn task kỹ thuật/vận hành

## Level 3 - Closure-grade verification
- đủ để dùng cho milestone quan trọng hoặc closure
- có evidence, acceptance mapping, và trạng thái đồng nhất giữa các source chính

---

# 5. Conflict rule

Nếu source-of-truth lệch nhau (ví dụ task board vs project metadata):
- không được đánh dấu hoàn tất mạnh nếu conflict ảnh hưởng đến kết luận
- phải ghi conflict
- phải có next action để resolve conflict

## Xử lý conflict giữa các source

### Nguyên tắc ưu tiên source khi conflict

**Khi task board và project.yaml lệch nhau về metrics:**

1. **Ưu tiên task board** nếu:
   - task board có chi tiết từng task rõ ràng
   - có evidence cụ thể cho từng task done
   - task board được cập nhật gần đây hơn

2. **Ưu tiên project.yaml** nếu:
   - task board chưa được cập nhật kịp
   - có approval/decision rõ ràng về số liệu trong project.yaml
   - project.yaml phản ánh kết quả sau verification/acceptance

3. **Không tin cả hai** nếu:
   - lệch quá lớn (ví dụ: 19 vs 2)
   - không có evidence rõ cho cả hai
   - không rõ source nào được cập nhật sau

### Case study: Conflict 19 vs 2

**Tình huống:**
- `project.yaml`: `completed_tasks: 19`
- `task-board.md`: `Completed: 2`
- Lệch: 17 tasks

**Phân tích:**
- Lệch quá lớn → không thể là sai số nhỏ
- Có thể:
  - task board chưa cập nhật kịp
  - project.yaml ghi nhầm/tự động tính sai
  - có task done nhưng chưa move vào Done section
  - có task được mark done không đúng acceptance criteria

**Hành động bắt buộc:**
1. **Không kết luận tiến độ mạnh** cho tới khi resolve
2. **Audit từng task** trong task board:
   - Đếm lại số task thực sự done
   - Kiểm tra evidence cho từng task done
   - Xác định task nào thiếu evidence
3. **Đối chiếu với artifacts khác:**
   - change log
   - issue log
   - handoffs
   - git commits
   - evidence folder
4. **Chọn source đúng:**
   - Nếu task board có evidence đầy đủ → tin task board, sửa project.yaml
   - Nếu có 19 tasks thực sự done nhưng task board chưa cập nhật → cập nhật task board, giữ project.yaml
   - Nếu không rõ → mark conflict unresolved, không dùng cả hai số liệu
5. **Ghi change log** về việc resolve conflict
6. **Update cả hai source** cho khớp sau khi xác định đúng

### Rule cứng cho conflict resolution

1. **Không tự chọn số đẹp hơn** để report
2. **Không average hai số** (ví dụ: (19+2)/2 = 10.5)
3. **Không bỏ qua conflict** và tiếp tục như không có gì
4. **Phải có audit trail** cho quyết định chọn source nào
5. **Phải cập nhật source sai** sau khi resolve
6. **Phải ghi lý do** tại sao conflict xảy ra để tránh lặp lại

---

# 6. Required fields khuyên dùng

## Task done entry nên có
- task id
- actor
- actual effort (nếu có)
- completed date
- evidence note hoặc reference
- verification level (nếu task quan trọng)

## Issue resolved entry nên có
- resolved by
- resolved actor
- resolved date
- resolution
- verified by / verified actor (nếu có)

## Project closure nên có
- final report
- closure approval
- final status wording đúng
- known gaps còn lại (nếu có)

---

# 7. Kết luận ngắn

Nguyên tắc cứng:
- **Done = có evidence tối thiểu + không còn blocker trực tiếp + trạng thái source-of-truth đủ nhất quán**
- **Close issue = có resolution + verify tối thiểu**
- **Close project = có deliverables + docs + approval + wording đúng mức hoàn tất**
