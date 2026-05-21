# Requirements Agent Report

## Scope
- Xây mini TODO CLI bằng Node.js, chạy local-only trong workspace.
- Chức năng cốt lõi:
  - Thêm TODO
  - Liệt kê TODO
  - Đánh dấu hoàn thành
  - Xoá TODO
- Lưu dữ liệu local file (ví dụ JSON), không dùng DB ngoài.
- Tạo evidence giao việc/handoff rõ giữa agents và output file theo vai.

## Acceptance Criteria
1. CLI chạy bằng Node.js có thể thực hiện đủ 4 thao tác: add/list/done/delete.
2. Dữ liệu TODO được giữ lại sau nhiều lần chạy (persist local file).
3. Có xử lý input lỗi cơ bản (thiếu tham số, id không hợp lệ) với thông báo rõ.
4. Không cài package mới; chỉ dùng built-in Node.js.
5. Có file handoff sang Backend và QA có thể test luồng chính.

## Non-goals
- Không làm UI web/mobile.
- Không auth, multi-user, sync cloud.
- Không deploy, không dùng secrets.
- Không tối ưu hiệu năng nâng cao, không refactor lớn ngoài phạm vi demo.

## Notes
- Mục tiêu chính demo: thể hiện phối hợp sub-agents qua chat + artefacts, không phải feature-rich product.
