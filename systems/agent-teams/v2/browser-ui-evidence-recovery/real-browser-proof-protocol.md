# Phase 79 — Real Browser Proof Protocol

## Purpose

Define minimum evidence for real browser UI proof while executable availability remains pending.

This protocol does not authorize browser install/download. If no executable is available, status remains Blocked or Fallback Only.

## Entry Conditions

Real browser proof may start only when all are true:

```text
browser/tool row selected from browser readiness matrix
install/download approval status recorded
browser executable path exists
version command succeeds
launch command is defined
artifact/output destination is defined
claim boundary is defined before execution
```

## Required Evidence Bundle

Every real browser proof report must include:

```text
Browser/tool name:
Executable path:
Version command:
Version output:
Launch command:
URL/file opened:
Raw launch output path:
Screenshot/artifact path if screenshot/visual claim requested:
Assertions performed:
Pass/fail result:
Claim boundary:
Fallback boundary if blocked:
```

## Minimum Real Browser Smoke Proof

Minimum acceptable smoke proof requires:

```text
executable path recorded
version output recorded
browser launch command recorded
page or file opened
raw output proves launch + page load
no screenshot/visual/a11y claim unless matching artifact/raw scan output exists
```

Accepted claim:

```text
Real browser smoke completed for <URL/file> using <browser/tool>.
```

Rejected if:

```text
package present but executable missing
executable path exists but launch not run
launch failed
raw output missing
```

## Real Browser Functional Proof

Functional proof requires smoke proof plus:

```text
user flow steps
assertions
raw output for each assertion or test runner log
failure screenshots/logs if available
```

Accepted claim:

```text
Real browser functional flow completed for <flow> using <browser/tool>.
```

## Screenshot / Visual Proof

Screenshot or visual proof requires:

```text
real browser executable launch evidence
screenshot capture command
artifact path
artifact provenance: timestamp, browser/tool, URL/file
comparison rule if visual regression is claimed
```

Accepted screenshot claim:

```text
Screenshot captured from real browser executable.
```

Visual regression claim requires additional approved comparison process. A screenshot alone is not visual regression proof.

## A11y Proof

A11y proof requires:

```text
a11y tool name and version
tool approval/provenance if installed or external
browser/executable relationship if tool drives browser
raw scan output path
severity summary
known exclusions
```

Accepted a11y claim:

```text
A11y scan completed with raw output.
```

## Blocked Path

If executable is missing or unsupported:

```text
Status: Blocked or Fallback Only
Allowed claim: browser-like fallback check completed
Forbidden claims: real browser tested, screenshot verified, a11y verified, visual regression passed
Required reference: fallback-browser-like-boundary.md
```

## Command Safety

Allowed without approval:

```text
read-only executable discovery
version command for existing executable
launch command for existing executable against local file/localhost only, after scope review
```

Requires explicit approval:

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
browser/cloud provider setup
external URL testing
cloud browser provider
```

## PM Acceptance Checklist

```text
[ ] Entry conditions complete?
[ ] Browser executable path recorded?
[ ] Version output recorded?
[ ] Launch output recorded?
[ ] URL/file opened recorded?
[ ] Assertions listed?
[ ] Artifact path recorded for screenshot/visual claim?
[ ] A11y raw output recorded for a11y claim?
[ ] Fallback label used when blocked?
[ ] Overclaims rejected?
```
