# Ownership Map

## Purpose

Define write boundaries before multiple agents work in the same project.

## Project / Phase

`<project name / phase>`

## Global Read-Only Inputs

- `<path>`

## Ownership Table

| Agent | Task ID | Owned Paths | Forbidden Paths | Can Run Parallel? | Notes |
|---|---|---|---|---|---|
| Product/Requirements Agent | REQ-001 | `<paths>` | `<paths>` | No | Requirements first |
| Technical Architecture Agent | ARCH-001 | `<paths>` | `<paths>` | Conditional | After requirements |
| API Contract Agent | API-001 | `<paths>` | `<paths>` | Conditional | Before FE/BE parallel |
| Frontend Agent | FE-001 | `<paths>` | `<paths>` | Yes/No | Requires API contract |
| Backend Agent | BE-001 | `<paths>` | `<paths>` | Yes/No | Requires API contract |
| QA/Test Agent | QA-001 | `<paths>` | `<paths>` | Yes/No | May run after acceptance criteria |
| Integration Agent | INT-001 | `<paths>` | `<paths>` | No | Final coordination |

## Conflict Notes

- `<known file/path conflict or none>`

## Parallel Wave Decision

```text
Approved parallel wave: Yes/No
Reason:
```

## PM Approval

```text
Approved by:
Date:
Scope:
```
