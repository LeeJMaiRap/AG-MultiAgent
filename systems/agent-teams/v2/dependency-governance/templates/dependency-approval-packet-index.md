# Dependency Approval Packet Index

Use this packet when any task needs an install/download/toolchain change.

## Packet Files

```text
dependency-approval-request-template.md
dependency-risk-review-template.md
install-provenance-log-template.md
```

## Flow

```text
1. Worker/PM fills dependency approval request.
2. PM or reviewer fills dependency risk review.
3. User approval is required for High/Critical risk or any install command that needs explicit user approval.
4. Only after approval, executor runs exact command.
5. Executor records command output and changed files.
6. Executor updates install provenance log.
7. PM accepts/rejects resulting evidence and claim boundary.
```

## Stop Conditions

Stop and ask before:

```text
any npm/pip/system/browser install
any package manager switch
any generated lockfile outside approved scope
any credentialed CLI
any cloud/DNS/billing/secrets/deploy tool
any destructive migration tool
```

## Minimum Decision Outcomes

```text
Approved
Rejected
Needs More Info
Fallback Approved
Blocked
```
