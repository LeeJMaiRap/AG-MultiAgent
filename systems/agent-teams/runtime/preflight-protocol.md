# Preflight Protocol

## Purpose

Catch missing tools, dependencies, permissions, and environment assumptions before real implementation work starts.

Phase 14 found a concrete gap: `npm run build` expected `tsc`, but TypeScript was not installed. Preflight prevents that class of failure from reaching implementation acceptance.

## When Required

Preflight is required before any delegated task with Verification Level:

```text
Local
Integration
Production
```

Preflight is optional for:

```text
Paper
Simulated
```

## PM Orchestrator Responsibilities

Before assigning real implementation work, PM Orchestrator must require a preflight block in the task packet.

PM Orchestrator must verify:

```text
- required commands are named
- required versions are stated when relevant
- dependency install policy is clear
- network policy is clear
- approval needs are clear
- fallback path exists if a tool is missing
```

## Worker Responsibilities

Before editing implementation files, worker must run preflight checks and report result.

Worker must not silently install dependencies, change stack, or bypass missing tools. If a tool is missing, worker must either:

```text
- use an approved dependency-free fallback inside scope, or
- return Blocked / Needs Review with exact missing tool and proposed fix
```

## Required Preflight Fields

Task packet should include:

```md
## Preflight Required

- `<command/tool/version check>`
- `<dependency availability check>`
- `<network/install policy>`
- `<fallback if missing>`
```

Agent report should include:

```md
## Preflight Result

```text
<check>
<result>
```
```

## Standard Checks

For Node/JS tasks:

```text
node -v
npm -v
npm run <script> --if-present
command -v <tool>
```

For test/build tasks:

```text
list package scripts
verify tool command exists
run dry/syntax check if available
```

For browser/UI tasks:

```text
browser package availability (Playwright/Puppeteer/etc.)
browser executable availability (Chromium/Chrome/etc.)
headless browser launch check when real browser proof is required
screenshot/output path policy
route to inspect
fallback vs Blocked rule if browser executable is missing
approval requirement for browser binary install/download
```

For browser/UI tasks, browser package presence alone is not enough for real browser proof. A real browser claim requires a successful browser executable launch. If browser binary install/download is required, worker must ask for explicit approval before running commands such as:

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
```

If approval is not granted, worker must either use an approved lower-evidence fallback or report Blocked / Needs Review. Fallback evidence such as local HTTP fetch + HTML assertions must not be described as screenshot, real browser runtime, visual regression, or accessibility scan proof.

For API tasks:

```text
server start command
port/env assumptions
curl or request tool availability
```

## Dependency / Network Policy

Default policy:

```text
- no dependency install unless task explicitly allows it
- no paid service setup
- no cloud/DNS/billing
- no real secrets
- if dependency missing, stop or use documented fallback
- no browser binary install/download unless task explicitly allows it and user approval is recorded
```

## Preflight Gate

Pass when:

```text
- all required tools exist, or approved fallback is selected
- required commands are runnable or blockers are documented
- dependency/network policy is followed
- evidence is captured in report
```

Fail / Needs Review when:

```text
- required tool missing and no approved fallback
- install/cloud/secret/deploy needed without approval
- command fails before implementation and root cause is unknown
- worker changes stack without PM/user approval
```

## Evidence Requirements

Preflight evidence can be:

```text
- command output
- version output
- package script listing
- explicit blocker with exact missing command/tool
- documented fallback decision
```

## Example

```text
Check: command -v tsc
Result: missing
Decision: Do not install dependencies. Switch to dependency-free JS + node --check because task allowed no-install fallback.
Status: PASS with fallback
```
