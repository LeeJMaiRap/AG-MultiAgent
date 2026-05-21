---
name: text-to-voice
description: Chuyển phản hồi text thành audio/voice để gửi lại qua Telegram hoặc kênh chat khác; dùng khi cần trả lời bằng giọng nói, tóm tắt ngắn gọn bằng audio, đọc lại nội dung quan trọng, hoặc hỗ trợ workflow PM khi anh muốn nghe thay vì đọc.
---

# Text to Voice

## Mục tiêu

Chuyển nội dung text thành audio đủ rõ, dễ nghe để gửi lại cho anh hoặc dùng trong các tình huống cần phản hồi bằng giọng nói.

Skill này giúp:
- chuyển câu trả lời text thành audio
- tạo voice response ngắn gọn, dễ nghe
- ưu tiên những nội dung phù hợp để nghe hơn là đọc
- hỗ trợ tóm tắt nhanh, nhắc việc hoặc giải thích ngắn bằng voice

## Dùng khi nào

Dùng skill này khi:
- anh yêu cầu trả lời bằng giọng nói
- nội dung phù hợp để nghe (tóm tắt ngắn, nhắc việc, giải thích nhanh)
- cần gửi audio qua Telegram thay vì chỉ text
- muốn tạo trải nghiệm tiện hơn khi đang bận hoặc không tiện đọc

## Không dùng khi nào

Không dùng skill này khi:
- nội dung quá dài, quá bảng biểu hoặc quá chi tiết kỹ thuật
- text còn đang nháp hoặc chưa chốt
- cần trích dẫn chính xác từng dòng/phần định dạng phức tạp
- mục tiêu là chuyển audio thành text (dùng `voice-to-text`)

## Input bắt buộc

- nội dung text đã hoàn chỉnh
- ngữ cảnh sử dụng (trả lời nhanh, tóm tắt, nhắc việc, giải thích ngắn)

## Input tùy chọn

- giọng đọc mong muốn
- ngôn ngữ
- mức độ tự nhiên / trang trọng
- có cần rút gọn trước khi đọc không
- có cần chia thành nhiều đoạn audio không

## Output

Output chuẩn là một audio file hoặc voice response, kèm metadata ngắn:

1. **Input Summary**
2. **Voice Script**
3. **Delivery Notes**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

## Quy tắc xử lý

### 1. Ưu tiên script dễ nghe, không bê nguyên text dài dòng
Nếu text gốc quá dài hoặc nhiều cấu trúc khó nghe, nên rút gọn thành voice script ngắn hơn nhưng không làm sai ý.

### 2. Phân biệt text gốc và voice script
Text gốc có thể dài hoặc formal hơn.
Voice script nên:
- tự nhiên hơn
- gãy gọn hơn
- dễ nghe hơn

### 3. Không làm mất ý quan trọng
Nếu rút gọn để đọc, không được bỏ mất:
- kết luận chính
- deadline
- action item
- cảnh báo quan trọng

### 4. Nội dung dài nên chia đoạn
Nếu nội dung dài, nên chia thành nhiều đoạn hoặc đề nghị giữ ở text thay vì cố đọc hết trong một audio dài.

### 5. Phải phù hợp với ngữ cảnh chat
Voice response trong Telegram nên:
- không quá dài dòng
- nghe tự nhiên
- ưu tiên điều người nghe cần nhớ

## Heuristic gợi ý khi phân tích

Trước khi tạo voice, rà theo các câu hỏi ngầm sau:
- Nội dung này có phù hợp để nghe không?
- Có cần rút gọn trước khi đọc không?
- Phần nào là takeaway quan trọng nhất?
- Audio nên ngắn gọn hay giải thích đầy đủ?
- Có nên giữ ở text thay vì voice nếu quá dài/technical không?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- status update
- task reminder
- summary response
- quick explanation

Đây là skill bridge từ output text sang output audio.

## Liên hệ với cấu trúc dự án

Skill này không bắt buộc tạo file trong `projects/`, nhưng có thể tạo:
- `response-audio.mp3`
- `summary-voice.ogg`
- hoặc voice attachment tạm để gửi qua chat

## Tiêu chí hoàn thành tốt

Một output tốt khi:
- script dễ nghe và tự nhiên
- không làm sai ý gốc
- giữ lại takeaway quan trọng
- độ dài phù hợp với ngữ cảnh chat
- người nghe có thể nắm ý nhanh mà không cần nhìn text đầy đủ

## Lỗi thường gặp cần tránh

- bê nguyên text dài dòng sang voice
- rút gọn quá mức làm mất ý chính
- đọc cả nội dung bảng biểu khó nghe
- dùng voice cho nội dung nên giữ ở text
- audio quá dài so với giá trị nhận được

## Cách dùng ngắn gọn

1. Nhận text đã hoàn chỉnh
2. Đánh giá nội dung có phù hợp để đọc không
3. Rút gọn thành voice script nếu cần
4. Giữ lại các ý chính / deadline / action items
5. Tạo audio output
6. Gửi audio qua kênh phù hợp

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `references/voice-script-guide.md` - hướng dẫn viết voice script dễ nghe

## Khi nào nên đọc thêm tài liệu tham chiếu

- Nếu text gốc quá dài và cần rút gọn: đọc `references/voice-script-guide.md`
- Nếu phân vân nội dung nào nên đọc thành voice: đọc `references/voice-script-guide.md`
