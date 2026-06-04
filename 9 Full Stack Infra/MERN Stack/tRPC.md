---
tags: [mern, integration, intermediate]
---

# tRPC

> End-to-end typesafe RPC for TypeScript. Define server procedures; the client gets fully-typed functions without codegen.

## Why
- Zero schemas (no GraphQL SDL, no OpenAPI)
- Types flow directly client ↔ server through a TS import
- Validate inputs with Zod (also gives type inference)
- Works with React Query under the hood (caching, mutations, infinite queries)

## Server (router)
```ts
// server/router.ts
import { initTRPC } from '@trpc/server';
import { z } from 'zod';

const t = initTRPC.create();

export const appRouter = t.router({
  user: t.router({
    byId: t.procedure
      .input(z.string())
      .query(({ input }) => db.user.findUnique({ where: { id: input } })),
    create: t.procedure
      .input(z.object({ email: z.string().email() }))
      .mutation(({ input }) => db.user.create({ data: input })),
  }),
});

export type AppRouter = typeof appRouter;
```

## Client (TS infers everything)
```tsx
import { createTRPCReact } from '@trpc/react-query';
import type { AppRouter } from '../server/router';

export const trpc = createTRPCReact<AppRouter>();

// inside a component
const { data } = trpc.user.byId.useQuery('user_1');
const mutate = trpc.user.create.useMutation();
```

## Middleware + context
```ts
const protectedProcedure = t.procedure.use(async ({ ctx, next }) => {
  if (!ctx.user) throw new TRPCError({ code: 'UNAUTHORIZED' });
  return next({ ctx: { ...ctx, user: ctx.user } });
});
```

## Real World Usage
- Internal SaaS dashboards (TS front + back)
- Tightly coupled Next.js apps (T3 stack)
- Replacing REST + manual typing
- Internal APIs where you control both sides

## Common Mistakes
- Using tRPC for public APIs (locks consumers into TS)
- Forgetting Zod inputs → un-validated procedures
- Returning Mongo `_id` (BSON) without serializing to string
- Mixing `@tanstack/react-query` v4 and v5 incompatibilities
- Server / client TS versions drifting in a monorepo

## Prerequisites
- [[TypeScript]] · [[Type Sharing]] · [[TanStack Query]] · [[API Contract]]

## What To Learn Next
- [[Form Lifecycle]] · [[Full-Stack Auth Flow]]

## Best Learning Resources

### Official Documentation
- [tRPC docs](https://trpc.io/docs)
- [tRPC + Next.js example](https://create.t3.gg/)

### Best YouTube Resource
- [Theo (t3.gg) — tRPC deep dives](https://www.youtube.com/@t3dotgg)
- [Jack Herrington — tRPC architectures](https://www.youtube.com/@jherr)

### Best Free Course
- [tRPC v11 quickstart](https://trpc.io/docs/quickstart)
- [create-t3-app](https://create.t3.gg/)

### Best Advanced Resource
- [tRPC source on GitHub](https://github.com/trpc/trpc)
- [Alex / KATT (creator) talks](https://www.youtube.com/results?search_query=tRPC+alex+katt)

### Best Practice Project
Replace REST endpoints in a Next.js app with tRPC procedures. Verify all client calls are typed; remove every hand-rolled fetch + type interface. Add a protected procedure for auth-gated mutations.

### Recommended Order to Learn
1. Router + procedure basics
2. Zod inputs + outputs
3. Queries + mutations on the client
4. Context + middleware (auth)
5. Subscriptions (websocket)
6. Server Actions vs tRPC tradeoff

## Interview Questions
**Q. tRPC vs GraphQL?**
A. tRPC: TS-only, zero schema, fastest DX inside TS apps. GraphQL: language-agnostic, federated, public-API friendly.

**Q. tRPC vs Server Actions?**
A. Server Actions are Next-native and form-friendly. tRPC works across any TS app (Vite SPA, Expo) and shines for many procedures.

## Related
- [[Type Sharing]] · [[API Contract]] · [[TanStack Query]] · [[TypeScript]]
