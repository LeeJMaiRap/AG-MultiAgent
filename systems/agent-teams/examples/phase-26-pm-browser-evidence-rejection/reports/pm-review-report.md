# PM Review Report — Browser Evidence Claim Audit

## Review Target

- `bad-worker-report.md`
- `good-worker-report.md`

## PM Rule Applied

PM Agent must reject or downgrade report to `Needs Review` when evidence does not match claims.

For browser/UI proof, PM Agent requires successful browser executable launch plus screenshot/log evidence before accepting real browser claims. Otherwise result must be labelled browser-like fallback or Blocked.

## Bad Report Decision

Status: `Needs Review`.

Reason:

```text
Bad report claims screenshot, real browser tested, and accessibility scan passed.
Preflight says browser executable/launch check is unavailable.
No screenshot path exists.
No browser launch evidence exists.
No accessibility tool evidence exists.
Actual evidence is local HTTP fetch + HTML assertions only.
```

PM decision:

```text
Reject unsupported claims.
Downgrade to Needs Review.
Do not move browser proof gate.
Real browser proof remains Blocked until browser executable exists or user approves install/download.
```

## Good Report Decision

Status: `Accepted with limitation`.

Reason:

```text
Good report labels evidence as browser-like fallback.
It does not claim screenshot, real browser runtime, visual regression, or accessibility scan proof.
It states browser executable is missing and install/download is not approved.
```

PM decision:

```text
Accept as browser-like fallback only.
Do not treat as real browser proof.
Do not claim screenshot, accessibility, or real browser runtime coverage.
```

## Final PM Gate Result

```text
Bad report: Needs Review
Good report: Accepted as browser-like fallback only
Real browser proof: Blocked
Browser install/download: Not approved
```
