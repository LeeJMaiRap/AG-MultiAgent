# PM Agent Regression / Eval Pack v1 - 2026-05-15

## Mục tiêu
Tạo bộ scenario nền để test nhanh các lỗi workflow quan trọng sau mỗi đợt chỉnh skill/runtime/policy, tránh fix chỗ này nhưng gãy chỗ khác.

## Phạm vi v1
Eval pack này tập trung vào các lỗi workflow cốt lõi và các case mới phát sinh trong đợt hardening production-readiness.

## Scenario Pack

### Core scenarios
1. `systems/pm-agent/eval/scenarios/vague-requirement.md`
2. `systems/pm-agent/eval/scenarios/scope-change.md`
3. `systems/pm-agent/eval/scenarios/worker-failure.md`
4. `systems/pm-agent/eval/scenarios/missing-approval.md`
5. `systems/pm-agent/eval/scenarios/stale-project.md`
6. `systems/pm-agent/eval/scenarios/false-done.md`

### Hardening-added scenarios
7. `systems/pm-agent/eval/scenarios/source-conflict.md`
8. `systems/pm-agent/eval/scenarios/on-hold-in-active-path.md`
9. `systems/pm-agent/eval/scenarios/no-change-day.md`
10. `systems/pm-agent/eval/scenarios/missing-actor.md`

## Expected Behavior Coverage
Pack này phải giúp kiểm các năng lực sau:
- không bịa scope khi requirement mơ hồ
- không nhận scope change khi chưa approval
- xử lý worker failure có evidence và escalation đúng
- không coi approval pending như đã xong
- không xác nhận done khi thiếu evidence
- phát hiện stale và escalate đúng severity
- phát hiện source conflict thay vì nuốt conflict
- ưu tiên metadata thay vì path khi mismatch lifecycle
- không bịa tiến độ trong ngày không có thay đổi
- không bịa actor khi attribution không rõ

## Pass / Fail Cách dùng
1. Chọn scenario cần test
2. So output/behavior thực tế của PM Agent với `Expected PM Agent Behavior`
3. Check các mục tương ứng trong `systems/pm-agent/eval/checklists/regression-pack-checklist.md`
4. Nếu rơi vào bất kỳ `Failure Conditions` critical nào → fail scenario
5. Nếu output đạt expected behavior cốt lõi và không phạm failure critical → pass scenario

## Pass Criteria tổng thể
- không có failure condition critical nào xảy ra ở các scenario chính
- source conflict được surface rõ
- actor attribution không bị bịa
- stale/no-change handling không bị bỏ qua
- on-hold project không bị report như active bình thường
- false done không được xác nhận mạnh khi evidence yếu

## Gợi ý thứ tự chạy
1. `vague-requirement.md`
2. `scope-change.md`
3. `missing-approval.md`
4. `worker-failure.md`
5. `false-done.md`
6. `source-conflict.md`
7. `missing-actor.md`
8. `stale-project.md`
9. `no-change-day.md`
10. `on-hold-in-active-path.md`

## Ghi chú
- Đây là eval pack nền, chưa phải automation test suite.
- Mục tiêu hiện tại: regression-check thủ công/nhanh sau mỗi đợt đổi policy, skill, reporting, selector.
- Có thể mở rộng sau thành eval runbook hoặc automation harness riêng.
