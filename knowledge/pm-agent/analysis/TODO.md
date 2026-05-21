# TODO

## Ghi chú tiếp tục từ phân tích cuộc họp

### Thông tin liên kết cuộc họp
- **Ngày họp:** 2026-04-25
- **Ngày tạo TODO:** 2026-05-05
- **File ghi chú cuộc họp liên quan:** `../Ghi-Chu-Cuoc-Hop/2026-04-25-Ghi-Chu-Cuoc-Hop.md`

### Mục tiêu
Lưu lại các phân tích và quyết định tạm thời của anh sau khi đọc phần phân tích cuộc họp. Sau khi hoàn thành Phần 6, sẽ áp dụng các nội dung phù hợp vào OpenClaw / hệ thống PM Agent.

### Kết luận đã chốt từ Phần 1 và 2
- Claude-mem đang hoạt động khá ổn nên không cần chỉnh sửa gì.
- Cần thiết kế quy tắc để Agent sử dụng Obsidian chuẩn xác.
- Cần cẩn thận thiết kế việc mount thư mục để OpenClaw thao tác với Obsidian.
- Cần phân tích và phân chia vai trò hợp lý giữa Claude-mem và Obsidian.
- Cần thiết kế luồng hoạt động phù hợp cho Claude-mem và Obsidian khi lưu thông tin.

---

## Kế hoạch triển khai tổng thể sau khi đã rà soát và gộp ý trùng

### Bước 0 - Hướng dẫn liên kết OpenClaw/Lệ với Telegram để anh và em có thể chat qua Telegram
**Mục tiêu:** tạo kênh giao tiếp thực tế đầu tiên giữa anh và em thông qua Telegram trước khi đi sâu vào các bước nâng cấp khác.

#### Việc cần làm
- Kiểm tra OpenClaw hiện có hỗ trợ/cấu hình Telegram tới đâu.
- Hướng dẫn anh tạo Telegram Bot và lấy bot token.
- Cấu hình Telegram cho OpenClaw.
- Kiểm tra anh có thể nhắn tin với Lệ qua Telegram thành công.
- Xác định đây là kênh chat chính dùng để tiếp tục phát triển PM Agent.

#### Kết quả mong muốn
- Anh và em có thể chat ổn định qua Telegram.
- Có nền giao tiếp thật để thử các bước tiếp theo.

---

### Bước 1 - Chốt nền bộ nhớ và kho tri thức
**Mục tiêu:** làm rõ vai trò của Claude-mem và Obsidian trước khi phát triển tính năng mới.

#### Việc cần làm
- Thiết kế quy tắc để Agent sử dụng Obsidian chuẩn xác.
- Phân chia vai trò giữa Claude-mem và Obsidian:
  - Claude-mem: nhớ ngữ cảnh, thông tin quan trọng, truy hồi khi cần.
  - Obsidian: lưu note, tài liệu, decision log, project knowledge.
- Thiết kế luồng lưu thông tin:
  - thông tin nào lưu vào Claude-mem
  - thông tin nào lưu vào Obsidian
  - thông tin nào chỉ xử lý tạm thời
- Xác định cấu trúc note/project trong Obsidian.

#### Kết quả mong muốn
- Có quy tắc rõ để tránh lưu sai chỗ, lưu trùng hoặc ghi chú lộn xộn.

---

### Ghi chú cập nhật roadmap
- **Bước 1 đã hoàn thành.**
- **Output của Bước 1** là 2 file hiện có trong nhóm nội dung này:
  - `../Ghi-Chu-Cuoc-Hop/2026-04-25-Ghi-Chu-Cuoc-Hop.md`
  - `./TODO.md`
- **Bước 2** sẽ bắt đầu từ việc **thiết kế hạ tầng thực tế**.

### Bước 2 - Thiết kế hạ tầng Obsidian + Docker + GitHub
**Mục tiêu:** tạo nền hạ tầng ổn định để OpenClaw có thể thao tác dữ liệu và source code an toàn, lâu dài.

**Trạng thái hiện tại:** **tạm đủ dùng để chuyển sang Bước 3**.

