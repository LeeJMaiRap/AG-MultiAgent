# OpenClaw Workspace

Production-ready workspace cho AI agent development và project management.

## Cấu trúc

```
workspace/
├── agent-core/          # Agent identity, memory, personal workspace
├── systems/             # Agent systems (PM Agent, etc.)
├── projects/            # Active and archived projects
├── knowledge/           # Research, analysis, meetings, references
├── ops/                 # Scripts, state, tmp, exports, logs
└── shared/              # Templates, schemas, utilities, assets
```

## Quick Navigation

### Agent Core
**Path:** `agent-core/`  
**Purpose:** Agent bản sắc, memory, workspace cá nhân  
**Key files:** AGENTS.md, SOUL.md, MEMORY.md, memory/

### Systems
**Path:** `systems/`  
**Purpose:** Hệ thống agent đang xây dựng  
**Current:** PM Agent (~70% production-ready)

### Projects
**Path:** `projects/`  
**Purpose:** Dự án thực tế được quản lý  
**Registry:** `projects/_index/projects-registry.md`

### Knowledge
**Path:** `knowledge/`  
**Purpose:** Tài liệu, nghiên cứu, meeting notes  
**Structure:** pm-agent/, meetings/, references/

### Ops
**Path:** `ops/`  
**Purpose:** Scripts, state, tmp, exports  
**Key:** scripts/voice/, tmp/, exports/

### Shared
**Path:** `shared/`  
**Purpose:** Templates, schemas, utilities dùng chung  
**Structure:** templates/, schemas/, utilities/, assets/

## Key Principles

1. **Clear separation of concerns**
   - Agent identity ≠ Systems ≠ Projects ≠ Knowledge

2. **File-based source of truth**
   - State nằm trong file, không phụ thuộc chat context

3. **Scalable structure**
   - Dễ thêm systems mới
   - Dễ quản lý nhiều projects
   - Dễ onboarding

4. **Production-ready mindset**
   - Policies, runbooks, eval
   - Approval workflow
   - Decision tracking
   - State management

## Getting Started

### For Agent Development
1. Read `agent-core/AGENTS.md`
2. Read `agent-core/SOUL.md`
3. Explore `systems/pm-agent/`

### For PM Agent Usage
1. Read `systems/pm-agent/README.md`
2. Check `systems/pm-agent/STATUS.md`
3. Review `projects/_index/active-projects.md`

### For Project Management
1. Check `projects/_index/projects-registry.md`
2. Review project structure in `projects/README.md`
3. Follow PM workflow in `systems/pm-agent/architecture/WORKFLOW.md`

## Maintenance

### Regular Tasks
- Update `projects/_index/` registry
- Clean `ops/tmp/` periodically
- Review and archive completed projects
- Update system STATUS.md

### Git Hygiene
- `node_modules/` ignored
- `ops/tmp/` ignored
- `ops/exports/*.zip` ignored
- Only source files tracked

## Version History

- **2026-05-14** - Workspace restructure + PM Agent runtime standardization
- **2026-04-24** - Initial PM Agent validation with web-ban-hang project

## Links

- **GitHub:** https://github.com/LeeJMaiRap/openclaw-workspace
- **Rollback points:**
  - `a8182dc` - Before restructure
  - `f4f5cf1` - After restructure
  - `c9c4199` - After path fixes
  - `cc8f01d` - After runtime standardization
  - `a9548b1` - After duplicate cleanup
  - `da7621c` - After repo cleanup
