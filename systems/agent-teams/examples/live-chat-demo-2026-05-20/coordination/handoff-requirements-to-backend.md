# Handoff: Requirements -> Backend

## Build Scope
Backend implement TODO CLI mini (Node.js, local):
- `add <text>`: tạo task mới
- `list`: in toàn bộ task với id + trạng thái
- `done <id>`: đánh dấu completed
- `delete <id>`: xoá task

## Functional Rules
- Dùng local JSON file để persist dữ liệu.
- ID duy nhất, ổn định trong 1 dataset.
- `list` hiển thị rõ pending/completed.
- Lệnh sai hoặc thiếu tham số phải trả usage/error message ngắn, dễ hiểu.

## Acceptance Criteria for Backend
- Chạy được tất cả command trên bằng Node.js local.
- Restart process vẫn giữ dữ liệu TODO.
- Không dùng package ngoài (no install).
- Code + output đủ để QA chạy test happy path và invalid input cơ bản.

## Non-goals / Guardrails
- Không thêm web server/API.
- Không tích hợp cloud/DB ngoài.
- Không đụng deploy pipeline.

## Implementation Notes
- Ưu tiên code đơn giản, dễ đọc cho demo.
- Nên tách module nhỏ: parse command, storage, todo service.
- Trả exit code khác 0 khi command invalid để QA dễ assert.
