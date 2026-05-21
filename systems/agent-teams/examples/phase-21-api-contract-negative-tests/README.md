# Phase 21 — API Contract + Negative HTTP Tests

## Purpose

Address Phase 20 findings before adding browser/database complexity.

## Scope

- Explicit local HTTP contract.
- Hardened dependency-free `node:http` server.
- Negative HTTP tests for malformed JSON and request body size.
- No deploy.

## Changes vs Phase 19

- Added `contracts/issue-http-contract.md`.
- Added max JSON body size guard.
- Malformed JSON returns `400`.
- Oversized JSON body returns `413`.
- Unknown server errors return generic `Internal server error`.
- Added negative tests.

## Final Result

Integration PASS for local pilot only. Not production-ready.
