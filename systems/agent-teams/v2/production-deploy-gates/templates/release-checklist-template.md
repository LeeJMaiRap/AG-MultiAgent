# Release Checklist Template

## Purpose

Confirm all required evidence, approvals, owners, and stop conditions before release/deploy approval.

This checklist does not authorize deploy by itself. Deploy-like action still requires explicit user approval in a deploy approval packet.

## Release Metadata

```text
Release ID:
Project:
Version / change set:
Target environment:
Release owner:
PM owner:
Date:
Verification level target: Production | Integration | Local | Simulated | Paper
Deploy approval packet:
Rollback/backout plan:
Post-deploy verification plan:
```

## Approval Gate

```text
[ ] Deploy approval packet exists.
[ ] Approval status is Approved, not Draft/Requested/Expired/Blocked.
[ ] Approval target matches release target.
[ ] Approval exact action matches planned action.
[ ] Approval scope has not changed.
[ ] Approval window is still valid.
[ ] No deploy-like action outside approval scope is included.
```

## Scope And Requirements Gate

```text
[ ] Requirements/acceptance criteria linked.
[ ] Release scope is explicit.
[ ] Out-of-scope changes listed.
[ ] User-visible changes summarized.
[ ] Known limitations documented.
[ ] PM acceptance dashboard/evidence index updated.
```

## Track 1 — Dependency / Toolchain Gate

```text
[ ] Dependency/toolchain preflight complete when applicable.
[ ] No silent install/download.
[ ] Package/lockfile changes reviewed when applicable.
[ ] Install provenance recorded when applicable.
[ ] Fresh approval exists for dependency/tooling install if needed.
```

## Track 2 — Project Type Pack Gate

```text
[ ] Project type pack selected or not applicable.
[ ] Pack boundaries preserved.
[ ] Required pack artifacts present.
[ ] Deviations documented.
```

## Track 3 — Security / Performance Gate

```text
[ ] Security evidence matrix completed when security claim exists.
[ ] Performance evidence matrix completed when performance claim exists.
[ ] Risk severity assessed.
[ ] High risk has required owner/PM/specialist sign-off when eligible.
[ ] Critical risk absent or mitigated; not accepted.
```

## Track 4 — Browser / UI Gate

```text
[ ] Browser/UI claim type declared: real browser | fallback browser-like | none.
[ ] Real browser claim has executable launch evidence and artifacts.
[ ] Screenshot/a11y/visual claim has real browser evidence.
[ ] Fallback is labelled fallback and not overclaimed.
[ ] Known browser blockers documented.
```

## Track 5 — Multi-Agent Execution Quality Gate

```text
[ ] Specialist reports exist.
[ ] Accepted claims link evidence index rows.
[ ] Verification level matches evidence.
[ ] Ownership conflicts resolved or sequenced.
[ ] Handoffs meet quality threshold.
[ ] PM acceptance dashboard is complete.
```

## Track 6 — Production / Deploy Gate

```text
[ ] Environment inventory complete.
[ ] Secret inventory uses references only, no values.
[ ] Rollback/backout plan complete.
[ ] Post-deploy verification plan complete.
[ ] Release checklist complete.
[ ] Production/deploy claim boundary explicit.
[ ] No cloud/DNS/billing/secrets action without explicit approval.
```

## Environment / Secrets Gate

```text
[ ] Target environment confirmed.
[ ] Target URL/resource confirmed.
[ ] Provider account/project confirmed, no credentials.
[ ] Secret values absent from all artifacts.
[ ] Secret references only.
[ ] Fresh explicit approval exists for any secret create/rotate/use/read action.
[ ] No `.env` or credential file committed.
```

## Rollback / Backout Gate

```text
[ ] Rollback owner assigned.
[ ] Rollback target matches release target.
[ ] Rollback trigger conditions defined.
[ ] Rollback steps explicit.
[ ] Rollback verification defined.
[ ] Data safety assessed.
[ ] Secret safety assessed.
[ ] Failure escalation exists.
```

## Post-Deploy Verification Gate

```text
[ ] Verification owner assigned.
[ ] Checks/commands listed.
[ ] Success signals defined.
[ ] Failure signals defined.
[ ] Evidence artifacts and paths defined.
[ ] Verification window defined.
```

## Communication Gate

```text
[ ] Release owner identified.
[ ] Incident/escalation owner identified.
[ ] User/customer communication owner identified if needed.
[ ] Maintenance window or expected impact documented if needed.
```

## Stop Conditions

Stop and ask user when:

```text
approval missing or expired
approval target/action mismatch
secret value appears anywhere
rollback/backout missing or vague
post-deploy verification missing
target environment ambiguous
Critical risk present
unapproved cloud/DNS/billing/secrets action requested
production claim lacks evidence bundle
```

## PM Release Decision

```text
Decision: Approved | Rejected | Blocked | Needs Review
Decision rationale:
Release approved for exact target/action:
Release not approved for:
Required follow-up:
```
