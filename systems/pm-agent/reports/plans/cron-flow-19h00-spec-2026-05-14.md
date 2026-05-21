# PM Agent Cron Flow 19:00 Spec - 2026-05-14

- **Scope:** Thiết kế cron/report flow chạy lúc 19:00 cho PM Agent
- **Status:** Draft for review
- **Applies to:** framework daily report + project daily report
- **Current stage:** Spec only, chưa bật cron production

## Vì sao file này lưu ở đây?

**Path:** `systems/pm-agent/reports/plans/cron-flow-19h00-spec-2026-05-14.md`

### Lý do
1. Đây là **thiết kế vận hành cho chính PM Agent framework**
2. Chưa phải cron đang bật thật trong runtime
3. Là tài liệu spec/plan trước khi triển khai production
4. Không phải artifact tạm trong `ops/`
5. Không phải project business cụ thể trong `projects/`

---

# Mục tiêu

Thiết kế một luồng báo cáo chạy lúc **19:00 mỗi ngày** để:
- sinh daily report nhất quán
- chọn đúng target cần report
- tránh spam report cho project đã dừng
- xử lý an toàn khi thiếu dữ liệu hoặc source conflict
- hỗ trợ cả framework report và project report

---

# 1. Cơ chế chạy đề xuất

## Đề xuất chính
**Ưu tiên: OpenClaw cron**

### Vì sao chọn OpenClaw cron
- cùng hệ với PM Agent
- dễ giữ ngữ cảnh workflow hơn system cron
- phù hợp với task logic của agent
- dễ mở rộng sang notify/report routing sau này

## Phương án fallback
**System cron** chỉ dùng khi:
- OpenClaw cron không đủ linh hoạt
- cần watchdog độc lập ngoài runtime agent
- có vấn đề với lifecycle của daemon/session

## Kết luận cơ chế chạy
- **Primary:** OpenClaw cron
- **Fallback:** system cron

---

# 2. Cron schedule rule

## Mốc mặc định
- **19:00 mỗi ngày**

## Timezone
- Mặc định phải theo **timezone cấu hình thực tế của ownerD:/Antigravity/LeeJ_MultiAgent**
- Không hardcode UTC nếu mục tiêu là báo cáo theo giờ sinh hoạt của anh

## Rule
Nếu triển khai thật, spec cron phải có trường:
- timezone
- schedule
- enabled/disabled

Ví dụ logic:
```yaml
schedule: "0 19 * * *"
timezone: "Asia/Ho_Chi_Minh"
enabled: false
```

**Lưu ý:** Hiện mới là spec, chưa bật thật.

---

# 3. Reporting targets

## Target loại A — Framework report
Path output:
`systems/pm-agent/reports/daily/YYYY-MM-DD.md`

### Khi nào chạy?
Chạy khi:
- PM Agent framework còn đang ở trạng thái active refinement / production-readiness work
- có thay đổi liên quan `systems/pm-agent/` trong ngày
- hoặc đang bật chế độ bắt buộc daily snapshot cho framework

### Khi nào bỏ qua?
Bỏ qua nếu:
- không có thay đổi đáng kể
- framework đang ở trạng thái ổn định và không cần daily snapshot
- owner tắt framework daily reporting

---

## Target loại B — Project report
Path output:
`projects/active/[project-name]/reports/daily/YYYY-MM-DD.md`

### Khi nào chạy?
Chạy khi project:
- có `project.yaml`
- status = `active`
- không bị exclude thủ công

### Không chạy mặc định khi:
- status = `on-hold`
- status = `stopped`
- status = `archived`

### Ngoại lệ
Vẫn có thể chạy nếu:
- owner yêu cầu rõ
- cần snapshot audit ngày cuối
- cần handoff/status capture đặc biệt

---

# 4. Project selector rule

## Rule mặc định
Chỉ chọn project có:
- nằm trong `projects/active/`
- có `project.yaml`
- `status: active`

## Rule loại trừ
Loại khỏi cron mặc định nếu:
- `status: on-hold`
- `status: stopped`
- `status: archived`
- có flag `daily_reporting: disabled` (nếu sau này thêm vào metadata)

## Rule tương lai nên có
Khuyên bổ sung vào `project.yaml` sau này:
```yaml
daily_reporting:
  enabled: true
  schedule: "19:00"
  notify: false
```

---

# 5. Output rule

## Naming
- mặc định: `YYYY-MM-DD.md`
- 1 file/ngày

## Overwrite vs append
### Rule đề xuất
- nếu file ngày đó **chưa có** → tạo mới
- nếu file ngày đó **đã có** → mặc định overwrite bằng bản mới nhất

### Lý do
- daily report nên có 1 canonical snapshot cuối ngày
- tránh sinh nhiều file rối

