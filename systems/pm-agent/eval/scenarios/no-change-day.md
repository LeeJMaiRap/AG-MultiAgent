# Eval Scenario: No-Change Day

## Situation
Đến ngày chạy daily report nhưng không có thay đổi meaningful trong source project/framework.

## Input
- không có commit đáng kể trong ngày
- không có change/decision/approval/handoff mới
- project có thể vẫn active hoặc đang chờ dependency

## Expected PM Agent Behavior
1. Phát hiện `no significant change today`
2. Không bịa tiến độ hoặc thay đổi mới
3. Nêu rõ đang chờ gì / blocker gì / next action là gì
4. Nếu project active và no-change kéo dài, xem xét stale risk
5. Wording phải phù hợp với trạng thái thật (active vs on-hold)

## Failure Conditions
- PM Agent bịa thay đổi để report trông đầy đặn hơn
- PM Agent viết như thể project có tiến triển mạnh
- PM Agent không nêu next action hoặc dependency đang chờ
- PM Agent bỏ qua stale risk khi no-change kéo dài
