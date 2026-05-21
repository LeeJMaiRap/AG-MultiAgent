# Project Lifecycle & Path Policy

Quy định chuẩn về **lifecycle status** và **folder path** của project, để tránh mismatch giữa metadata và vị trí lưu trữ.

## Mục tiêu

Policy này giúp:
- tránh selector/report hiểu sai trạng thái project
- tránh vận hành nhầm project non-active như active
- chuẩn hóa cách xử lý khi project chuyển trạng thái
- rõ ràng về source of truth khi path và metadata conflict

---

# 1. Lifecycle status chuẩn

PM Agent chỉ nhận 4 trạng thái lifecycle chính:

## `active`
Project đang được vận hành, có tiến triển meaningful, có owner/team đang làm việc.

**Đặc điểm:**
- có task đang in-progress
- có update thường xuyên
- có owner action rõ ràng
- có next actions cụ thể

## `on-hold`
Project tạm dừng có kế hoạch, chờ điều kiện nào đó để tiếp tục.

**Đặc điểm:**
- không có tiến triển hiện tại
- có lý do tạm dừng rõ ràng
- có điều kiện để resume
- owner vẫn có ý định tiếp tục sau

## `stopped`
Project dừng không có kế hoạch tiếp tục trong tương lai gần.

**Đặc điểm:**
- không có tiến triển
- không có kế hoạch resume rõ ràng
- có thể do:
  - thay đổi ưu tiên
  - thiếu resource
  - blocker không giải quyết được
  - owner quyết định không tiếp tục

## `archived`
Project đã hoàn tất hoặc đã đóng chính thức, được lưu trữ để tham khảo.

**Đặc điểm:**
- không còn vận hành
- đã có kết quả cuối (thành công hoặc thất bại)
- được giữ lại để:
  - tham khảo
  - lessons learned
  - audit
  - demo/reference

---

# 2. Folder path chuẩn

Mỗi lifecycle status có folder path tương ứng:

| Status | Path |
|--------|------|
| `active` | `projects/active/[project-name]/` |
| `on-hold` | `projects/on-hold/[project-name]/` |
| `stopped` | `projects/stopped/[project-name]/` |
| `archived` | `projects/archived/[project-name]/` |

---

# 3. Source of truth khi conflict

### Rule cứng
**Khi path và metadata conflict, ưu tiên `project.yaml` metadata.**

### Ví dụ conflict
- Path: `projects/active/web-ban-hang/`
- Metadata: `status: on-hold`

→ **Selector phải coi project này là `on-hold`**, không phải `active`.

### Lý do ưu tiên metadata
- `project.yaml` là single source of truth cho trạng thái project
- path có thể chưa kịp migrate
- path có thể bị sai do thao tác thủ công
- metadata được cập nhật có kiểm soát hơn

---

# 4. Migration policy

### Khi nào phải migrate path?

**Bắt buộc migrate khi:**
- project chuyển từ `active` → `on-hold/stopped/archived`
- project chuyển từ `on-hold` → `active` hoặc `stopped/archived`
- project chuyển từ `stopped` → `archived`

**Không bắt buộc migrate ngay khi:**
- đang trong giai đoạn chuyển tiếp
- owner chưa confirm chính thức
- đang chờ approval để đổi status

### Cách migrate

**Bước 1:** Cập nhật `project.yaml` metadata trước
```yaml
status: on-hold  # hoặc stopped/archived
updated_at: 2026-05-15T06:54:00Z
```

**Bước 2:** Move folder
```bash
mv projects/active/[project-name] projects/on-hold/[project-name]
```

**Bước 3:** Cập nhật `source_of_truth` trong `project.yaml` nếu cần
```yaml
source_of_truth: projects/on-hold/[project-name]
```

**Bước 4:** Ghi change log
```markdown
## [2026-05-15] Project lifecycle change
- Status: active → on-hold
- Path: projects/active/web-ban-hang → projects/on-hold/web-ban-hang
- Reason: [lý do cụ thể]
- Actor: human:Doanh
```

---

# 5. Xử lý mismatch trong vận hành

### Khi selector/report gặp mismatch

**Hành vi bắt buộc:**
1. Đọc `project.yaml` metadata làm source of truth
2. Log warning về mismatch
3. Áp dụng rule theo metadata, không theo path
4. Ghi mismatch vào report/audit output
5. Đề xuất migrate path nếu mismatch kéo dài

