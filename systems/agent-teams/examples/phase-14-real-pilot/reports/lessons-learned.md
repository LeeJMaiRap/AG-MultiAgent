# Phase 14 Lessons Learned

## Worked

```text
- Verification Level forced real command evidence.
- Local test/build caught concrete implementation issues.
- Strict owned paths kept PM Agent and templates untouched.
- No-deploy boundary held.
```

## Found

```text
- Assuming TypeScript compiler exists was wrong.
- Dependency-free pilot is safer for first real validation.
- Evidence logs are useful and should be committed for pilot traceability.
```

## Recommendation

Phase 15 should either:

```text
A. Expand real pilot to tiny UI/API with local-only checks.
B. Harden runtime protocol to require a preflight tool/dependency check before real implementation tasks.
```
