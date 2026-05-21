# Conflict Resolution Protocol

## Purpose

Define what happens when agents conflict on scope, files, contracts, or conclusions.

## Conflict Types

1. **File conflict**
   - two agents need same file/path

2. **Contract conflict**
   - frontend/backend expectations differ

3. **Architecture conflict**
   - implementation disagrees with approved architecture

4. **Scope conflict**
   - agent adds work not approved

5. **Quality conflict**
   - agent says done, reviewer/test says not done

## Resolution Order

1. Stop conflicting work.
2. Identify source of conflict.
3. Preserve current state.
4. Ask owning agent for clarification if needed.
5. PM Orchestrator decides if within approved scope.
6. Escalate to user if scope/risk/cost changes.
7. Update contract/plan/ownership map.
8. Resume work sequentially or with new ownership.

## File Conflict Rule

If two agents need same write path:

- do not run in parallel
- split file ownership if safe
- otherwise sequence tasks
- Integration Agent handles final coordination

## Contract Conflict Rule

API Contract Agent owns final contract recommendation.
PM Orchestrator approves or escalates to user.
Frontend/Backend agents must not silently diverge.

## Quality Conflict Rule

If QA/Review rejects implementation:

- PM Orchestrator records finding
- original agent fixes if within scope
- user decides if finding changes scope/timeline
