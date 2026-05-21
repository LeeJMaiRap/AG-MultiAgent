---
name: project-plan-generator
description: Tạo file `02-planning/plan.md` - kế hoạch triển khai dự án từ charter, requirements hoặc spec; dùng khi cần chia dự án thành phases, WBS, dependencies, resource allocation, communication plan, risk mitigation và success criteria để chuẩn bị execution.
---

# Project Plan Generator

## Mục tiêu

Tạo tài liệu Project Plan để biến yêu cầu và đặc tả thành kế hoạch triển khai cụ thể, có thể theo dõi và dùng để điều phối thực thi.

Skill này giúp:
- chia dự án thành các phase có logic triển khai rõ ràng
- tạo WBS ở mức đủ dùng cho việc lập task và điều phối
- xác định dependencies giữa các phần việc
- phân bổ nguồn lực và effort ước lượng
- xác định communication plan, risk mitigation và success criteria

## Dùng khi nào

Dùng skill này khi:
- đã có charter và/hoặc requirements/spec tương đối rõ
- cần lập kế hoạch triển khai trước khi bắt đầu execution
- cần tổ chức thứ tự thực hiện và phân bổ nguồn lực
- cần chuyển từ “biết phải làm gì” sang “làm theo trình tự nào”

## Không dùng khi nào

Không dùng skill này khi:
- đầu vào còn quá mơ hồ, chưa chốt phạm vi
- mục tiêu là tạo đặc tả kỹ thuật chi tiết (dùng `project-spec-generator`)
- mục tiêu là tạo task-board vận hành hằng ngày (dùng `task-board-builder`)
- chỉ cần liệt kê một vài việc rời rạc, không cần plan hoàn chỉnh

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- project charter
- requirements document
- project spec

## Input tùy chọn

- timeline / deadline
- danh sách người hoặc agent tham gia
- resource constraints
- risk register sơ bộ
- priority giữa các module
- phạm vi MVP đã chốt

## Output

Output là file `plan.md` theo cấu trúc chuẩn với 7 phần:

1. **Phases**
2. **Work Breakdown Structure (WBS)**
3. **Dependencies**
4. **Resource Allocation**
5. **Communication Plan**
6. **Risk Mitigation**
7. **Success Criteria**

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám sát template trong `systems/pm-agent/templates/plan-template.md`, và có thể bổ sung phần `Risk Mitigation` / `Success Criteria` khi đầu vào đủ dữ liệu.

## Quy tắc xử lý

### 1. Phase phải phản ánh logic triển khai thực tế
Phase không được chia ngẫu nhiên. Thứ tự phase phải hợp lý theo bản chất công việc, ví dụ:
- setup / foundation
- core features
- support features
- testing / data / QA
- deployment / finalization

### 2. WBS phải đủ chi tiết để chuyển sang task sau này
WBS không nên quá thô như chỉ có 2-3 dòng, nhưng cũng không nên chi tiết tới mức thành task board hoàn chỉnh.

Mức phù hợp là:
- phase / module
- sub-task chính
- đủ để nhìn ra phạm vi công việc

### 3. Dependencies phải thể hiện thứ tự phụ thuộc thật
Dependencies phải chỉ ra:
- việc nào phải làm trước
- việc nào phụ thuộc đầu ra của việc khác
- điểm nghẽn nào có thể làm chậm dự án

Không được chỉ liệt kê cho có.

### 4. Resource allocation phải bám thực tế nguồn lực
Nếu có thông tin về người/agent/team thì phải gán hợp lý.
Nếu chưa rõ, có thể ghi:
- Chưa xác định
- Worker Agent
- Team nội bộ

Không được bịa năng lực hoặc số lượng resource không có căn cứ.

### 5. Ước lượng effort phải tương đối hợp lý
Estimated hours không cần chính xác tuyệt đối, nhưng phải hợp lý theo phạm vi.
Không được để effort phi thực tế so với scope.

### 6. Communication plan phải phục vụ điều phối
Communication plan nên nêu rõ:
- check-in khi nào
- cập nhật trạng thái khi nào
- review ở mốc nào
- ai cần được thông báo

### 7. Risk mitigation phải gắn với plan
Nếu có rủi ro rõ ràng, phải có cách giảm thiểu cụ thể, không chỉ nêu rủi ro mà không có hướng xử lý.

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Dự án nên chia thành bao nhiêu giai đoạn hợp lý?
- Module nào phải hoàn thành trước để module khác chạy theo?
- Có hạng mục nào là critical path?
- Nguồn lực hiện có là gì và nên phân vào đâu?
- Có phase nào nên giới hạn để giữ đúng MVP?
- Điểm rủi ro lớn nhất trong execution là gì?
- Thành công của plan được đánh giá bằng các mốc nào?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `project-charter-generator`
- `requirements-document-generator`
- `project-spec-generator`

Và là đầu vào cho:
- `wbs-generator`
- `schedule-generator`
- `task-board-builder`

Đây là tài liệu nối giữa planning ở mức chiến lược và execution ở mức task.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/02-planning/plan.md
```

File này là kế hoạch triển khai trung tâm của giai đoạn planning.

## Tiêu chí hoàn thành tốt

Một project plan tốt khi:
- phase rõ ràng, theo đúng logic triển khai
- WBS đủ chi tiết để chuyển sang task-level planning
- dependencies thể hiện được critical path
- resource allocation hợp lý với bối cảnh
- communication plan dùng được thật
- risk mitigation gắn với các rủi ro thực tế
- success criteria phản ánh đúng mục tiêu delivery

## Lỗi thường gặp cần tránh

- phase chia quá cảm tính
- WBS quá sơ sài hoặc quá chi tiết
- dependencies không có giá trị thực tế
- effort estimation phi thực tế
- resource allocation không bám nguồn lực thật
- communication plan chỉ viết cho có
- plan trùng lặp với spec hoặc task-board

## Cách dùng ngắn gọn

1. Đọc charter / requirements / spec
2. Chia dự án thành các phase hợp lý
3. Lập WBS ở mức planning
4. Xác định dependencies chính
5. Gán resource và effort tương đối
6. Viết communication plan và risk mitigation
7. Chốt success criteria
8. Xuất file `plan.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ project plan thực tế
- Tham khảo: `systems/pm-agent/templates/plan-template.md`
- Tham khảo: `projects/active/web-ban-hang/02-planning/plan.md`
