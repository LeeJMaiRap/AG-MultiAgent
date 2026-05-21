# Known Blockers And Limits

## Blocker 1 — Real Browser Automation

Status: Blocked.

Evidence:

```text
npx playwright install chromium
Failed to install browsers
Error: ERROR: Playwright does not support chromium on ubuntu26.04-x64

Playwright chromium.launch
browserType.launch: Executable doesn't exist at /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell
```

Impact:

```text
No real browser screenshot proof.
No real browser runtime proof.
No visual regression proof.
No browser-based accessibility scan proof.
```

Rule:

```text
Use browser-like fallback only when explicitly labelled fallback.
PM Agent must reject screenshot/real-browser/a11y/visual claims without launch evidence.
```

Possible future options need fresh approval:

```text
npx playwright install
apt install chromium
apt-get install chromium
remote/browser service
container/browser image change
```

## Limit 2 — TypeScript Compiler Missing In Pilots

Status: Ready with fallback.

Evidence:

```text
command -v tsc: missing; fallback selected
node --check used in local pilots
```

Impact:

```text
No TypeScript compile proof for dependency-free pilots.
```

Rule:

```text
If project requires TypeScript build, preflight must verify tsc or approved package setup first.
```

## Limit 3 — Production Readiness Not Proven

Status: Needs hardening.

Missing evidence:

```text
auth/access control
persistent database
migration plan
secrets handling
load/performance tests
security audit
observability
backup/rollback
deployment proof
```

Rule:

```text
Agent-Teams v1 may run local/integration pilots only. Production requires separate approval and production preflight.
```

## Limit 4 — Human Approval Gates Still Manual

Status: Accepted v1 constraint.

Affected actions:

```text
external installs/downloads
system packages
cloud services
deployments
public communications
secret access
```

Rule:

```text
PM Agent must pause and request exact-command approval before any gated action.
```
