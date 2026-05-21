# PM Agent Update Plan - 2026-05-14

- **Scope:** Đợt nâng cấp production-readiness cho chính `systems/pm-agent/`
- **Owner:** Anh Doanh + PM Agent
- **Status:** Active plan - revised to Option B on 2026-05-15
- **Purpose:** Biến PM Agent từ framework đã validate sang hệ có thể đưa vào sử dụng thực tế ổn định hơn.
- **Execution mode:** Interleaved priority execution (Option B), không khóa cứng hoàn tất toàn bộ Phase 2 rồi mới sang Phase 3.

## Vì sao file này lưu ở đây?

**Path:** `systems/pm-agent/reports/plans/update-pma-plan-2026-05-14.md`

### Lý do chọn vị trí này
1. Đây là **kế hoạch nâng cấp cho chính PM Agent framework**
2. Không phải project nghiệp vụ trong `projects/`
3. Không phải tri thức tham khảo tĩnh trong `knowledge/`
4. Không phải memory cá nhân trong `agent-core/`
5. `systems/pm-agent/reports/plans/` phù hợp cho các kế hoạch vận hành / nâng cấp / đợt cải tiến của framework

---

# Revision Note - 2026-05-15

## Vì sao cần revise plan?
Sau khi chạy production cron thực tế và review trạng thái hiện tại của framework, phát sinh 3 điểm mới:
1. **Phase 2 không còn là phần chỉ ở mức thiết kế** vì cron/report flow 19:00 đã có spec, runbook và đã chạy production.
2. **Xuất hiện operational mismatch** giữa project path và metadata status (`projects/active/web-ban-hang` nhưng `status: on-hold`).
3. **Acceptance verification và stale detection** cần được kéo lên sớm hơn vì tác động trực tiếp tới độ tin cậy vận hành.

## Quyết định mới
- **Không bỏ Phase 3**.
- **Không giữ tuần tự cứng Phase 2 → Phase 3**.
- Chuyển sang **Option B**:
  - hoàn tất các phần quan trọng còn lại của Phase 2
  - kéo một phần critical của Phase 3 lên làm sớm
  - thêm `lifecycle/path policy` như một hạng mục ưu tiên mới

---

# Checklist tổng thể đợt update

## Mục tiêu đợt này
- tăng production-readiness của PM Agent
- làm report hằng ngày đáng tin hơn
- tăng khả năng audit “ai làm gì”
- chuẩn hóa vận hành cho project thực tế
- giảm khoảng cách giữa framework hiện tại và production use
- giảm rủi ro “done giả”, stale project, và selector/report mismatch

## Trạng thái tổng thể hiện tại
- **Framework + validation completion:** ~85-88%
- **Production-readiness estimate:** ~78-82%
- **Framework stage:** Evaluation / Refinement after first real project validation
- **Production cron:** đã chạy thực tế
- **Production-grade state:** chưa hoàn tất

## Mức ưu tiên hiện tại

### Phase 1 - Foundation đã hoàn tất mức nền
- [x] Chuẩn hóa **actor tracking convention**
- [x] Gắn actor vào các artifact vận hành chính
- [x] Cập nhật `production-readiness-checklist.md` cho khớp thực tế
- [x] Chuẩn hóa cấu trúc daily reporting cho framework và project

### Phase 2 - Daily reporting hardening
- [x] Thiết kế cron/report flow 19:00
- [x] Chuẩn hóa nguồn dữ liệu cho `daily-project-report-generator`
- [x] Bổ sung stale/no-change handling cho daily report
- [x] Quy định output policy cho daily report
- [x] Framework vs project report separation ở mức nền
- [x] Production cron chạy lần đầu
- [x] PDF export flow được kích hoạt

### Cross-phase Priority - Policy fix phát sinh từ thực tế
- [x] Chốt `lifecycle/path policy`
- [x] Quy định rõ `metadata status` vs `folder path` cái nào là source of truth
- [x] Quy định cách xử lý target `on-hold/stopped/archived` đang nằm sai thư mục
- [x] Thêm warning/audit logging cho mismatch

### Phase 3 - Hardening cho production
- [x] Tạo acceptance verification rules
- [x] Tạo stale-project detection rules
- [x] Bổ sung regression/eval pack v1
- [x] Bổ sung archived/portfolio dashboard foundation

