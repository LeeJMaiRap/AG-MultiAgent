# Shared

Vùng này chứa **templates, schemas, utilities, và assets** dùng chung.

## Cấu trúc

```
shared/
├── templates/           # Templates dùng chung
├── schemas/             # Schemas dùng chung
├── utilities/           # Utility scripts/functions
└── assets/              # Assets (images, icons, etc.)
```

## Templates

Templates có thể dùng chung giữa nhiều systems/projects.

Ví dụ:
- Document templates
- Config templates
- Boilerplate code

## Schemas

Schemas định nghĩa cấu trúc dữ liệu dùng chung.

Ví dụ:
- JSON schemas
- YAML schemas
- Data models

## Utilities

Utility scripts/functions có thể tái sử dụng.

Ví dụ:
- File processing utilities
- Data transformation utilities
- Common helpers

## Assets

Assets tĩnh dùng chung.

Ví dụ:
- Icons
- Images
- Fonts
- Static resources

## Vai trò trong workspace

Shared là **thư viện dùng chung**, tránh duplicate code/config.

Khác với:
- `systems/` - System-specific code
- `ops/scripts/` - Operational scripts
- `knowledge/` - Documentation
