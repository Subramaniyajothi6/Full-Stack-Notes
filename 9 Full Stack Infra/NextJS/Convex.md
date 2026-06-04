---
tags: [infra, backend, intermediate]
---

# Convex

> Reactive, serverless backend platform. Database + functions + realtime subscriptions in one TS-native stack.

## Why it matters
Eliminates the API layer. Frontend subscribes to queries; Convex pushes updates automatically. Strong consistency, transactional functions, no schema migrations on day one.

## Core ideas
- **Functions** — `query`, `mutation`, `action` written in TS
- **Reactive queries** — `useQuery` rerenders on data change automatically
- **Database** — document-relational; indexes; transactions; ACID
- **File storage** — built-in
- **Cron + scheduled functions**
- **Auth** — Clerk, Auth0, custom

## Example
```ts
// convex/messages.ts
import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: { channel: v.string() },
  handler: async (ctx, { channel }) => {
    return await ctx.db
      .query("messages")
      .withIndex("by_channel", q => q.eq("channel", channel))
      .order("desc")
      .take(50);
  },
});

export const send = mutation({
  args: { channel: v.string(), body: v.string() },
  handler: async (ctx, { channel, body }) => {
    await ctx.db.insert("messages", { channel, body, ts: Date.now() });
  },
});
```

```tsx
// React component
const messages = useQuery(api.messages.list, { channel });
```

## Real World Usage
- Realtime collaborative apps (chat, docs, dashboards)
- Internal tools where API + DB friction matters
- AI apps with reactive state

## Common Mistakes
- Loading thousands of rows into a single query — paginate
- Long-running work in mutations — use `action` (no transaction guarantee, but can call external APIs)
- Treating `useQuery` as raw fetch — it's a subscription
- Skipping indexes — `withIndex` is essential at scale

## Prerequisites
- [[React MOC|React]] · [[Next.js App Router]]

## What To Learn Next
- [[Edge Computing]] · [[WebSockets|WebSockets]]

## Best Learning Resources

### Official Documentation
- [Convex Docs](https://docs.convex.dev/) — example-first
- [Convex tutorial](https://docs.convex.dev/tutorial)

### Best YouTube Resource
- [Convex (official)](https://www.youtube.com/@Convex)
- [Theo — Convex deep dives](https://www.youtube.com/@t3dotgg)
- [Web Dev Cody — Convex builds](https://www.youtube.com/@WebDevCody)

### Best Free Course
- [Convex tutorial chat app](https://docs.convex.dev/tutorial) — official walkthrough
- [convex-demos GitHub](https://github.com/get-convex/convex-demos)

### Best Advanced Resource
- [Convex engineering blog — ACID, MVCC](https://stack.convex.dev/) — internals
- [Stack by Convex](https://stack.convex.dev/) — patterns and case studies

### Best Practice Project
Build a realtime kanban: Convex tables for boards/columns/cards, mutations for create/move/edit, presence via mutation that updates a `users` doc, file uploads via Convex storage. No REST/GraphQL/WebSocket layer of your own.

### Recommended Order to Learn
1. Schema + functions + queries
2. `useQuery` reactivity
3. Indexes + pagination
4. Mutations + transactions
5. Actions (external calls)
6. Cron + auth

## Interview Questions
**Q. How does Convex push updates?**
A. Maintains query subscriptions per client; on mutation commit, recomputes affected queries and ships diffs.

**Q. Convex vs Firebase vs Supabase?**
A. Firebase: realtime + auth, weaker queries. Supabase: Postgres + GoTrue, REST-ish. Convex: TS functions + reactive queries with transactional consistency.

**Q. When NOT to use Convex?**
A. When you need a SQL-only stack, complex existing relational DB, or want maximum control over your DB engine.

## Related
- [[Next.js App Router]] · [[WebSockets|WebSockets]]
