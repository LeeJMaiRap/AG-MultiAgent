# PHẦN 3: Kiến trúc PM Agent cho OpenClaw

## Tổng quan
Phần này mô tả kiến trúc PM Agent được thiết kế cho OpenClaw, bao gồm các agent, vai trò, và cách chúng phối hợp.

## Mô hình kiến trúc đề xuất

### Mô hình 1: Single PM Agent (MVP)
Chỉ có 1 agent làm tất cả.

**Ưu điểm:**
- Dễ làm bản đầu tiên
- Ít phức tạp
- Phù hợp demo nhanh

**Nhược điểm:**
- Dễ bị quá tải context
- Khó tách vai trò
- Khó mở rộng

### Mô hình 2: PM Agent + Worker Agents (Recommended)
Có 1 PM Agent trung tâm và 1 hoặc nhiều Worker Agent.

**Cấu trúc:**
- **PM Agent**
  - Nhận yêu cầu từ user
  - Phân tích nghiệp vụ PM
  - Lập kế hoạch
  - Chia task
  - Giao việc
  - Theo dõi
  - Tổng hợp kết quả

- **Worker Agent(s)**
  - Nhận task cụ thể
  - Thực hiện task
  - Trả kết quả
  - Báo blocker nếu có

**Ưu điểm:**
- Hợp lý với OpenClaw
- Dễ hiện thực bằng `sessions_spawn`
- Đúng tinh thần agentic workflow
- Có thể mở rộng dần

**Nhược điểm:**
- Cần cơ chế giao tiếp giữa các agent
- Cần cách lưu project state rõ ràng

### Mô hình 3: Planner + PM Manager + Executors (Advanced)
Gần với APM repo hơn.

**Cấu trúc:**
- **Planner Agent** - khám phá yêu cầu, tạo Spec/Plan/Rules
- **PM Manager Agent** - điều phối toàn bộ execution
- **Executor Agents** - thực hiện từng task cụ thể
- **Reviewer Agent** (tùy chọn) - review kết quả

**Ưu điểm:**
- Kiến trúc đẹp
- Chuẩn agentic hơn
- Dễ scale
- Phù hợp nghiên cứu sâu

**Nhược điểm:**
- Hơi nặng cho bài thực tập cá nhân
- Mất thời gian dựng quy trình
- Khó demo nhanh

## Đề xuất thực tế cho bài tập của anh

### Giai đoạn 1 — MVP
Xây:
- **1 PM Agent**
- **1 Executor Agent**

PM Agent làm:
- Phân tích yêu cầu
- Lập kế hoạch
- Tạo tài liệu
- Tạo task list
- Gọi Executor Agent khi cần thực thi

Executor Agent làm:
- Tạo file
- Sửa file
- Code
- Test
- Trả kết quả

### Giai đoạn 2 — Nâng cấp
Thêm:
- **Reviewer Agent**
- **Reporter Agent**

### Giai đoạn 3 — Hoàn thiện
Tách thành:
- Planner
- Manager
- Worker
- Reviewer

## Mapping kiến trúc sang OpenClaw

### PM Agent chính
Chạy ở main session, chịu trách nhiệm:
- Giao tiếp với user
- Phân tích yêu cầu
- Ra quyết định điều phối
- Cập nhật project docs
- Gọi sub-agent khi cần

### Worker Agent
Tạo bằng sub-agent/session riêng:
- Nhận một task cụ thể
- Làm xong thì trả kết quả
- Không cần biết toàn bộ dự án

Ví dụ:
- worker-code
- worker-docs
- worker-test

## Project state nên lưu ở đâu

**Cấu trúc:**
```
projects/[project-name]/
├── 01-initiation/
│   ├── charter.md
│   └── requirements.md
├── 02-planning/
│   ├── spec.md
│   ├── plan.md
│   ├── rules.md
│   ├── wbs.md
│   ├── schedule.md
│   └── risk-register.md
├── 03-execution/
│   ├── task-board.md
│   ├── issue-log.md
│   └── change-log.md
├── 04-monitoring/
│   └── status-dashboard.md
└── 05-closure/
    ├── final-report.md
    └── lessons-learned.md
```

**Ý nghĩa:**
- Đây là **single source of truth**
- Agent có thể restart mà không mất trạng thái
- Dễ chứng minh nghiệp vụ PM
- Dễ demo cho HUECIT

## Human-in-the-loop nên đặt ở đâu

### Bắt buộc hỏi
- Scope chưa rõ
- Có nhiều hướng triển khai khác nhau
- Thay đổi lớn về mục tiêu
- Chuẩn bị xóa/sửa nhiều dữ liệu
- Chuẩn bị xác nhận kết quả cuối cùng

### Có thể tự làm
- Draft tài liệu
- Chia task
- Cập nhật tiến độ
- Tạo issue/risk log
- Tạo báo cáo
- Đề xuất action plan

## Luồng hoạt động thực tế

Ví dụ user nhập:
> "Hãy làm PM Agent để quản lý dự án xây dựng website quản lý thực tập"

PM Agent sẽ:
1. Phân tích yêu cầu
2. Tạo charter.md
3. Tạo câu hỏi làm rõ
4. Sau khi có trả lời:
   - Tạo WBS
   - Tạo schedule
   - Tạo risk register
   - Tạo task board
5. Chọn task đầu tiên
6. Spawn Worker Agent để làm task
7. Nhận kết quả
8. Update trạng thái dự án
9. Nếu có blocker thì hỏi user
10. Lặp lại cho đến khi hoàn tất
11. Tạo final report

## Kết luận

**Kiến trúc nên làm cho bài của anh:**
- 1 PM Agent chính
- 1 hoặc nhiều Worker Agent
- Project state lưu thành file
- Human-in-the-loop ở các điểm quyết định
- Tài liệu PM được tạo và cập nhật tự động
- Execution thật thông qua sub-agent / task delegation

---

**Ngày phân tích:** 2026-04-24
**Người phân tích:** Lệ (PM Agent)
