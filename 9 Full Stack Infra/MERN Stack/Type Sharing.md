---
tags: [mern, integration, intermediate]
---

# Type Sharing

> One source of truth for types across frontend and backend. Eliminates "client expects X, server sends Y" drift.

## Why it matters
Manual TypeScript interfaces in two places diverge silently. Type sharing makes the contract a runtime + compile-time guarantee.

## Patterns (lightest → heaviest)

### 1. Zod schemas in a shared module
```ts
// shared/user.ts
import { z } from 'zod';
export const User = z.object({ id: z.string(), email: z.string().email() });
export type User = z.infer<typeof User>;

// server: validate + type
const parsed = User.parse(req.body);

// client: validate response
const user = User.parse(await fetch('/api/me').then(r => r.json()));
```

### 2. tRPC — types flow automatically
Client imports a type-only reference to the server router. No codegen, no schema files.

### 3. OpenAPI + codegen
Spec → run `openapi-typescript` → generated `.d.ts` consumed by client. Best for public APIs.

### 4. GraphQL + codegen
Schema → `graphql-codegen` → typed hooks (`useGetUserQuery`).

### 5. Prisma `$inferred` types
Reuse Prisma model types in the API layer; ship them to the client as input/output types of your chosen API style.

## Folder layout
```
apps/
  web/         (React)
  api/         (Express / Next API routes)
packages/
  shared/      (zod schemas, types) ← imported by both
```

A monorepo (pnpm workspaces / Turborepo / Nx) is the natural home.

## Real World Usage
- Vercel / Linear / Cal.com — heavy tRPC for internal velocity
- Public SaaS — OpenAPI codegen so 3rd-party SDKs work
- Mobile apps — GraphQL + codegen for typed hooks
- Auth payloads (`User`, `Session`) — always shared

## Common Mistakes
- Duplicating types in both client and server (drift guaranteed)
- Importing server-only modules into shared package (Zod is fine, Prisma client is not)
- Sharing huge entity types when only a subset is exposed (over-share leak)
- Skipping runtime validation — types lie at the network boundary

## Prerequisites
- [[TypeScript]] · [[API Contract]]

## What To Learn Next
- [[Form Lifecycle]] · [[Protected Routes End-to-End]]

## Best Learning Resources

### Official Documentation
- [Zod docs](https://zod.dev/)
- [tRPC docs — Concepts](https://trpc.io/docs/concepts)
- [openapi-typescript](https://github.com/drwpow/openapi-typescript)

### Best YouTube Resource
- [Matt Pocock — Zod & TS](https://www.youtube.com/@mattpocockuk)
- [Theo — tRPC + monorepo](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Total TypeScript — type sharing patterns (free chapters)](https://www.totaltypescript.com/)
- [Turborepo Quickstart](https://turbo.build/repo/docs)

### Best Advanced Resource
- [Effect TS — schemas](https://effect.website/) — alternative beyond Zod
- [Prisma + tRPC monorepo blueprints (create-t3-app)](https://create.t3.gg/)

### Best Practice Project
Build a tiny monorepo: `apps/web` (Vite + React), `apps/api` (Express), `packages/shared` (Zod schemas). Define `User` once, validate on both ends. Then add a second consumer (`apps/cli`) and confirm zero changes needed.

### Recommended Order to Learn
1. Zod + `z.infer` basics
2. Pulling Zod schemas into a shared package
3. tRPC for internal apps
4. OpenAPI codegen for public APIs
5. Prisma type re-use
6. Monorepo tooling (pnpm + Turborepo)

## Interview Questions
**Q. Why not just share TS interfaces?**
A. Interfaces are compile-time only; the network is runtime. Validation libraries (Zod) give you both.

**Q. Tradeoffs of monorepo vs separate repos for type sharing?**
A. Monorepo: instant shared types, single PR cuts both sides. Separate: independent deploys, harder type sync (need codegen).

**Q. How do you avoid leaking server-only types to the client?**
A. Keep shared types in a leaf package that depends only on cross-runtime libs (Zod yes; Prisma client no).

## Related
- [[TypeScript]] · [[API Contract]] · [[Validation]] · [[Form Lifecycle]]
