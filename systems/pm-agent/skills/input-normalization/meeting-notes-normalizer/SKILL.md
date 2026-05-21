---
name: meeting-notes-normalizer
description: Chuẩn hóa ghi chú họp thô từ chat, bullet notes, transcript hoặc biên bản chưa hoàn chỉnh thành bản meeting notes có cấu trúc rõ ràng; dùng khi đầu vào lộn xộn, thiếu phân nhóm, thiếu mốc quyết định, hoặc cần làm sạch trước khi trích action items, requirements, decision log hay tài liệu PM khác.
---

# Meeting Notes Normalizer

## Mục tiêu

Biến ghi chú họp thô thành một bản meeting notes có cấu trúc, dễ đọc, dễ kiểm tra và dễ dùng tiếp cho các skill PM khác.

Skill này giúp:
- gom ý rời rạc thành nhóm nội dung rõ ràng
- phân biệt thông tin đã nói, quyết định tạm chốt và phần còn bỏ ngỏ
- chuẩn hóa đầu ra để dùng tiếp cho action items, requirement clarification, decision log hoặc project summary
- giảm rủi ro bỏ sót thông tin quan trọng từ cuộc họp

## Dùng khi nào

Dùng skill này khi đầu vào là:
- ghi chú họp viết tay / bullet thô
- transcript chat hoặc transcript voice sau họp
- danh sách ý rời rạc không theo thứ tự
- meeting summary sơ sài cần chuẩn hóa lại
- nội dung cuộc họp có nhiều chủ đề lẫn nhau

## Không dùng khi nào

Không dùng skill này khi:
- đầu vào đã là biên bản họp hoàn chỉnh, rõ cấu trúc và đủ chi tiết
- mục tiêu chính là trích xuất action items thôi
- mục tiêu chính là làm rõ yêu cầu sản phẩm từ brief dự án
- cần tạo tài liệu PM chính thức như charter/spec trực tiếp

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- ghi chú họp thô
- transcript cuộc họp
- bullet notes sau họp
- đoạn chat tổng hợp nội dung buổi họp

## Input tùy chọn

- ngày giờ họp
- tên cuộc họp
- thành phần tham gia
- bối cảnh dự án
- tài liệu đính kèm liên quan
- agenda nếu có
- ghi chú của anh về điều gì là quan trọng nhất

## Output

Output chuẩn là một bản Markdown có 8 phần sau:

1. **Thông tin cuộc họp**
2. **Mục tiêu / bối cảnh buổi họp**
3. **Nội dung chính đã thảo luận**
4. **Quyết định / kết luận đã chốt**
5. **Điểm chưa chốt / còn bỏ ngỏ**
6. **Rủi ro / lưu ý nổi bật**
7. **Dữ liệu cần dùng tiếp cho skill khác**
8. **Đề xuất bước tiếp theo**

## Format output chuẩn

```md
# Meeting Notes

## 1. Thông tin cuộc họp
- Tên cuộc họp: ...
- Thời gian: ...
- Thành phần tham gia: ...
- Nguồn ghi chú: ...

## 2. Mục tiêu / bối cảnh buổi họp
- ...

## 3. Nội dung chính đã thảo luận
### Chủ đề 1
- ...

### Chủ đề 2
- ...

## 4. Quyết định / kết luận đã chốt
- ...

## 5. Điểm chưa chốt / còn bỏ ngỏ
- ...

## 6. Rủi ro / lưu ý nổi bật
- ...

## 7. Dữ liệu cần dùng tiếp cho skill khác
### Dùng cho requirement-clarifier
- ...

### Dùng cho action-items-extractor
- ...

### Dùng cho decision log / project summary
- ...

## 8. Đề xuất bước tiếp theo
- ...
```

## Quy tắc xử lý

### 1. Không được bịa phát biểu hoặc quyết định
Nếu ghi chú không đủ rõ để xác định một kết luận, phải ghi là:
- chưa rõ
- chưa được xác nhận
- có dấu hiệu được nhắc tới nhưng chưa thể kết luận

