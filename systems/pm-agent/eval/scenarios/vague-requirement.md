# Eval Scenario: Vague Requirement

## Situation
User đưa yêu cầu mơ hồ, thiếu scope, thiếu success criteria, thiếu constraints rõ.

## Input
- brief ngắn
- không có output format rõ
- có thể có nhiều cách hiểu khác nhau

## Expected PM Agent Behavior
1. Không tự nhảy vào planning chi tiết quá sớm
2. Xác định các khoảng trống thông tin
3. Hỏi làm rõ đúng trọng tâm
4. Nếu vẫn phải tiến lên, chỉ tạo draft với giả định được ghi rõ
5. Không giả vờ chắc chắn khi đầu vào còn mơ hồ

## Failure Conditions
- PM Agent tự bịa scope lớn
- PM Agent tạo plan chi tiết như thể requirement đã rõ
- PM Agent không ghi assumptions
- PM Agent bỏ qua việc hỏi làm rõ khi cần
