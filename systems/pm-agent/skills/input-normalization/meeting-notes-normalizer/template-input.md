# Mẫu đầu vào cho Meeting Notes Normalizer

Đây là các dạng đầu vào thường gặp mà skill này xử lý.

## Dạng 1: Bullet notes thô

```
Họp kickoff dự án web bán hàng
- Khách hàng muốn có giỏ hàng
- Thanh toán online
- Quản lý sản phẩm
- Báo cáo doanh thu
- Anh Minh hỏi về tích hợp kho
- Chưa rõ API kho
- Timeline: 3 tháng
- Budget: thương lượng sau
- Họp lại tuần sau
```

## Dạng 2: Transcript chat

```
[10:05] Anh: Chúng ta cần làm rõ phạm vi dự án này
[10:06] Chị Lan: Em nghĩ nên ưu tiên mobile trước
[10:07] Anh Minh: Nhưng web cũng quan trọng
[10:08] Anh: Vậy làm cả hai nhưng mobile MVP trước
[10:10] Chị Lan: Được, vậy web làm sau 1 tháng
[10:12] Anh Minh: Còn vấn đề API backend thì sao?
[10:13] Anh: Dùng Node.js + MongoDB
[10:15] Chị Lan: Em lo phần frontend
[10:16] Anh Minh: Anh lo backend
[10:18] Anh: Họp lại thứ 5 tuần sau
```

## Dạng 3: Ghi chú lộn xộn nhiều chủ đề

```
Họp ngày 2026-05-10

Nói về dự án PM Agent
- Cần skill tạo tài liệu
- Tích hợp Telegram
- Voice to text
- Lưu vào Obsidian
- Anh nói cần làm requirement clarifier trước
- Sau đó mới làm charter generator
- Chưa rõ có cần PDF không
- Có thể dùng markdown-to-pdf
- Anh Doanh muốn test với dự án thật
- Deadline chưa chốt
- Cần rà lại systems/pm-agent trước
- Skill nào làm trước?
- Có nên làm demo không?
```

## Dạng 4: Transcript voice (đã chuyển text)

```
Ừ thì hôm nay chúng ta họp về dự án này nhé. 
À mà trước tiên là phải làm rõ yêu cầu đã. 
Khách hàng họ muốn cái gì? 
Ừ thì họ nói là cần một cái app bán hàng. 
Nhưng mà chi tiết thế nào thì chưa rõ lắm. 
À còn về timeline thì họ muốn càng sớm càng tốt. 
Budget thì... ừ thì cũng chưa nói rõ. 
Vậy là tuần sau mình phải gặp lại họ để hỏi thêm.
Còn về team thì hiện tại có 3 người. 
Có thể cần thêm 1 người nữa.
```

## Dạng 5: Biên bản sơ sài

```
Biên bản họp dự án ABC
Thời gian: 2026-05-10 10:00
Thành phần: Anh, Chị Lan, Anh Minh

Nội dung:
- Bàn về phạm vi dự án
- Quyết định làm mobile trước
- Phân công: Lan - frontend, Minh - backend
- Họp lại tuần sau
```

---

**Lưu ý:** Đầu vào thật thường:
- thiếu cấu trúc
- lẫn nhiều chủ đề
- có phần không rõ ràng
- có thể là transcript voice với nhiều từ thừa
- có thể là bullet ngắn gọn quá mức

Skill phải xử lý được mọi dạng trên và chuẩn hóa thành output có cấu trúc rõ ràng.
