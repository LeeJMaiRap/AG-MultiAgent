# Cấu trúc Obsidian đề xuất cho PM Agent

## Mục tiêu
Thiết kế cấu trúc note/project trong Obsidian để PM Agent có nơi lưu tri thức, tài liệu, decision log và project artifacts một cách rõ ràng, tránh trùng lặp với memory.

## Nguyên tắc thiết kế
- Obsidian là knowledge base và document system, không phải chat log.
- Mỗi project có một thư mục riêng.
- Mỗi loại artifact PM có chỗ cố định.
- Decision, action item, meeting note phải dễ truy hồi.
- Markdown là định dạng chính; PDF chỉ là output xuất ra khi cần.

## Cấu trúc vault tổng thể
```text
ObsidianVault/
├── 00-Inbox/
├── 01-Projects/
├── 02-Areas/
├── 03-Resources/
├── 04-Templates/
├── 05-Archive/
└── 99-System/
```

## 00-Inbox
Nơi chứa thông tin thô/chưa phân loại.

Dùng cho:
- ghi chú họp thô
- transcript voice chưa xử lý
- nội dung anh gửi cần phân loại sau
- ý tưởng chưa chốt

Quy tắc:
- Không để lâu trong Inbox.
- Khi đã xử lý xong phải chuyển vào project/resource phù hợp hoặc archive.

## 01-Projects
Nơi lưu toàn bộ project đang làm.

Cấu trúc mỗi project:
```text
01-Projects/
└── [Project-Name]/
    ├── 00-Project-Overview.md
    ├── 01-Charter.md
    ├── 02-Requirements.md
    ├── 03-Planning/
    │   ├── WBS.md
    │   ├── Schedule.md
    │   ├── Risk-Register.md
    │   └── Communication-Plan.md
    ├── 04-Meetings/
    ├── 05-Decisions/
    │   └── Decision-Log.md
    ├── 06-Action-Items/
    │   └── Action-Items.md
    ├── 07-Status-Reports/
    ├── 08-Issues-And-Changes/
    │   ├── Issue-Log.md
    │   └── Change-Log.md
    ├── 09-Deliverables/
    └── 99-Archive/
```

## 02-Areas
Nơi lưu các lĩnh vực dài hạn không thuộc một project cụ thể.

Ví dụ:
- PM Agent Development
- Internship / HUECIT
- Learning Software Engineering
- Personal Productivity

## 03-Resources
Nơi lưu tài liệu tham khảo dùng lại nhiều lần.

Ví dụ:
- PM frameworks
- Agile/Scrum notes
- BRD/PRD references
- prompt patterns
- checklist mẫu

## 04-Templates
Nơi lưu template Obsidian.

Template nên có:
- Meeting Minutes template
- Action Items template
- Decision Log entry template
- Project Charter template
- PRD template
- BRD template
- Weekly Status Report template
- Risk Register template

## 05-Archive
Nơi lưu project/note đã kết thúc hoặc không còn active.

Quy tắc:
- Không xóa tri thức quan trọng.
- Project đã đóng thì chuyển từ `01-Projects` sang `05-Archive`.

## 99-System
Nơi lưu quy tắc vận hành của knowledge base.

Ví dụ:
- Obsidian storage rules
- naming convention
- tagging convention
- PM Agent knowledge flow

## Quy tắc đặt tên file
Dùng tên rõ nghĩa, ưu tiên tiếng Anh cho artifact chuẩn PM nếu cần đồng bộ tài liệu:
- `Meeting-2026-05-06-[Topic].md`
- `Decision-2026-05-06-[Short-Title].md`
- `Weekly-Status-2026-W19.md`
- `Action-Items.md`
- `Risk-Register.md`

## Tag đề xuất
- `#project`
- `#meeting`
- `#decision`
- `#action-item`
- `#risk`
- `#issue`
- `#requirement`
- `#pm-agent`
- `#draft`
- `#final`

## Luồng từ Telegram/chat sang Obsidian
1. Nhận nội dung từ Telegram/chat.
2. Phân loại: tạm thời, memory, Obsidian, hoặc cả hai.
3. Nếu là note/tài liệu dự án, tạo hoặc cập nhật file trong project tương ứng.
4. Nếu là decision lớn, cập nhật `Decision-Log.md`.
5. Nếu có action item, cập nhật `Action-Items.md`.
6. Nếu cần nhớ để vận hành, ghi tóm tắt vào memory.
7. Báo lại cho anh đã lưu ở đâu.

## Quy tắc human-in-the-loop
Phải hỏi anh trước khi:
- tạo project folder mới trong Obsidian
- đổi cấu trúc vault
- di chuyển/xóa nhiều note
- lưu thông tin nhạy cảm
- đánh dấu decision là final khi anh chưa chốt

Có thể tự làm khi:
- tạo draft note theo yêu cầu rõ ràng
- cập nhật action items từ meeting đã xử lý
- thêm decision đã được anh xác nhận
- tạo status report nháp

## Kết luận
Obsidian là source of truth cho tài liệu và tri thức dự án. Memory chỉ giữ ngữ cảnh và tóm tắt cần truy hồi nhanh. PM Agent phải luôn phân biệt rõ hai vai trò này khi lưu thông tin.
