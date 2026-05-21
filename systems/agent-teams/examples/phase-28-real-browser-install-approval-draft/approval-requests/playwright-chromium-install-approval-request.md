# Approval Request — Install Playwright Chromium Browser Binary

## Request Summary

Approval requested before running one browser binary install/download command for future real browser proof.

## Exact Command Requested

```sh
npx playwright install chromium
```

## Why Needed

Phase 22 preflight showed:

```text
node -v: v22.22.2
npm -v: 10.9.7
playwright package: available
playwright chromium launch: unavailable
error: browserType.launch: Executable doesn't exist at /root/.cache/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-linux64/chrome-headless-shell
puppeteer package: missing
chromium command: missing
fallback used: dependency-free browser-like HTML proof via local HTTP fetch
```

Real browser proof, screenshot proof, visual regression proof, and browser-based accessibility scans require a launchable browser executable. Current environment cannot provide that proof.

## Expected Network / Download Impact

```text
The command may download a Chromium browser binary from Playwright-managed external sources/CDN.
Network access is required.
Download size may be large and version-dependent.
The command may reuse or update Playwright cache if available.
```

## Expected Disk / Environment Impact

```text
Expected primary write path: ~/.cache/ms-playwright/**
Expected browser family: Chromium
Expected system package change: none from this command itself
Expected package.json/package-lock.json change: none from browser binary install itself
Expected node_modules change: none unless Playwright package manager behavior differs in current environment
```

## Files / Paths Likely Affected

```text
~/.cache/ms-playwright/**
/root/.cache/ms-playwright/**
```

Potentially unaffected but monitored:

```text
package.json
package-lock.json
node_modules/**
```

## Approval Scope

Approval covers only this exact command:

```sh
npx playwright install chromium
```

Approval does not cover:

```text
npx playwright install
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
other npm installs
system package installs
cloud/browser service use
DNS/billing changes
deploy actions
secret access
additional chained commands
```

## Rollback / Cleanup Plan

If rollback is needed, likely cleanup target:

```text
~/.cache/ms-playwright/** chromium browser cache created by this command
/root/.cache/ms-playwright/** chromium browser cache created by this command
```

Cleanup should be approved before removing broad cache paths because other projects may share Playwright browser cache.

If package files unexpectedly change, revert only those package file changes after review.

## Verification After Approval And Install

If user approves and command succeeds, next worker should verify:

```text
browser executable path exists
Playwright Chromium launch succeeds
minimal page open succeeds
screenshot output path can be written
```

Evidence required:

```text
install command output
browser launch result
screenshot/log path if real browser proof is claimed
cleanup/rollback status
```

## Fallback If Not Approved

```text
Continue using browser-like fallback only if task accepts lower-evidence proof.
Mark real browser proof as Blocked.
Do not claim screenshot, visual regression, browser runtime, or accessibility scan proof.
```

## User Decision Needed

Approve or reject exact command:

```sh
npx playwright install chromium
```
