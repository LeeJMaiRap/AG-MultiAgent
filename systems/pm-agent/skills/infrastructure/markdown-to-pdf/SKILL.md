---
name: markdown-to-pdf
description: Chuyển file Markdown sang PDF để phục vụ trình bày, báo cáo hoặc chia sẻ tài liệu PM; dùng khi đã có tài liệu `.md` hoàn chỉnh và cần xuất bản PDF có bố cục dễ đọc, nhất quán, có thể dùng cho charter, requirements, spec, plan, report hoặc lessons learned.
---

# Markdown to PDF

## Mục tiêu

Chuyển tài liệu Markdown thành PDF trình bày ổn định, dễ đọc và phù hợp để chia sẻ, lưu trữ hoặc demo.

Skill này giúp:
- xuất PDF từ các tài liệu PM đã hoàn chỉnh
- giữ nội dung Markdown làm nguồn gốc, PDF là đầu ra trình bày
- tạo đầu ra nhất quán cho charter, requirements, spec, plan, report, lessons learned
- giảm công chỉnh tay khi cần gửi tài liệu cho người khác

## Dùng khi nào

Dùng skill này khi:
- đã có file `.md` hoàn chỉnh
- cần file `.pdf` để chia sẻ, nộp, trình bày hoặc lưu trữ
- cần xuất tài liệu PM theo định dạng ổn định

## Không dùng khi nào

Không dùng skill này khi:
- nội dung Markdown còn đang nháp nhiều
- mục tiêu là tạo nội dung tài liệu, không phải xuất bản
- cần chỉnh lại logic tài liệu trước
- cần một format khác ngoài PDF

## Input bắt buộc

- đường dẫn file Markdown nguồn
- đường dẫn file PDF đầu ra hoặc quy ước nơi lưu đầu ra

## Input tùy chọn

- title hiển thị
- paper size (A4, Letter)
- margin
- font size
- có/không có timestamp
- style mode nếu script hỗ trợ sau này

## Output

- một file `.pdf` được xuất từ nội dung Markdown nguồn
- file PDF phải đọc được, bố cục rõ, không lỗi encoding cơ bản

## Quy tắc xử lý

### 1. Markdown là nguồn gốc, PDF là đầu ra
Không chỉnh PDF thủ công như nguồn dữ liệu chính. Nếu cần sửa nội dung, phải sửa ở file Markdown rồi xuất lại.

### 2. Chỉ xuất khi nội dung đã đủ ổn định
Nếu tài liệu còn đang đổi lớn, ưu tiên tiếp tục làm việc ở `.md` trước khi xuất PDF.

### 3. Tên file đầu ra phải rõ ràng
Ví dụ:
- `charter.pdf`
- `requirements.pdf`
- `project-plan.pdf`
- `status-report-2026-05-11.pdf`

### 4. Bố cục ưu tiên tính dễ đọc
PDF nên:
- giữ heading rõ ràng
- có khoảng cách hợp lý
- không cắt nội dung vô lý
- hỗ trợ tiếng Việt nếu môi trường/rendering cho phép

### 5. Nếu xuất lỗi, phải báo nguyên nhân có thể kiểm tra
Ví dụ:
- file nguồn không tồn tại
- lỗi quyền ghi file đầu ra
- lỗi công cụ render
- lỗi font / encoding

### 6. Không thay đổi nội dung gốc ngoài ý muốn
Script chuyển đổi không được âm thầm chỉnh nội dung logic của Markdown.

### 7. Ưu tiên quy trình đơn giản, ít phụ thuộc
Nếu có thể, dùng script ổn định trong repo thay vì quy trình thủ công dài dòng.

## Heuristic gợi ý khi dùng

Trước khi xuất PDF, kiểm tra nhanh:
- file Markdown đã hoàn chỉnh chưa?
- heading có hợp lý không?
- có bảng hoặc danh sách nào dễ vỡ layout không?
- có cần timestamp hoặc version trong tên file không?
- PDF này dùng để demo, lưu trữ hay gửi người khác?

## Liên hệ với workflow PM

Skill này thường chạy sau khi đã hoàn tất một trong các tài liệu:
- `project-charter-generator`
- `requirements-document-generator`
- `project-spec-generator`
- `project-plan-generator`
- `status-dashboard-updater`
- `lessons-learned-writer`

Đây là skill xuất bản/hạ tầng, không phải skill tạo nội dung.

## Liên hệ với cấu trúc dự án

Skill này không bắt buộc tạo file trong một thư mục cố định, nhưng thường được dùng để xuất PDF từ:
- `projects/[project-name]/.../*.md`
- `docs/.../*.md`

Ví dụ đầu ra:
- `projects/[project-name]/01-initiation/charter.pdf`
- `projects/[project-name]/02-planning/spec.pdf`

## Cách dùng ngắn gọn

1. Xác định file Markdown nguồn
2. Chọn tên/đường dẫn PDF đầu ra
3. Chạy script chuyển đổi
4. Kiểm tra file PDF đã tạo
5. Nếu lỗi, sửa nguồn hoặc cấu hình rồi xuất lại

## Script đi kèm

- `scripts/md_to_pdf.py`

### Ví dụ chạy script

```bash
python3 scripts/md_to_pdf.py input.md output.pdf
```

## Tài nguyên đi kèm

- `template-output.md` - mô tả đầu ra mong muốn
- `scripts/md_to_pdf.py` - script chuyển đổi cơ bản
