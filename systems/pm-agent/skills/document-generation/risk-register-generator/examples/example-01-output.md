# Risk Register: Hệ thống quản lý task nội bộ

## Risk Matrix
```
High   |         | R-002, R-004 |       |
Medium | R-003   | R-001, R-005 |       |
Low    |         |              |       |
       Low       Medium        High
                 Impact
```

## Risk List
| ID | Risk | Probability | Impact | Score | Mitigation | Owner | Status |
|----|------|-------------|--------|-------|------------|-------|--------|
| R-001 | Budget chưa được chốt rõ có thể ảnh hưởng phạm vi triển khai | Medium | Medium | 4 | Chốt MVP scope độc lập với phần mở rộng, xác nhận budget sớm | Owner | Open |
| R-002 | Scope mở rộng thêm dashboard nâng cao hoặc tích hợp ngoài làm trễ timeline | High | Medium | 6 | Khóa MVP scope, dùng change management cho mọi yêu cầu mới | PM Agent | Open |
| R-003 | Người dùng nội bộ phản hồi chậm làm chậm việc tinh chỉnh yêu cầu | Medium | Low | 2 | Lên lịch review định kỳ, gom feedback theo mốc | PM Agent | Open |
| R-004 | File upload phức tạp hơn dự kiến gây chậm implementation | High | Medium | 6 | Dùng thư viện có sẵn, giới hạn loại/size file ở MVP | Developer A | Open |
| R-005 | Phân quyền có bug ảnh hưởng bảo mật và trải nghiệm | Medium | Medium | 4 | Test phân quyền kỹ, review code, kiểm tra role cả frontend/backend | Developer A + Developer B | Open |

## Mitigation Plans

### R-001: Budget chưa được chốt rõ
- **Plan:** Giữ MVP scope tối giản và xác nhận budget ở giai đoạn sớm
- **Trigger:** Khi xuất hiện yêu cầu cần thêm effort ngoài MVP hoặc owner chưa chốt ngân sách
- **Action:**
  - Chốt danh sách in-scope/out-of-scope rõ ràng
  - Xin xác nhận budget hoặc giới hạn nguồn lực
  - Trì hoãn các hạng mục mở rộng
- **Owner:** Owner
- **Status:** Open

### R-002: Scope mở rộng làm trễ timeline
- **Plan:** Kiểm soát thay đổi qua change management
- **Trigger:** Khi có yêu cầu thêm dashboard nâng cao, tích hợp ngoài hoặc tính năng mới ngoài MVP
- **Action:**
  - Đánh giá impact tới timeline
  - Chỉ cho phép thêm sau khi owner phê duyệt
  - Nếu cần, dời sang phase sau MVP
- **Owner:** PM Agent
- **Status:** Open

### R-003: Người dùng nội bộ phản hồi chậm
- **Plan:** Tạo nhịp review đều đặn và deadline feedback rõ ràng
- **Trigger:** Khi feedback bị chậm hơn 2-3 ngày hoặc bỏ lỡ review session
- **Action:**
  - Lên lịch review cố định hàng tuần
  - Gửi checklist feedback ngắn gọn
  - Escalate khi thiếu feedback cho quyết định quan trọng
- **Owner:** PM Agent
- **Status:** Open

### R-004: File upload phức tạp hơn dự kiến
- **Plan:** Giữ implementation đơn giản trong MVP
- **Trigger:** Khi upload logic bắt đầu ảnh hưởng mạnh tới timeline hoặc phát sinh vấn đề storage/security
- **Action:**
  - Dùng multer hoặc thư viện tương đương
  - Giới hạn file size và file type
  - Nếu cần, giảm phạm vi attachment trong MVP
- **Owner:** Developer A
- **Status:** Open

### R-005: Phân quyền có bug
- **Plan:** Tăng kiểm tra quyền ở cả frontend và backend
- **Trigger:** Khi phát hiện role bypass, mismatch quyền hoặc lỗi truy cập trái phép
- **Action:**
  - Review middleware authorization
  - Test các case admin/member riêng biệt
  - Thêm checklist security review trước release
- **Owner:** Developer A + Developer B
- **Status:** Open

## Risk Monitoring
- **Review frequency:** Weekly trong planning, 2 lần/tuần trong execution
- **Escalation criteria:** Score >= 6 hoặc risk chuyển trạng thái nghiêm trọng hơn
- **Owner:** PM Agent

## Risk Summary
- **Total risks:** 5
- **High priority:** 2
- **Medium priority:** 2
- **Low priority:** 1
- **Open:** 5
- **Mitigated:** 0
- **Closed:** 0

## Recommended Actions
1. Khóa phạm vi MVP càng sớm càng tốt
2. Chốt budget/nguồn lực trước khi thêm tính năng ngoài lõi
3. Tạo lịch review feedback cố định với người dùng nội bộ
4. Ưu tiên test phân quyền và file upload sớm trong implementation
