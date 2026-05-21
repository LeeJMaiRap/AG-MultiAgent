# Reference: Vercel Agent Skills

Source: https://github.com/vercel-labs/agent-skills

## Summary

Vercel Agent Skills provide practical skills for AI coding agents, especially around React, Next.js, UI quality, performance, React Native, animations, composition patterns, and deployment.

Useful areas:

- React/Next.js performance optimization
- UI review best practices
- accessibility/performance/UX audits
- React composition patterns
- View Transition API
- Vercel deployment

## Best Fit In Agent-Teams

### Frontend Agent

Use for:

- React/Next.js implementation practices
- component design
- composition patterns
- UI states and responsiveness
- accessibility basics

### UX/Design Agent

Use for:

- UI review checklist
- interaction quality
- forms, focus states, typography, theming, touch behavior

### Performance Review Agent

Use for:

- eliminating waterfalls
- bundle size optimization
- server-side performance
- client data fetching
- re-render/rendering performance

### DevOps/Deployment Agent

Use for:

- Vercel deployment flow
- preview URL and deploy handoff pattern

### Backend Agent

Use only when project uses Next.js backend/API routes/server actions.

## Suggested OpenClaw-Native Skills Later

```text
systems/agent-teams/skills/frontend/react-nextjs-performance.md
systems/agent-teams/skills/frontend/ui-review.md
systems/agent-teams/skills/frontend/react-composition-patterns.md
systems/agent-teams/skills/performance/web-performance-review.md
systems/agent-teams/skills/devops/vercel-deploy.md
```

## What Not To Copy Blindly

- deployment automation without approval
- framework-specific assumptions when project is not Next.js/React
- browser/UI rules irrelevant to backend-only tasks
