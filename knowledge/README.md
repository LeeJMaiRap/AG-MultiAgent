# Knowledge

Vùng này chứa **tài liệu, nghiên cứu, phân tích, và meeting notes**.

## Cấu trúc

```
knowledge/
├── pm-agent/            # Tri thức về PM Agent
│   ├── research/        # Nghiên cứu, business process
│   ├── analysis/        # Phân tích chi tiết
│   ├── examples/        # Ví dụ workflow
│   └── summaries/       # Tóm tắt, overview
├── meetings/            # Meeting notes
│   ├── raw/             # Ghi chú thô
│   └── normalized/      # Đã chuẩn hóa
└── references/          # Tài liệu tham khảo
```

## PM Agent Knowledge

### Research
Tài liệu nghiên cứu về quy trình PM, business process.

### Analysis
Phân tích chi tiết:
- So sánh tài liệu tham khảo
- Quy trình PM chuẩn
- Kiến trúc PM Agent
- Thiết kế tài liệu
- Workflow chi tiết
- Prompt và instruction
- Ví dụ thực tế
- Cách triển khai trên OpenClaw

### Examples
Ví dụ workflow thực tế, demo flow.

### Summaries
Tóm tắt, overview, structure.

## Meetings

### Raw
Ghi chú họp thô, chưa xử lý.

### Normalized
Đã chuẩn hóa, trích xuất action items.

## Vai trò trong workspace

Knowledge là **kho tri thức** phục vụ nghiên cứu và tham khảo.

Khác với:
- `systems/pm-agent/` - Framework đang vận hành
- `projects/` - Dự án thực tế
- `agent-core/memory/` - Memory vận hành agent
