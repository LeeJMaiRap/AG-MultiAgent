# Risk Register: Hệ thống quản lý công việc nội bộ

## Risk Matrix
```
High   |        | R-001 | R-002 |
Medium | R-003  |       |       |
Low    |        |       |       |
       Low    Medium   High
            Impact
```

## Risk List
| ID | Risk | Probability | Impact | Score | Mitigation | Owner | Status |
|----|------|-------------|--------|-------|------------|-------|--------|
| R-001 | Scope dashboard tăng làm trễ MVP | Medium | High | 6 | Khóa dashboard ở mức tổng hợp cơ bản | PM Agent | Open |
| R-002 | API contract đổi muộn gây rework frontend | High | High | 9 | Chốt request/response schema sớm | Backend dev | Open |
| R-003 | Tester part-time phản hồi chậm | Medium | Low | 2 | Lịch review cố định + smoke checklist | PM Agent | Open |

## Mitigation Plans

### R-001: Scope dashboard tăng làm trễ MVP
- **Plan:** Chỉ giữ dashboard ở mức tổng hợp task theo trạng thái trong MVP.
- **Trigger:** Nếu frontend core chậm hoặc yêu cầu dashboard tăng thêm beyond summary.
- **Action:** Freeze scope dashboard, dời charts/trends sang phase sau.
- **Owner:** PM Agent
- **Contingency plan:** Nếu stakeholder vẫn cần thêm insight, xuất report text/manual thay vì build UI mới.
- **Cost estimate:** Nếu risk xảy ra và không khóa scope, có thể tốn thêm 4-6h frontend + 2-4h backend.
- **Status:** Open

### R-002: API contract đổi muộn gây rework frontend
- **Plan:** Chốt ví dụ request/response schema ngay từ spec và review với frontend trước khi code UI.
- **Trigger:** Backend thay response shape hoặc thêm field bắt buộc sau khi frontend đã build.
- **Action:** Review API contract trong 24h, publish sample payload chính thức.
- **Owner:** Backend dev
- **Contingency plan:** Nếu vẫn phải thay contract, tạo mapping layer tạm ở frontend để giảm rework lớn.
- **Cost estimate:** Rework có thể mất 6-10h frontend nếu thay đổi muộn.
- **Status:** Open

### R-003: Tester part-time phản hồi chậm
- **Plan:** Đặt review slot cố định và dùng smoke checklist ngắn.
- **Trigger:** Không có feedback trong vòng 2 ngày làm việc từ lúc gửi build.
- **Action:** PM Agent nhắc lịch và thu hẹp test scope theo smoke flow critical.
- **Owner:** PM Agent
- **Contingency plan:** Frontend/backend self-test các flow chính trước khi chờ vòng test đầy đủ.
- **Cost estimate:** Có thể delay 1-2 ngày nếu feedback không đến đúng lúc.
- **Status:** Open

## Risk Monitoring
- **Review frequency:** Weekly
- **Escalation criteria:** Score >= 6 hoặc blocker đụng critical path
- **Owner:** PM Agent

## Risk Summary
- **Total risks:** 3
- **High priority:** 2
- **Medium priority:** 1
- **Low priority:** 0
- **Open:** 3
- **Mitigated:** 0
- **Closed:** 0

## Recommended Actions
1. Chốt API contract chính thức trước khi frontend mở TASK-004
2. Freeze dashboard scope ở mức summary cho MVP
3. Chuẩn bị smoke checklist sớm cho phase QA
