# Agent Registry

## Purpose

Track available Agent-Teams roles, their scope, activation rules, and current implementation status.

This registry is the PM Orchestrator's first lookup before delegating work.

## Status Values

```text
planned       = role approved but not implemented
draft         = initial spec exists
active        = ready for PM Orchestrator delegation
on-demand     = used only when project risk/need triggers it
retired       = no longer used
```

## Core Agents

| Agent | Status | Use When | Owns | Must Not Do |
|---|---|---|---|---|
| PM Orchestrator | planned | any Agent-Teams project | planning, delegation, monitoring, quality gates, user reporting | implement FE/BE/QA directly |
| Product/Requirements Agent | planned | requirements unclear or new project starts | PRD, user stories, acceptance criteria, question backlog | choose technical architecture alone |
| Technical Architecture Agent | planned | architecture/stack/module choices needed | architecture proposal, ADRs, boundaries, data flow | implement features |
| API Contract Agent | planned | FE/BE integration needed | endpoints, schemas, errors, auth rules, contract change control | implement FE/BE |
| Frontend Agent | planned | UI implementation needed | frontend files, components, pages, states, accessibility | change backend/database without task scope |
| Backend Agent | planned | API/data/business logic needed | backend files, database schema, validation, auth/authz | change frontend UI without task scope |
| QA/Test Agent | planned | acceptance verification needed | test plans, e2e/API tests, bug reports | mark work done without evidence |
| Integration Agent | planned | multiple parts must work together | integration checks, env wiring, merge notes, full-app verification | change product scope |

## On-Demand Agents

| Agent | Status | Trigger | Owns |
|---|---|---|---|
| UX/Design Agent | planned | UI/UX quality matters | user flows, screen maps, design direction |
| Security Review Agent | planned | auth/data/payment/upload/public API risk | security checklist, findings, mitigation advice |
| Performance Review Agent | planned | load time/query/bundle/scale risk | performance findings, optimization advice |
| Code Review Agent | planned | pre-merge or quality concern | maintainability review, code smell, test gaps |
| DevOps/Deployment Agent | planned | deployment/CI/Docker/env needed | deploy plan, env guide, rollback path |
| Documentation Agent | planned | handoff/user docs/API docs needed | README, setup guide, docs |
| Challenge Agent | planned | assumptions need stress test | risks, edge cases, counterarguments |

## Delegation Rule

PM Orchestrator may delegate only when:

1. target agent exists in this registry
2. task has objective and success criteria
3. owned paths and forbidden paths are defined
4. required inputs exist or are explicitly missing as blockers
5. report format is specified
