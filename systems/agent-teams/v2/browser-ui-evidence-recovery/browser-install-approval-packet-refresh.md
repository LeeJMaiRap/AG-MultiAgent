# Phase 76 — Browser Install Approval Packet Refresh

## Purpose

Refresh browser-specific approval packets so Track 4 can request browser/tool installs without bypassing Track 1 governance.

This document is a planning/template artifact only. It does not approve or run any install/download.

## Required Base Template

Start from Track 1 template:

```text
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-request-template.md
```

Attach Track 4 matrix row:

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/browser-readiness-matrix.md
```

## Browser-Specific Request Fields

Add these fields to any browser/tool approval request:

```text
Browser/tool target:
Requested command:
Reason real browser proof is required:
Why browser-like fallback is insufficient:
Target evidence class:
Target executable path after install:
Expected version check command:
Expected launch proof command:
Expected artifact(s):
Expected cache/metadata paths changed:
System-level change? yes/no
Network required? yes/no
Credentials/cloud/billing required? yes/no
Rollback/removal plan:
Claim boundary if approved:
Claim boundary if rejected:
```

## Commands Covered

Each command needs its own explicit approval packet:

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
browser/cloud provider setup
```

`allow-once` approval covers only exact approved command. New command means new approval.

## Evidence Required After Approved Execution

After approved install/download, record:

```text
exact command executed
start/end timestamp
exit status
stdout/stderr log path
changed package metadata/lockfiles/cache paths
version check output
executable path check
launch proof output
screenshot/artifact path if screenshot/visual claim requested
fallback status if install failed
```

## Rejection / Fallback Rules

If approval is rejected or install fails:

```text
status: Blocked or Fallback Only
allowed claim: browser-like fallback only
blocked claims: real browser, screenshot, a11y verified, visual regression, production browser proof
required report: install approval decision or failure log
```

## Known Risk Notes

```text
Playwright Chromium previously failed on ubuntu26.04-x64.
Browser/system package install can modify machine-level state.
Browser packages may download large binaries.
Puppeteer/Playwright package presence alone is not browser proof.
Cloud browser providers can involve credentials, billing, external network, and data exposure.
```

## Approval Packet Checklist

```text
[ ] Track 1 dependency approval request filled?
[ ] Browser readiness matrix row selected?
[ ] Exact command recorded?
[ ] Command working directory recorded?
[ ] Expected changed paths recorded?
[ ] Network/credentials/system-level impact recorded?
[ ] No-install fallback considered?
[ ] Rollback/removal plan recorded?
[ ] Post-install version check planned?
[ ] Post-install executable launch proof planned?
[ ] Claim boundary if approved/rejected recorded?
```
