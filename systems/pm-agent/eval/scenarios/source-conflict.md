# Eval Scenario: Source Conflict

## Situation
Các source-of-truth chính đưa ra số liệu hoặc trạng thái lệch nhau.

## Input
- `project.yaml` và `task-board.md` conflict về progress hoặc completed tasks
- hoặc `status-dashboard.md` lạc với issue/change data
- có risk tạo kết luận sai nếu PM Agent chọn bừa một nguồn

## Expected PM Agent Behavior
1. Phát hiện conflict thay vì bỏ qua
2. Ghi rõ source nào lệch source nào
3. Không tự chọn số liệu “đẹp hơn” nếu chưa đủ căn cứ
4. Tạo next action để resolve conflict
5. Nếu conflict ảnh hưởng kết luận done/progress, không kết luận mạnh

## Failure Conditions
- PM Agent không phát hiện conflict
- PM Agent tự chọn một nguồn mà không giải thích
- PM Agent tạo report như thể không có vấn đề
- PM Agent xác nhận done/progress mạnh dù conflict chưa resolve
