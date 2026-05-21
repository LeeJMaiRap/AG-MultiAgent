# Runbook: Worker Failed

Áp dụng khi worker/subagent fail hoặc trả kết quả không đạt.

## Dấu hiệu
- Worker crash / timeout
- Output thiếu / sai / không usable
- Worker không bám acceptance criteria
- Worker tạo side effects không mong muốn

## Cách xử lý

1. **Xác nhận failure type**
   - technical failure?
   - quality failure?
   - context failure?
   - dependency failure?

2. **Thu thập evidence**
   - lỗi cụ thể
   - output đã có
   - task id
   - acceptance criteria bị fail

3. **Quyết định hướng xử lý**
   - retry với prompt rõ hơn
   - chia nhỏ task
   - PM Agent tự làm
   - escalate nếu high-risk

4. **Cập nhật tài liệu**
   - issue-log.md
   - task-board.md
   - status-dashboard.md
   - handoff note nếu retry

5. **Nếu thay đổi lỗi đã làm bẩn trạng thái project**
   - dùng thêm `project-rollback-recovery.md`
   - quyết định rollback hay recovery có kiểm soát

## Retry policy
- Retry tối đa 2 lần nếu lỗi do prompt/context
- Không retry mù khi lỗi do strategy sai
- Sau 2 lần fail: escalate hoặc đổi approach

## Lesson learned
Sau khi giải quyết, ghi lesson learned nếu failure pattern có thể lặp lại.
