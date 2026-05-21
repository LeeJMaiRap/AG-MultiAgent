# Phase 29 Task Packet — Approved Browser Install Attempt

## Task ID

`QA-029`

## Assigned Agent

QA/Test Agent + PM Review

## Objective

Run approved command `npx playwright install chromium`, then verify Chromium launch and screenshot availability.

## Context

User approved the exact command after Phase 28 approval request draft.

## Owned Paths

- `systems/agent-teams/examples/phase-29-approved-browser-install-attempt/**`

## Forbidden Paths

- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- app pilot source folders

## Acceptance Criteria

- [x] Run approved exact command only.
- [x] Capture install output.
- [x] Run launch check after install attempt.
- [x] Capture launch output.
- [x] Do not run alternate install/download command without fresh approval.
- [x] Report Blocked if browser executable still missing.

## Verification Level

Local.

## Preflight Required

Approved command:

```sh
npx playwright install chromium
```

Install/network policy:

```text
Only this exact command approved.
No apt install.
No npm install playwright.
No npm install puppeteer.
No npx playwright install without chromium argument.
```

## Verification Required

- `reports/install-attempt.log`
- `reports/browser-launch-check.log`
- screenshot path only if launch succeeds

## Final Status

Blocked.
