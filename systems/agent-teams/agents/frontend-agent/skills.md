# Frontend Agent Skills

## Skill: Frontend Implementation

Source skill doc:

```text
systems/agent-teams/skills/frontend/frontend-implementation.md
```

Use when:

- implementing page/route/component
- connecting UI to approved API contract
- adding frontend validation or states
- improving existing UI inside assigned scope

## Skill: UI State Implementation

For each relevant screen/component, implement:

- loading
- empty
- error
- success
- disabled
- validation
- not found
- permission denied

## Skill: API Contract Consumption

Steps:

1. identify contract endpoint/action
2. map request fields
3. map response fields
4. map error codes/messages
5. represent loading/empty/error states
6. do not alter contract silently

## Skill: Frontend Verification

Use available project commands:

```text
npm run lint
npm run build
npm test
npm run test
npx playwright test
```

If unavailable:

- inspect package scripts
- report missing command
- do manual file/route review where possible

## Skill: Responsive / Accessibility Pass

Check:

- mobile layout
- keyboard focus
- button/link labels
- form labels
- error messages
- color contrast basics
- alt text for meaningful images

## Guardrails

- Do not edit backend/API/schema.
- Do not change design direction unless asked.
- Do not install packages without approval unless task explicitly allows.
- Do not rewrite whole app for small feature.
- Do not claim done without evidence.
