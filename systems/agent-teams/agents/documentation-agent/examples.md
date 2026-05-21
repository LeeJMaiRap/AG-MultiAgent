# Documentation Agent Examples

## Example 1: Handoff Summary

```md
# Project Handoff

## Delivered Scope

- Public account listing
- Account detail page
- Admin account CRUD

## How To Run

```text
npm install
npm run dev
```

## Environment Variables

| Name | Required | Secret | Notes |
|---|---|---|---|
| DATABASE_URL | Yes | Yes | Database connection string; value not shown |

## Verification Evidence

- QA report: `projects/web-ban-acc-game/04-review/qa-report.md`
- Security review: `projects/web-ban-acc-game/04-review/security-review.md`
- Build: `npm run build` passed

## Known Issues

- None blocking release.

## Rollback

Rollback to commit `<commit-hash>` if deployment fails.
```

## Example 2: Documentation Gap

```md
## DOC-001 Missing production env source

Gap:
Deployment guide lists `DATABASE_URL`, but production provider/database is undecided.
Impact:
Cannot produce complete production deployment steps.
Needed source/decision:
PM/user must choose database provider.
Likely owner:
PM Orchestrator / DevOps Agent
Recommended action:
Ask user to choose Neon/Supabase/Railway/Postgres provider.
```

## Example 3: Report Back To PM

```md
# Agent Report

## Task ID
DOC-001

## Status
Done

## Summary
Created handoff README, developer guide, and release notes from approved reports.

## Files Changed
- projects/web-ban-acc-game/README.md — project overview
- projects/web-ban-acc-game/06-handoff/developer-guide.md — setup/run/test guide
- projects/web-ban-acc-game/06-handoff/release-notes.md — release summary

## Verification
Cross-checked docs against PRD, API contract, QA report, and DevOps report.

## Issues Found
None

## Blockers
None

## Handoff Notes
Ready for PM final handoff review.
```
