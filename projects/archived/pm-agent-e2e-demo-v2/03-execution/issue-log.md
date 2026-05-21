# Issue Log: Hệ thống quản lý công việc nội bộ

## Active Issues (Vấn đề đang mở)

### ISS-001: API contract cho task list chưa ổn định
- **Severity:** High
- **Status:** Open
- **Reported by:** Frontend dev
- **Reported date:** 2026-05-16
- **Description:** Frontend chưa thể khóa UI task list vì response schema của task list API còn thay đổi ở field ownerName, pagination wrapper và status enum.
- **Impact:** Chặn TASK-004 và có thể kéo chậm toàn bộ frontend core.
- **Root cause:** Chưa có bước review contract chính thức trước khi backend bắt đầu expose response thử nghiệm. Phân tích 5 Whys sơ bộ cho thấy: (1) schema thay đổi → vì chưa freeze response shape; (2) chưa freeze → vì spec cũ thiếu API contract chi tiết; (3) spec thiếu chi tiết → vì planning trước đó chưa ép phải mô tả request/response; (4) chưa ép mô tả → vì chưa có template/spec guide đủ chặt; (5) template chưa chặt → vì workflow PM Agent bản cũ chưa phát hiện rõ pain point integration.
- **Resolution:** Chốt response schema, publish sample payload và review với frontend trước khi tiếp tục TASK-004.
- **Assigned to:** Backend dev
- **Target resolution:** 2026-05-17

## Resolved Issues (Vấn đề đã giải quyết)

### ISS-002: Lỗi JWT config ban đầu
- **Severity:** Medium
- **Status:** Resolved
- **Reported by:** Backend dev
- **Reported date:** 2026-05-14
- **Resolved by:** Backend dev
- **Resolved date:** 2026-05-15
- **Resolution:** Chuẩn hóa env config, token secret và expiry settings.
- **Prevention action:** Tạo checklist config auth trước khi mở test flow login/register ở dự án sau.

## Issue Statistics
- **Total issues:** 2
- **Open:** 1
- **Resolved:** 1
- **Average resolution time:** ~1 ngày
