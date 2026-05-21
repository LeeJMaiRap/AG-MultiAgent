# Agent Core

Vùng này chứa **bản sắc, memory, và workspace cá nhân** của agent.

## Nội dung

### Identity Files
- `AGENTS.md` - Quy tắc vận hành, workflow, vai trò agent
- `SOUL.md` - Tính cách, nguyên tắc, ranh giới
- `IDENTITY.md` - Tên, creature, vibe, emoji, avatar
- `USER.md` - Thông tin về người dùng
- `TOOLS.md` - Ghi chú cục bộ về tools/setup
- `HEARTBEAT.md` - Checklist cho heartbeat polling
- `MEMORY.md` - Long-term memory (chỉ load trong main session)

### Memory Structure
```
memory/
├── daily/              # Raw logs theo ngày
├── observations/       # Insights có cấu trúc
├── index.json         # Metadata tìm kiếm
└── MEMORY_SCHEMA.md   # Schema memory
```

## Quy tắc quan trọng

### Memory Security
- `MEMORY.md` **chỉ load trong main session** (direct chat với owner)
- **Không load trong shared contexts** (Discord, group chats)
- Lý do: chứa thông tin cá nhân, không nên leak ra ngoài

### Write It Down
- Memory có giới hạn — muốn nhớ thì **ghi vào file**
- "Mental notes" không tồn tại qua session restart
- Text > Brain 📝

## Vai trò trong workspace

Agent-core là **source of truth cho bản sắc agent**.

Các vùng khác:
- `systems/` - Hệ thống agent đang xây (PM Agent, etc.)
- `projects/` - Dự án thực tế
- `knowledge/` - Tài liệu, research, meeting notes
- `ops/` - Scripts, tmp, exports, logs
- `shared/` - Templates, schemas, utilities dùng chung
