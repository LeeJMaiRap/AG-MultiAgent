# Phase 26 — PM Browser Evidence Rejection Simulation

## Purpose

Validate that PM Agent applies Phase 25 browser evidence rules during report review.

## Scope

Paper simulation only.

No browser install, no browser download, no app code changes, no runtime automation.

## Scenario

A browser/UI worker submits two reports:

1. Bad report: claims `screenshot`, `real browser tested`, and `accessibility scan passed`, but evidence only shows browser-like fallback.
2. Good report: correctly labels the same evidence as browser-like fallback and avoids real browser claims.

PM Agent must reject or downgrade the bad report to `Needs Review`, and may accept the good report only as lower-evidence fallback.

## Expected PM Decision

```text
Bad report -> Needs Review
Good report -> Accepted as browser-like fallback, not real browser proof
```
