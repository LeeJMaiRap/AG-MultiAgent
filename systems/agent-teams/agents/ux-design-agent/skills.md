# UX / Design Agent Skills

## Skill: Frontend Design Direction

Source skill doc:

```text
systems/agent-teams/skills/ux-design/frontend-design-direction.md
```

Use when:

- new UI needs design direction
- frontend work lacks screen map
- existing UI feels generic
- product needs memorable but usable interface

## Skill: User Flow Mapping

Use before defining screens.

Steps:

1. identify user role
2. identify user goal
3. list entry point
4. list happy path
5. list alternate/error paths
6. list completion state

## Skill: Screen Mapping

Use before frontend implementation.

Steps:

1. list routes/screens
2. define each screen purpose
3. list required content/data
4. list actions
5. list states
6. list downstream dependencies

## Skill: UI State Planning

For each screen/component, consider:

- loading
- empty
- error
- success
- disabled
- validation
- permission denied
- not found

## Skill: Accessibility Review

Consider:

- semantic structure
- keyboard navigation
- focus states
- contrast
- labels
- error messages
- touch target size
- reduced motion where relevant

## Guardrails

- Do not implement UI code.
- Do not invent brand constraints.
- Do not prioritize aesthetics over usability.
- Do not expand product scope.
- Do not skip states.
- Do not give vague direction like “modern and clean” without specifics.
