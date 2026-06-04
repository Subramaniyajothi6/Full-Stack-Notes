---
tags: [nextjs, intermediate, pattern]
---

# Data Fetching Patterns (Next.js)

> Where you fetch data shapes performance and UX. App Router prefers fetching **inside server components**.

## Pattern 1: Server component awaits
```tsx
export default async function PostPage({ params }: { params: { id: string } }) {
  const post = await db.post.findUnique({ where: { id: params.id } });
  if (!post) notFound();
  return <Article post={post} />;
}
```
Default for SEO-critical content. Cacheable. Ships zero JS for the fetch logic.

## Pattern 2: Parallel fetches inside one server component
```tsx
export default async function Dashboard() {
  const [stats, recent] = await Promise.all([getStats(), getRecent()]);
  ...
}
```
Don't serialize awaits — fire in parallel.

## Pattern 3: Streamed per-section data
Split slow sections into their own server components, wrap each in Suspense — see [[Streaming and Suspense]].

## Pattern 4: Client-side with TanStack Query
For frequently changing data (live counts, comments) inside a client component:
```tsx
'use client';
const { data } = useQuery({ queryKey: ['comments', id], queryFn: ... });
```
See [[TanStack Query]].

## Pattern 5: Mutations via Server Actions
Form submits and writes go through [[Server Actions]] + `revalidateTag` / `revalidatePath`.

## When to use which
| Need                          | Pattern                  |
|-------------------------------|--------------------------|
| SEO content                   | Server component await   |
| Personalized dashboard        | Server component + `noStore()` |
| Frequently updated client UI  | TanStack Query           |
| Forms / mutations             | Server Actions           |
| Webhooks / public API         | Route Handlers           |

## React `cache()` for dedup
```ts
import { cache } from 'react';
export const getPost = cache(async (id: string) => db.post.findUnique({ where: { id } }));
```
Called twice in the same render → one DB hit.

## Real World Usage
- Blog: server component fetches post
- Dashboard: server fetches static + client fetches live
- E-commerce PDP: server fetches product, client manages cart
- AI chat: server fetches history, client streams new messages

## Common Mistakes
- `useEffect + fetch` in a server-rendered tree (no SSR, just CSR)
- Sequential `await`s instead of `Promise.all`
- Calling client-only libs inside server components
- Duplicate fetches in one render — wrap with `cache()`
- Putting auth tokens in client component fetches when a server component would be safer

## Prerequisites
- [[Next.js App Router]] · [[React Server Components]] · [[Caching and Revalidation]]

## What To Learn Next
- [[Streaming and Suspense]] · [[Server Actions]] · [[TanStack Query]]

## Best Learning Resources

### Official Documentation
- [Next.js — Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching)
- [React — `cache()`](https://react.dev/reference/react/cache)

### Best YouTube Resource
- [Lee Robinson — Data fetching patterns](https://www.youtube.com/@leerob)
- [Theo — Server vs client data](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Next.js Learn — Fetching Data](https://nextjs.org/learn)

### Best Advanced Resource
- [Vercel templates repo](https://vercel.com/templates) — production patterns

### Best Practice Project
Build a Reddit-style feed: server-rendered list (cached), per-post server-rendered detail page, client-side live comment count (TanStack Query), comment submission (Server Action with optimistic update).

### Recommended Order to Learn
1. Async server component await
2. Parallel with `Promise.all`
3. React `cache()` dedup
4. Suspense boundaries for streaming
5. Client-side TanStack Query for live data
6. Server Actions for writes

## Interview Questions
**Q. Why fetch in server components by default?**
A. Closer to data source, no client waterfalls, zero JS shipped for fetch logic, cached automatically.

**Q. When does CSR (`useEffect + fetch`) still make sense?**
A. Live / user-interactive data not tied to SEO — comments, presence, charts that update often.

## Related
- [[React Server Components]] · [[Server Actions]] · [[Caching and Revalidation]] · [[TanStack Query]] · [[Streaming and Suspense]]
