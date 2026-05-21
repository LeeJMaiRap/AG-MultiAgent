# Phase 25 Verification Report — PM Browser Preflight Alignment

## Status

PASS.

## Scope

Align PM Agent docs with Agent-Teams browser preflight guidance from Phase 23 and Phase 24.

## Verification Level

Paper.

## Files Changed

```text
systems/pm-agent/architecture/SYSTEM-PROMPT.md
systems/pm-agent/architecture/WORKFLOW.md
systems/pm-agent/skills/README.md
```

## Files Created

```text
systems/agent-teams/examples/phase-25-pm-browser-preflight-alignment/phase-25-verification-report.md
```

## Changes Made

### PM System Prompt

Added browser/UI proof rule requiring PM Agent to distinguish:

```text
browser package available
browser executable available
headless browser launch successful
```

Added PM rejection rule for unsupported claims:

```text
screenshot
real browser tested
browser runtime verified
visual regression passed
accessibility scan passed
```

If report only has browser-like fallback such as local HTTP fetch + HTML assertions, PM Agent must label it as lower-evidence fallback and must not accept real browser claims.

Added explicit approval gate for browser binary install/download commands:

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
```

### PM Workflow

Updated Preflight Ready gate:

```text
browser/UI tasks distinguish browser package availability from browser executable launch readiness
browser binary install/download requires explicit user approval before worker runs install/download commands
```

Updated Verification Level workflow:

```text
browser/UI proof requires successful browser executable launch plus screenshot/log evidence before accepting real browser claims
otherwise label result as browser-like fallback or Blocked
```

### PM Skills README

Updated preflight routing rule:

```text
Browser/UI proof must check browser package availability and browser executable launch readiness separately.
Browser-like fallback evidence must not be accepted as screenshot, real browser runtime, visual regression, or accessibility scan proof.
Browser binary install/download requires explicit user approval before commands such as npx playwright install or apt install chromium run.
```

## Acceptance Criteria

- [x] PM Agent requires browser package and executable launch checks for browser/UI proof.
- [x] PM Agent rejects real browser/screenshot/a11y/visual claims when only fallback evidence exists.
- [x] PM Agent requires explicit user approval before browser install/download commands.
- [x] PM Agent remains orchestrator-only.
- [x] No browser install/download occurred.
- [x] No app pilot files changed.
- [x] No Agent-Teams runtime/templates changed in this phase.

## Evidence Claims Check

This is Paper-level documentation alignment. No runtime proof claimed.

## Final Status

Pass.
