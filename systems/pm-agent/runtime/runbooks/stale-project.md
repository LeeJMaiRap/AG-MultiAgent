# Runbook: Stale Project

Áp dụng khi project/task/approval/issue có dấu hiệu bị stale.

## Bước xử lý

1. **Xác định loại stale**
   - stale task?
   - stale approval?
   - stale issue?
   - stale project?

2. **Thu thập bằng chứng**
   - last update khi nào?
   - source nào cho thấy đang stale?
   - có conflict giữa metadata và trạng thái thực không?

3. **Phân loại mức độ**
   - stale nhẹ
   - stale rõ
   - stale nặng

4. **Hành động**
   - ghi vào daily report / status dashboard
   - thêm next action
   - escalate owner nếu cần
   - đề xuất đổi status thành on-hold/stopped nếu cần

5. **Cập nhật source-of-truth**
   - project.yaml
   - status dashboard
   - task board / approval log / issue log nếu liên quan

## Rule cứng
Không tiếp tục coi project là active bình thường nếu stale nặng kéo dài.
