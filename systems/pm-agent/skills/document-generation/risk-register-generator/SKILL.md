---
name: risk-register-generator
description: Tạo file `02-planning/risk-register.md` - đăng ký rủi ro dự án với risk matrix, risk list, mitigation plans và monitoring từ charter, plan, spec hoặc phân tích rủi ro; dùng khi cần quản lý rủi ro có cấu trúc với probability, impact, score, mitigation và owner.
---

# Risk Register Generator

## Mục tiêu

Tạo tài liệu Risk Register để nhận diện, đánh giá và quản lý rủi ro dự án một cách có hệ thống, giúp giảm thiểu tác động tiêu cực và tăng khả năng thành công.

Skill này giúp:
- tạo risk matrix trực quan
- liệt kê rủi ro với probability, impact và score
- xây dựng mitigation plans cụ thể
- gán owner cho từng rủi ro
- thiết lập risk monitoring process

## Dùng khi nào

Dùng skill này khi:
- đã có charter, plan hoặc spec
- cần quản lý rủi ro có cấu trúc
- cần mitigation plans cụ thể
- cần theo dõi rủi ro trong execution

## Không dùng khi nào

Không dùng skill này khi:
- dự án quá đơn giản, không có rủi ro đáng kể
- chỉ cần ghi chú rủi ro sơ bộ trong charter
- mục tiêu là tạo issue log (dùng `issue-log-updater`)

## Input bắt buộc

Ít nhất phải có một trong các nguồn sau:
- project charter với rủi ro sơ bộ
- project plan với risk mitigation
- phân tích rủi ro từ team

## Input tùy chọn

- risk assessment đã có
- historical data từ dự án tương tự
- constraints và assumptions
- stakeholder concerns

## Output

Output là file `risk-register.md` với 4 phần chính:

1. **Risk Matrix** - ma trận rủi ro trực quan
2. **Risk List** - danh sách rủi ro chi tiết
3. **Mitigation Plans** - kế hoạch giảm thiểu
4. **Risk Monitoring** - quy trình theo dõi

## Format output chuẩn

Xem `template-output.md` để biết format đầy đủ.

Output phải bám theo `systems/pm-agent/templates/risk-register-template.md`.

## Quy tắc xử lý

### 1. Risk phải cụ thể và có thể xảy ra
Risk không phải là vấn đề đã xảy ra (đó là issue), mà là:
- điều có thể xảy ra trong tương lai
- có tác động tiêu cực nếu xảy ra
- có thể giảm thiểu được

### 2. Probability và Impact phải có căn cứ
- **Probability:** High/Medium/Low dựa trên likelihood thực tế
- **Impact:** High/Medium/Low dựa trên mức độ ảnh hưởng tới scope/time/cost/quality

### 3. Risk Score phải tính đúng
Score = Probability × Impact (theo thang điểm)
- High/High = 9
- High/Medium = 6
- Medium/Medium = 4
- Low/High = 3
- Low/Low = 1

### 4. Mitigation plan phải actionable và có contingency
Mỗi mitigation plan phải có:
- **Plan:** chiến lược giảm thiểu
- **Trigger:** khi nào kích hoạt
- **Action:** hành động cụ thể
- **Owner:** người chịu trách nhiệm
- **Contingency plan:** nếu mitigation fail thì làm gì
- **Cost estimate:** nếu risk xảy ra thì mất bao nhiêu effort/time

### 5. Risk matrix phải trực quan
Risk matrix dạng ASCII art phải:
- dễ nhìn
- phản ánh đúng vị trí risk theo probability/impact
- giúp ưu tiên risk nhanh

### 6. Phải có risk monitoring process
Risk register không phải tài liệu tĩnh, phải có:
- review frequency
- escalation criteria
- owner chịu trách nhiệm theo dõi

### 7. Phải có summary và recommended actions
Summary cần:
- total risks
- phân loại theo priority
- số lượng open/mitigated/closed
- recommended actions ngắn gọn

## Heuristic gợi ý khi phân tích

Khi đọc đầu vào, rà theo các câu hỏi ngầm sau:
- Rủi ro nào có thể làm dự án thất bại?
- Rủi ro nào về timeline, scope, quality, cost?
- Rủi ro nào về technical, resource, external factors?
- Probability và impact của từng rủi ro là gì?
- Làm sao giảm thiểu từng rủi ro?
- Ai chịu trách nhiệm theo dõi từng rủi ro?

## Liên hệ với workflow PM

Skill này thường chạy sau:
- `project-charter-generator`
- `project-plan-generator`
- `project-spec-generator`

Và hỗ trợ cho:
- execution monitoring
- issue management
- change management

Risk register là công cụ quản lý rủi ro chính trong suốt dự án.

## Liên hệ với cấu trúc dự án

Skill này tạo file:
```
projects/[project-name]/02-planning/risk-register.md
```

File này là tài liệu quản lý rủi ro chính thức.

## Tiêu chí hoàn thành tốt

Một risk register tốt khi:
- risk matrix trực quan, dễ đọc
- risk list đầy đủ với probability/impact/score
- mitigation plans cụ thể, actionable
- có owner cho từng rủi ro
- có risk monitoring process
- có summary và recommended actions
- realistic và hữu ích

## Lỗi thường gặp cần tránh

- risk quá chung chung hoặc không realistic
- probability/impact không có căn cứ
- risk score tính sai
- mitigation plans mơ hồ
- không có owner
- không có monitoring process
- risk register chỉ là hình thức

## Cách dùng ngắn gọn

1. Đọc charter / plan / spec
2. Nhận diện rủi ro chính
3. Đánh giá probability và impact
4. Tính risk score
5. Tạo risk matrix
6. Viết mitigation plans
7. Gán owner và thiết lập monitoring
8. Xuất file `risk-register.md` vào đúng thư mục dự án

## Tài nguyên đi kèm

- `template-output.md` - mẫu đầu ra chuẩn
- `examples/` - ví dụ risk register thực tế
- Tham khảo: `systems/pm-agent/templates/risk-register-template.md`
- Tham khảo: `projects/active/web-ban-hang/02-planning/risk-register.md`
