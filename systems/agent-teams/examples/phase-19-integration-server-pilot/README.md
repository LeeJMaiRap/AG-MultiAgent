# Phase 19 — Integration Server Pilot

## Purpose

Raise Phase 18 local API/UI pilot from `Local` to `Integration` by verifying real HTTP routes against a dependency-free local server.

## Scope

- Dependency-free `node:http` server.
- `GET /api/issues`.
- `POST /api/issues`.
- `GET /issues` HTML route.
- Integration tests using built-in `fetch` and ephemeral local port.
- No deploy.

## Verification Level

Integration.

## Commands

Run inside `app/`:

```text
npm test
npm run build
```

## Evidence

```text
reports/preflight.log
reports/npm-test.log
reports/npm-build.log
reports/agent-report.md
reports/verification-report.md
```