#### Ghi chú thiết kế
- Note thiết kế hạ tầng thực tế đã tạo tại: `./BUOC-2-THIET-KE-HA-TANG-THUC-TE.md`
- Checklist triển khai thực tế đã tạo tại: `./BUOC-2-CHECKLIST-TRIEN-KHAI-HA-TANG.md`
- Quyết định tạm chốt: dùng mô hình **host-first storage + mounted access + GitHub for repos**.
- Không để Obsidian vault, source code hoặc skill quan trọng chỉ sống bên trong container.

#### Việc cần làm
- Thiết kế cách mount thư mục Obsidian từ ổ D vào Docker/WSL.
- Kiểm tra quyền đọc/ghi của OpenClaw với thư mục Obsidian.
- Xác định cách liên kết source code với GitHub để tránh code bị “kẹt” trong container.
- Chốt mô hình làm việc với source code:
  - code ở host và mount vào container
  - hoặc clone/pull từ GitHub theo quy trình rõ ràng
- Đảm bảo có thể commit/pull/push thuận tiện.

#### Kết quả mong muốn
- OpenClaw thao tác được với Obsidian.
- Source code và skill có thể quản lý ổn định bằng Git/GitHub.

#### Trạng thái hiện tại của Bước 2
- Đã chốt vault Obsidian thật:
  - Tên vault: `OpenClaw-Vault`
  - Đường dẫn Windows: `D:\OpenClaw\Obsidian\OpenClaw-Vault`
  - Đường dẫn WSL: `/mnt/d/OpenClaw/Obsidian/OpenClaw-Vault`
- Đã xác minh WSL nhìn thấy vault và đọc được `.obsidian`, `Welcome.md`.
- Đã xác minh container hiện tại **chưa có mount nào** và **chưa nhìn thấy vault Obsidian**.
- **Tạm thời bỏ qua phần mount Obsidian vào container** theo quyết định hiện tại.
- Đã chốt và tạo thư mục repo/source code trên host:
  - Windows: `D:\OpenClaw\Repos`
  - WSL: `/mnt/d/OpenClaw/Repos`
- Đã copy workspace từ container ra host:
  - Windows: `D:\OpenClaw\Repos\openclaw-workspace`
  - WSL: `/mnt/d/OpenClaw/Repos/openclaw-workspace`
- Đã kiểm tra Git trên repo host:
  - ban đầu nhiều file bị `M` do file mode khi copy sang ổ D
  - đã dùng `core.filemode false`
  - hiện chỉ còn các thay đổi thật cần xét commit
- Đã gắn GitHub remote và push thành công:
  - Repo: `https://github.com/LeeJMaiRap/openclaw-workspace`
  - Branch: `main`
  - Commit: `799fa40` - `Move workspace to host and update PM Agent roadmap`
- Đã tạo note quy trình đồng bộ tạm thời khi container còn tách khỏi host:
  - `./QUY-TRINH-DONG-BO-CONTAINER-TACH-HOST.md`
- **Kết luận:** Bước 2 hiện đã **tạm đủ dùng** để chuyển sang **Bước 3 - thiết kế nhóm skill lõi cho PM Agent**.

---

### Bước 3 - Thiết kế nhóm skill lõi cho PM Agent ✅
**Mục tiêu:** chia năng lực của agent thành các skill nhỏ, rõ đầu vào - đầu ra.

**Trạng thái:** ✅ **Đã hoàn thành** (cập nhật 2026-05-14)

**Kết quả đạt được:**
- ✅ Đã chốt danh sách **17 skill lõi** theo 4 nhóm chức năng
- ✅ Đã viết đầy đủ **spec + template + ví dụ cho 17/17 skill**
- ✅ Đã hoàn thành 4 nhóm:
  - `input-normalization` (3/3)
  - `document-generation` (8/8)
  - `project-operations` (5/5)
  - `infrastructure` (1/1)
- ✅ Đã có script thật cho `markdown-to-pdf`
- ✅ Đã **test workflow end-to-end** và tạo demo output tại:
  - `projects/pm-agent-e2e-demo/`
- ✅ Đã commit/push lên GitHub

