# Intake Form — local-bookmarks-cli-v1

## Project Name

`local-bookmarks-cli-v1`

## Goal

Create a dependency-free local CLI for adding, listing, searching, and deleting bookmarks stored in a local JSON file.

## User / Operator

Local developer/operator using terminal on this machine.

## In Scope

- Add bookmark with title and URL.
- List saved bookmarks.
- Search bookmarks by title or URL substring.
- Delete bookmark by id.
- Store bookmarks in a local JSON file under the project folder.
- Provide local command examples and integration test plan.

## Out of Scope

- Browser extension.
- Web UI.
- Cloud sync.
- Authentication.
- Real secrets.
- Production deployment.
- Browser automation, screenshots, accessibility, or visual proof.

## Verification Level Target

`Integration`

Recommended for v1 local project:

```text
Integration
```

## Constraints

```text
local-only
no real secrets
no cloud/DNS/billing
no deploy
no dependency install unless approved
Node.js dependency-free preferred
Wave 2 implementation requires user approval after Wave 1
```

## Approval Gates

- [x] Implementation start approval required after Wave 1.
- [x] Dependency install approval required if needed.
- [x] Browser binary install/download approval required if needed.
- [x] Deploy/production work approval required separately if ever in scope.

## Rollback Point

```text
Repository commit before Phase 43: b87712d
```
