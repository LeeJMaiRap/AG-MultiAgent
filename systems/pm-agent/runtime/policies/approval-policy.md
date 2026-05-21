# Approval Policy

Quy định về quy trình phê duyệt trong PM Agent workflow.

## Các loại approval

### 1. Scope Approval
**Khi nào cần:**
- Sau khi tạo charter và requirements
- Trước khi chuyển sang planning phase

**Ai approve:**
- Project owner

**Format:**
```markdown
## Scope Approval
- **Date:** YYYY-MM-DD
- **Requested by:** [Name/Role]
- **Requested actor:** [human:... / agent:main / subagent:... / unknown]
- **Approver:** [Name]
- **Approver actor:** [human:... / agent:main / subagent:... / unknown]
- **Status:** ✅ Approved / ❌ Rejected / ⏸️ On Hold
- **Comments:** [Optional feedback]
- **Conditions:** [Any conditions for approval]
```

### 2. Plan Approval
**Khi nào cần:**
- Sau khi hoàn tất planning docs (spec, plan, wbs, schedule, risks)
- Trước khi bắt đầu execution

**Ai approve:**
- Project owner
- Key stakeholders (nếu có)

**Format:**
```markdown
## Plan Approval
- **Date:** YYYY-MM-DD
- **Requested by:** [Name/Role]
- **Requested actor:** [human:... / agent:main / subagent:... / unknown]
- **Approver:** [Name]
- **Approver actor:** [human:... / agent:main / subagent:... / unknown]
- **Documents reviewed:**
  - [ ] Spec
  - [ ] Plan
  - [ ] WBS
  - [ ] Schedule
  - [ ] Risk Register
- **Status:** ✅ Approved / ❌ Rejected / ⏸️ On Hold
- **Comments:** [Feedback]
```

### 3. Change Request Approval
**Khi nào cần:**
- Khi có thay đổi scope
- Khi có thay đổi timeline/budget
- Khi có thay đổi success criteria

**Ai approve:**
- Project owner (mandatory)
- PM Agent (review)
- Affected stakeholders (consult)

**Format:**
```markdown
## Change Request CR-XXX
- **Date:** YYYY-MM-DD
- **Requested by:** [Name]
- **Requested actor:** [human:... / agent:main / subagent:... / unknown]
- **Type:** Scope / Timeline / Budget / Other
- **Description:** [What changes]
- **Rationale:** [Why]
- **Impact:**
  - Scope: [Impact]
  - Timeline: [Impact]
  - Budget: [Impact]
  - Quality: [Impact]
- **Approver:** [Name]
- **Approver actor:** [human:... / agent:main / subagent:... / unknown]
- **Status:** ✅ Approved / ❌ Rejected / ⏸️ Pending
- **Decision date:** YYYY-MM-DD
```

### 4. Closure Approval
**Khi nào cần:**
- Khi tất cả task đã hoàn thành
- Trước khi đóng project chính thức

**Ai approve:**
- Project owner

**Format:**
```markdown
## Closure Approval
- **Date:** YYYY-MM-DD
- **Requested by:** [Name/Role]
- **Requested actor:** [human:... / agent:main / subagent:... / unknown]
- **Approver:** [Name]
- **Approver actor:** [human:... / agent:main / subagent:... / unknown]
- **Deliverables verified:**
  - [ ] All tasks completed
  - [ ] All acceptance criteria met
  - [ ] Final report created
  - [ ] Lessons learned documented
- **Status:** ✅ Approved / ❌ Rejected
- **Comments:** [Final feedback]
```

## Approval workflow

```
Request → Review → Approve/Reject → Log → Notify
```

1. **Request:** PM Agent tạo approval request
2. **Review:** Owner/stakeholder review
3. **Approve/Reject:** Owner quyết định
4. **Log:** Ghi lại vào `approvals/` directory
5. **Notify:** Thông báo kết quả cho các bên liên quan

## Timeout policy

- Scope approval: 24 giờ
- Plan approval: 48 giờ
- Change request: 24 giờ (urgent), 72 giờ (normal)
- Closure approval: 48 giờ

Nếu quá timeout mà không có phản hồi:
- PM Agent escalate
- Nếu vẫn không có phản hồi: assume approved (với low-risk items) hoặc on-hold (với high-risk items)

## Rejection handling

Khi approval bị reject:
1. PM Agent phải hiểu lý do reject
2. Điều chỉnh theo feedback
3. Resubmit approval request
4. Log lại lịch sử reject + adjustment