**Danh sách 17 skill:**

*Nhóm A - Chuẩn hóa đầu vào (3):*
1. requirement-clarifier
2. meeting-notes-normalizer
3. action-items-extractor

*Nhóm B - Sinh tài liệu PM (8):*
4. project-charter-generator
5. requirements-document-generator
6. project-spec-generator
7. project-plan-generator
8. rules-generator
9. wbs-generator
10. schedule-generator
11. risk-register-generator

*Nhóm C - Vận hành dự án (5):*
12. task-board-builder
13. issue-log-updater
14. change-log-updater
15. status-dashboard-updater
16. lessons-learned-writer

*Nhóm D - Hạ tầng (1):*
17. markdown-to-pdf

---

### Bước 4 - Review kết quả E2E và tinh chỉnh skill ✅
**Mục tiêu:** rà soát output từ workflow end-to-end demo, xác định skill nào cần cải thiện.

**Trạng thái:** ✅ **Đã hoàn thành** (cập nhật 2026-05-14)

**Kết quả đạt được:**
- ✅ Đã review toàn bộ output trong `projects/pm-agent-e2e-demo/`
- ✅ Đã xác định 10 skills cần cải thiện, phân loại theo mức độ ưu tiên
- ✅ Đã sửa 9/10 skills (change-log-updater không cần sửa gấp)
- ✅ Đã thêm 6 reference guides mới:
  - `api-spec-guide.md`
  - `data-model-guide.md`
  - `clarification-questions-guide.md`
  - `recommended-actions-guide.md`
  - `metrics-notes-guide.md`
- ✅ Đã commit và push lên GitHub
- ✅ Đã làm lại bài test E2E với bộ skill mới (`pm-agent-e2e-demo-v2`)
- ✅ Đã xác nhận chất lượng output cải thiện rõ rệt

**Các skill đã cải thiện:**
1. project-spec-generator (ưu tiên CAO)
2. requirement-clarifier (ưu tiên TRUNG BÌNH)
3. status-dashboard-updater (ưu tiên TRUNG BÌNH)
4. wbs-generator (ưu tiên THẤP)
5. schedule-generator (ưu tiên THẤP)
6. risk-register-generator (ưu tiên THẤP)
7. issue-log-updater (ưu tiên THẤP)
8. lessons-learned-writer (ưu tiên THẤP)
9. task-board-builder (ưu tiên THẤP)

---

### Bước 5 - Tích hợp PM Agent vào workflow thực tế 🔄
**Mục tiêu:** áp dụng PM Agent vào công việc thật của anh, không chỉ là demo.

**Trạng thái:** 🔄 **Chưa bắt đầu**

#### Giai đoạn 1 - Chọn dự án pilot
- Chọn 1 dự án thật (có thể là dự án thực tập hoặc side project)
- Xác định scope và mục tiêu rõ ràng
- Chuẩn bị input thật (meeting notes, requirements, brief...)

#### Giai đoạn 2 - Chạy workflow thật
- Dùng PM Agent để tạo tài liệu thật cho dự án pilot
- Theo dõi task board, issue log, status dashboard
- Ghi nhận những chỗ skill hoạt động tốt và chỗ nào còn thiếu

#### Giai đoạn 3 - Cải tiến dựa trên thực tế
- Sửa skill dựa trên feedback từ dự án pilot
- Bổ sung skill mới nếu phát hiện thiếu
- Tinh chỉnh workflow cho phù hợp với cách làm việc thật

#### Kết quả mong muốn
- PM Agent trở thành công cụ hỗ trợ PM thực sự hữu ích
- Không chỉ là demo mà dùng được trong công việc hằng ngày

---

### Bước 6 - Nâng cấp trải nghiệm Telegram (tùy chọn) ⏸️
**Mục tiêu:** cải thiện cách tương tác qua Telegram khi cần.

**Trạng thái:** ⏸️ **Tạm hoãn** (Telegram text đã hoạt động ổn định)

