# Browser Install Approval Request Template

## Request Summary

I need approval before running a browser binary install/download command for real browser proof.

## Requested Command

Choose exactly one command per approval request:

```sh
npx playwright install chromium
```

Alternative examples that require separate approval:

```sh
npx playwright install
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
```

## Why Needed

```text
Current browser package or test harness exists, but browser executable launch is unavailable.
Real browser proof, screenshot proof, visual regression, or accessibility scan requires a working browser executable.
```

## Expected Network / Download Impact

```text
The command may download browser binaries from external package/CDN sources.
Download size may be large and version-dependent.
Network access is required.
Retry/cache behavior depends on the package manager/tool.
```

## Expected Disk / Environment Impact

```text
Playwright browser install usually writes browser binaries to a tool cache such as ~/.cache/ms-playwright.
npm install commands may change node_modules and may update package-lock.json/package.json depending on command and flags.
apt install commands change system packages and require elevated privileges.
```

## Files / Paths Likely Affected

```text
~/.cache/ms-playwright/**
node_modules/** if npm install is used
package.json/package-lock.json if npm install modifies project dependencies
system package database if apt/apt-get is used
```

## Approval Scope

Approval covers only the exact command above.

Approval does not cover:

```text
other npm installs
apt/system installs
cloud/browser services
DNS/billing changes
deploy actions
secrets
additional chained commands
```

## Rollback / Cleanup Plan

```text
If using Playwright cache install, remove the downloaded browser cache path after confirmation if rollback is needed.
If using npm install, revert package file changes and remove node_modules changes as appropriate.
If using apt install, use system package removal only with explicit approval because it is destructive/system-level.
```

## Fallback If Not Approved

```text
Use browser-like fallback evidence only if task accepts lower-evidence proof.
Otherwise mark task Blocked / Needs Review.
Do not claim screenshot, real browser runtime, visual regression, or accessibility scan proof.
```

## User Approval Needed

```text
Please approve or reject this exact command:
<npx/playwright/npm/apt command here>
```
