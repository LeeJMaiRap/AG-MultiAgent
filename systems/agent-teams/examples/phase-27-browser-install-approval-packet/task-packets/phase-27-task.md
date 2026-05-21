# Phase 27 Task Packet — Browser Install Approval Packet

## Task ID

`PM-027`

## Assigned Agent

PM Agent / Orchestrator Documentation

## Objective

Create a reusable approval packet and runbook for browser binary install/download requests.

## Context

Real browser proof is Blocked when browser executable is missing. Browser binary install/download requires explicit user approval. PM Agent needs a standard packet before asking.

## Inputs

- `systems/agent-teams/examples/phase-23-browser-tooling-readiness/reports/browser-install-approval-gate.md`
- `systems/agent-teams/runtime/preflight-protocol.md`
- `systems/agent-teams/examples/phase-26-pm-browser-evidence-rejection/reports/phase-26-verification-report.md`

## Read-Only References

- `systems/pm-agent/architecture/SYSTEM-PROMPT.md`
- `systems/pm-agent/architecture/WORKFLOW.md`

## Owned Paths

- `systems/agent-teams/examples/phase-27-browser-install-approval-packet/**`

## Forbidden Paths

- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `systems/agent-teams/examples/phase-22-browser-ui-proof/app/**`
- `systems/agent-teams/examples/phase-26-pm-browser-evidence-rejection/**`

## Acceptance Criteria

- [ ] Approval request template includes exact command.
- [ ] Approval request template includes network/download impact.
- [ ] Approval request template includes disk/system/package impact.
- [ ] Approval request template includes rollback/cleanup notes.
- [ ] Approval request template includes fallback option if user does not approve.
- [ ] Runbook lists pre-approval, approval, execution, verification, cleanup, and reporting steps.
- [ ] Risk notes cover dependency changes, system packages, cache size, CI mismatch, and security review.
- [ ] No browser install/download occurs.

## Verification Level

Paper.

## Preflight Required

Not required for Paper verification.

Guardrails:

```text
Do not run npx playwright install.
Do not run npx playwright install chromium.
Do not run npm install playwright.
Do not run npm install puppeteer.
Do not run apt install chromium.
Do not run apt-get install chromium.
```

## Verification Required

- grep coverage for approval packet fields.
- `git diff --check`.
- status review confirming only Phase 27 files are staged/committed.

## Constraints

- Documentation only.
- No dependency install.
- No browser binary download.
- No cloud/browser service.
- No deploy.

## Return Format

Phase report with evidence and commit hash.
