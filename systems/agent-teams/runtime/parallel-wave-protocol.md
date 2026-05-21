# Parallel Wave Protocol

## Purpose

Define when and how PM Orchestrator may run multiple agents at the same time.

## Parallel Work Is Allowed When

```text
[ ] Tasks are independent
[ ] Inputs are stable enough
[ ] Ownership map exists
[ ] No shared write paths
[ ] No agent needs another agent's unfinished output
[ ] Integration owner is known
```

## Parallel Work Is Not Allowed When

- requirements are unclear
- architecture is still unstable
- API contract does not exist for FE/BE work
- agents would edit same files or same code region
- task output depends on another unfinished task
- project risk requires human decision first

## Wave Types

### Research/Review Wave

Safe parallel examples:

```text
Architecture Agent: propose architecture
Challenge Agent: critique assumptions
Security Agent: identify likely risk areas
```

### Planning Wave

Safe parallel examples:

```text
Frontend Agent: UI implementation plan
Backend Agent: backend implementation plan
QA Agent: test plan
```

Only after requirements + architecture + API contract exist.

### Execution Wave

Allowed only with strict ownership map.

Example:

```text
Frontend Agent owns src/app/products/**
Backend Agent owns src/app/api/products/** and prisma/**
QA Agent owns tests/products/**
```

## Wave Report

After a parallel wave, PM Orchestrator must create a wave summary:

```md
# Parallel Wave Summary

## Wave ID

## Agents Run

## Completed

## Blocked

## Conflicts

## Integration Notes

## Next Decision
```