> Note: Acceptance verification đã được làm sớm hơn do hiểu nhầm thứ tự. Từ đây sẽ quay lại bám rule: hoàn tất phase hiện tại rồi mới sang phase tiếp theo.

---

# Kế hoạch chi tiết

## Phase 1 — Actor tracking + trạng thái thật

### 1.1. Tạo chuẩn actor tracking
**Mục tiêu:** Mọi thay đổi quan trọng phải biết ai làm.

**Status:** Done at foundation level

**Checklist:**
- [x] Định nghĩa actor format chuẩn:
  - `human:[name]`
  - `agent:main`
  - `subagent:[label-or-session]`
  - `unknown`
- [x] Tạo file policy cho actor tracking
- [x] Chỉ rõ nguồn actor ưu tiên:
  1. explicit actor trong docs
  2. handoff
  3. change log / decision log
  4. git author
  5. unknown
- [x] Quy định khi nào **không được bịa actor**

**Output mong muốn:**
- policy file cho actor tracking trong `systems/pm-agent/runtime/policies/`

---

### 1.2. Gắn actor vào artifact chính
**Mục tiêu:** Report sau này có dữ liệu thật để tổng hợp.

**Status:** Done at foundation level

**Checklist:**
- [x] Cập nhật quy ước cho:
  - task board
  - change log
  - issue log
  - handoffs
  - decisions
  - approvals
- [x] Tạo mẫu handoff có trường actor rõ ràng
- [x] Tạo quy ước change entry có actor rõ ràng
- [x] Tạo quy ước issue update có actor rõ ràng

**Output mong muốn:**
- update template / guideline / sample output trong PM Agent

---

### 1.3. Sửa readiness checklist cho đúng thực tế
**Mục tiêu:** PM Agent tự đánh giá đúng trạng thái hiện tại.

**Status:** Done

**Checklist:**
- [x] Đối chiếu checklist hiện tại với cấu trúc thực tế
- [x] Mark lại các mục đã có nhưng đang ghi thiếu
- [x] Tách rõ:
  - foundation đã xong
  - partial
  - chưa làm
- [x] Thêm ghi chú blocker thực tế

**Output mong muốn:**
- `systems/pm-agent/eval/checklists/production-readiness-checklist.md` phản ánh đúng trạng thái thật

---

## Phase 2 — Daily report 19:00

### 2.1. Hardening skill `daily-project-report-generator`
**Mục tiêu:** Skill không chỉ sinh khung mà bắt đầu đọc dữ liệu thật tốt hơn.

**Status:** Done

**Checklist:**
- [x] Đọc thêm từ:
  - git log
  - handoffs
  - decisions
  - approvals
  - change log
- [x] Bổ sung actor attribution logic
- [x] Bổ sung no-change mode
- [x] Bổ sung stopped/on-hold project handling
- [x] Bổ sung framework-report mode cho `systems/pm-agent/`

**Output mong muốn:**
- skill daily report usable hơn cho thực tế

---

### 2.2. Cron flow 19:00
**Mục tiêu:** Mỗi ngày có thể tự sinh report đúng giờ với hành vi rõ ràng, audit được.

**Status:** Foundation done, production running

**Checklist:**
- [x] Chọn cơ chế chạy:
  - OpenClaw cron
  - hoặc system cron
- [x] Xác định project selector rule:
  - active only
  - exclude stopped/on-hold/archived
- [x] Xác định naming rule cho report
- [x] Xác định fail behavior:
  - nếu thiếu dữ liệu thì sao
  - nếu không có thay đổi thì sao
- [x] Xác định notify policy:
  - chỉ ghi file
  - hay báo luôn cho anh
- [x] Có spec cron flow 19:00
- [x] Có runbook vận hành
- [x] Đã chạy production thực tế
- [x] Tăng logging/audit output cho selected vs skipped targets
- [x] Theo dõi ổn định các lần chạy tiếp theo

**Output mong muốn:**
- cron flow usable trong production có kiểm soát

---

## Cross-phase Priority — Lifecycle / Path Policy

### X.1. Chốt lifecycle/path policy
**Mục tiêu:** Tránh selector/report hiểu sai trạng thái project do lệch giữa path và metadata.

**Status:** Done

**Checklist:**
- [x] Định nghĩa mapping lifecycle chuẩn:
  - `active` → `projects/active/`
  - `on-hold` → `projects/on-hold/`
  - `stopped` → `projects/stopped/`
  - `archived` → `projects/archived/`
