# Cutover Decision — Agent-Teams v1 local pilot

## Decision

Accept local pilot and keep Agent-Teams v1 ready for controlled local real-project use.

## Decision Type

```text
Accept local pilot
```

## What This Means

Agent-Teams v1 is accepted for:

```text
small local-only projects
contract-first delivery
dependency-free or preflight-cleared stacks
Integration verification with real local commands
strict evidence claim boundaries
```

Agent-Teams v1 is not accepted for:

```text
production deployment without new approval gates
browser screenshot/a11y/visual claims while browser executable remains blocked
cloud/DNS/billing/secrets tasks without explicit approval
projects needing persistence/auth/security hardening unless scoped separately
```

## Entry Criteria Met

- Requirements and acceptance criteria existed before implementation.
- API contract existed before Backend/Frontend implementation.
- Ownership map existed before Wave 2.
- Implementation followed frozen contract.
- Integration tests passed locally.
- Build/syntax check passed.
- Challenge review rejected overclaims.

## Exit Criteria

- Phase 35 PM acceptance artifacts committed.
- Local pilot status documented as accepted.
- Remaining blockers documented.
- Next-phase recommendation documented.
