# Daily Report Cron Runbook

## Purpose
Run the PM Agent 19:00 daily reporting flow via OpenClaw cron.

## Trigger
OpenClaw cron runs an agent turn in an isolated session.

## Event Contract
When the 19:00 cron job runs, the agent should execute this flow in order:
1. Generate or update the framework daily report when framework reporting is relevant.
2. Scan `projects/active/` for projects with `project.yaml` and `status: active`.
3. Skip projects with `status: on-hold`, `stopped`, or `archived`.
4. Generate project daily reports only for eligible active projects.
5. Surface source conflicts in report output instead of silently reconciling them.
6. Export the framework daily report Markdown to PDF.
7. **Attempt to send the resulting PDF to Telegram** with a short caption.
8. **If Telegram delivery fails:** log the failure, continue without error (file-only mode fallback).
9. **Log selector audit output** with:
   - framework target selected/skipped
   - project candidates scanned
   - eligible active projects count
   - skipped projects with reasons
10. **Create cron run log** in `systems/pm-agent/reports/daily/YYYY-MM-DD-cron-log.md` with:
   - execution summary
   - steps executed with status
   - selector audit
   - artifacts created
   - issues encountered
   - recommendations

## Source Of Truth
Primary spec:
`systems/pm-agent/reports/plans/cron-flow-19h00-spec-2026-05-14.md`

## Current Default
- Schedule target: 19:00
- Timezone currently configured in cron job: Asia/Ho_Chi_Minh
- Delivery: Telegram announce with framework report PDF
- Recommended enablement: monitor first real scheduled run to confirm PDF generation + delivery remain stable

## Monitoring & Stability

### What to monitor
- Cron execution time vs scheduled time
- PDF generation success rate
- Telegram delivery success rate (optional, not critical)
- Selector accuracy (active vs skipped)
- Source conflict detection rate
- Report generation errors

### Success criteria
- Framework report generated every run
- PDF export succeeds
- Selector skips non-active projects correctly
- Audit log created with full context
- **Delivery succeeds OR fails gracefully with clear reason**

### Failure modes
- **Telegram bot kicked/blocked** → continue with file-only mode (not a critical failure)
- PDF generation fails → deliver markdown only
- No active projects → framework report only
- Source conflict detected → surface in report, continue

### Delivery Fallback Strategy
**Primary:** Telegram delivery  
**Fallback:** File-only mode (PDF + MD in `reports/daily/`)  
**Critical:** Report generation itself, not delivery method

**Rule:** Telegram delivery failure should NOT fail the entire cron job. Files are always created regardless of delivery status.

### Stability tracking
After each run, check:
- `systems/pm-agent/reports/daily/YYYY-MM-DD-cron-log.md` exists
- selector audit section present
- issues/recommendations logged if any
- artifacts created as expected
- delivery status logged (success/fail/skipped)

### Escalation
Escalate if:
- 3 consecutive runs fail **report generation** (not delivery)
- selector consistently wrong
- PDF generation broken >24h
- **No escalation needed** for Telegram delivery failures alone
