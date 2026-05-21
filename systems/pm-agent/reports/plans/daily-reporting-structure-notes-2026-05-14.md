# Daily Reporting Structure Notes - 2026-05-14

## Chuẩn hóa đã chốt

### Framework reports
- Path: `systems/pm-agent/reports/daily/YYYY-MM-DD.md`
- Dùng để report cho chính PM Agent framework
- Chỉ nên tạo khi framework còn active refinement / production-readiness work

### Project reports
- Path: `projects/active/[project-name]/reports/daily/YYYY-MM-DD.md`
- Dùng để report cho project active
- Không mặc định tạo cho archived projects

### Status handling
- `active` → có thể chạy daily bình thường
- `on-hold` → chỉ tạo nếu có lý do hoặc chế độ theo dõi riêng
- `stopped` → không nên tạo daily mặc định
- `archived` → không chạy daily mặc định

### Naming rule
- Mặc định: `YYYY-MM-DD.md`
- 1 file/ngày là chuẩn

### Source of truth
- Framework report → `systems/pm-agent/STATUS.md`, runtime, eval, skills, git log
- Project report → `project.yaml`, task/change/issue/status, decisions, approvals, handoffs, git log

## Kết luận
Phase 1.4 hoàn tất khi skill và policy đã phản ánh rõ sự tách biệt framework vs project reporting.
