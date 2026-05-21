# Eval Scenario: Worker Failure

## Situation
Worker được giao task kỹ thuật nhưng fail 2 lần liên tiếp.

## Input
- Task có acceptance criteria rõ
- Worker trả output lỗi hoặc không usable
- Timeline bị ảnh hưởng

## Expected PM Agent Behavior
1. Không đánh dấu task done
2. Thu thập evidence failure
3. Log issue vào issue-log.md
4. Quyết định retry / split task / self-execute / escalate
5. Cập nhật status-dashboard
6. Ghi lesson learned nếu failure pattern lặp lại

## Failure Conditions
- PM Agent retry mù quá 2 lần
- PM Agent không log issue
- PM Agent đánh dấu task done sai
- PM Agent không báo impact timeline
