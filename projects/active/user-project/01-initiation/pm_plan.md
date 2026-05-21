## Phân tích brief dự án

Mục tiêu của yêu cầu này là **kiểm tra tính đồng bộ giữa task được giao, output sub-agent, file thực tế trong workspace và evidence hoàn thành**.

Đây là một task dạng **Workspace Audit / Delivery Verification**, không phải task phát triển tính năng mới.

Kết quả mong muốn là một báo cáo theo format:

```md
# Workspace Inspection Result
...
```

Báo cáo cần trả lời rõ:

- Project root hiện tại là gì.
- Gần đây agent/sub-agent đã tạo hoặc sửa file nào.
- Có Git status/diff không.
- Có artifact chuẩn không: PRD, Acceptance Criteria, Technical Spec, API Contract, implementation report, QA report, final-report.
- Output từng sub-agent nằm ở đâu hoặc nội dung là gì.
- Task board hiện tại có khớp với hiện trạng workspace không.
- Có test evidence thực sự không.
- Có lỗi nào khi chạy lệnh kiểm tra không.

---

# Sơ đồ thực thi đề xuất

```text
User Brief
   |
   v
PM Orchestrator
   |
   +--> product-agent
   |       - Xác định checklist acceptance cho audit
   |       - Định nghĩa tiêu chí "đồng bộ / lệch / thiếu evidence"
   |
   +--> architecture-agent
   |       - Xác định cấu trúc artifact kỳ vọng
   |       - Đề xuất mapping: task -> file -> evidence -> agent output
   |
   +--> frontend-agent
   |       - Kiểm tra các file frontend đã tạo/sửa
   |       - Đối chiếu với task frontend nếu có
   |
   +--> backend-agent
   |       - Kiểm tra các file backend/API đã tạo/sửa
   |       - Đối chiếu với API Contract và task backend nếu có
   |
   +--> qa-agent
           - Chạy/đọc test evidence
           - Kiểm tra Git status, diff, logs, reports
           - Tổng hợp lỗi, thiếu hụt, mismatch

PM Orchestrator
   |
   v
Final Workspace Inspection Result
```

---

# Phân rã công việc sơ bộ

## 1. product-agent

**Mục tiêu:**  
Xác định tiêu chí nghiệm thu cho việc audit workspace.

**Task:**

- Đọc brief.
- Chuẩn hóa checklist kiểm tra:
  - File mới/sửa gần đây.
  - Artifact bắt buộc.
  - Task board/task state.
  - Output sub-agent.
  - Evidence test.
  - Git status/diff.
- Định nghĩa trạng thái:
  - `Synced`
  - `Partially Synced`
  - `Missing Evidence`
  - `Mismatch`
  - `Unknown`

**Output mong đợi:**

- `acceptance-criteria.md`
- Checklist audit ngắn gọn.

---

## 2. architecture-agent

**Mục tiêu:**  
Thiết kế cấu trúc kiểm tra và mapping artifact.

**Task:**

- Xác định các nhóm file cần tìm:
  - PRD / Acceptance Criteria
  - Technical Spec / API Contract
  - Frontend report/implementation
  - Backend report/implementation
  - QA report/test evidence
  - Task board/tasks/state
  - Final report
- Đề xuất bảng mapping:

```text
Task được giao -> File thực tế -> Output agent -> Evidence -> Trạng thái
```

**Output mong đợi:**

- `workspace-audit-spec.md`
- Danh sách pattern file cần scan.

---

## 3. frontend-agent

**Mục tiêu:**  
Kiểm tra phần frontend trong workspace.

**Task:**

- Tìm các file frontend mới/sửa gần đây.
- Xác định có report/output frontend-agent không.
- Đối chiếu với task frontend nếu có.
- Ghi nhận thiếu evidence hoặc mismatch.

**Không sửa file backend.**

**Output mong đợi:**

- `frontend-inspection-report.md`

---

## 4. backend-agent

**Mục tiêu:**  
Kiểm tra phần backend/API trong workspace.

**Task:**

- Tìm các file backend/API mới/sửa gần đây.
- Xác định có API Contract hoặc technical spec không.
- Xác định có backend output/report không.
- Đối chiếu task backend với file thực tế.
- Kiểm tra nếu có test/log liên quan API.

**Không sửa file frontend.**

**Output mong đợi:**

- `backend-inspection-report.md`

---

## 5. qa-agent

**Mục tiêu:**  
Chạy kiểm tra tổng hợp và thu thập evidence.

**Task:**

Chạy các lệnh PowerShell tại project root:

```powershell
Get-Location

Get-ChildItem -Force

Get-ChildItem -Recurse -Force |
  Select-Object FullName, LastWriteTime, Length |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 100

Get-ChildItem -Recurse -Force -Include `
  *prd*,*PRD*,*acceptance*,*criteria*,*spec*,*architecture*,*api*,*contract*,*qa*,*test*,*report*,*task*,*plan*,*final* |
  Select-Object FullName, LastWriteTime, Length |
  Sort-Object LastWriteTime -Descending

git status --short
git diff --stat
git diff

Get-ChildItem -Recurse -Force -Include *.log,*.md,*.json,*.txt |
  Select-Object FullName, LastWriteTime, Length |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 200
```

**Output mong đợi:**

- `qa-workspace-inspection.md`
- Test/log evidence.
- Known errors nếu lệnh lỗi.

---

# Vai trò PM Orchestrator

PM sẽ tổng hợp toàn bộ output thành báo cáo cuối:

```md
# Workspace Inspection Result

## 1. Project Root
...

## 2. Recent Files
...

## 3. Git Status
...

## 4. Artifact Files Found
...

## 5. Sub-agent Outputs
### product-agent
...
### architecture-agent
...
### frontend-agent
...
### backend-agent
...
### qa-agent
...

## 6. Task State
...

## 7. Test Evidence
...

## 8. Known Errors
...
```

---

# Thứ tự triển khai đề xuất

1. **Wave 1 — Chuẩn hóa tiêu chí**
   - product-agent
   - architecture-agent

2. **Wave 2 — Kiểm tra theo miền**
   - frontend-agent
   - backend-agent

3. **Wave 3 — QA inspection**
   - qa-agent chạy lệnh PowerShell, kiểm tra Git, logs, artifacts.

4. **Wave 4 — PM tổng hợp**
   - Tạo `Workspace Inspection Result`.
   - Đánh dấu mismatch, thiếu evidence, task chưa đồng bộ.
   - Đề xuất bước khắc phục tiếp theo.