# Ops

Vùng này chứa **scripts, state, tmp, exports, và logs** phục vụ vận hành.

## Cấu trúc

```
ops/
├── scripts/             # Scripts automation
│   ├── image/           # Image processing
│   ├── voice/           # Voice processing
│   └── maintenance/     # Maintenance scripts
├── state/               # Runtime state
│   ├── pm-agent/        # PM Agent state
│   ├── sessions/        # Session state
│   └── cache/           # Cache
├── tmp/                 # Temporary files
│   ├── image/           # Image artifacts
│   ├── voice/           # Voice artifacts
│   └── pm-agent/        # PM Agent tmp
├── exports/             # Exported artifacts
│   ├── pm-agent/        # PM Agent exports
│   └── projects/        # Project exports
└── logs/                # Logs
```

## Scripts

### Voice
- `voice_to_text.py` - STT (Whisper)
- `text_to_voice.py` - TTS (Edge TTS)
- `telegram_voice_ingest.py` - Semi-auto voice ingest
- `reply_as_voice.py` - Generate voice reply

### Image
Image processing scripts.

### Maintenance
Maintenance và cleanup scripts.

## State

Runtime state cho các hệ thống.

**Lưu ý:** State không phải source of truth. Source of truth nằm trong:
- `projects/` cho project data
- `systems/` cho system config
- `agent-core/memory/` cho agent memory

## Tmp

Temporary artifacts, runtime outputs.

**Quy tắc:**
- Không commit vào git (đã ignore)
- Có thể xóa bất kỳ lúc nào
- Chỉ giữ `.gitkeep` để preserve structure

## Exports

Exported artifacts (zip, tar.gz, etc.)

**Quy tắc:**
- Không commit binary lớn vào git
- Giữ structure, ignore content

## Vai trò trong workspace

Ops là **vùng vận hành**, chứa artifact tạm và scripts.

Khác với:
- `systems/` - Framework code
- `projects/` - Project data
- `knowledge/` - Documentation
