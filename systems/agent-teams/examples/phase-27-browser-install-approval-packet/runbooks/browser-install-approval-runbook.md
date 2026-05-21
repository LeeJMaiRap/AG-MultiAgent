# Browser Install Approval Runbook

## Purpose

Guide PM Agent and workers through a safe browser install/download approval flow.

## 1. Pre-Approval Evidence

Collect and report:

```text
node -v
npm -v
browser package check
browser executable path check
browser launch check
current task Verification Level
why real browser proof is required
```

## 2. Decide Whether Install Is Needed

Install/download is needed only if all are true:

```text
real browser proof is required
browser executable launch fails or executable is missing
fallback is not accepted or not enough
user has not already approved exact command
```

If fallback is enough, do not request install.

## 3. Prepare Approval Packet

Use:

```text
systems/agent-teams/examples/phase-27-browser-install-approval-packet/templates/browser-install-approval-request-template.md
```

Packet must include:

```text
exact command
why needed
network/download impact
disk/environment impact
files/paths likely affected
approval scope
rollback/cleanup plan
fallback if rejected
```

## 4. Ask User

Ask with one exact command only.

Do not combine commands with:

```text
&&
;
|
multiple install commands
```

If multiple commands are needed, request separate approval for each.

## 5. Execute Only If Approved

After approval, worker may run only approved exact command.

Worker must not add flags, chain commands, change package manager, or switch to apt/system install without separate approval.

## 6. Verify After Install

Run:

```text
browser executable path check
browser launch check
minimal real browser smoke test
screenshot output path check if screenshot proof is required
```

Report evidence:

```text
command output
browser launch result
screenshot/log path
cleanup status
```

## 7. Cleanup / Rollback

Cleanup must match install type:

```text
Playwright cache: remove cache path only if approved or clearly safe for local workspace policy.
npm install: revert package file changes if unintended; do not remove broad node_modules without approval.
apt install: ask explicit approval before package removal.
```

Prefer no cleanup if it would be destructive or affect other projects.

## 8. If Rejected Or Fails

Choose one:

```text
use browser-like fallback if task allows it
return Blocked
return Needs Review with exact missing executable/error
```

Do not claim real browser proof.
