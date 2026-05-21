# Cross-Project Risk View

Góc nhìn rủi ro xuyên nhiều project để tìm pattern lặp lại trong cách PM Agent vận hành.

---

## Current Cross-Project Observation
Vì danh mục project hiện còn nhỏ, view này hiện thiên về **pattern/risk hypotheses** hơn là thống kê lớn.

---

## Repeating Risk Patterns

### 1. Source-of-truth drift
**Mô tả:** Các artifact khác nhau có thể lệch nhau về progress/status.

**Đã thấy ở đâu:**
- `web-ban-hang`: `project.yaml` và `task-board.md` conflict về completed/completion

**Rủi ro:**
- daily report sai
- dashboard sai
- PM Agent kết luận sai về trạng thái dự án

**Mitigation direction:**
- conflict detection trong reporting
- acceptance verification
- stale/source audit định kỳ

---

### 2. Done giả / verification yếu
**Mô tả:** Task có thể bị coi là done quá sớm nếu thiếu evidence hoặc verify.

**Đã thấy ở đâu:**
- pattern đã được xác định là risk trong PM Agent hardening

**Rủi ro:**
- task board đẹp nhưng trạng thái thật không chắc chắn
- final status dễ bị tô hồng

**Mitigation direction:**
- acceptance verification policy
- regression scenario `false-done`

---

### 3. Active nhưng thực tế đã dừng
**Mô tả:** Project vẫn ghi `active` trong metadata dù không còn active work.

**Đã thấy ở đâu:**
- `web-ban-hang` trước khi được đổi sang `on-hold`

**Rủi ro:**
- cron/report chạy sai target
- portfolio view sai
- owner hiểu nhầm tình trạng thực

**Mitigation direction:**
- stale-project detection
- status sync discipline

---

### 4. Actor attribution yếu
**Mô tả:** Khó truy chính xác ai làm gì nếu artifact không có actor fields.

**Rủi ro:**
- audit yếu
- lessons learned khó tin cậy
- report khó phân biệt human / main agent / subagent

**Mitigation direction:**
- actor tracking policy
- actor fields trong approvals/decisions/change/issues/handoffs

---

## Current Cross-Project Risk Status
- **High:** source-of-truth drift
- **High:** false done / weak verification
- **Medium:** stale active status
- **Medium:** weak actor attribution

---

## Current Limitation
View này hiện còn dựa trên ít project, nên nên coi là:
- **operational learning view**
- chưa phải thống kê lớn đủ mạnh

---

## Next Step
Khi có thêm project active mới, cần cập nhật view này để:
- xem risk nào lặp lại nhiều nhất
- risk nào đã giảm sau hardening
- hardening nào thực sự hiệu quả

Last updated: 2026-05-14T10:05:00Z
