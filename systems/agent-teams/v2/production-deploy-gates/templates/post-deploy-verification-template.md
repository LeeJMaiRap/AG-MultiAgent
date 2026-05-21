# Post-Deploy Verification Template

## Purpose

Define exact verification checks, owners, expected signals, and evidence artifacts after an approved deploy-like action.

A deploy is not release-ready unless post-deploy verification is planned before approval and executed after approved deploy.

## Verification Metadata

```text
Verification ID:
Project / release:
Related deploy approval packet:
Related release checklist:
Related rollback/backout plan:
Target environment:
Verification owner:
PM owner:
Verification status: Planned | Running | Passed | Failed | Blocked | Not Run
Verification window:
```

## Target Confirmation

```text
Expected environment:
Actual environment checked:
Expected URL/resource:
Actual URL/resource checked:
Provider account/project, no credentials:
Target matches approval packet: Yes / No
Target matches release checklist: Yes / No
```

If target mismatch exists:

```text
Decision: Failed / Blocked
Action: stop, do not claim post-deploy verified, consider rollback/backout
```

## Verification Preconditions

```text
[ ] Deploy action completed under explicit approval.
[ ] Release checklist exists.
[ ] Rollback/backout plan exists.
[ ] Environment/secrets policy followed.
[ ] No secret values in evidence.
[ ] Verification owner available.
[ ] Rollback owner reachable during verification window.
```

## Smoke Checks

```text
Check ID:
Owner:
Command/action:
Expected result:
Actual result:
Status: Pass | Fail | Blocked | Not Run
Evidence path/log:
```

Recommended smoke check categories:

```text
service/process health
primary endpoint or command
critical user path
configuration sanity
version/build identifier
basic data read/write only if approved
```

## Functional Acceptance Checks

```text
Acceptance criterion:
Verification method:
Expected result:
Actual result:
Status: Pass | Fail | Blocked | Not Run
Evidence path/log:
```

## Security Checks

Only claim security verification when Track 3 evidence supports it.

```text
Security check:
Required evidence:
Expected result:
Actual result:
Status: Pass | Fail | Blocked | Not Run | Not Applicable
Evidence path/log:
```

Examples:

```text
no secret values exposed in logs/artifacts
expected auth/access control behavior
HTTPS/TLS endpoint where applicable
known High/Critical risks unchanged or mitigated
```

## Performance Checks

Only claim performance verification when Track 3 evidence supports it.

```text
Performance check:
Required evidence:
Expected threshold:
Actual result:
Status: Pass | Fail | Blocked | Not Run | Not Applicable
Evidence path/log:
```

## Browser / UI Checks

Only claim real browser/screenshot/a11y/visual proof when Track 4 real browser evidence exists.

```text
UI check type: real browser | fallback browser-like | none
Executable launch evidence path:
Screenshot/a11y/visual artifact path:
Fallback labelled: Yes / No / Not Applicable
Status: Pass | Fail | Blocked | Not Run | Not Applicable
```

## Monitoring / Logs

```text
Monitoring source:
Time window checked:
Expected signal:
Actual signal:
Errors observed:
Alert status:
Evidence path/log:
```

Do not include secret values in logs or copied output.

## Rollback Trigger Review

```text
Rollback trigger condition:
Observed: Yes / No
Severity:
Decision: continue monitoring | rollback | block | ask user
Decision owner:
Evidence path/log:
```

## Incident / Escalation

```text
Incident needed: Yes / No
Escalation owner:
User/customer communication needed: Yes / No
Summary:
Follow-up owner:
```

## Final Verification Decision

```text
Decision: Passed | Failed | Blocked | Not Run
Decision rationale:
Accepted claim boundary:
Rejected/blocked claims:
Evidence index row(s):
PM acceptance dashboard link:
Follow-up tasks:
```

## Claim Rules

```text
Do not claim post-deploy verified unless actual approved deploy occurred and verification passed.
Do not claim production-ready from planned verification only.
Do not claim security/performance/browser proof without matching Track 3/4 evidence.
Do not include secret values in evidence.
Failed or blocked verification must trigger rollback review or explicit user decision.
```
