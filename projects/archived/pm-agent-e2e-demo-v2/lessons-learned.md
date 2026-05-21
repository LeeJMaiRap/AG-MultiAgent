# Lessons Learned: Hệ thống quản lý công việc nội bộ

## What Went Well
1. **Bộ tài liệu planning bám sát nhau hơn** - Clarification, charter, requirements và spec cùng phản ánh một scope MVP nhất quán.
2. **Pain point integration được lộ ra sớm** - Blocker API contract được nhìn thấy trước khi frontend đi quá sâu.
3. **Scope control tốt hơn** - Dashboard được khóa sớm ở mức summary để bảo vệ timeline.

## What Could Be Improved
1. **API contract cần được freeze sớm hơn** - Nếu không, frontend dễ bị block và rework.
2. **Cần checklist handoff backend ↔ frontend rõ hơn** - Sample payload và enum/status nên được chốt trước khi build UI.
3. **Defect/quality metrics ở giai đoạn sớm còn yếu** - Không nên ghi số đẹp nếu chưa có dữ liệu test đủ mạnh.

## Key Insights
- Insight 1: Clarification mạnh hơn sẽ giúp khóa scope sớm và giảm vòng hỏi lại ở planning.
- Insight 2: Spec có API contract và data model chi tiết giúp giảm đáng kể nguy cơ integration mismatch.
- Insight 3: Dashboard chỉ hữu ích khi recommended actions thật sự actionable (owner + deadline + priority).

## Recommendations
1. For similar projects in future: Freeze API contract trước khi mở frontend core.
2. For PM Agent improvements: Duy trì spec template có API Specification và Data Model chi tiết.
3. For team process improvements: Thêm checklist handoff và smoke validation sớm.

## Metrics Summary
- **Estimation accuracy:** Chưa đủ dữ liệu cuối kỳ, nhưng forecast đang lệch nhẹ +2 ngày
- **On-time delivery:** Chưa kết thúc, hiện at risk nhẹ
- **Budget variance:** Forecast +4h so với plan
- **Defect escape rate:** N/A ở giai đoạn hiện tại
- **Team satisfaction:** Chưa có dữ liệu đáng tin cậy

## Knowledge Transfer
- **Documentation location:** `projects/archived/pm-agent-e2e-demo-v2/`
- **Key contacts:** Owner, PM Agent, Backend dev, Frontend dev, Tester part-time
- **Related projects:** `projects/active/web-ban-hang/`
- **Lessons learned repository:** `projects/pm-agent-e2e-demo-v2/lessons-learned.md`

## Action Items
- [ ] Thêm checklist freeze API contract vào workflow PM Agent
  - **Owner:** PM Agent
  - **Deadline:** 2026-05-20
- [ ] Thêm sample payload review step vào handoff backend/frontend
  - **Owner:** PM Agent
  - **Deadline:** 2026-05-20
- [ ] Rà lại template dashboard để chỉ dùng quality metrics khi có dữ liệu đủ mạnh
  - **Owner:** PM Agent
  - **Deadline:** 2026-05-21
