# Wave 2 Task Packet — Implementation Only

## Task ID

`W2-001`

## Assigned Agents

```text
Backend Agent
Frontend Agent if UI exists
```

## Objective

Implement scoped code according to accepted Wave 1 contract and ownership map.

## Inputs

```text
planning/requirements.md
planning/acceptance-criteria.md
planning/architecture.md
contracts/feature-contract.md
planning/ownership-map.md
```

## Owned Paths

```text
app/src/**
app/package.json if needed and approved by scope
reports/preflight.log
reports/build-or-syntax.log
reports/implementation-report.md
```

## Forbidden Paths

```text
contracts/** unless PM/user approves contract change
systems/pm-agent/**
systems/agent-teams/runtime/**
systems/agent-teams/templates/**
```

## Verification Level

`Local`

## Preflight Required

- runtime version check
- package manager version check when relevant
- required command/tool checks
- dependency install policy
- fallback/blocker rule if missing

## Acceptance Criteria

- [ ] Preflight logged.
- [ ] Implementation follows contract.
- [ ] Build/syntax check passes or blocker documented.
- [ ] No unapproved install/download/deploy.
- [ ] No Integration claim unless Wave 3 tests run.

## Return Format

Create `reports/implementation-report.md` with evidence paths.
