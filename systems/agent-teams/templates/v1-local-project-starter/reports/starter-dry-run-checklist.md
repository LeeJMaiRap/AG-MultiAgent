# Starter Dry-Run Checklist — <project-name>

## Purpose

Use this after copying `systems/agent-teams/templates/v1-local-project-starter/` into a new project.

The starter is scaffolding only. This checklist proves the copied starter was filled enough for Wave 1 planning without accidentally treating template placeholders as evidence.

## Starter Packet Setup

- [ ] Starter folder copied into project workspace.
- [ ] Project folder renamed or placed at final planned path.
- [ ] `app/.gitkeep` kept as placeholder until implementation approval.
- [ ] No app source files created during Wave 1 unless explicitly approved.
- [ ] Starter content treated as scaffolding, not completed evidence.

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

- [ ] `planning/intake-form.md` placeholders replaced.
- [ ] `planning/requirements.md` placeholders replaced.
- [ ] `planning/acceptance-criteria.md` placeholders replaced.
- [ ] `planning/architecture.md` placeholders replaced.
- [ ] `planning/ownership-map.md` placeholders replaced.
- [ ] `contracts/feature-contract.md` placeholders replaced.
- [ ] `task-packets/wave-1-planning-task.md` placeholders replaced.
- [ ] `reports/wave-1-verification-report.md` placeholders replaced.

## Wave 1 Required Files

- [ ] `planning/intake-form.md`
- [ ] `planning/requirements.md`
- [ ] `planning/acceptance-criteria.md`
- [ ] `planning/architecture.md`
- [ ] `planning/ownership-map.md`
- [ ] `contracts/feature-contract.md`
- [ ] `task-packets/wave-1-planning-task.md`
- [ ] `reports/wave-1-verification-report.md`

## Wave 1 Evidence Boundary

Allowed claim:

```text
Wave 1 planning docs filled
starter dry-run complete
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
Pass | Needs placeholder cleanup | Blocked
```

## Notes

```text
<notes>
```
