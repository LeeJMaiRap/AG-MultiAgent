# Phase 28 Task Packet — Real Browser Install Approval Request Draft

## Task ID

`PM-028`

## Assigned Agent

PM Agent / Orchestrator Documentation

## Objective

Create a concrete approval request draft for `npx playwright install chromium` using the Phase 27 approval packet.

## Context

Real browser proof is blocked because Playwright Chromium executable is missing. User asked to do Phase 28, which prepares approval material only.

## Inputs

- `systems/agent-teams/examples/phase-27-browser-install-approval-packet/templates/browser-install-approval-request-template.md`
- `systems/agent-teams/examples/phase-27-browser-install-approval-packet/runbooks/browser-install-approval-runbook.md`
- `systems/agent-teams/examples/phase-22-browser-ui-proof/reports/preflight.log`

## Read-Only References

- `systems/agent-teams/runtime/preflight-protocol.md`
- `systems/pm-agent/architecture/SYSTEM-PROMPT.md`

## Owned Paths

- `systems/agent-teams/examples/phase-28-real-browser-install-approval-draft/**`

## Forbidden Paths

- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `systems/agent-teams/examples/phase-22-browser-ui-proof/app/**`
- `systems/agent-teams/examples/phase-27-browser-install-approval-packet/**`

## Acceptance Criteria

- [ ] Draft approval request names exact command `npx playwright install chromium`.
- [ ] Draft includes why needed and Phase 22 evidence.
- [ ] Draft includes network/download impact.
- [ ] Draft includes disk/environment impact.
- [ ] Draft includes affected paths.
- [ ] Draft defines approval scope and exclusions.
- [ ] Draft includes rollback/cleanup plan.
- [ ] Draft includes fallback if not approved.
- [ ] No install/download occurs.

## Verification Level

Paper.

## Preflight Required

Not required for Paper verification.

Guardrails:

```text
Do not run npx playwright install chromium.
Do not run npx playwright install.
Do not run npm install playwright.
Do not run npm install puppeteer.
Do not run apt install chromium.
Do not run apt-get install chromium.
```

## Verification Required

- grep coverage for approval-request terms.
- process check showing no install command running.
- `git diff --check`.

## Constraints

- Documentation only.
- No dependency install.
- No browser binary download.
- No cloud/browser service.
- No deploy.
