# Projects

Vùng này chứa các **dự án thực tế** được PM Agent quản lý.

## Cấu trúc

```
projects/
├── _index/              # Registry và dashboard
├── active/              # Dự án đang vận hành
└── archived/            # Dự án đã hoàn tất hoặc hủy
```

## Active Projects

Xem: `_index/active-projects.md`

Hiện có:
- **web-ban-hang** - Trang Web Bán Hàng (demo-ready)

## Project Structure

Mỗi project tuân theo cấu trúc PM chuẩn:

```
[project-name]/
├── project.yaml         # Metadata
├── 01-initiation/       # Charter, requirements
├── 02-planning/         # Spec, plan, wbs, schedule, risks
├── 03-execution/        # Task board, issue log, change log
├── 04-monitoring/       # Status dashboard
├── 05-closure/          # Final report, lessons learned
├── decisions/           # Decision log
├── approvals/           # Approval records
├── handoffs/            # Handoff notes
└── evidence/            # Verification artifacts
```

## Registry

- **projects-registry.md** - Danh sách toàn bộ project
- **active-projects.md** - Dashboard project đang chạy

## Quy tắc

1. **Mỗi project phải có `project.yaml`**
2. **Source of truth nằm trong file, không phụ thuộc chat**
3. **Approval phải được ghi lại**
4. **Decision quan trọng phải log**
5. **Closure phải có final report**

## Vai trò trong workspace

Projects là nơi chứa **output thực tế** của PM Agent.

Khác với:
- `systems/pm-agent/` - Framework PM Agent
- `knowledge/` - Tài liệu nghiên cứu
- `agent-core/` - Memory agent
