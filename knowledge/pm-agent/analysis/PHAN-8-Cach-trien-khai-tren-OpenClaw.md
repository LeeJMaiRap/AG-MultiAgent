# PHẦN 8: Cách triển khai PM Agent trên OpenClaw

## Tổng quan
Phần này hướng dẫn cách biến những gì đã phân tích thành một PM Agent chạy được thật trên OpenClaw.

## Cấu trúc file/folder cho PM Agent

### Cấu trúc đề xuất

```text
workspace/
├── docs/
│   ├── PM-Business-Process.md
│   ├── PM-Agent-Business-Process.md
│   └── pm-agent/
│       ├── SYSTEM-PROMPT.md
│       ├── WORKFLOW.md
│       ├── PROMPTS/
│       │   ├── 01-initiate.md
│       │   ├── 02-planning.md
│       │   ├── 03-task-board.md
│       │   ├── 04-execute.md
│       │   ├── 05-monitor.md
│       │   └── 06-closure.md
│       ├── TEMPLATES/
│       │   ├── charter-template.md
│       │   ├── requirements-template.md
│       │   ├── spec-template.md
│       │   ├── plan-template.md
│       │   ├── rules-template.md
│       │   ├── wbs-template.md
│       │   ├── schedule-template.md
│       │   ├── risk-register-template.md
│       │   ├── task-board-template.md
│       │   ├── issue-log-template.md
│       │   ├── change-log-template.md
│       │   ├── status-dashboard-template.md
│       │   ├── final-report-template.md
│       │   └── lessons-learned-template.md
│       ├── EXAMPLES/
│       │   └── example-project-workflow.md
│       └── README.md
├── memory/
│   └── observations/
│       └── pm-projects.md
└── projects/
    └── [project-name]/
        ├── 01-initiation/
        ├── 02-planning/
        ├── 03-execution/
        ├── 04-monitoring/
        └── 05-closure/
```

## Bước 1: Tạo System Prompt cho PM Agent

Cần tạo file:
`systems/pm-agent/architecture/SYSTEM-PROMPT.md`

Nội dung là system prompt định nghĩa vai trò, trách nhiệm, nguyên tắc, workflow.

## Bước 2: Tạo các template

Cần tạo các file template trong `systems/pm-agent/templates/`:
- charter-template.md
- requirements-template.md
- spec-template.md
- plan-template.md
- rules-template.md
- wbs-template.md
- schedule-template.md
- risk-register-template.md
- task-board-template.md
- issue-log-template.md
- change-log-template.md
- status-dashboard-template.md
- final-report-template.md
- lessons-learned-template.md

## Bước 3: Tạo README hướng dẫn

Tạo file `systems/pm-agent/README.md` mô tả:
- PM Agent là gì
- Cách khởi động
- Cách sử dụng
- Cấu trúc dự án
- Ví dụ

## Bước 4: Tạo Workflow tổng thể

Tạo file `systems/pm-agent/architecture/WORKFLOW.md` mô tả:
- Initiation
- Planning
- Execution
- Monitoring
- Closure

## Bước 5: MVP Implementation Plan

### MVP Scope
Chỉ cần làm được:
1. **Initiation** ✅
   - Nhận yêu cầu
   - Tạo charter
   - Hỏi làm rõ

2. **Planning** ✅
   - Tạo spec/plan/rules
   - Tạo WBS
   - Tạo task-board

3. **Execution** ✅ (simplified)
   - Chọn 1-2 task
   - Tự làm hoặc gọi worker
   - Cập nhật task-board

4. **Closure** ✅
   - Tạo final-report
   - Tạo lessons-learned

### MVP không cần
- Monitoring chi tiết
- Risk/issue/change management phức tạp
- Multiple workers
- Handoff mechanics

## Bước 6: Roadmap triển khai

### Phiên bản 1.0 (MVP) - Tuần 1
- [ ] Tạo system prompt
- [ ] Tạo templates
- [ ] Tạo workflow docs
- [ ] Test với 1 ví dụ nhỏ
- [ ] Tạo final report

### Phiên bản 1.1 - Tuần 2
- [ ] Thêm risk/issue/change management
- [ ] Thêm status dashboard
- [ ] Thêm periodic monitoring

### Phiên bản 1.2 - Tuần 3
- [ ] Thêm multiple workers
- [ ] Thêm handoff mechanics
- [ ] Thêm context management

### Phiên bản 2.0 - Sau đó
- [ ] Convert thành skill
- [ ] Thêm automation
- [ ] Thêm integration

## Bước 7: Cách chạy PM Agent lần đầu

### Bước 1: Load System Prompt
Gửi message cho PM Agent:
```
Bạn là Lệ, PM Agent. Đây là system prompt của bạn:

[COPY NỘI DUNG SYSTEM-PROMPT.md]

Bạn đã hiểu vai trò của mình chưa?
```

