# Track 4 — Browser / UI Evidence Recovery Plan

## Purpose

Recover trustworthy Browser / UI evidence for Agent-Teams without weakening existing proof rules.

Track 4 starts from current blocker:

```text
Playwright Chromium install failed on ubuntu26.04-x64.
Missing executable: /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell
No real browser screenshot/a11y/visual claim exists.
```

## Non-Goals

Track 4 does not approve installs/downloads by itself.

Track 4 does not allow:

```text
silent browser/tool install
calling browser-like fallback real browser proof
claiming screenshot/a11y/visual evidence without executable launch
production/deploy/browser cloud service usage without explicit approval
```

## Evidence Classes

```text
Blocked: required executable/tool missing or failed.
Fallback: non-browser or browser-like simulation; must be labelled fallback.
Real Browser Smoke: executable launched, local page opened, log/screenshot captured.
Real Browser Functional: smoke plus user-flow assertions and captured evidence.
A11y Evidence: real browser or approved a11y tool run with raw output.
Visual Evidence: screenshot or visual artifact captured from real browser executable.
```

## Browser Readiness Matrix Plan

Matrix must define:

```text
tool/executable
check command
expected result
approval needed
fallback path
allowed claims
blocked claims
artifact path
```

Known entries:

```text
Playwright Chromium: blocked on ubuntu26.04-x64 install support.
Existing browser executable: unknown; must detect before claim.
System chromium/chrome: install needs explicit approval if missing.
Browser-like tests: allowed only as fallback.
```

## Approval Gate Plan

Any command below requires explicit approval before execution:

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
browser/cloud provider setup
```

Approval packet must use Track 1 Dependency / Toolchain Governance.

## Browser Evidence Report Plan

Every browser evidence claim must include:

```text
browser/tool name
executable path
version command output
launch command
URL/file opened
screenshot/log/artifact path
assertions performed
raw output
claim boundary
fallback label if not real browser
```

## UI Claim Rules

```text
No executable launch -> no real browser claim.
No screenshot artifact -> no screenshot/visual claim.
No a11y command output -> no accessibility/a11y claim.
Browser-like fallback -> only fallback claim.
Headless launch counts only with executable path and output/artifact.
```

## PM Acceptance Rules

PM may accept only these claims when evidence exists:

```text
Fallback browser-like UI check completed.
Real browser smoke completed.
Real browser functional flow completed.
A11y scan completed with raw output.
Visual screenshot captured from real browser executable.
```

PM must reject:

```text
real browser tested without executable launch evidence
screenshot verified without artifact
accessible/a11y verified without scan output
visual regression passed without approved visual evidence process
production/browser cloud proof without deploy/cloud approval
```

## Recommended Phase Breakdown

```text
Phase 74: Browser / UI Evidence Recovery plan
Phase 75: browser readiness matrix — complete
Phase 76: browser install approval packet refresh — complete
Phase 77: executable discovery dry-run, no install — complete
Phase 78: fallback browser-like evidence boundary hardening — complete
Phase 79: real browser proof protocol, pending executable availability — complete
Phase 80: dry-run claim rejection for browser/a11y/visual overclaims — complete
```

## Track 4 Exit Criteria

Track 4 is complete when:

```text
browser readiness matrix exists
approval packet refresh exists
executable discovery procedure exists
fallback boundary is wired into runbooks
real browser proof protocol exists
dry-run proves browser/a11y/visual overclaim rejection
no gate weakens Track 1 dependency governance, Track 3 evidence gates, or deploy restrictions
```
