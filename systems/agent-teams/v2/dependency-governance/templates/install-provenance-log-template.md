# Install Provenance Log

## Purpose

Record every approved dependency/toolchain install or download.

No install/download should appear here unless it was approved first.

## Log Entries

### Entry Template

```text
Entry ID: <YYYYMMDD-project-short-name-install-001>
Request ID: <dependency-request-id>
Project / Phase: <project-or-phase>
Approver: <name-or-agent>
Executor: <name-or-agent>
Date/time: <YYYY-MM-DD HH:MM TZ>
Working directory: <path>
Exact command: <command>
Source registry/url: <registry-or-url>
Package/tool/version: <name/version>
Risk level: Low | Medium | High | Critical
Files changed: <paths>
Lockfile changed: Yes | No | N/A
Command log path: <path>
Version check command/result: <command/result>
Verification command/result: <command/result>
Rollback/removal notes: <notes>
Final status: Installed | Failed | Rolled Back | Blocked
```

## Claim Boundary Reminder

```text
Package installed != feature verified
Tool available != tests passed
Browser package installed != browser proof
Dependency approval != production approval
```
