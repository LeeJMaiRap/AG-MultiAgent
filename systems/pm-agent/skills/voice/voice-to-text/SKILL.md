---
name: voice-to-text
description: Chuyển voice note hoặc file audio thành text để đưa vào workflow PM Agent; dùng khi đầu vào là tin nhắn thoại, ghi âm cuộc họp, voice note Telegram hoặc audio ngắn cần transcript để tiếp tục xử lý như requirement clarification, meeting notes, action items hoặc cập nhật dự án.
---

# Voice to Text

## Mục tiêu

Chuyển đầu vào dạng giọng nói thành transcript text đủ rõ để tiếp tục đi vào workflow PM Agent như một đầu vào text bình thường.

Skill này giúp:
- nhận voice note hoặc audio file
- chuyển audio thành text
- làm sạch transcript ở mức cơ bản
- đánh dấu phần nghe không chắc chắn
- đưa transcript vào các skill PM khác như `meeting-notes-normalizer`, `requirement-clarifier`, `action-items-extractor`

## Dùng khi nào

Dùng skill này khi:
- anh gửi voice note qua Telegram
- có file audio ghi chú họp hoặc nói nhanh ý tưởng dự án
- cần chuyển lời nói thành text để lưu, phân tích hoặc tạo tài liệu PM
- cần transcript sơ bộ trước khi bóc tách requirement/action items

## Không dùng khi nào

Không dùng skill này khi:
- đầu vào đã là text rõ ràng
- audio quá kém, quá nhiễu hoặc không nghe được phần lớn nội dung
- mục tiêu là tạo audio từ text (dùng `text-to-voice`)
- cần biên bản họp hoàn chỉnh ngay mà chưa có transcript thô

## Input bắt buộc

- file audio hoặc voice note
- ngữ cảnh ngắn về loại nội dung (ví dụ: voice note yêu cầu, ghi chú họp, cập nhật task)

## Input tùy chọn

- tên cuộc họp / dự án
- ngôn ngữ chính của audio
- kỳ vọng output (raw transcript hoặc transcript đã làm sạch)
- speaker hints nếu biết trước
- timestamp requirement nếu cần

## Output

Output chuẩn là transcript Markdown hoặc text có cấu trúc cơ bản gồm:

1. **Input Summary**
2. **Transcript**
3. **Unclear Segments** (nếu có)
4. **Suggested Next Step**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

## Quy tắc xử lý

### 1. Ưu tiên độ trung thực của transcript
Không được tự bịa phần nghe không rõ. Nếu không chắc, phải đánh dấu:
- `[unclear]`
- `[inaudible]`
- `[need confirmation]`

### 2. Tách transcript với suy luận
Transcript là những gì nghe được.
Nếu có suy đoán hoặc chuẩn hóa, phải để riêng, không trộn vào lời gốc.

### 3. Giữ nội dung đủ dùng cho bước sau
Không cần làm đẹp quá mức. Mục tiêu là tạo transcript usable cho các skill PM tiếp theo.

### 4. Đánh dấu đoạn cần xác nhận
Nếu có số liệu, deadline, tên riêng hoặc quyết định quan trọng nhưng nghe không chắc, phải đánh dấu để xác nhận lại.

### 5. Nếu transcript quá thô, gợi ý bước tiếp theo
Ví dụ:
- đưa sang `meeting-notes-normalizer`
- đưa sang `requirement-clarifier`
- xác nhận lại đoạn unclear trước

### 6. Không giả vờ độ chính xác tuyệt đối
Nếu audio chất lượng kém, phải nói rõ transcript chỉ là bản sơ bộ.

## Heuristic gợi ý khi phân tích

Khi xử lý audio, rà theo các câu hỏi ngầm sau:
- Đây là voice note ngắn hay ghi chú họp dài hơn?
- Audio có đủ rõ để transcript trực tiếp không?
- Có đoạn nào chứa deadline, số liệu, tên người, tên dự án cần xác nhận lại không?
- Transcript này nên đi tiếp vào skill nào trong workflow PM?
- Có cần giữ nguyên cách nói hay làm sạch câu chữ ở mức tối thiểu?

## Liên hệ với workflow PM

Skill này thường chạy trước:
- `meeting-notes-normalizer`
- `requirement-clarifier`
- `action-items-extractor`

Đây là skill bridge từ input audio sang input text.

## Liên hệ với cấu trúc dự án

Skill này không bắt buộc tạo file cố định, nhưng output có thể lưu thành:
- `raw-transcript.md`
- `meeting-transcript.md`
- hoặc dùng trực tiếp làm input cho skill kế tiếp

## Tiêu chí hoàn thành tốt

Một output tốt khi:
- transcript đủ rõ để người đọc hiểu ý chính
- đoạn unclear được đánh dấu trung thực
- không trộn transcript với suy diễn
- có gợi ý bước kế tiếp phù hợp
- dùng được ngay cho workflow PM

## Lỗi thường gặp cần tránh

- tự bịa nội dung khi nghe không rõ
- làm transcript quá sạch đến mức mất ý gốc
- không đánh dấu đoạn unclear
- trộn transcript với tóm tắt/suy luận
- không chỉ ra nên làm gì tiếp theo với transcript

## Cách dùng ngắn gọn

1. Nhận voice note / file audio
2. Chuyển audio thành transcript text
3. Đánh dấu các đoạn unclear
4. Làm sạch transcript ở mức tối thiểu
5. Gợi ý skill kế tiếp phù hợp
6. Xuất transcript

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `references/transcript-quality-guide.md` - hướng dẫn đánh giá chất lượng transcript

## Khi nào nên đọc thêm tài liệu tham chiếu

- Nếu audio có nhiều đoạn không rõ: đọc `references/transcript-quality-guide.md`
- Nếu phân vân nên đánh dấu transcript thế nào: đọc `references/transcript-quality-guide.md`
