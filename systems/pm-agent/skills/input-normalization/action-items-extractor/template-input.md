# Mẫu đầu vào cho Action Items Extractor

Đây là các dạng đầu vào thường gặp mà skill này xử lý.

## Dạng 1: Meeting notes đã chuẩn hóa

```
# Meeting Notes - Kickoff dự án web bán hàng

## Quyết định đã chốt
- Dự án sẽ dùng React + Node.js
- Lan phụ trách frontend, Minh phụ trách backend
- Timeline: 3 tháng

## Điểm chưa chốt
- Chưa rõ API kho
- Chưa chốt budget
- Chưa rõ phạm vi MVP chi tiết

## Đề xuất bước tiếp theo
- Cần làm rõ yêu cầu chi tiết
- Cần làm rõ API kho
- Họp lại tuần sau
```

## Dạng 2: Ghi chú họp thô có việc cần làm

```
Họp ngày 2026-05-10

- Anh Minh sẽ kiểm tra API kho trước thứ 5
- Chị Lan chuẩn bị mockup UI cho buổi họp sau
- Anh sẽ viết charter.md trong tuần này
- Cần hỏi khách hàng về budget
- Phải chốt phạm vi MVP trước khi bắt đầu code
- Họp lại thứ 5 tuần sau lúc 10h
```

## Dạng 3: Transcript chat chốt việc

```
[10:15] Anh: Vậy ai sẽ làm phần backend?
[10:16] Minh: Anh làm được
[10:17] Anh: Ok, anh Minh lo backend. Deadline tuần sau nhé
[10:18] Lan: Em lo frontend
[10:19] Anh: Lan làm UI trước, deadline cũng tuần sau
[10:20] Anh: Còn anh sẽ viết tài liệu requirements
[10:21] Minh: Vậy anh viết xong khi nào?
[10:22] Anh: Thứ 3 tuần này
```

## Dạng 4: Requirement clarification có next steps

```
# Requirement Clarification

## Câu hỏi cần xác nhận
1. API kho có sẵn chưa?
2. Budget là bao nhiêu?
3. Phạm vi MVP bao gồm những gì?

## Đề xuất bước tiếp theo
- Làm rõ API kho với team IT
- Chốt budget với khách hàng
- Tạo charter.md sau khi có đủ thông tin
- Họp lại để chốt phạm vi MVP
```

## Dạng 5: Danh sách ý lẫn lộn

```
Sau buổi họp:
- Phải viết spec
- Minh check API
- Lan làm mockup
- Hỏi khách hàng về timeline
- Chuẩn bị demo cho tuần sau
- Chưa rõ ai làm testing
- Cần setup môi trường dev
- Họp lại thứ 5
```

---

**Lưu ý:** Đầu vào thật thường:
- lẫn lộn giữa quyết định, discussion và action
- có việc được giao rõ ràng, có việc chỉ là gợi ý
- có việc có owner/deadline, có việc không có
- có thể thiếu ngữ cảnh về mức ưu tiên

Skill phải phân biệt được và tách rõ từng loại.
