# PM Agent Regression Pack Checklist

## Core Workflow
- [ ] Vague requirement được xử lý đúng
- [ ] Scope change được xử lý đúng
- [ ] Worker failure được xử lý đúng
- [ ] Missing approval được xử lý đúng
- [ ] False done được xử lý đúng
- [ ] Stale project được xử lý đúng
- [ ] Source conflict được xử lý đúng
- [ ] On-hold project in active path được xử lý đúng
- [ ] No-change day được xử lý đúng
- [ ] Missing actor được xử lý đúng

## Governance
- [ ] Actor attribution không bị bịa
- [ ] Approval rules không bị bỏ qua
- [ ] Acceptance verification được áp dụng đúng
- [ ] Source conflict được báo ra, không bị nuốt
- [ ] Lifecycle/path mismatch được phát hiện và log

## Reporting
- [ ] Framework report không bị lẫn với project report
- [ ] Project on-hold không bị report như active bình thường
- [ ] Daily report không tạo kết luận quá mạnh khi evidence yếu
- [ ] No-change được nêu rõ thay vì bịa tiến độ
- [ ] Stale được phát hiện và escalate đúng severity

## Pass Criteria
- Không có failure condition critical nào xảy ra trong các scenario chính
- Mỗi scenario có expected behavior rõ và pass/fail criteria
- Regression pack có thể chạy lại sau mỗi đợt update skill/runtime/policy
