# Completion Evidence Policy

## Purpose

Prevent false “done” reports.

## Core Rule

No task is complete without evidence.

## Evidence Types

### File Evidence

- files created/changed/deleted
- diff summary
- paths match owned paths

### Command Evidence

- lint result
- test result
- build result
- script output

### Runtime Evidence

- app route checked
- API call checked
- screenshot if UI
- logs if service behavior matters

### Review Evidence

- checklist completed
- findings listed by severity
- accepted risks documented

## Minimum Evidence by Task Type

| Task Type | Minimum Evidence |
|---|---|
| Requirements | document path + acceptance checklist |
| Architecture | architecture doc path + tradeoff summary |
| API Contract | contract doc path + schema summary |
| Frontend | files changed + lint/build/test/manual UI check |
| Backend | files changed + test/API check/build |
| QA/Test | test plan/results + bug reports if any |
| Integration | full-app verification + conflict notes |
| Review | findings + severity + recommendation |
| Docs | docs path + coverage summary |

## PM Rejection Rule

PM Orchestrator must reject “done” when:

- no evidence is provided
- evidence does not match acceptance criteria
- verification failed but status says done
- files changed outside owned paths
- report hides blockers
