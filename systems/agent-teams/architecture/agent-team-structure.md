# Agent-Team Structure

## Core Principle

PM Agent is the single Lead / Orchestrator. It coordinates work, but does not implement specialist work directly.

Specialist agents own specialist domains and return structured reports with evidence.

## Core Team

1. **PM Orchestrator**
   - Owns planning, delegation, dependency tracking, risk/change/issue handling, quality gates, and user reporting.

2. **Product/Requirements Agent**
   - Owns PRD, user stories, acceptance criteria, scope clarification, and question backlog.

3. **Technical Architecture Agent**
   - Owns architecture, stack decisions, module boundaries, data flow, and ADRs.

4. **API Contract Agent**
   - Owns endpoint contracts, request/response schemas, auth rules, error format, pagination/filtering/sorting.

5. **Frontend Agent**
   - Owns UI implementation, components, responsive behavior, accessibility, frontend state/forms, frontend tests.

6. **Backend Agent**
   - Owns API implementation, database schema, business logic, validation, auth/authz, backend tests.

7. **QA/Test Agent**
   - Owns test plan, e2e/API tests, acceptance verification, regression checks, bug reports.

8. **Integration Agent**
   - Owns combining frontend/backend/tests, resolving integration issues, running full-app verification.

## Optional / On-Demand Agents

1. **UX/Design Agent**
   - Used when product needs strong user experience, screen maps, visual direction, or design system decisions.

2. **Security Review Agent**
   - Used when auth, user data, payments, uploads, public APIs, or production deployment are involved.

3. **Performance Review Agent**
   - Used when load time, query speed, bundle size, caching, or scale matters.

4. **Code Review Agent**
   - Used before merge/handoff to check maintainability, duplication, architecture drift, and test gaps.

5. **DevOps/Deployment Agent**
   - Used for CI/CD, Docker, env config, cloud deploy, monitoring basics, and rollback path.

6. **Documentation Agent**
   - Used for README, setup guide, API docs, handoff notes, user/admin guide.

7. **Challenge Agent**
   - Used to challenge assumptions, find edge cases, and critique plans/design/architecture.

## Non-Goals

- PM Orchestrator does not code frontend/backend features.
- Specialist agents do not change scope without PM/user approval.
- Agents do not touch files outside owned paths.
- Agents do not claim done without evidence.
