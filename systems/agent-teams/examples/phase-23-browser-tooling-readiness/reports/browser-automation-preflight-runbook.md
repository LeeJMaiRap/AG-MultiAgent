# Browser Automation Preflight Runbook

## Purpose

Before claiming real browser proof, verify that browser automation can actually launch a browser executable.

## Required Checks

Run and capture output:

```sh
node -v
npm -v
node -e "try { require.resolve('playwright'); console.log('playwright available') } catch { console.log('playwright missing') }"
node -e "try { require.resolve('puppeteer'); console.log('puppeteer available') } catch { console.log('puppeteer missing') }"
command -v chromium || command -v chromium-browser || command -v google-chrome || true
node -e "const { chromium } = require('playwright'); (async()=>{ try { const browser=await chromium.launch({headless:true}); console.log('chromium launch ok'); await browser.close(); } catch(e) { console.log('chromium launch failed'); console.log(e.message); process.exit(2); } })();"
```

## PASS Conditions

Real browser automation preflight passes when:

```text
- browser automation package exists, and
- browser executable exists, and
- headless browser launch succeeds, and
- screenshot/output path is defined, and
- target route/server start command is known
```

## FAIL / NEEDS REVIEW Conditions

Real browser automation preflight fails when:

```text
- browser package missing and install is not approved
- browser executable missing and download/install is not approved
- headless browser launch fails
- sandbox/display dependencies missing and no approved fix exists
- external download is required without user approval
```

## Fallback Options

Allowed only when task accepts non-real-browser evidence:

```text
- browser-like HTML proof through local HTTP fetch
- static HTML structure assertions
- accessibility-oriented markup checks without running browser
- mark real browser proof as Blocked and continue with lower evidence level
```

Fallback must state:

```text
- why real browser was unavailable
- what evidence level fallback provides
- which claims are not allowed
```

## Disallowed Claims With Fallback

If no browser executable launches, do not claim:

```text
- real browser tested
- screenshot verified
- client-side JavaScript runtime verified
- visual regression passed
- accessibility scan passed
- production-ready UI
```

## Evidence Output

Save preflight to:

```text
reports/browser-preflight.log
```

Save real browser artifacts to:

```text
reports/screenshots/<route-name>.png
reports/browser-test.log
```

If blocked, save:

```text
reports/browser-blocker.md
```
