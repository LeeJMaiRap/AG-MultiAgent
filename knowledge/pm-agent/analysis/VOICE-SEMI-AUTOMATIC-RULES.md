# Voice Semi-Automatic Rules

## Mục tiêu
Định nghĩa cách vận hành semi-automatic cho voice trong Telegram trước khi tích hợp auto hoàn toàn.

## Rule 1 - Audio vào thì ưu tiên STT trước
Khi anh gửi voice/audio:
1. Lưu file vào `tmp/voice/incoming/`
2. Chạy `scripts/voice/telegram_voice_ingest.py`
3. Đọc report route gợi ý
4. Chỉ auto đi tiếp nếu transcript đủ rõ và loại nội dung đủ rõ

## Rule 2 - Chỉ auto-route nhẹ, không auto-trust tuyệt đối
Cho phép auto gợi ý route sang:
- `requirement-clarifier`
- `meeting-notes-normalizer`
- `action-items-extractor`
- `issue-log-updater`
- `status-dashboard-updater`

Nhưng vẫn phải manual review nếu có:
- deadline
- số liệu
- tên riêng
- quyết định quan trọng

## Rule 3 - Chỉ trả voice khi anh yêu cầu rõ hoặc nội dung rất phù hợp
Dùng `scripts/voice/reply_as_voice.py` khi:
- anh yêu cầu voice
- hoặc câu trả lời là summary/reminder ngắn

Không auto voice cho:
- bảng biểu
- code/config
- spec dài
- nội dung cần copy/paste chính xác

## Rule 4 - Fallback luôn tồn tại
- STT lỗi -> trả text báo lỗi + đề nghị gửi lại audio rõ hơn
- TTS lỗi -> fallback sang text thường
- confidence thấp -> ưu tiên xác nhận lại

## Rule 5 - Runtime file là tạm thời
- incoming/generated/transcripts ở `tmp/voice/`
- không commit git
- transcript quan trọng thì chuyển vào project docs hoặc memory phù hợp

## Script dùng cho giai đoạn này
- `scripts/voice/voice_to_text.py`
- `scripts/voice/text_to_voice.py`
- `scripts/voice/telegram_voice_ingest.py`
- `scripts/voice/reply_as_voice.py`
