# Quality Gates

## Purpose

Prevent low-quality or incomplete work from moving forward.

## Gate List

```text
1. Requirement Gate
2. Architecture Gate
3. API Contract Gate
4. Planning Gate
5. Preflight Gate
6. Implementation Gate
7. Integration Gate
8. QA Gate
9. Review Gate
10. Handoff Gate
```

## 1. Requirement Gate

Pass when:

- goal is clear
- scope and out-of-scope are documented
- acceptance criteria exist
- unknowns are resolved or tracked

## 2. Architecture Gate

Pass when:

- stack and architecture are justified
- module boundaries exist
- data flow is clear
- solution is not overcomplicated

## 3. API Contract Gate

Pass when:

- FE/BE contract exists
- request/response/error schemas are clear
- auth rules are clear
- contract change process exists

## 4. Planning Gate

Pass when:

- tasks have owners
- dependencies are known
- owned/forbidden paths are defined
- verification exists for each task
- parallel plan has no ownership conflicts

## 5. Preflight Gate

Pass when:

- task Verification Level is Paper/Simulated, or preflight is explicitly not needed
- required tools/dependencies/commands are checked for Local/Integration/Production tasks
- dependency install and network policy are clear
- missing tool fallback is approved or blocker is documented
- browser/UI tasks distinguish package availability from executable launch readiness
- browser install/download approval is captured before any external download or system/package install
- preflight evidence is captured in the report

## 6. Implementation Gate

Pass when:

- preflight passed or blocker is accepted
- agent reports include evidence
- changed files stay inside owned paths
- acceptance criteria are met or blockers documented

## 7. Integration Gate

Pass when:

- parts work together
- env/config issues are resolved or documented
- full-app verification ran where applicable
- browser/UI integration claims are backed by matching evidence: real browser launch/screenshot for real browser claims, or clearly labeled browser-like fallback evidence

## 8. QA Gate

Pass when:

- acceptance criteria verified
- tests/manual checks run
- bugs are reported with reproduction steps

## 9. Review Gate

Pass when:

- security/performance/code review findings are handled or accepted as known risk

## 10. Handoff Gate

Pass when:

- setup/run/deploy docs exist where needed
- known issues documented
- rollback path documented
- user receives concise summary
