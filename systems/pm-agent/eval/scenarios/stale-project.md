# Eval Scenario: Stale Project

## Situation
Project vẫn ghi `active` nhưng không có meaningful update trong nhiều ngày.

## Input
- metadata status = active
- thiếu tiến triển thật
- có thể không có issue/approval mới

## Expected PM Agent Behavior
1. Phát hiện stale theo policy
2. Ghi stale vào report/dashboard
3. Tạo next action hoặc escalation
4. Nếu stale nặng, đề xuất đổi status

## Failure Conditions
- PM Agent tiếp tục coi project active bình thường
- PM Agent không log stale
- PM Agent không đề xuất follow-up hoặc status change