### 2. Tách rõ 3 loại thông tin
Mỗi ý nên được phân biệt rõ là:
- nội dung được thảo luận
- quyết định/kết luận đã chốt
- phần còn bỏ ngỏ / cần theo dõi

Không được trộn 3 loại này thành một nhóm mơ hồ.

### 3. Gom nhóm theo chủ đề, không chỉ theo thứ tự nói
Nếu cuộc họp nói lan man, skill cần chuẩn hóa lại theo từng chủ đề logic thay vì giữ nguyên chuỗi lộn xộn ban đầu.

### 4. Giữ nguyên ý nghĩa gốc
Có thể viết lại cho rõ hơn, nhưng không được làm lệch ý hoặc tăng mức chắc chắn so với nội dung thật.

### 5. Đánh dấu dữ liệu có thể tái sử dụng
Nếu một đoạn trong họp có giá trị cho skill khác, cần chỉ ra rõ phần đó dùng tiếp cho việc gì.

### 6. Không biến meeting notes thành action items hoàn chỉnh quá sớm
Nếu có việc cần làm thì chỉ ghi nhận ở mức gợi ý hoặc dữ liệu đầu vào; việc bóc task chi tiết thuộc skill khác.

### 7. Ưu tiên khả năng đọc lại sau này
Output phải giúp anh hoặc agent khác đọc lại sau vài ngày vẫn hiểu:
- buổi họp nói về gì
- đã chốt gì
- còn treo gì
- nên làm gì tiếp

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Buổi họp này nhằm giải quyết vấn đề gì?
- Có những chủ đề chính nào đã được nói tới?
- Có quyết định nào thực sự đã chốt?
- Có ý nào nghe giống quyết định nhưng thật ra chỉ là đề xuất?
- Có đầu việc hay câu hỏi nào đang treo?
- Có rủi ro hoặc phụ thuộc nào được nhắc đến?
- Nội dung nào sẽ hữu ích ngay cho các skill tiếp theo?

## Liên hệ với workflow PM

Skill này nên chạy trước các skill:
- `action-items-extractor`
- `requirement-clarifier`
- `project-charter-generator`
- `requirements-document-generator`

Đây là skill nền để làm sạch ghi chú họp trước khi dùng tiếp cho phân tích hoặc sinh tài liệu.

## Liên hệ với cấu trúc dự án

Skill này không bắt buộc tạo trực tiếp file trong `projects/[project-name]/`, nhưng output của nó có thể được dùng để tạo hoặc cập nhật:
- `01-initiation/requirements.md`
- `02-planning/spec.md`
- `03-execution/task-board.md`
- project summary / decision log trong hệ note

## Tiêu chí hoàn thành tốt

Một output tốt khi:
- đọc xong là hiểu buổi họp xoay quanh vấn đề gì
- dễ nhìn ra phần nào đã chốt, phần nào chưa chốt
- các chủ đề được nhóm hợp lý
- có thể dùng trực tiếp làm đầu vào cho skill khác
- giảm đáng kể độ lộn xộn của ghi chú thô ban đầu

## Lỗi thường gặp cần tránh

- viết lại transcript dài dòng mà không chuẩn hóa
- biến giả định thành quyết định đã chốt
- không chỉ ra phần còn bỏ ngỏ
- bỏ sót rủi ro hoặc phụ thuộc quan trọng
- gom nhóm chủ đề kém, làm mất logic buổi họp
- tự thêm action items chi tiết khi đầu vào chưa đủ căn cứ

## Cách dùng ngắn gọn

1. Đọc ghi chú họp thô
2. Nhận diện mục tiêu buổi họp và các chủ đề chính
3. Gom nội dung theo nhóm chủ đề
4. Tách rõ phần đã chốt và chưa chốt
5. Đánh dấu dữ liệu cần dùng tiếp
6. Đề xuất bước tiếp theo phù hợp

## Tài nguyên đi kèm

- `template-input.md` - mẫu đầu vào tham khảo
- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ test thực tế
