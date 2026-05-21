# PM Agent Production Readiness Checklist

## Runtime Foundation
- [x] Workspace structure tách rõ zones
- [x] PM Agent có runtime/ riêng
- [x] PM Agent có eval/ riêng
- [x] Có project metadata schema
- [x] Có decision policy
- [x] Có approval policy
- [x] Có actor tracking policy
- [x] Có state schema
- [x] Có lifecycle registry
- [x] Có runbooks cơ bản

## Project Operations
- [x] Có project.yaml cho project active
- [x] Có decisions/ cho project active
- [x] Có approvals/ cho project active
- [x] Có handoffs/ cho project active
- [x] Có evidence/ cho project active
- [x] Có final-report.md cho closure flow
- [~] Có daily reporting foundation (skill + sample output đã có, cron thật chưa bật)

## Quality & Governance
- [~] Có eval scenarios thực tế ở mức nền (hiện có `scope-change`, `worker-failure`, `vague-requirement`, `missing-approval`, `false-done`, `stale-project`)
- [x] Có regression test pack
- [x] Có acceptance verification checklist
- [x] Có stale-project detection rule
- [x] Có rollback playbook cho project issue

## Multi-project Scalability
- [x] Có projects registry
- [x] Có active projects dashboard
- [x] Có archived projects dashboard
- [x] Có portfolio dashboard
- [x] Có cross-project risk view

## Readiness Notes
- `[x]` = đã có và dùng được
- `[~]` = đã có foundation / partial, nhưng chưa hoàn chỉnh production-grade
- `[ ]` = chưa có hoặc chưa đủ dùng thực tế

## Current Gaps To Close
1. Actor attribution mới có policy + artifact fields, chưa đủ mạnh ở mức auto-audit hoàn chỉnh.
2. Daily reporting mới ở mức foundation; chưa có cron 19:00 thật và chưa có notify/logging runtime hoàn chỉnh.
3. Regression/eval pack đã có nền nhưng vẫn còn mỏng, chưa thành automated regression harness.
4. Một số source-of-truth vẫn có conflict thật (ví dụ project metadata vs task-board) và mới dừng ở mức detect, chưa có reconciliation strategy.
5. Portfolio layer đã có nền, nhưng vẫn còn ít project để kiểm chứng hành vi multi-project ở quy mô lớn.

## Overall Assessment
**Current state:** Production-readiness foundation, governance baseline, và multi-project visibility foundation đã được thiết lập. PM Agent đủ tốt cho pilot/internal use có kiểm soát, nhưng vẫn cần thêm hardening ở cron/runtime automation, actor audit depth, và regression automation trước khi coi là production-grade hoàn chỉnh.
