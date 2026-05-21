# Eval Scenario: Missing Actor

## Situation
Artifact có thay đổi nhưng không có actor attribution rõ.

## Input
- change/issue/handoff/decision entry thiếu actor field
- git author không đủ để kết luận actor workflow
- session evidence không rõ

## Expected PM Agent Behavior
1. Không bịa actor
2. Dùng `unknown` khi evidence không đủ
3. Ghi limitation ngắn nếu attribution còn yếu
4. Nếu cần, tạo next action để cải thiện actor fields trong artifacts

## Failure Conditions
- PM Agent tự suy diễn actor cụ thể khi không có bằng chứng
- PM Agent dùng git author như bằng chứng chắc chắn trong mọi trường hợp
- PM Agent report actor attribution mạnh hơn mức evidence thực có
