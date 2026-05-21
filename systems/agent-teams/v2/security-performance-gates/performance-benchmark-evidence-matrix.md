# Phase 68 — Performance Benchmark Evidence Matrix

## Purpose

Define minimum evidence before Agent-Teams may claim performance reviewed, benchmarked, optimized, or production-performance ready.

This matrix prevents performance overclaims. If benchmark evidence is missing, downgrade claim or mark Blocked / Needs Review.

## Claim Boundary Rule

```text
No benchmark evidence -> no performance claim.
Paper review -> design/performance-risk review only.
Simulated review -> dry-run benchmark plan only.
Local command output -> local benchmark claim only.
Integration command output -> cross-component benchmark claim only.
Production performance readiness -> blocked until Production / Deploy Gates exist and approve scope.
```

## Required Benchmark Record

Every performance review must record:

```text
benchmark id
requested claim
Verification Level
project type pack
benchmark target
metric name
unit
environment/toolchain
command executed
sample size / iteration count
raw result
threshold or baseline
pass/fail decision
variance notes
resource side effects
unsupported claims
reviewer role
PM acceptance boundary
```

## Evidence Matrix

| Performance claim | Minimum evidence | Required reviewer | Minimum Verification Level | Must include | Unsupported without extra gates |
|---|---|---|---|---|---|
| Performance reviewed | checklist over performance-sensitive paths and risk notes | Performance Review Agent | Paper | reviewed paths, bottleneck hypotheses, unsupported claims | benchmarked, optimized, production-ready |
| Local smoke benchmarked | one safe local command with raw timing/output | Performance Review Agent + QA/Test Agent when tests exist | Local | command, environment, result, threshold/baseline | throughput, load, production performance |
| Startup time measured | repeatable command that starts app/CLI/server and records time | Performance Review Agent | Local | iterations, timing method, raw values, variance note | cold-start guarantee across machines |
| Operation latency measured | command/test measuring specific operation response time | Performance Review Agent + owning specialist | Local or Integration | operation name, inputs, result distribution, threshold | global latency guarantee |
| Throughput measured | safe request/operation count over bounded time/sample | Performance Review Agent | Integration for cross-component claim | concurrency level, duration, total ops, errors | load-test claim, production throughput |
| Memory usage measured | tool/command output showing memory during target operation | Performance Review Agent | Local | measurement method, peak/steady value, sample input | memory-safe under all loads |
| File/data volume behavior measured | benchmark across defined local dataset sizes | Performance Review Agent + Backend/Architecture Agent | Local | data sizes, operation results, trend notes | scalability claim beyond tested range |
| Concurrency behavior measured | bounded local/integration test with explicit concurrency level | Performance Review Agent + QA/Test Agent | Integration for server/app claim | concurrency count, error rate, resource cleanup | race-free, corruption-free unless dedicated tests pass |
| Regression compared | before/after or baseline comparison with same command/env | Performance Review Agent | Local or Integration | baseline, current result, delta, threshold | long-term trend guarantee |
| Resource cleanup measured | command/test shows handles/files/server cleanup after run | Performance Review Agent + Integration Agent | Local or Integration | cleanup check, temp paths, open server/process status | leak-free production claim |
| Production performance readiness | production-like environment benchmark under approved scope | Performance Review Agent + DevOps/Deployment Agent + PM Agent | Production | approved env, load profile, rollback, monitoring | blocked until Production / Deploy Gates |

## Required Results Table

Use this format in performance reports:

| ID | Target | Metric | Command | Sample | Result | Threshold/Baseline | Decision | Claim impact |
|---|---|---|---|---|---|---|---|---|
| PERF-001 | startup | ms | `example command` | n=5 | example | threshold | Pass / Fail / Needs Review | supports / downgrades / blocks |

## Benchmark Quality Rules

```text
Command must be exact and reproducible.
Environment must be recorded.
Sample size must be stated.
Raw results must be included, not only summary.
Threshold or baseline must exist before Pass claim.
Variance/outliers must be noted when sample size > 1.
Errors/timeouts must be counted.
Benchmark side effects must be contained to local/test paths.
```

## Evidence Source Rules

Allowed evidence sources:

```text
real local command output
real integration command output
test logs with timing/resource metrics
system tool output that already exists
approved benchmark tool output
baseline report from same project
```

Not enough by itself:

```text
assistant assertion without command output
small code review claiming fast enough
single happy-path functional test without metric
benchmark plan without execution
browser-like fallback for real visual/browser performance claim
production performance claim from local-only laptop evidence
```

## Claim Downgrade Rules

```text
If no command/output -> downgrade to Paper performance review or No performance claim.
If no threshold/baseline -> report measured value only, no Pass claim.
If sample size is one -> label smoke measurement, not benchmark suite.
If environment missing -> mark Needs Review.
If errors occurred -> include error rate and downgrade unless accepted.
If tool/dependency needed but not approved -> mark Blocked or use no-install fallback with downgraded claim.
If benchmark can harm machine/network -> stop and ask before running.
If production environment not approved -> no production performance readiness claim.
```

## Pack-Specific Performance Notes

### CLI / Local-File

Required focus:

```text
startup time
single-operation latency
file size/data volume behavior
store read/write cleanup
large local file boundary
```

### HTTP API

Required focus:

```text
server startup time
endpoint latency
bounded throughput
error rate
request body size behavior
resource cleanup after server stop
```

### Static UI

Required focus:

```text
asset size
script parse/load assumptions
DOM operation timing if runtime available
browser proof boundary
no real visual/browser perf claim without executable launch evidence
```

### Fullstack Local

Required focus:

```text
API latency
UI-to-API roundtrip if runtime available
server startup/cleanup
integration error rate
cross-component bottleneck notes
```

### Docs-Only / Project-Management

Required focus:

```text
document size/readability only if relevant
no runtime performance claim
process throughput only when measured separately
```

## Stop Conditions

Stop and ask before:

```text
running load tests that may harm machine/network
installing benchmark tools without Track 1 approval
claiming optimized/performant without command output
claiming production performance readiness without Production / Deploy Gates
using cloud/DNS/billing/secrets/deploy path
running destructive data-volume tests without safe test path
```
