# Phase 80 — Browser / A11y / Visual Overclaim Rejection Dry Run

## Purpose

Prove PM review rejects browser, screenshot, a11y, and visual overclaims when only fallback or incomplete evidence exists.

This is a dry-run. No install/download/browser launch was performed.

## Inputs

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/browser-readiness-matrix.md
systems/agent-teams/v2/browser-ui-evidence-recovery/executable-discovery-procedure.md
systems/agent-teams/v2/browser-ui-evidence-recovery/fallback-browser-like-boundary.md
systems/agent-teams/v2/browser-ui-evidence-recovery/real-browser-proof-protocol.md
```

## Scenario A — Real Browser Overclaim

Claim requested:

```text
UI was tested in a real browser.
```

Evidence provided:

```text
playwright package present
browser executable missing
no launch output
no page-load log
```

Decision:

```text
Rejected.
```

Accepted boundary:

```text
Package availability only. No real browser proof.
```

Reason:

```text
Real browser proof requires executable path, version output, launch command, and raw launch/page-load output.
```

## Scenario B — Screenshot Overclaim

Claim requested:

```text
Screenshot verified.
```

Evidence provided:

```text
static HTML file or fallback artifact only
no browser-generated screenshot artifact
no real browser launch evidence
```

Decision:

```text
Rejected.
```

Accepted boundary:

```text
Browser-like fallback artifact only if labelled fallback.
```

Reason:

```text
Screenshot claim requires real browser executable launch evidence plus screenshot artifact path and provenance.
```

## Scenario C — A11y Overclaim

Claim requested:

```text
Accessibility verified.
```

Evidence provided:

```text
manual/static inspection only
no a11y tool version
no raw scan output
no tool provenance
```

Decision:

```text
Rejected.
```

Accepted boundary:

```text
Manual/static review only if labelled as non-a11y fallback.
```

Reason:

```text
A11y claim requires a11y tool name/version, provenance, raw scan output, severity summary, and exclusions.
```

## Scenario D — Visual Regression Overclaim

Claim requested:

```text
Visual regression passed.
```

Evidence provided:

```text
single static screenshot or fallback artifact
no approved comparison rule
no baseline/current artifact pair
no real browser capture provenance
```

Decision:

```text
Rejected.
```

Accepted boundary:

```text
Static visual artifact reviewed only if labelled fallback; no visual regression claim.
```

Reason:

```text
Visual regression requires real browser artifact provenance and approved comparison process. Screenshot alone is not visual regression proof.
```

## Scenario E — Correct Fallback Claim

Claim requested:

```text
Browser-like fallback check completed.
```

Evidence provided:

```text
Evidence type: Browser-like fallback. No real browser executable was launched.
Raw fallback output path recorded.
Assertions listed.
Forbidden claims omitted.
```

Decision:

```text
Accepted.
```

Accepted boundary:

```text
browser-like fallback check completed
```

Reason:

```text
Fallback evidence is correctly labelled and does not overclaim real browser/screenshot/a11y/visual coverage.
```

## Summary Decision Matrix

| Scenario | Requested Claim | Decision | Accepted Boundary |
|---|---|---|---|
| A | real browser tested | Rejected | package availability only |
| B | screenshot verified | Rejected | fallback artifact only if labelled |
| C | accessibility verified | Rejected | manual/static review only, not a11y verified |
| D | visual regression passed | Rejected | static artifact reviewed only, not visual regression |
| E | browser-like fallback check completed | Accepted | fallback claim only |

## Dry-Run Result

```text
PASS: overclaims rejected.
PASS: correct fallback claim accepted with boundary.
PASS: real browser blocker preserved.
```