- [x] Chốt source of truth khi path và metadata conflict:
  - ưu tiên `project.yaml`
  - path chỉ là signal phụ
- [x] Định nghĩa migration policy:
  - move ngay
  - hoặc delay move nhưng phải log mismatch
- [x] Bổ sung rule cho cron/report selector khi gặp mismatch
- [x] Bổ sung warning/audit output cho mismatch

**Output mong muốn:**
- policy rõ cho lifecycle/path
- tránh report sai target
- tránh vận hành nhầm project non-active như active

---

## Phase 3 — Hardening production

### 3.1. Acceptance verification
**Mục tiêu:** Tránh task “done giả”.

**Status:** Done

**Checklist:**
- [x] Định nghĩa thế nào là done
- [x] Định nghĩa evidence tối thiểu
- [x] Định nghĩa khi nào được close issue
- [x] Định nghĩa khi nào được close project
- [x] Phân biệt rõ `demo-ready`, `validated`, `production-ready`

**Lý do được kéo lên sớm:**
- ảnh hưởng trực tiếp tới độ tin cậy report
- giảm false close / false done
- giúp audit meaningful hơn

---

### 3.2. Stale-project detection
**Mục tiêu:** Không để project chết mềm mà không biết.

**Status:** Done

**Checklist:**
- [x] Xác định ngưỡng stale theo thời gian
- [x] Xác định stale task / stale approval / stale project
- [x] Định nghĩa cách escalate
- [x] Định nghĩa severity level:
  - warning
  - needs-review
  - blocked
  - owner-attention

**Lý do làm sau acceptance verification:**
- tránh stale detection bị noisy / false positive
- cần bám trên definition of done rõ ràng

---

### 3.3. Regression / eval pack
**Mục tiêu:** Sau mỗi đợt chỉnh skill/runtime không bị tụt chất lượng.

**Status:** Done

**Checklist:**
- [x] Tạo scenario:
  - vague requirement
  - scope change
  - worker failure
  - missing approval
  - stale project
  - false done
  - source conflict
  - on-hold project nằm trong `projects/active/`
  - no-change day
  - missing actor
- [x] Tạo expected behaviors
- [x] Tạo checklist pass/fail

**Output mong muốn:**
- eval pack v1 đủ để test nhanh các lỗi workflow quan trọng

---

# Thứ tự triển khai theo Option B

## Priority order mới
1. **Hoàn tất hardening daily report**
2. **Chốt lifecycle/path policy**
3. **Acceptance verification rules**
4. **Stale detection rules**
5. **Regression/eval pack v1**
6. **Archived/portfolio/dashboard foundation** (sau)

## Ý nghĩa của order mới
- Không ép hoàn tất toàn bộ Phase 2 rồi mới sang Phase 3
- Giữ focus vào các hạng mục tăng **độ tin cậy vận hành thực tế**
- Ưu tiên các phần có tác động trực tiếp tới:
  - report quality
  - auditability
  - false done prevention
  - stale detection
  - selector correctness

---

# Tiêu chí hoàn thành đợt update

Đợt update này được xem là đạt khi:
- [x] PM Agent có actor tracking policy rõ ràng
- [x] Daily report có thể phản ánh actor tốt hơn
- [x] Readiness checklist khớp với trạng thái thật
- [x] Có spec rõ cho cron 19:00
- [x] Có lifecycle/path policy rõ ràng
- [x] Có rule cơ bản để tránh done giả
- [x] Có rule phát hiện project stale
- [x] Có bộ eval nền cho các lỗi workflow chính
- [x] Cron/report logging đủ rõ để audit selected vs skipped targets

---

# Ghi chú

## Những gì đã thay đổi so với bản plan đầu
- Phase 3 **không bị bỏ**
- Một phần critical của Phase 3 được **bring-forward**
- Bổ sung hạng mục mới: `lifecycle/path policy`
- Cập nhật plan từ mode **phase-gated** sang **priority-interleaved**

## Chưa làm ngay trong bước này
- chưa mở rộng portfolio dashboard đầy đủ
- chưa coi PM Agent là production-grade hoàn chỉnh
- chưa mở rộng thêm automation ngoài các lớp đang harden

## Sau revision này
Em sẽ bám theo **Option B** và ưu tiên theo thứ tự mới, thay vì giữ tuần tự cứng theo phase cũ.
