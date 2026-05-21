---
name: action-items-extractor
description: Trích xuất action items từ ghi chú họp, transcript, chat, requirement clarification hoặc meeting notes đã chuẩn hóa; dùng khi cần chuyển nội dung thảo luận thành danh sách việc cần làm có owner, deadline, priority, status sơ bộ và điểm còn thiếu để follow-up.
---

# Action Items Extractor

## Mục tiêu

Biến nội dung thảo luận hoặc tài liệu đầu vào thành danh sách việc cần làm rõ ràng, có thể theo dõi và dùng tiếp cho task-board hoặc quản lý công việc PM.

Skill này giúp:
- phát hiện các việc cần làm được nói trực tiếp hoặc ngầm suy ra hợp lý từ kết luận cuộc họp
- tách action item ra khỏi phần thảo luận chung
- gắn owner, deadline, priority, dependency khi đầu vào có đủ dữ liệu
- chỉ ra phần còn thiếu cần xác nhận thêm
- chuẩn hóa đầu ra để dễ chuyển sang `task-board-builder`

## Dùng khi nào

Dùng skill này khi đầu vào là:
- meeting notes đã chuẩn hóa
- ghi chú họp thô
- transcript cuộc họp
- đoạn chat chốt việc
- requirement clarification có đề xuất bước tiếp theo
- danh sách ý đang cần chuyển thành đầu việc theo dõi

## Không dùng khi nào

Không dùng skill này khi:
- mục tiêu là làm rõ yêu cầu sản phẩm, không phải bóc việc
- đầu vào chưa có đủ ngữ cảnh để xác định việc cần làm
- cần tạo task-board hoàn chỉnh cho toàn dự án từ đầu
- cần theo dõi issue hoặc change request, không phải action item ngắn hạn

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- meeting notes
- transcript họp
- chat chốt việc
- notes sau họp
- requirement clarification / summary có phần next steps

## Input tùy chọn

- tên dự án
- ngày họp / ngày phát sinh action items
- danh sách người tham gia
- owner khả dĩ của từng việc
- deadline / timeline đã nhắc tới
- mức ưu tiên nếu đã được nói rõ
- quy ước trạng thái công việc của dự án

## Output

Output chuẩn là một bản Markdown có 6 phần sau:

1. **Bối cảnh trích xuất**
2. **Danh sách action items chính**
3. **Action items chưa đủ dữ liệu**
4. **Dependency / blocker / lưu ý**
5. **Câu hỏi cần xác nhận thêm**
6. **Đề xuất bước tiếp theo**

## Format output chuẩn

```md
# Action Items

## 1. Bối cảnh trích xuất
- Nguồn: ...
- Thời điểm: ...
- Phạm vi: ...

## 2. Danh sách action items chính
| ID | Việc cần làm | Owner | Deadline | Priority | Status | Ghi chú |
|----|---------------|-------|----------|----------|--------|--------|
| AI-01 | ... | ... | ... | ... | Todo | ... |

## 3. Action items chưa đủ dữ liệu
| ID | Việc cần làm | Thiếu gì | Gợi ý xử lý |
|----|---------------|----------|-------------|
| AI-U01 | ... | ... | ... |

## 4. Dependency / blocker / lưu ý
- ...

## 5. Câu hỏi cần xác nhận thêm
1. ...?
2. ...?

## 6. Đề xuất bước tiếp theo
- ...
```

## Quy tắc xử lý

### 1. Chỉ trích xuất việc có tính hành động
Action item phải là việc có thể thực hiện được, ví dụ:
- làm rõ API kho
- chuẩn bị tài liệu kickoff
- chốt phạm vi MVP
- họp lại với khách hàng

Không đưa vào action item những câu chỉ mang tính nhận xét hoặc bối cảnh.

### 2. Phân biệt rõ “quyết định” và “việc cần làm”
Ví dụ:
- “dùng React + Node.js” là quyết định / định hướng
- “chuẩn bị base project React + Node.js” mới là action item

### 3. Không được tự bịa owner hoặc deadline như fact
Nếu đầu vào không ghi rõ, phải để:
- `Chưa rõ`
- `Cần xác nhận`
- hoặc ghi vào bảng “chưa đủ dữ liệu”

### 4. Có thể suy ra action item hợp lý, nhưng phải ghi chú rõ
Nếu từ ngữ cảnh có thể suy ra một việc gần như chắc chắn cần làm, vẫn có thể đưa ra nhưng phải đánh dấu đó là:
- suy ra từ kết luận
- chưa được nêu trực tiếp
- cần xác nhận nếu ảnh hưởng lớn

### 5. Gộp các việc trùng nhau
Nếu nhiều câu trong cuộc họp nói cùng một việc, phải gộp thành một action item rõ ràng hơn, tránh lặp.

### 6. Ưu tiên output dễ chuyển sang task board
Tên action item nên:
- ngắn gọn
- bắt đầu bằng động từ
- đủ rõ để giao việc

### 7. Tách nhóm “đủ dữ liệu” và “chưa đủ dữ liệu”
Những việc thiếu owner/deadline/phạm vi vẫn có giá trị, nhưng không nên trộn chung với nhóm đã sẵn sàng theo dõi.

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Có việc nào được giao trực tiếp cho ai không?
- Có việc nào được hẹn phải làm trước cuộc họp sau không?
- Có phần nào được kết luận là “cần làm rõ”, “cần chuẩn bị”, “cần kiểm tra”, “cần chốt” không?
- Có blocker hoặc dependency nào tạo ra đầu việc follow-up không?
- Có việc nào chỉ là ý tưởng, chưa đủ để xem là action item không?
- Có việc nào nên tách thành 2 action item nhỏ hơn không?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `meeting-notes-normalizer`
- `requirement-clarifier`

Và thường là đầu vào cho:
- `task-board-builder`
- `issue-log-updater` (nếu phát hiện blocker hoặc issue)
- các buổi follow-up tiếp theo

## Liên hệ với cấu trúc dự án

Skill này không bắt buộc ghi trực tiếp vào `projects/[project-name]/`, nhưng output của nó rất phù hợp để dùng tạo hoặc cập nhật:
- `03-execution/task-board.md`
- `03-execution/issue-log.md` (khi có blocker/issue)
- note follow-up hoặc checklist làm việc

## Tiêu chí hoàn thành tốt

Một output tốt khi:
- nhìn vào là biết phải làm gì tiếp theo
- việc nào có thể giao ngay được thể hiện rõ
- việc nào còn thiếu owner/deadline được tách riêng
- không nhầm lẫn giữa discussion, decision và action
- đủ sạch để chuyển sang task board gần như trực tiếp

## Lỗi thường gặp cần tránh

- đưa quá nhiều câu mô tả chung vào danh sách việc
- tự gán owner/deadline không có trong đầu vào
- bỏ sót action item ngầm nhưng quan trọng
- trộn action items sẵn sàng với action items thiếu dữ liệu
- viết tên việc quá dài hoặc quá mơ hồ
- biến toàn bộ cuộc họp thành task list dày đặc không có ưu tiên

## Cách dùng ngắn gọn

1. Đọc đầu vào
2. Tách phần quyết định, phần discussion và phần việc cần làm
3. Gộp các action item trùng nhau
4. Gắn owner / deadline / priority nếu có dữ liệu
5. Tách nhóm việc còn thiếu dữ liệu
6. Đề xuất bước tiếp theo

## Tài nguyên đi kèm

- `template-input.md` - mẫu đầu vào tham khảo
- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ test thực tế
