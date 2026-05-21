# PM Agent - Hướng dẫn sử dụng

## Giới thiệu
PM Agent (Lệ) là một Agent AI quản lý dự án trên OpenClaw.

## Mục tiêu
PM Agent có khả năng:
- nhận yêu cầu dự án
- phân tích và chuẩn hóa yêu cầu
- tạo bộ tài liệu PM
- chia task
- điều phối thực thi
- theo dõi tiến độ
- tạo báo cáo tổng kết

## Cấu trúc thư mục

```text
systems/pm-agent/
├── architecture/
│   ├── SYSTEM-PROMPT.md
│   ├── WORKFLOW.md
│   └── STORAGE-RULES.md
├── prompts/
├── templates/
├── skills/
├── runtime/
├── eval/
├── README.md
└── STATUS.md

projects/active/[project-name]/
├── 01-initiation/
├── 02-planning/
├── 03-execution/
├── 04-monitoring/
└── 05-closure/
```

## Cách sử dụng

### 1. Khởi động PM Agent
Load file `SYSTEM-PROMPT.md` vào context của PM Agent.

### 2. Gửi yêu cầu dự án
Ví dụ:

```text
Hãy quản lý dự án: Xây dựng một PM Agent bằng OpenClaw.
```

### 3. PM Agent sẽ thực hiện
- Phân tích yêu cầu
- Tạo charter
- Hỏi làm rõ nếu cần
- Lập kế hoạch
- Tạo task-board
- Thực thi hoặc giao worker
- Cập nhật trạng thái
- Tạo final report

### 4. Luồng vận hành
1. Initiation
2. Planning
3. Execution
4. Monitoring
5. Closure

## Các file quan trọng
- `architecture/SYSTEM-PROMPT.md` - vai trò và quy tắc của PM Agent
- `architecture/WORKFLOW.md` - workflow tổng thể
- `prompts/` - prompt theo từng giai đoạn
- `templates/` - template tài liệu dự án

## Dự án mẫu
Xem `knowledge/pm-agent/examples/example-project-workflow.md`

## Gợi ý MVP
Phiên bản đầu tiên nên tập trung vào:
- initiation
- planning
- task-board
- thực thi 1-2 task
- final report

## Ghi chú
- Project state phải lưu bằng file
- Human-in-the-loop chỉ dùng cho quyết định quan trọng
- Worker prompt phải rõ ràng và có acceptance criteria
