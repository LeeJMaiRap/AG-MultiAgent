# Skill: Frontend Design Direction

## Purpose

Create intentional, product-specific frontend direction before UI implementation.

This adapts ideas from:

```text
systems/agent-teams/references/anthropic-frontend-design.md
systems/agent-teams/references/vercel-agent-skills.md
```

## When To Use

Use when:

- new frontend feature needs UX/design plan
- UI risks becoming generic
- frontend agent needs screen map and states
- user experience is unclear
- visual direction needs approval before implementation

## Inputs

- requirements
- target users
- product goal
- user stories
- acceptance criteria
- brand/design constraints if any

## Process

### 1. Understand Product Intent

Write:

```text
Who is using this?
What are they trying to do?
What matters most: speed, trust, delight, clarity, conversion, admin efficiency?
```

### 2. Define UX Principles

Pick 3-5 concrete principles.

Bad:

```text
modern, clean, beautiful
```

Good:

```text
- product cards prioritize price/status above decorative metadata
- contact CTA is visible without scrolling on mobile detail screen
- admin forms minimize repeated typing
```

### 3. Map Core Flows

Use:

```text
FLOW-001 <name>
Actor:
Goal:
Steps:
Alternative paths:
Completion state:
```

### 4. Map Screens

Use:

```text
SCREEN-001 <name>
Route if known:
Purpose:
Primary user action:
Content sections:
Required data:
States:
```

### 5. Choose Design Direction

Include:

- aesthetic direction
- layout strategy
- typography feel
- color/contrast notes
- interaction/motion notes
- mobile/responsive notes

Keep it tied to product purpose.

### 6. Plan UI States

For each major screen:

```text
loading
empty
error
success
disabled
validation
not found
permission denied
```

### 7. Accessibility / Usability Notes

Include:

- keyboard/focus behavior
- labels/error text
- contrast needs
- responsive touch targets
- semantic structure

### 8. Frontend Handoff

List:

- routes/pages
- components needed
- data needed
- interactions
- acceptance checks
- open questions

## Output Checklist

```text
[ ] Product intent clear
[ ] UX principles concrete
[ ] Core flows mapped
[ ] Screens mapped
[ ] UI states included
[ ] Design direction specific
[ ] Accessibility notes included
[ ] Frontend handoff actionable
[ ] Open questions listed
```

## Common Mistakes

- vague “modern clean” direction
- jumping into component code
- missing empty/error states
- ignoring mobile
- treating admin UX as afterthought
- making visuals inconsistent with product purpose
