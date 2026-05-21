# Thiết kế Voice Workflow thật cho Telegram / OpenClaw / PM Agent

## Mục tiêu
Biến voice thành một phần tự nhiên của trải nghiệm chat với Lệ trên Telegram, thay vì chỉ là test kỹ thuật thủ công.

Workflow này phải hỗ trợ cả 2 chiều:
- **Voice-to-Text (STT):** anh gửi voice → Lệ transcript → xử lý tiếp
- **Text-to-Voice (TTS):** Lệ tạo câu trả lời text → chuyển sang audio → gửi lại Telegram

---

## 1. Nguyên tắc thiết kế

### 1.1. Text vẫn là nguồn sự thật chính
- Transcript từ STT chỉ là đầu vào trung gian.
- Nếu audio chứa thông tin quan trọng như deadline, số liệu, tên riêng, cần đánh dấu hoặc xác nhận lại.
- Không tự động xem transcript là đúng tuyệt đối.

### 1.2. Voice là lớp giao diện, không thay PM workflow lõi
- PM workflow vẫn xoay quanh text/Markdown/documents.
- Voice chỉ là cách đưa input vào hoặc đưa output ra.

### 1.3. Ưu tiên fallback an toàn
- TTS lỗi → gửi text thường
- STT lỗi → báo anh gửi lại audio rõ hơn hoặc transcript thủ công
- STT confidence thấp → trả transcript + gắn cờ cần xác nhận

### 1.4. File runtime là tạm thời
- Audio vào/ra, transcript tạm, runner tạm chỉ sống trong `tmp/voice/`
- Chỉ các transcript hoặc note thực sự quan trọng mới đẩy sang `projects/...` hoặc memory phù hợp

---

## 2. Cấu trúc thư mục runtime

```text
/root/.openclaw/workspace/ops/tmp/voice/
├── incoming/      # audio anh gửi vào
├── generated/     # audio em tạo ra để gửi lại
└── transcripts/   # transcript STT và file trung gian liên quan
```

### Quy ước đặt tên file
Dùng format:
- `<timestamp>-<message-id>-incoming.ogg`
- `<timestamp>-<message-id>-reply.ogg`
- `<timestamp>-<message-id>-transcript.md`

Ví dụ:
- `20260514-154500-1181-incoming.ogg`
- `20260514-154503-1181-transcript.md`
- `20260514-154510-1181-reply.ogg`

---

## 3. Workflow Voice-to-Text (Telegram -> PM Agent)

## 3.1. Luồng chuẩn
1. Anh gửi voice note trên Telegram
2. OpenClaw tải attachment audio về
3. Audio lưu tạm vào `tmp/voice/incoming/`
4. Gọi `scripts/voice/voice_to_text.py`
5. Sinh transcript vào `tmp/voice/transcripts/`
6. Lệ đọc transcript và phân loại ý định
7. Tùy intent, transcript đi tiếp vào skill phù hợp
8. Lệ trả lại kết quả cho anh bằng text hoặc voice

## 3.2. Routing sau transcript

### Trường hợp A - Voice note là yêu cầu dự án / brief
→ đưa vào:
- `requirement-clarifier`

### Trường hợp B - Voice note là ghi chú họp
→ đưa vào:
- `meeting-notes-normalizer`
- sau đó có thể sang `action-items-extractor`

### Trường hợp C - Voice note là cập nhật tình trạng / task / blocker
→ đưa vào:
- `task-board-builder`
- `issue-log-updater`
- `status-dashboard-updater`

### Trường hợp D - Voice note chỉ là hỏi nhanh / chat thường
→ trả lời trực tiếp, không cần đẩy vào PM workflow

## 3.3. Rule confidence cho STT

### High confidence
- Transcript rõ, ít lỗi
- Có thể đi tiếp vào skill PM ngay

### Medium confidence
- Ý chính ổn nhưng có vài đoạn chưa chắc
- Trả transcript + đánh dấu phần cần xác nhận
- Chỉ đi tiếp nếu phần quan trọng không mơ hồ

### Low confidence
- Audio nhiễu / transcript lỗi nhiều
- Không tự động đi tiếp PM workflow
- Báo anh gửi lại audio rõ hơn hoặc xác nhận lại transcript

## 3.4. Rule xác nhận bắt buộc
Nếu transcript chứa một trong các loại thông tin sau mà không chắc chắn thì phải hỏi lại:
- deadline / ngày tháng
- estimate / số tiền / số lượng
- tên người / tên dự án / tên task
- quyết định yes/no quan trọng

---

## 4. Workflow Text-to-Voice (PM Agent -> Telegram)

## 4.1. Luồng chuẩn
1. Lệ tạo câu trả lời text
2. Đánh giá xem có nên voice không
3. Nếu nên voice, rút gọn thành voice script nếu cần
4. Gọi `scripts/voice/text_to_voice.py`
5. Sinh audio vào `tmp/voice/generated/`
6. Gửi file `.ogg` lại Telegram
7. Nếu lỗi, fallback sang text

## 4.2. Khi nào nên trả lời bằng voice

