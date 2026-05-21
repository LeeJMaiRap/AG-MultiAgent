# Systems

Vùng này chứa các **hệ thống agent** đang được xây dựng và vận hành.

## Hiện có

### PM Agent
**Location:** `systems/pm-agent/`

PM Agent (Lệ) là một agent AI quản lý dự án, có khả năng:
- Tiếp nhận và phân tích yêu cầu dự án
- Tạo bộ tài liệu PM chuẩn
- Chia task và điều phối thực thi
- Theo dõi tiến độ, rủi ro, thay đổi
- Tạo báo cáo tổng kết

**Cấu trúc:**
```
pm-agent/
├── README.md              # Hướng dẫn sử dụng
├── STATUS.md              # Trạng thái PM Agent framework
├── architecture/          # Thiết kế hệ thống
├── prompts/               # Prompt theo phase
├── templates/             # Template tài liệu
├── skills/                # Skill modules
├── runtime/               # Policies, runbooks, config
├── eval/                  # Scenarios, checklists
├── scripts/               # Automation scripts
└── changelog/             # Lịch sử phát triển
```

**Production-readiness:** ~70%

## Quy ước

Mỗi system nên có:
- `README.md` - Giới thiệu và hướng dẫn
- `STATUS.md` - Trạng thái hiện tại
- `architecture/` - Thiết kế
- `runtime/` - Vận hành thực tế
- `eval/` - Kiểm chứng chất lượng

## Vai trò trong workspace

Systems là nơi chứa **sản phẩm agent** đang phát triển.

Khác với:
- `agent-core/` - Bản sắc agent cá nhân
- `projects/` - Dự án do agent quản lý
- `knowledge/` - Tri thức và tài liệu
