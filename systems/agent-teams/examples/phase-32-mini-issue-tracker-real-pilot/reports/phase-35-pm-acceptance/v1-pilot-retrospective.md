# v1 Pilot Retrospective — Agent-Teams mini-issue-tracker-v1

## What Worked

- Contract-first flow prevented Frontend/Backend mismatch.
- Ownership map gave clear write boundaries.
- Preflight and dependency-free stack avoided silent installs.
- `node --check` fallback handled missing `tsc` cleanly.
- Local HTTP integration tests gave stronger evidence than paper/simulated proof.
- Challenge review kept claims honest.

## What Did Not Work / Still Blocked

- Real browser proof remains blocked by unavailable Playwright Chromium executable and unsupported install path on `ubuntu26.04-x64`.
- No real browser screenshot or accessibility scan evidence exists.
- Pilot has no persistence/auth/security hardening by design.
- Evidence is local Integration only, not Production.

## Process Lessons

- Keep Wave 1 planning separate from Wave 2 implementation.
- Keep Wave 3 integration evidence separate from implementation commit.
- Require Phase acceptance report before calling v1 pilot complete.
- Keep logs in reports so evidence survives git history.
- Do not turn fallback evidence into stronger claims.

## Recommended Agent-Teams v1 Rule Updates

- For first real project, keep phase gates:
  - Wave 1: requirements + UX + architecture + contract + ownership.
  - Wave 2: implementation only.
  - Wave 3: integration + QA + reviews.
  - Wave 4: PM acceptance + retrospective.
- Keep browser work optional unless executable launch succeeds.
- Keep production work blocked until deploy/security/rollback gates exist.

## Next Recommended Phase

Phase 36 Option A — Agent-Teams v1 operating guide update.

Goal:

```text
Distill Phase 31-35 local pilot into reusable v1 runbook/checklist for future real projects.
```
