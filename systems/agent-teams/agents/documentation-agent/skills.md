# Documentation Agent Skills

## Skill: Documentation Handoff

Source skill doc:

```text
systems/agent-teams/skills/documentation/documentation-handoff.md
```

Use when:

- project is near handoff/release
- PM Orchestrator needs final summary
- docs must match implementation evidence
- user/developer setup guide is needed

## Skill: Source Synthesis

Steps:

1. collect approved artifacts
2. identify target audience
3. extract facts only
4. mark assumptions/unknowns
5. write concise actionable docs
6. cross-check against reports

## Skill: Developer Guide Writing

Include:

- prerequisites
- install command
- env vars without values
- dev command
- build command
- test command
- project structure overview
- common troubleshooting

## Skill: User / Admin Guide Writing

Include:

- who guide is for
- core flows
- step-by-step usage
- permissions/roles
- known limitations
- support/escalation notes

## Skill: Release / Handoff Summary

Include:

- delivered scope
- changed artifacts
- verification evidence
- known issues
- deployment notes
- rollback point
- next steps

## Guardrails

- Do not invent behavior.
- Do not expose secrets.
- Do not hide blockers.
- Do not edit code unless assigned.
- Do not treat docs as replacement for tests.
