# Browser Install / Download Approval Gate

## Purpose

Prevent agents from silently downloading browser binaries or changing environment state.

## Rule

Browser binary install/download requires explicit user approval before running commands such as:

```sh
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
```

## Approval Request Must Include

```text
- exact command to run
- why it is needed
- expected network/download behavior
- expected disk impact
- whether it changes package files or system packages
- rollback/removal plan if available
- alternative fallback option
```

## Approval Does Not Cover

Approval for one command does not cover:

```text
- additional package installs
- apt/system installs
- cloud/browser service subscriptions
- DNS/billing changes
- deploy actions
```

## If Approval Is Not Granted

Worker must choose one:

```text
- use approved fallback evidence level
- return Blocked / Needs Review
```

Worker must not:

```text
- run browser install anyway
- hide missing browser executable
- claim screenshot or real browser proof
```
