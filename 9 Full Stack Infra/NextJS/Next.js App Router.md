---
tags: [infra, frontend, intermediate]
---

# Next.js App Router

> File-based routing built on React Server Components, with nested layouts, streaming, and server actions.

## Why it matters
The default for new Next.js apps. Lets you mix server-rendered, statically generated, and client-interactive UI in the same tree, with first-class data fetching.

## Core ideas
- **`app/` directory** — folders = routes; `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`
- **Server Components by default** — async, data-fetched on server, ship 0 JS
- **`'use client'`** — opt into Client Component for state/effects/handlers
- **Layouts persist** across navigation (don't re-render) — perfect for sidebars
- **Streaming** — `<Suspense>` boundaries flush HTML progressively
- **Server Actions** — mutate data on server via `'use server'`-tagged async functions
- **Route handlers** — `route.ts` with `GET`/`POST` exports replace API routes
- **Caching** — fetch is cached by default; opt-out via `{ cache: 'no-store' }` or revalidation

## Quick example
```tsx
// app/posts/[id]/page.tsx
export default async function Post({ params }: { params: { id: string } }) {
  const post = await db.post.findUnique({ where: { id: params.id } });
  return <article>{post.body}</article>;
}
```

## Real World Usage
- E-commerce: SSR product pages + client cart
- Dashboards: streaming widgets with per-section Suspense
- Marketing sites with ISR for blog posts

## Common Mistakes
- Adding `'use client'` to a layout — kills server-only parents
- Importing client-only libs into server components
- Forgetting `cache: 'no-store'` for personalized data
- Calling Server Actions inside event handlers without `useTransition`

## Prerequisites
- [[React MOC|React]] · [[React Server Components]]

## What To Learn Next
- [[Pages Router]] (legacy comparison) · [[Edge Computing]] · [[TanStack Query]]

## Best Learning Resources

### Official Documentation
- [Next.js Docs — App Router](https://nextjs.org/docs/app) — single best source
- [React Docs — Server Components](https://react.dev/reference/rsc/server-components)

### Best YouTube Resource
- [Theo (t3.gg)](https://www.youtube.com/@t3dotgg) — opinionated, current
- [Jack Herrington — Next.js series](https://www.youtube.com/@jherr) — clean architectural breakdowns
- [Lee Robinson (Next.js dev)](https://www.youtube.com/@leerob)

### Best Free Course
- [Next.js Learn (official)](https://nextjs.org/learn) — interactive, builds a real app

### Best Advanced Resource
- [Next.js GitHub — examples](https://github.com/vercel/next.js/tree/canary/examples) — patterns straight from the team
- [Vercel engineering blog](https://vercel.com/blog) — caching, streaming deep dives

### Best Practice Project
Build a multi-author blog with App Router: server-rendered posts, streamed comments via Suspense, server actions for create/edit/delete, and edge-cached author pages. Add an admin route guarded with middleware.

### Recommended Order to Learn
1. Project setup + file conventions
2. Layouts + nested routes
3. Server vs Client Components
4. Data fetching + caching
5. Server Actions + forms
6. Middleware + edge runtime

## Interview Questions
**Q. App Router vs Pages Router?**
A. App Router uses RSC, nested layouts, streaming, server actions. Pages Router is `getStaticProps`/`getServerSideProps` + client React only.

**Q. When does `fetch` cache?**
A. By default, indefinitely. Opt out with `cache: 'no-store'` or revalidate with `next: { revalidate: 60 }`.

**Q. What's a Server Action?**
A. Async function tagged `'use server'`; the framework wires it to a hidden POST endpoint and provides progressive enhancement.

**Q. How does streaming work?**
A. Suspense boundaries split the response; the server flushes HTML chunks as data resolves.

## Related
- [[Pages Router]] · [[React Server Components]] · [[Edge Computing]]
