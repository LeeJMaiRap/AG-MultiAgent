# Stale Project Detection Checklist

## Task stale check
- [ ] Có task `In Progress` nào không update > 3 ngày?
- [ ] Có task `Blocked` nào không có action/escalation > 2 ngày?
- [ ] Có task assign rồi nhưng không có output/evidence mới?

## Approval stale check
- [ ] Có approval nào pending quá timeout?
- [ ] Có approval stale nhưng chưa follow-up?

## Issue stale check
- [ ] Có high-severity issue không update > 2 ngày?
- [ ] Có medium/low issue không update > 5 ngày?

## Project stale check
- [ ] Project `active` có thiếu meaningful update > 3 ngày?
- [ ] Project `active` có thực chất đã dừng nhưng chưa đổi status?
- [ ] Có conflict giữa metadata status và trạng thái thực tế?

## Escalation check
- [ ] Nếu stale nhẹ: đã ghi vào report/dashboard chưa?
- [ ] Nếu stale rõ: đã thêm next action chưa?
- [ ] Nếu stale nặng: đã đề xuất đổi status hoặc escalate owner chưa?
