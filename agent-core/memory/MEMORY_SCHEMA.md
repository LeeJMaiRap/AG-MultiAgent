# Memory Schema - Hệ Thống Lưu Trữ Bộ Nhớ của Lệ

## Cấu Trúc Thư Mục

```
memory/
├── MEMORY_SCHEMA.md          # File này - định nghĩa cấu trúc
├── MEMORY.md                 # Bộ nhớ dài hạn (curated)
├── daily/
│   ├── 2026-04-24.md        # Ghi chép hàng ngày (raw logs)
│   └── ...
├── observations/
│   ├── projects.md          # Quan sát về dự án
│   ├── preferences.md       # Sở thích & cách làm việc của anh
│   ├── tools.md             # Công cụ & cấu hình
│   └── lessons.md           # Bài học & kinh nghiệm
└── index.json               # Index tìm kiếm (metadata)
```

## Loại Bộ Nhớ

### 1. MEMORY.md (Long-term, Curated)
- **Mục đích:** Bộ nhớ dài hạn, chỉ chứa những gì quan trọng
- **Cập nhật:** Hàng tuần hoặc khi có sự kiện quan trọng
- **Nội dung:** Quyết định, bối cảnh, ưu tiên, ranh giới
- **Ví dụ:** Dự án hiện tại, mục tiêu, công nghệ yêu thích

### 2. daily/YYYY-MM-DD.md (Daily Logs, Raw)
- **Mục đích:** Ghi chép hàng ngày, raw logs
- **Cập nhật:** Mỗi phiên làm việc
- **Nội dung:** Những gì em làm, kết quả, vấn đề gặp phải
- **Ví dụ:** "Anh yêu cầu em tham khảo claude-mem repo..."

### 3. observations/*.md (Structured Insights)
- **projects.md:** Dự án, công nghệ, tiến độ
- **preferences.md:** Cách anh thích làm việc, style code, tools
- **tools.md:** Cấu hình, SSH hosts, API keys (không lưu secrets!)
- **lessons.md:** Bài học, anti-patterns, best practices

### 4. index.json (Search Index)
```json
{
  "lastUpdated": "2026-04-24T13:42:19Z",
  "entries": [
    {
      "id": "obs-001",
      "type": "project",
      "title": "HUECIT Internship",
      "date": "2026-04-24",
      "tags": ["work", "internship", "huecit"],
      "file": "observations/projects.md",
      "keywords": ["internship", "software engineering", "huecit"]
    }
  ]
}
```

## Quy Trình Cập Nhật

1. **Mỗi phiên:** Ghi vào `daily/YYYY-MM-DD.md`
2. **Hàng ngày (heartbeat):** Review daily logs, cập nhật `observations/*.md`
3. **Hàng tuần:** Curate `MEMORY.md` từ observations
4. **Mỗi lần cập nhật:** Refresh `index.json`

## Tìm Kiếm

Em sẽ sử dụng `memory_search` để tìm kiếm:
- Query: "dự án hiện tại"
- Tags: "work", "project", "internship"
- Date range: Tuần này, tháng này, v.v.

## Ví Dụ Nội Dung

### observations/projects.md
```markdown
# Projects

## HUECIT Internship (Current)
- **Status:** Active
- **Duration:** [Start] - [End]
- **Tech Stack:** [Languages, frameworks]
- **Key Tasks:** [List]
- **Progress:** [%]
```

### observations/preferences.md
```markdown
# Preferences & Work Style

## Communication
- Prefer detailed explanations
- Think before speaking
- Proactive suggestions welcome

## Tools & Environment
- WSL + Ubuntu + Docker
- Laptop: Lenovo IdeaPad Slim 3
- Web chat only
```

---

**Mục tiêu:** Xây dựng bộ nhớ bền vững, có cấu trúc, dễ tìm kiếm, giống như claude-mem nhưng đơn giản hơn và phù hợp với OpenClaw.
