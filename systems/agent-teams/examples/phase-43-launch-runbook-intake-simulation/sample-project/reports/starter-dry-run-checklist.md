# Starter Dry-Run Checklist — local-bookmarks-cli-v1

## Purpose

Use this after copying `systems/agent-teams/templates/v1-local-project-starter/` into a new project.

Phase 43 uses this checklist to validate the Phase 42 launch runbook on a fake local project.

## Starter Packet Setup

- [x] Starter folder copied into project workspace.
- [x] Project folder renamed or placed at final planned path.
- [x] `app/.gitkeep` kept as placeholder until implementation approval.
- [x] No app source files created during Wave 1.
- [x] Starter content treated as scaffolding, not completed evidence.

## Placeholder Cleanup

Check filled Wave 1 docs for remaining generic placeholders.

Recommended command:

```sh
grep -R "<project-name>\|<feature-name>\|<date>\|<owner>\|<goal>\|<requirement>\|<capability>\|<behavior>\|<observable acceptance condition>\|<runtime" -n planning contracts task-packets/wave-1-planning-task.md reports/wave-1-verification-report.md
```

Expected result after Wave 1 fill:

```text
no matches in filled Wave 1 docs
```

Checklist:

- [x] `planning/intake-form.md` placeholders replaced.
- [x] `planning/requirements.md` placeholders replaced.
- [x] `planning/acceptance-criteria.md` placeholders replaced.
- [x] `planning/architecture.md` placeholders replaced.
- [x] `planning/ownership-map.md` placeholders replaced.
- [x] `contracts/feature-contract.md` placeholders replaced.
- [x] `task-packets/wave-1-planning-task.md` placeholders replaced.
- [x] `reports/wave-1-verification-report.md` placeholders replaced.

## Wave 1 Required Files

- [x] `planning/intake-form.md`
- [x] `planning/requirements.md`
- [x] `planning/acceptance-criteria.md`
- [x] `planning/architecture.md`
- [x] `planning/ownership-map.md`
- [x] `contracts/feature-contract.md`
- [x] `task-packets/wave-1-planning-task.md`
- [x] `reports/wave-1-verification-report.md`

## Wave 1 Evidence Boundary

Allowed claim:

```text
Wave 1 planning docs filled
starter dry-run complete
launch runbook flow simulated
```

Forbidden claim without later evidence:

```text
implemented
tested
working
production-ready
deployed
secure
performant
accessible
real browser tested
screenshot verified
visual regression passed
```

## Final Dry-Run Decision

```text
Pass
```

## Notes

```text
Phase 43 validated starter copy, Wave 1 fill, placeholder cleanup gate, and stop-before-Wave-2 behavior. No implementation created.
```
