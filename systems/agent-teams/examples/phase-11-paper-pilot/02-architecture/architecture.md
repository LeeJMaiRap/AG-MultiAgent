# Architecture — Issue Tracker MVP

## Recommended Stack

```text
- Next.js App Router
- React + TypeScript
- Tailwind CSS
- Zod validation
- SQLite/Prisma for local MVP or mocked storage during paper pilot
- Playwright/Vitest for future real validation
```

## Modules

```text
app/(public)/page.tsx -> landing
app/issues/page.tsx -> issue list
app/issues/[id]/page.tsx -> issue detail
app/issues/new/page.tsx -> create issue
app/api/issues/route.ts -> list/create
app/api/issues/[id]/route.ts -> detail/update
lib/issues/* -> issue service/schema
```

## Data Model

```text
Issue:
- id
- title
- description
- priority: Low | Medium | High
- status: Open | In Progress | Done
- createdAt
- updatedAt
```

## Tradeoffs

```text
- simple local/mock auth avoids real secret risk
- small API surface reduces FE/BE mismatch
- future production auth/deploy requires new approval
```
