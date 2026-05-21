# Claim Adjustment — Dry Run Dependency Approval

## Original Desired Claim

```text
Project can use Vitest for CLI test execution.
```

## Evidence Available

```text
dependency request: available
risk review: available
PM decision: fallback approved
install execution: not performed
package metadata diff: none
lockfile diff: none
version check: not performed
npm test with Vitest: not performed
```

## Adjusted Claim

```text
Agent-Teams v2 dependency governance can process a dependency request and choose a no-install fallback in dry-run mode.
```

## Allowed Claims

```text
Dependency request flow simulated.
Risk review simulated.
PM approval gate simulated.
Fallback approval documented.
No-install scope preserved.
```

## Rejected Claims

```text
Vitest installed.
Vitest usable in project.
Vitest tests passed.
Lockfile/provenance install evidence exists.
Integration verification with Vitest exists.
```

## Verification Level

```text
Simulated
```
