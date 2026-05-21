---
name: change-log-updater
description: Tạo hoặc cập nhật file `03-execution/change-log.md` từ change requests, quyết định thay đổi scope/timeline/budget hoặc điều chỉnh implementation; dùng khi cần ghi nhận chính thức các thay đổi đã đề xuất, được phê duyệt hoặc bị từ chối trong quá trình dự án.
---

# Change Log Updater

## Mục tiêu

Tạo và duy trì tài liệu Change Log để theo dõi mọi thay đổi quan trọng trong dự án, đặc biệt là thay đổi về scope, timeline, budget hoặc implementation direction.

Skill này giúp:
- ghi nhận change request một cách chính thức
- theo dõi trạng thái pending / approved / rejected
- làm rõ impact của thay đổi lên scope, timeline, budget
- lưu justification và approval history
- giúp tránh thay đổi ngầm không được kiểm soát

## Dùng khi nào

Dùng skill này khi:
- có yêu cầu thay đổi phạm vi dự án
- có điều chỉnh timeline hoặc budget
- có quyết định thay đổi implementation direction quan trọng
- cần lưu dấu vết phê duyệt thay đổi

## Không dùng khi nào

Không dùng skill này khi:
- thay đổi quá nhỏ, không ảnh hưởng scope/timeline/budget
- chỉ là bug fix bình thường trong execution
- chỉ là issue phát sinh (dùng `issue-log-updater`)
- chỉ là risk tương lai (dùng `risk-register-generator`)

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- change request từ owner/team
- quyết định thay đổi từ PM Agent
- note họp / chat có chốt thay đổi quan trọng

## Input tùy chọn

- requested by
- requested date
- approved by
- approved date
- implementation status
- impact estimate

## Output

Output là file `change-log.md` với 2 phần chính:

1. **Change Requests**
2. **Change Statistics**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/change-log-template.md`.

## Quy tắc xử lý

### 1. Chỉ ghi change đủ lớn để cần theo dõi chính thức
Một thay đổi nên vào change log khi nó ảnh hưởng ít nhất một trong các yếu tố:
- scope
- timeline
- budget
- implementation direction quan trọng

### 2. Mỗi change phải có ID duy nhất
Format:
- `CHG-001`
- `CHG-002`
- ...

ID phải tuần tự và không trùng lặp.

### 3. Phân loại type rõ ràng
Ví dụ:
- Scope addition
- Scope removal / reduction
- Timeline change
- Budget change
- Technical direction change

### 4. Impact phải tách rõ theo 3 chiều
Tối thiểu cần xem impact tới:
- **Scope:** phần nào thay đổi
- **Timeline:** nhanh hơn / chậm hơn / giữ nguyên
- **Budget:** tăng / giảm / không đổi / chưa rõ

### 5. Justification phải đủ thuyết phục
Mỗi change cần trả lời rõ:
- tại sao cần thay đổi?
- nếu không đổi thì rủi ro là gì?
- thay đổi này phục vụ mục tiêu gì?

### 6. Approval history phải rõ ràng
Nếu đã được chốt, phải ghi:
- approved by
- approved date
- status

Nếu chưa chốt, phải để pending rõ ràng, không được giả định là approved.

### 7. Implementation status phải phản ánh thực tế
Ví dụ:
- Pending
- In Progress
- Completed
- Not Started

Đây là trạng thái thực thi sau khi change được chấp nhận, không phải trạng thái phê duyệt.

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Đây có phải thay đổi chính thức hay chỉ là ý tưởng thảo luận?
- Thay đổi này tác động tới scope, timeline hay budget như thế nào?
- Có cần owner phê duyệt không?
- Đây là scope addition hay scope reduction?
- Change này đã được thực thi chưa?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- meeting notes / quyết định từ owner
- charter / plan / execution updates

Và hỗ trợ cho:
- `status-dashboard-updater`
- change management process
- scope control

Change log là nơi kiểm soát các thay đổi chính thức của dự án.

## Liên hệ với cấu trúc dự án

Skill này tạo hoặc cập nhật file:
```
projects/[project-name]/03-execution/change-log.md
```

File này là lịch sử thay đổi chính thức của dự án.

## Tiêu chí hoàn thành tốt

Một change log tốt khi:
- change requests rõ ràng, không mơ hồ
- status approved/pending/rejected đúng thực tế
- impact được mô tả cụ thể
- justification hợp lý
- approval history đầy đủ
- statistics chính xác

## Lỗi thường gặp cần tránh

- đưa bug fix nhỏ vào change log
- nhầm issue thành change
- ghi thay đổi chưa được phê duyệt như đã approved
- impact quá mơ hồ
- thiếu approved by / approved date
- statistics sai số lượng

## Cách dùng ngắn gọn

1. Đọc change request / quyết định thay đổi
2. Xác định có đủ lớn để vào change log không
3. Gán ID, type, status
4. Mô tả impact và justification
5. Ghi approval history và implementation status
6. Cập nhật statistics
7. Xuất/cập nhật `change-log.md`

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ change log thực tế
- Tham khảo: `systems/pm-agent/templates/change-log-template.md`
- Tham khảo: `projects/active/web-ban-hang/03-execution/change-log.md`