### Bước 2: Gửi yêu cầu dự án
```
Hãy quản lý dự án: [YÊU CẦU]
```

### Bước 3: PM Agent sẽ
- Phân tích
- Hỏi câu hỏi
- Tạo charter
- Chờ xác nhận

### Bước 4: User xác nhận
```
Được, charter này ổn. Hãy tiếp tục lập kế hoạch.
```

### Bước 5: PM Agent tạo planning docs
- spec.md
- plan.md
- rules.md
- wbs.md
- schedule.md
- risk-register.md

### Bước 6: User xác nhận
```
Kế hoạch ổn. Hãy tạo task board và bắt đầu thực thi.
```

### Bước 7: PM Agent thực thi
- Tạo task-board.md
- Chọn task đầu tiên
- Thực thi hoặc gọi worker
- Cập nhật trạng thái

### Bước 8: Lặp cho đến khi hoàn tất
- Mỗi task → review → update
- Cập nhật task-board
- Cập nhật status

### Bước 9: Đóng dự án
```
Dự án hoàn tất. Hãy tạo final report.
```

### Bước 10: PM Agent tạo báo cáo
- final-report.md
- lessons-learned.md

## Bước 8: Cách tạo sub-agent worker

Khi PM Agent cần gọi worker, nó sẽ dùng `sessions_spawn`.

### Logic tạo worker
1. Xác định task cần làm
2. Tạo prompt rõ ràng cho worker
3. Spawn sub-agent:
   - runtime: `subagent`
   - task: `[WORKER_PROMPT]`
   - label: `worker-[task-id]`
4. Chờ kết quả
5. Review output
6. Cập nhật project state

### Ví dụ worker prompt
```markdown
Bạn là Worker Agent.

## Task
[TASK_NAME]

## Input
Read: [INPUT_FILES]

## Output
Create: [OUTPUT_FILES]

## Acceptance Criteria
- [CRITERIA_1]
- [CRITERIA_2]

## Do not
- Change project scope
- Modify charter or plan
- Report blocker without trying alternatives

## When blocked
Report blocker with:
- What you tried
- Why it failed
- What you need
```

## Bước 9: Cách lưu project state

Rất quan trọng: project state phải nằm trong file, không phụ thuộc chat context.

Sau mỗi execution, PM Agent phải cập nhật:
1. `task-board.md`
   - Update task status
   - Update % completion

2. `issue-log.md`
   - Add new issues
   - Update issue status

3. `change-log.md`
   - Add new changes
   - Update change status

4. `status-dashboard.md`
   - Update metrics
   - Update timeline status
   - Update risk status

5. `memory/observations/pm-projects.md`
   - Log project progress
   - Log key decisions

## Bước 10: Testing & Validation

Trước khi demo cho HUECIT, nên test:

### Test 1: Initiation
- [ ] PM Agent nhận yêu cầu
- [ ] PM Agent tạo charter
- [ ] PM Agent hỏi câu hỏi làm rõ
- [ ] Charter được xác nhận

### Test 2: Planning
- [ ] PM Agent tạo spec/plan/rules
- [ ] PM Agent tạo WBS
- [ ] PM Agent tạo schedule
- [ ] PM Agent tạo risk register

### Test 3: Execution
- [ ] PM Agent tạo task-board
- [ ] PM Agent chọn task
- [ ] PM Agent thực thi hoặc gọi worker
- [ ] PM Agent cập nhật trạng thái

### Test 4: Closure
- [ ] PM Agent tạo final report
- [ ] PM Agent tạo lessons learned
- [ ] Project được đóng

## Bước 11: Demo cho HUECIT

Khi demo, nên:
1. **Giải thích bối cảnh** (2 phút)
   - PM Agent là gì
   - Tại sao cần PM Agent
   - Kiến trúc tổng thể

2. **Chạy ví dụ nhỏ** (5-10 phút)
   - Gửi yêu cầu dự án
   - PM Agent phân tích
   - Tạo charter
   - Tạo planning docs
   - Tạo task-board
   - Thực thi 1-2 task
   - Tạo final report

3. **Trình bày kết quả** (3 phút)
   - Các file được tạo
   - Workflow được thực hiện
   - Lessons learned

4. **Q&A** (5 phút)

## Kết luận

Để triển khai PM Agent, cần:
1. Tạo cấu trúc folder
2. Tạo system prompt
3. Tạo templates
4. Tạo workflow docs
5. Tạo prompts cho từng giai đoạn
6. Test với ví dụ nhỏ
7. Tạo final report
8. Demo cho HUECIT

Tất cả những gì đã phân tích ở phần 1-7 đều có thể dùng được ngay.

---

**Ngày phân tích:** 2026-04-24
**Người phân tích:** Lệ (PM Agent)
