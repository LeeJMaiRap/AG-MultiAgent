# Phase 75 — Browser Readiness Matrix

## Purpose

Define readiness checks, approval gates, fallback paths, allowed claims, and blocked claims for Browser / UI evidence.

This matrix is docs-only. It does not run browser checks or approve installs.

## Readiness Status Values

```text
Ready: executable/tool exists, version captured, launch/artifact command succeeds.
Needs Approval: install/download/setup required before check can run.
Blocked: required executable/tool unavailable or known unsupported.
Fallback Only: non-browser/browser-like check can run but cannot support real browser claim.
Unknown: detection not performed yet.
```

## Matrix

| Tool / evidence path | Check command | Expected result | Approval needed | Fallback path | Allowed claims | Blocked claims | Artifact path |
|---|---|---|---|---|---|---|---|
| Playwright Chromium bundled browser | `npx playwright --version` then executable launch proof | version plus successful browser launch | install/download approval needed if browser missing | browser-like fallback tests | real browser smoke only after launch proof | real browser/screenshot/a11y/visual while executable missing | `reports/browser-launch.log`, `reports/browser-screenshot.png` |
| Known Playwright Chromium path | `test -x /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell` | executable exists and is runnable | none for check; install approval if missing | browser-like fallback tests | real browser smoke only after successful launch | any real browser claim when missing | `reports/browser-executable-check.log` |
| System Chromium | `command -v chromium || command -v chromium-browser` | executable path printed | `apt install chromium` / `apt-get install chromium` requires explicit approval if missing | browser-like fallback tests | real browser smoke after version + launch + artifact | screenshot/a11y/visual unless artifact exists | `reports/system-browser-check.log` |
| Google Chrome / Chrome stable | `command -v google-chrome || command -v google-chrome-stable` | executable path printed | install/download requires explicit approval if missing | browser-like fallback tests | real browser smoke after version + launch + artifact | real browser claim while missing | `reports/system-browser-check.log` |
| Puppeteer bundled browser | `node -e "require('puppeteer')"` plus launch proof | package available and browser launches | `npm install puppeteer` requires explicit approval if missing | browser-like fallback tests | real browser smoke after launch proof | real browser/screenshot while missing | `reports/puppeteer-launch.log` |
| Playwright package only | `node -e "require('playwright')"` | package import works | `npm install playwright` requires explicit approval if missing | browser-like fallback tests | package availability only; no browser claim | real browser claim without executable launch | `reports/playwright-package-check.log` |
| Browser-like UI tests | project test command, no browser executable | deterministic UI logic assertion output | no browser install if dependency-free | itself | fallback browser-like check completed | real browser, screenshot, a11y, visual claims | `reports/browser-like-test.log` |
| Static HTML inspection | file/content grep or parser command | expected DOM/text markers found | no browser install if dependency-free | itself | static UI file inspection | runtime browser behavior, a11y, visual claims | `reports/static-html-inspection.log` |
| A11y CLI/tool | approved tool command with raw output | scan output and exit code captured | install/download approval if tool missing | manual/static review labelled fallback | a11y scan only after approved raw output | accessibility/a11y verified while missing | `reports/a11y-scan.log` |
| Screenshot artifact | real browser command captures image | screenshot file exists and linked | browser install/setup approval if needed | static artifact preview labelled fallback | screenshot captured from real browser | visual/screenshot claim without file | `reports/screenshot.png` |
| Cloud browser provider | provider-specific command/session URL | session proof + artifact | explicit cloud/billing/secrets approval required | local fallback only | approved cloud browser evidence only | any cloud proof without approval | `reports/cloud-browser-session.md` |

## Known Blocker Record

```text
Tool: Playwright Chromium
Environment: ubuntu26.04-x64
Observed failure: Failed to install browsers
Observed error: Error: ERROR: Playwright does not support chromium on ubuntu26.04-x64
Missing executable: /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell
Decision: Blocked for real browser proof until supported executable exists and launch evidence is captured.
```

## Detection Commands Allowed Without Install

These commands are allowed as read-only/detection checks when scoped to local machine state:

```text
command -v chromium || command -v chromium-browser || true
command -v google-chrome || command -v google-chrome-stable || true
test -x /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell
node -e "try { require('playwright'); console.log('playwright package present') } catch (error) { console.log('playwright package missing') }"
node -e "try { require('puppeteer'); console.log('puppeteer package present') } catch (error) { console.log('puppeteer package missing') }"
```

Do not turn package presence into browser proof. Launch and artifact evidence are still required.

## Commands Requiring Explicit Approval

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
browser/cloud provider setup
```

## Claim Boundary Rules

```text
Executable not found -> Blocked or Fallback Only.
Package exists but executable not launched -> package/tool availability only.
Executable launched but no artifact -> real browser smoke may pass only if raw launch output proves page load; no screenshot/visual claim.
Screenshot exists but source not real browser -> fallback artifact only.
A11y tool missing -> no a11y verified claim.
Cloud/browser provider missing approval -> no cloud browser evidence claim.
```

## PM Acceptance Checklist

```text
[ ] Tool/executable row selected?
[ ] Detection command/result recorded?
[ ] Install/download approval status recorded?
[ ] Launch command/output recorded when real browser claim requested?
[ ] Artifact path recorded when screenshot/visual claim requested?
[ ] A11y raw output recorded when a11y claim requested?
[ ] Fallback label used when executable proof missing?
[ ] Blocked claims listed?
```
