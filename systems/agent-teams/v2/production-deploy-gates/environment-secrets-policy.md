# Phase 92 — Environment / Secrets Policy

## Purpose

Define how Agent-Teams documents environments and handles secrets before any production/deploy-like action.

This policy prevents leaking secret values, confusing target environments, and approving deploys without access boundaries.

## Scope

Applies to:

```text
local-like environments used for deploy rehearsal
staging / preview / production environments
cloud provider projects/accounts
DNS zones/domains
external services
CI/CD deploy contexts
secret stores and environment variables
```

Out of scope unless explicitly approved:

```text
creating secrets
rotating secrets
reading secret values
writing secrets to files
changing cloud/DNS/billing settings
running deploy commands
```

## Environment Inventory Template

```text
Environment ID:
Environment name:
Environment type: Local | Preview | Staging | Production | External Service | Other
Owner:
Purpose:
URL/resource identifier:
Cloud/provider account, no credentials:
Data sensitivity: Public | Internal | Confidential | Restricted
Deploy allowed: Yes / No / Approval Required
Approval packet link:
Rollback/backout link:
Post-deploy verification link:
Known blockers:
```

## Secret Inventory Template

Do not include secret values.

```text
Secret ID:
Secret purpose:
Environment:
Storage/reference location, no values:
Owner:
Needed for deploy: Yes / No
Access required by: human / CI/CD / service / agent: specify
Agent may view value: No
Agent may request user approval for use: Yes / No
Rotation needed: Yes / No / Unknown
Last rotation known: date / unknown
Notes without values:
```

## Secret Handling Rules

```text
Never paste secret values into docs, reports, prompts, chat, logs, screenshots, commits, or evidence artifacts.
Never commit `.env` files or credential files.
Never print secret values with shell commands.
Never ask agents to retrieve or reveal secret values.
Use secret references only: secret name, vault path, CI/CD variable name, or provider reference.
If secret value appears, stop work and treat as incident requiring user review.
```

## Agent Permissions Boundary

```text
PM Agent may record secret existence and required approval, not secret values.
Specialist agents may document expected secret references, not values.
DevOps/Deployment Agent may propose secret storage patterns, not create/use secrets without approval.
Review agents may flag secret exposure risk, not inspect values.
No agent may run secret-reading commands without explicit approval.
```

## Approval Requirements

Fresh explicit approval is required before:

```text
creating a secret
rotating a secret
using a secret in a deploy command
reading a secret value
printing environment variables that may include secrets
adding CI/CD secret variables
connecting external service credentials
```

Approval must specify:

```text
secret reference, no value
target environment
action: create | rotate | use | read | configure
time/scope boundary
who performs action
where evidence will be recorded without values
```

## Evidence Rules

Allowed evidence:

```text
secret reference name with value redacted
provider/vault path without sensitive value
screenshot with secret values hidden/redacted
CI/CD variable presence with value hidden
command output that does not include secret values
```

Forbidden evidence:

```text
raw secret value
unredacted `.env` file
full credential JSON/key/token
screenshots showing secret value
logs containing secret value
diff adding secret value
```

## Environment Confusion Guard

PM must confirm before deploy-like action:

```text
target environment name
target URL/resource
provider account/project
approval packet target matches command target
rollback target matches deploy target
post-deploy verification target matches deploy target
```

If target mismatch exists:

```text
Decision: Blocked
Action: update packet or request fresh approval
```

## Incident Trigger

Stop and ask user when:

```text
secret value appears in workspace/chat/log/report
unknown credential file appears
agent is asked to reveal a secret
approval target does not match deploy target
production environment is ambiguous
```

## PM Acceptance Rule

PM may accept environment/secrets readiness only when:

```text
environment inventory exists
secret inventory uses references only, no values
approval packet links environment/secrets review
no target mismatch exists
no secret values appear in artifacts
required approvals are explicit and scoped
```

PM must reject or mark Blocked when:

```text
secret values appear anywhere
environment target is ambiguous
approval target mismatches deploy target
secret action lacks explicit approval
secret handling owner missing
```
