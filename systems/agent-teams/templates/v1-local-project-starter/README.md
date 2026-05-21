# Agent-Teams v1 Local Project Starter Packet

## Purpose

Copy this starter packet when beginning a new small local-only Agent-Teams project.

## How To Use

1. Copy this folder into a new project example or project workspace.
2. Rename placeholders like `<project-name>`, `<feature-name>`, `<date>`, and `<owner>`.
3. Use `reports/starter-dry-run-checklist.md` to confirm Wave 1 docs have no leftover template placeholders.
4. Complete Wave 1 before implementation.
5. Run Wave 2 only after contract and ownership map are accepted.
6. Run Wave 3 for local integration evidence.
7. Run Wave 4 for PM acceptance and retrospective.

## Guardrails

```text
local-only by default
PM Agent orchestrator-only
contract-first before FE/BE parallel work
Wave 1 filled docs must not contain generic starter placeholders
preflight required for Local/Integration/Production
no silent dependency install
use `systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md` before any install/download need
use `systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md` before toolchain evidence claims
use `systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md` before accepting metadata/lockfile changes
no deploy/cloud/DNS/billing/secrets without explicit approval
no real browser/screenshot/a11y/visual claim without browser executable launch evidence
```

## Folder Map

```text
planning/
contracts/
task-packets/
reports/            # includes dry-run, verification, QA/review, acceptance skeletons
app/                # placeholder for implementation when approved
```


## CLI / Local-File Project Notes

Use these notes when the new project is a command-line tool or local-file workflow.

Recommended patterns:

```text
Use a project-specific local data path override for tests, e.g. <PROJECT_STORE_PATH>.
Keep tests isolated in temporary directories.
Use dependency-free test harnesses when possible.
Assert JSON output shape and stable error codes.
Cover happy path and negative/error paths.
Record exact local commands in reports/test.log and reports/build.log.
Do not claim concurrency safety, corruption recovery, packaging, or production readiness unless separately tested.
```

Example Wave 3 CLI/local-file scenarios:

```text
add/list/search/delete happy path
missing required flag
invalid URL or malformed input
unknown id / not found
unknown command / usage error
store path override works with isolated temp data
```

## Project Type Pack Add-on

For v2 work, select one primary pack during Wave 1 using:

```text
systems/agent-teams/v2/project-type-packs/pack-selection-runbook.md
```

Pack guidance is additive. It does not weaken v1/v2 guardrails.

## Wave Order

```text
Wave 1: planning / contract / ownership
Wave 2: implementation only
Wave 3: integration / QA / review
Wave 4: PM acceptance / retrospective
```
