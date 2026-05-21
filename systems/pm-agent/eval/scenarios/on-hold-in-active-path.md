# Eval Scenario: On-Hold Project In Active Path

## Situation
Project nằm trong `projects/active/` nhưng metadata `project.yaml` ghi `status: on-hold`.

## Input
- path = `projects/active/[project-name]`
- metadata status = `on-hold`
- selector/report có nguy cơ hiểu sai nếu bám path thay vì metadata

## Expected PM Agent Behavior
1. Ưu tiên metadata làm source of truth
2. Không report project này như active delivery project
3. Log path/metadata mismatch
4. Đề xuất migrate path hoặc xác nhận lại status nếu cần
5. Trong cron selector audit, target phải bị skip đúng lý do

## Failure Conditions
- PM Agent coi project là active chỉ vì folder path
- PM Agent generate project daily report như active bình thường
- PM Agent không log mismatch
- PM Agent không đề xuất action để xử lý mismatch
