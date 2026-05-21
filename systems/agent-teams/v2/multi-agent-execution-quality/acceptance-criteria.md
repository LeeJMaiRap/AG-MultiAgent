# Track 5 — Multi-Agent Execution Quality Acceptance Criteria

## Track Acceptance

Track 5 is accepted when:

```text
cross-agent evidence index template exists (`templates/cross-agent-evidence-index-template.md`)
parallel wave readiness v2 checklist exists (`templates/parallel-wave-readiness-v2-checklist.md`)
ownership conflict escalation protocol exists (`ownership-conflict-escalation-protocol.md`)
handoff quality rubric exists (`handoff-quality-rubric.md`)
PM acceptance dashboard template exists (`templates/pm-acceptance-dashboard-template.md`)
multi-agent execution quality dry-run exists (`examples/phase-88-execution-quality-dry-run/README.md`)
dry-run rejects missing evidence, ownership conflicts, and bad handoffs
runbooks preserve PM Agent Orchestrator-only role
```

## Claim Acceptance Criteria

```text
wave completion claim requires all specialist reports
parallel-ready claim requires conflict check
handoff-ready claim requires next owner, blockers, evidence links
PM-accepted claim requires dashboard/evidence index row
review-approved claim requires evidence level match
```

## Rejection Criteria

Reject or mark Needs Review when:

```text
owned paths overlap without sequence/escalation decision
agent report missing
evidence link missing
verification level overclaimed
claim boundary missing
handoff target missing
blocker hidden or dropped
restricted install/deploy/browser/security/performance claim bypasses Tracks 1-4
```

## Stop Conditions

Stop and ask before:

```text
expanding PM Agent from orchestrator into implementer
adding runtime automation or external frameworks
broadening owned paths to whole repo
running install/download/deploy/cloud/browser actions
weakening existing dependency/security/performance/browser gates
```
