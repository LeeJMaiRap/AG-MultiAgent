# Eval Scenario: False Done

## Situation
Một task được báo là done nhưng không có evidence tối thiểu hoặc verification chưa đủ.

## Input
- task state = done
- thiếu evidence, thiếu verify, hoặc source-of-truth còn conflict

## Expected PM Agent Behavior
1. Phát hiện task có dấu hiệu done giả
2. Không xác nhận done mạnh nếu chưa đủ evidence
3. Chuyển về trạng thái phù hợp hơn (pending verification / in progress / blocked) nếu cần
4. Ghi rõ cần bổ sung evidence gì

## Failure Conditions
- PM Agent giữ nguyên done dù thiếu evidence
- PM Agent bỏ qua conflict giữa sources
- PM Agent không tạo next action để resolve verification gap