### Nên dùng voice
- Tóm tắt ngắn
- Nhắc việc
- Giải thích ngắn gọn
- Phản hồi theo yêu cầu rõ của anh
- Khi anh nói rõ: “trả lời bằng voice”

### Không nên dùng voice
- Nội dung có bảng biểu dài
- API spec, code, config
- Nhiều bullet kỹ thuật phức tạp
- Nội dung cần copy/paste chính xác

## 4.3. Rule độ dài audio

### Ngắn (ưu tiên)
- dưới ~45 giây
- phù hợp với Telegram voice note tự nhiên

### Trung bình
- 45–90 giây
- chỉ dùng nếu nội dung thật sự đáng nghe

### Dài
- >90 giây
- nên hỏi lại hoặc chuyển về text + voice summary

## 4.4. Rule tạo voice script
- Không bê nguyên text dài dòng sang audio
- Ưu tiên takeaway trước
- Giữ nguyên deadline, action items, cảnh báo quan trọng
- Nếu text quá dài, tạo:
  - text đầy đủ
  - voice summary ngắn

---

## 5. Trigger rules trong chat Telegram

## 5.1. Trigger cho STT
Tự chạy STT khi:
- message là voice/audio attachment từ anh

## 5.2. Trigger cho TTS
Tự chạy TTS khi:
- anh yêu cầu rõ “trả lời bằng voice”
- hoặc câu trả lời thuộc nhóm summary/reminder ngắn và anh đã bật chế độ voice ưu tiên (nếu sau này có setting)

## 5.3. Trigger không nên tự động
Không nên tự trả voice mặc định cho mọi câu trả lời vì:
- dễ làm chat bị nặng
- không phải nội dung nào cũng hợp để nghe
- gây lãng phí thời gian và quota

---

## 6. Chính sách lưu trữ và dọn file

## 6.1. File tạm
- audio incoming/generated/transcript test giữ trong `tmp/voice/`
- không commit Git

## 6.2. Khi nào giữ lại lâu hơn
Chỉ giữ lâu hơn nếu audio/transcript gắn với:
- ghi chú họp quan trọng
- brief dự án thật
- quyết định PM cần audit lại

Khi đó nên chuyển phần nội dung hữu ích sang:
- `projects/[project]/...`
- hoặc memory / note phù hợp

## 6.3. Dọn rác
Sau này nên có script cleanup:
- xóa file tạm cũ hơn X ngày
- giữ lại file mới nhất nếu đang cần debug

---

## 7. Fallback / Error handling

## 7.1. STT fail
- Báo: không transcript được audio
- Gợi ý gửi lại audio rõ hơn
- Hoặc nhờ anh xác nhận transcript ngắn nếu có phần nghe được

## 7.2. TTS fail
- fallback sang text ngay
- log lỗi vào metadata trong `generated/`
- nếu cần thì retry + fallback voice khác

## 7.3. Network/provider issue
- retry hữu hạn
- không treo vô hạn
- trả kết quả text thay vì chờ quá lâu

---

## 8. Tích hợp với PM Agent skills

## 8.1. STT -> Requirement flow
Voice brief -> transcript -> `requirement-clarifier` -> charter/requirements/spec

## 8.2. STT -> Meeting flow
Voice meeting note -> transcript -> `meeting-notes-normalizer` -> `action-items-extractor`

## 8.3. STT -> Execution update flow
Voice update -> transcript -> task/issue/dashboard updates

## 8.4. PM output -> TTS
Status summary / reminder / quick explanation -> voice script -> TTS -> Telegram voice note

---

## 9. Mức triển khai đề xuất

## Giai đoạn 1 - Manual-assisted
- Đã đạt gần xong
- Có script TTS/STT riêng
- Em gọi script thủ công khi cần

## Giai đoạn 2 - Semi-automatic
- Khi nhận voice Telegram, em tự gọi STT
- Khi anh yêu cầu voice, em tự gọi TTS
- Chưa cần setting phức tạp

## Giai đoạn 3 - Workflow-aware
- Tự route transcript sang đúng skill PM
- Có confidence rules + confirm rules
- Có cleanup policy
- Có voice summary strategy

---

## 10. Quyết định đề xuất hiện tại

### Nên làm ngay
1. Giữ script hiện tại làm nền
2. Dùng semi-automatic rules:
   - audio vào -> STT
   - yêu cầu voice rõ ràng -> TTS
3. Chưa bật auto-voice mặc định cho mọi reply
4. Transcript PM quan trọng phải qua bước xác nhận nếu confidence không cao

### Chưa cần làm ngay
- auto voice cho toàn bộ reply
- lưu mọi transcript vào project docs
- multi-speaker diarization
- voice preference system phức tạp

---

## 11. Kết luận
Thiết kế bước 3 không phải để “thêm khả năng kỹ thuật mới”, mà để chốt:
- **khi nào** dùng voice
- **đi đâu** sau transcript
- **fallback thế nào** nếu lỗi
- **lưu file ở đâu**
- **cái gì được xem là đủ an toàn để đi tiếp vào PM workflow**

Mục tiêu cuối cùng là: voice trở thành một phần tự nhiên của Telegram workflow với Lệ, chứ không chỉ là demo kỹ thuật rời rạc.
