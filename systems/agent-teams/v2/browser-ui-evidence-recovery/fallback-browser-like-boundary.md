# Phase 78 — Fallback Browser-Like Evidence Boundary

## Purpose

Harden fallback browser-like evidence rules so fallback checks are useful but never confused with real browser, screenshot, a11y, or visual proof.

## Definition

Fallback browser-like evidence means:

```text
UI logic, markup, contract, routing, rendering helper, or static artifact checks that do not launch a real browser executable.
```

Fallback can support limited confidence for local UI behavior, but cannot support real browser claims.

## Allowed Fallback Evidence

```text
DOM/string rendering unit tests without browser executable
static HTML inspection
server response HTML/body inspection
browser-like integration tests using simulated request/response
component output snapshot from non-browser renderer
manual static review labelled fallback
```

## Forbidden Fallback Claims

Fallback evidence must not claim:

```text
real browser tested
screenshot verified
visual regression passed
accessible/a11y verified
cross-browser compatible
responsive layout verified
production browser proof
```

## Required Label

Every fallback report must include exact label:

```text
Evidence type: Browser-like fallback. No real browser executable was launched.
```

## Required Boundary Block

Use this block in reports:

```text
Allowed claim: browser-like fallback check completed.
Forbidden claims: real browser tested, screenshot verified, a11y verified, visual regression passed.
Reason: no browser executable launch evidence and no browser-generated artifact.
```

## Fallback Evidence Record

```text
Fallback ID:
Project / phase:
Check type:
Command or inspection method:
Raw output path:
Files/URLs inspected:
Assertions made:
What this supports:
What this does not support:
Browser executable launched: No
Screenshot/artifact from real browser: No
A11y scan raw output: No unless separate approved tool output exists
Claim boundary:
```

## PM Review Rule

PM may accept:

```text
browser-like fallback check completed
static UI inspection completed
UI contract/render helper checked without real browser
```

PM must reject:

```text
real browser tested
screenshot verified
visual proof
visual regression passed
a11y verified
cross-browser compatibility
```

unless Track 4 real browser/a11y/visual evidence exists.

## Report Examples

### Correct

```text
Browser-like fallback check completed for task list rendering. No real browser executable was launched. No screenshot/a11y/visual claim is made.
```

### Incorrect

```text
Browser UI tested successfully.
```

Reason incorrect:

```text
Ambiguous. Could imply real browser execution.
```

### Correct Downgrade

```text
Claim requested: real browser tested.
Decision: Rejected.
Accepted boundary: browser-like fallback check completed.
Reason: browser executable missing.
```

## Stop Conditions

Stop and ask before:

```text
presenting fallback output as real browser evidence
using static artifact as screenshot proof
claiming a11y/visual/cross-browser coverage from fallback
omitting fallback label from PM acceptance report
using fallback to bypass browser install approval or executable discovery
```