#### Các nâng cấp có thể làm sau
- Voice-to-text: nhận voice note và chuyển thành text
- Text-to-voice: trả lời bằng voice khi cần
- File handling: xử lý file đính kèm tốt hơn
- Rich formatting: tận dụng Telegram formatting tốt hơn

#### Khi nào nên làm
- Khi workflow PM Agent đã ổn định
- Khi phát hiện voice/file thật sự cần thiết cho công việc
- Không ưu tiên cao hơn việc làm cho PM Agent hoạt động tốt

---

### Bước 7 - Tích hợp Obsidian sâu hơn (tùy chọn) ⏸️
**Mục tiêu:** liên kết PM Agent với Obsidian vault khi cần.

**Trạng thái:** ⏸️ **Tạm hoãn**

#### Việc có thể làm sau
- Mount Obsidian vault vào container
- Tự động lưu tài liệu PM vào Obsidian
- Sync giữa `projects/` và Obsidian vault
- Tận dụng Obsidian graph view cho project knowledge

#### Khi nào nên làm
- Khi workflow hiện tại (GitHub + workspace) không đủ
- Khi thật sự cần Obsidian features (backlinks, graph, plugins...)
- Không ưu tiên cao hơn việc PM Agent hoạt động tốt

---

## Roadmap hiện tại (cập nhật 2026-05-14)

### Đã hoàn thành ✅
0. ✅ Telegram đã kết nối và hoạt động ổn định
1. ✅ Đã chốt vai trò Claude-mem và Obsidian
2. ✅ Đã thiết kế hạ tầng GitHub + Docker (tạm đủ dùng)
3. ✅ Đã thiết kế và hoàn thành 17 skill lõi
4. ✅ Đã test workflow end-to-end và tạo demo output
5. ✅ Đã review E2E, xác định và sửa 9 skills cần cải thiện
6. ✅ Đã làm lại bài test E2E với bộ skill mới, xác nhận chất lượng tốt hơn
7. ✅ Đã bổ sung 2 skill voice còn thiếu:
   - `voice-to-text`
   - `text-to-voice`

### Đang làm / Sắp làm 🔄
8. 🔄 Tích hợp PM Agent vào workflow thực tế (chọn dự án pilot)

### Tạm hoãn / Tùy chọn ⏸️
9. ⏸️ Tích hợp Obsidian sâu hơn

---

## Nội dung đã được gộp / loại trùng
- Các ý “skill tài liệu PM” ở Phần 3 và Phần 4 đã được gộp lại thành 1 luồng chung.
- Các ý “Telegram + voice” đã được gộp thành thứ tự triển khai rõ ràng.
- Các ý về Claude-mem + Obsidian được đẩy lên đầu vì đây là nền tảng.
- Các ý về PDF được hạ xuống sau Markdown để tránh làm sai thứ tự ưu tiên.

---

## Ghi chú làm việc tiếp theo
- **Ưu tiên ngay:** Review output E2E demo để xác định skill nào cần cải thiện
- **Tiếp theo:** Chọn 1 dự án thật để áp dụng PM Agent
- **Nguyên tắc:** Tập trung vào việc làm cho PM Agent hoạt động tốt trong thực tế, không chạy theo tính năng phụ
- **Không ưu tiên:** Voice, Obsidian mount, hay các tính năng "nice to have" khác cho đến khi workflow cốt lõi đã ổn định

---

## Quy tắc làm việc anh vừa bổ sung
- Khi anh đưa ra 1 yêu cầu:
  - nếu yêu cầu chỉ có 1-2 nội dung chính thì trả lời trực tiếp
  - nếu yêu cầu có từ 3 nội dung chính trở lên thì phải liệt kê các phần nội dung trước, rồi hỏi anh muốn bắt đầu từ phần nào / có đồng ý bắt đầu từ phần 1 không
- Mục đích là tránh trả lời quá dài gây lỗi truncated.
- Không được nghĩ mình thông minh nên đưa ra thông tin gì cũng đúng.
- Thông tin đưa ra phải giải quyết đúng vấn đề anh đang hỏi, tránh sai lệch làm mất năng suất công việc.
- Ưu tiên chậm mà đúng, sát yêu cầu hơn là trả lời nhanh nhưng sai.