## Ngoại lệ
Nếu muốn giữ nhiều lần chạy trong cùng ngày, phải bật mode đặc biệt:
- `YYYY-MM-DD-update-2.md`

Nhưng **không nên là mặc định**.

---

# 6. No-change behavior

## Nếu không có thay đổi đáng kể
Vẫn có 2 chiến lược có thể chọn:

### Strategy A — vẫn tạo report
Report ghi rõ:
- `No significant change today`
- đang chờ gì
- trạng thái hiện tại là gì

### Strategy B — không tạo report, chỉ log skip
Dùng khi muốn tránh report rỗng.

## Đề xuất
- **Framework:** có thể dùng Strategy A nếu đang trong giai đoạn refinement mạnh
- **Project:** mặc định dùng **Strategy B** để tránh rác, trừ khi owner muốn snapshot mỗi ngày bất kể có thay đổi hay không

---

# 7. Source conflict behavior

## Nếu phát hiện conflict giữa sources
Ví dụ:
- `project.yaml` khác `task-board.md`
- status dashboard khác metrics hiện tại

## Rule
- report **vẫn được tạo**
- phải có section `Source Conflicts Detected`
- không được tự chọn bừa một nguồn đẹp hơn
- next actions phải yêu cầu resolve conflict nếu conflict ảnh hưởng điều hành

## Nếu conflict nghiêm trọng
Có thể đánh dấu report:
- `Needs review`
- hoặc `Data conflict present`

---

# 8. Fail behavior

## Nếu thiếu dữ liệu một phần
Ví dụ thiếu:
- issue log
- approvals
- handoffs

### Rule
- vẫn tạo report nếu còn đủ source tối thiểu
- ghi phần thiếu là:
  - `None`
  - hoặc `unknown`
- không fail toàn bộ job

## Nếu thiếu dữ liệu cốt lõi
Ví dụ:
- project mode mà thiếu `project.yaml`
- framework mode mà thiếu `systems/pm-agent/STATUS.md`

### Rule
- không tạo report chính thức
- ghi log failure
- nếu notify bật → gửi cảnh báo ngắn

---

# 9. Notify policy

## Chính sách đề xuất mặc định
- **Mặc định:** chỉ ghi file, **không gửi tin nhắn**

## Vì sao
- giảm spam
- report daily không phải lúc nào cũng cần đẩy ra chat
- owner có thể xem khi cần

## Tùy chọn sau này
Có thể hỗ trợ:
- `notify: false` → chỉ ghi file
- `notify: summary` → gửi 1 dòng tóm tắt
- `notify: full` → gửi toàn bộ report hoặc PDF

## Trigger nên notify dù mặc định false
- cron fail
- thiếu source tối thiểu
- conflict nghiêm trọng
- report target bị skip bất thường

---

# 10. Framework vs project precedence

## Rule đề xuất
Cron 19:00 nên xử lý theo thứ tự:
1. framework report
2. project reports active
3. log skipped targets
4. emit summary nội bộ (nếu cần)

## Lý do
- framework report cho biết chính PM Agent có đang khỏe không
- sau đó mới tới từng project

---

# 11. Logging & audit

Cron flow nên log:
- chạy lúc nào
- target nào được chọn
- target nào bị skip
- report path nào được sinh
- có conflict hay không
- fail reason nếu có

Tối thiểu nên có log nội bộ ở runtime hoặc file log sau này.

---

# 12. Chốt thiết kế đề xuất

## Quyết định hiện tại
- **Cron engine ưu tiên:** OpenClaw cron
- **Schedule:** 19:00 theo timezone cấu hình thật
- **Framework report:** chạy có điều kiện
- **Project report:** chỉ cho project `status: active`
- **On-hold/stopped/archived:** không chạy mặc định
- **No-change project:** mặc định skip, không tạo rác
- **Conflict:** vẫn tạo report nhưng phải báo conflict
- **Notify mặc định:** không gửi chat, chỉ ghi file

---

# 13. Việc cần làm sau khi duyệt spec

## Trước khi bật cron thật
- [ ] Chốt timezone chính thức
- [ ] Chốt có cần framework report mỗi ngày không
- [ ] Chốt policy no-change cho project
- [ ] Chốt có thêm flag `daily_reporting.enabled` vào `project.yaml` không
- [ ] Chốt notify policy

## Khi bắt đầu triển khai
- [ ] Implement selector rule
- [ ] Implement cron config
- [ ] Implement logging
- [ ] Test active project
- [ ] Test on-hold project bị skip đúng cách
- [ ] Test source conflict behavior

---

# Kết luận ngắn

Spec này chọn hướng an toàn:
- **không spam**
- **không tạo report sai ngữ cảnh**
- **không tự hòa giải dữ liệu mâu thuẫn**
- **ưu tiên framework + project active thật sự**

