# Phase 77 — Browser Executable Discovery Procedure

## Purpose

Define read-only executable discovery for Browser / UI Evidence Recovery.

This procedure may detect local browser/tool state. It must not install/download anything.

## Allowed Read-Only Commands

```bash
command -v chromium || command -v chromium-browser || true
command -v google-chrome || command -v google-chrome-stable || true
if test -x /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell; then printf '%s\n' 'present executable'; else printf '%s\n' 'missing executable'; fi
node -e "try { require('playwright'); console.log('playwright package present') } catch (error) { console.log('playwright package missing') }"
node -e "try { require('puppeteer'); console.log('puppeteer package present') } catch (error) { console.log('puppeteer package missing') }"
```

## Forbidden Commands Without Approval

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
browser/cloud provider setup
```

## Interpretation Rules

```text
No browser executable path -> no real browser claim.
Package present but executable missing -> package availability only, not browser proof.
Executable path present but not launched -> executable availability only, not browser smoke proof.
Executable launched successfully with output/artifact -> may support real browser smoke claim.
Screenshot/a11y/visual claims still require dedicated artifacts/raw output.
```

## Required Output

Record discovery output to:

```text
reports/discovery.log
```

Then classify:

```text
Ready: executable found and launch proof exists.
Unknown: detection skipped or incomplete.
Blocked: executable missing or unsupported.
Fallback Only: no executable proof, browser-like checks only.
```
