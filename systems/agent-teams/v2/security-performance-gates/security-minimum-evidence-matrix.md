# Phase 67 Option A — Security Minimum Evidence Matrix

## Purpose

Define minimum evidence before Agent-Teams may claim any security review, security hardening, or security readiness.

This matrix prevents security overclaims. If required evidence is missing, downgrade claim or mark Blocked / Needs Review.

## Claim Boundary Rule

```text
No security evidence -> no security claim.
Paper review -> design/risk review claim only.
Simulated review -> dry-run claim only.
Local evidence -> local-only security claim only.
Integration evidence -> cross-component security claim only.
Production security readiness -> blocked until Production / Deploy Gates exist and approve scope.
```

## Required Security Review Record

Every security review must record:

```text
review id
requested claim
Verification Level
project type pack
reviewed files/paths
threat/risk categories reviewed
findings table
severity per finding
mitigation/acceptance decision
unsupported claims
evidence source
reviewer role
PM acceptance boundary
```

## Evidence Matrix

| Security claim | Minimum evidence | Required reviewer | Minimum Verification Level | Must include | Unsupported without extra gates |
|---|---|---|---|---|---|
| Security reviewed | checklist over in-scope paths and findings table | Security Review Agent | Paper | scope, reviewed paths, findings, unsupported claims | secure, hardened, production-ready |
| Basic input validation reviewed | input boundary list plus positive/negative validation evidence or design review | Security Review Agent + QA/Test Agent when tests exist | Paper for design, Local for runtime claim | accepted/rejected inputs, error behavior, abuse cases | complete validation, injection safe |
| Error handling reviewed | error paths reviewed for leak/raw stack/internal details | Security Review Agent | Paper or Local | error classes, user-facing messages, log boundary | no information leakage globally |
| Auth/access control reviewed | auth model, roles, protected actions, bypass cases | Security Review Agent + Architecture/API Contract Agent | Paper or Integration | actor matrix, permission checks, negative cases | production auth readiness |
| Secret handling reviewed | secret inventory and no-secret-in-repo/path review | Security Review Agent + DevOps/Deployment Agent when env involved | Paper or Local | secret sources, storage, logs, config paths | safe production secrets |
| Dependency/toolchain risk reviewed | Track 1 approval packet or no-dependency statement | Security Review Agent | Paper | package/tool identity, install/provenance/lockfile impact, fallback | dependency safe, supply-chain safe |
| Data storage/file permission reviewed | storage paths, file modes, data sensitivity, corruption/loss risks | Security Review Agent + Backend/Architecture Agent | Paper or Local | local path boundary, permission assumptions, backup/recovery limits | production data safety |
| Network exposure reviewed | bound interfaces, ports, CORS/origin policy, public exposure risk | Security Review Agent + Backend/DevOps Agent | Paper or Integration | localhost/public boundary, route list, exposure decision | internet-safe service |
| Unsafe eval/command execution reviewed | scan/review for eval, shell exec, dynamic imports, command construction | Security Review Agent + Code Review Agent | Paper or Local | call sites, input sources, escaping/allowlist decision | command-injection safe globally |
| Destructive action reviewed | destructive commands/actions and confirmation/rollback expectations | Security Review Agent + PM Agent | Paper | destructive list, safeguards, rollback or recovery | destructive-safe production ops |
| Logging/privacy leakage reviewed | logs/reports/errors reviewed for secrets/PII/internal paths | Security Review Agent + Documentation Agent | Paper or Local | log locations, sample outputs, redaction needs | privacy compliant |
| Local-only security reviewed | all relevant local categories reviewed with explicit non-production boundary | Security Review Agent | Local if runtime evidence, Paper if docs only | local threat model, unsupported production claims | production security readiness |
| Production security readiness | full evidence matrix plus deploy/environment/secrets/rollback gates | Security Review Agent + DevOps/Deployment Agent + PM Agent | Production | approved production scope, environment proof, risk acceptance | blocked until Production / Deploy Gates |

## Required Findings Table

Use this format in security reports:

| ID | Category | Severity | Finding | Evidence | Recommendation | Decision | Claim impact |
|---|---|---|---|---|---|---|---|
| SEC-001 | input validation | Medium | example | file/path or command output | fix or accept | Open / Mitigated / Accepted | blocks / downgrades / no impact |

## Severity Use

Until Phase 69 rubric exists, use provisional severity labels:

```text
Critical
High
Medium
Low
Info
```

Rules:

```text
Critical blocks acceptance.
High blocks security claim unless explicitly accepted by owner/PM and claim is not production-ready.
Medium can pass controlled local pilot only with mitigation or accepted residual risk.
Low/Info must be recorded.
```

## Evidence Source Rules

Allowed evidence sources:

```text
file review excerpts
contract review
architecture notes
real command output
local test output
integration test output
approved dependency packet
approved preflight result
```

Not enough by itself:

```text
assistant assertion without reviewed paths
package presence without provenance
browser-like fallback for real browser/a11y/security scan claim
untested checklist marked pass
production safety based on local-only review
```

## Claim Downgrade Rules

```text
If no reviewed files/paths -> downgrade to No security claim.
If only paper review -> claim Security reviewed at Paper level only.
If no negative tests for runtime validation -> do not claim validation enforced.
If auth not implemented -> record auth/access control as Not Applicable or Missing; do not claim auth security.
If dependency install not approved -> do not claim dependency risk accepted.
If secrets are not in scope -> do not claim secret handling complete.
If network exposure is localhost-only -> do not claim public exposure safety.
If any Critical finding remains open -> acceptance blocked.
```

## Pack-Specific Security Notes

### CLI / Local-File

Required focus:

```text
file path traversal
store permissions assumptions
malformed local data
unsafe shell execution
stdout/stderr privacy leakage
destructive delete/update actions
```

### HTTP API

Required focus:

```text
request validation
malformed JSON
body size limit
auth/access control if present
error response leakage
CORS/origin/network exposure
```

### Static UI

Required focus:

```text
DOM injection/XSS risks
unsafe localStorage/sessionStorage use
external script/link provenance
form input handling
browser proof boundary
```

### Fullstack Local

Required focus:

```text
API contract mismatch
UI-to-API input trust boundary
local server exposure
shared error handling
cross-component data leakage
```

### Docs-Only / Project-Management

Required focus:

```text
secrets/PII in docs
private links or tokens
unsafe operational instructions
overclaiming implementation/security readiness
```

## Stop Conditions

Stop and ask before:

```text
claiming secure/hardened/production-ready without matrix evidence
accepting Critical finding
accepting High finding without explicit owner/PM decision
running security tools that require install/download without Track 1 approval
running destructive/security-sensitive tests
using secrets, cloud, DNS, billing, deploy, or public exposure path
```