**Ví dụ log warning:**
```
WARNING: Path/metadata mismatch detected
- Path: projects/active/web-ban-hang
- Metadata status: on-hold
- Action: Treating as on-hold per metadata priority
- Recommendation: Migrate path to projects/on-hold/web-ban-hang
```

### Khi cron/daily report chạy

**Rule selector:**
- Chỉ report project có `status: active` trong metadata
- Skip project có `status: on-hold/stopped/archived` dù path là `active/`
- Log skipped targets với lý do rõ ràng
- Ghi mismatch vào audit section nếu có

---

# 6. Delay migration policy

### Khi nào được delay migration?

**Cho phép delay tạm thời khi:**
- project vừa chuyển status trong vài giờ
- đang chờ owner confirm chính thức
- đang trong handoff/approval flow

**Thời gian delay tối đa:**
- `active` → `on-hold`: 24 giờ
- `active` → `stopped`: 48 giờ
- `on-hold` → `stopped`: 48 giờ
- `stopped` → `archived`: 7 ngày
- `on-hold` → `active`: 24 giờ

**Sau timeout:**
- phải migrate hoặc escalate
- không để mismatch kéo dài vô thời hạn

---

# 7. Audit logging rule

### Mỗi lần phát hiện mismatch phải log

**Log format:**
```markdown
## Path/Metadata Mismatch Detected
- Date: YYYY-MM-DD HH:MM UTC
- Project: [project-name]
- Path: projects/[actual-folder]/[project-name]
- Metadata status: [actual-status]
- Duration: [how long mismatch exists]
- Action taken: [treated as X per metadata priority]
- Recommendation: [migrate path / escalate / confirm status]
```

### Log location
- Framework daily report: `systems/pm-agent/reports/daily/YYYY-MM-DD.md`
- Selector audit section trong cron log

---

# 8. Escalation rule

### Khi nào phải escalate?

**Escalate ngay khi:**
- mismatch kéo dài quá timeout cho phép
- không rõ status thật là gì
- có conflict giữa nhiều source (metadata vs path vs dashboard vs owner statement)

**Escalation action:**
- ghi rõ trong daily report
- đề xuất owner confirm status
- không tự quyết định migrate nếu chưa rõ ý định owner

---

# 9. Rule cứng

1. **Metadata thắng path** khi conflict
2. **Không tự migrate** nếu chưa có approval/confirmation rõ ràng
3. **Phải log mismatch** mỗi lần phát hiện
4. **Không để mismatch kéo dài** quá timeout cho phép
5. **Selector phải bám metadata**, không bám path
6. **Report phải ghi rõ** khi có mismatch

---

# 10. Ví dụ thực tế

## Case 1: Project vừa chuyển on-hold
```yaml
# project.yaml
status: on-hold
updated_at: 2026-05-15T06:00:00Z
```

**Path hiện tại:** `projects/active/web-ban-hang/`

**Hành vi đúng:**
- Selector coi project là `on-hold`
- Skip trong daily active project report
- Log warning về mismatch
- Đề xuất migrate trong vòng 24h

## Case 2: Project archived nhưng chưa move
```yaml
# project.yaml
status: archived
updated_at: 2026-05-10T10:00:00Z
```

**Path hiện tại:** `projects/active/web-ban-hang/`

**Hành vi đúng:**
- Selector coi project là `archived`
- Skip hoàn toàn trong daily report
- Log warning nghiêm trọng (đã quá 5 ngày)
- Escalate yêu cầu migrate ngay

## Case 3: Không rõ status thật
```yaml
# project.yaml
status: active
updated_at: 2026-04-20T10:00:00Z
```

**Path hiện tại:** `projects/active/web-ban-hang/`
**Observation:** Không có update meaningful quá 25 ngày

**Hành vi đúng:**
- Selector vẫn coi là `active` theo metadata
- Nhưng phải trigger stale detection
- Đề xuất owner xác nhận status thật
- Có thể đề xuất chuyển `on-hold` hoặc `stopped`

---

# 11. Kết luận ngắn

**Nguyên tắc cứng:**
- Metadata là source of truth
- Path phải theo metadata
- Mismatch phải được log và xử lý
- Không để mismatch kéo dài vô thời hạn
- Selector/report phải bám metadata, không bám path
