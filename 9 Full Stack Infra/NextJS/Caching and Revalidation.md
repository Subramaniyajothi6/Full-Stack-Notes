---
tags: [nextjs, advanced, performance]
---

# Caching and Revalidation (Next.js)

> Four layers of cache in App Router: Request memo, Data cache, Full-route cache, Router cache. Plus tag/path revalidation.

## The four caches
| Cache              | Where    | Lifetime          | Key                              |
|--------------------|----------|-------------------|----------------------------------|
| Request memoization| server   | one request       | function call within a render    |
| Data cache         | server   | persistent        | `fetch()` URL + opts (+ tags)    |
| Full-route cache   | server   | until revalidated | route + RSC payload              |
| Router cache       | client   | session           | route segments                   |

## fetch caching defaults
```ts
fetch(url)                                  // cached forever (default in App Router)
fetch(url, { cache: 'no-store' })           // opt out — fresh every time
fetch(url, { next: { revalidate: 60 } })    // ISR-style 60s
fetch(url, { next: { tags: ['posts'] } })   // tag for invalidation
```

## Revalidate by tag
```ts
// after mutating data
import { revalidateTag } from 'next/cache';
revalidateTag('posts');
```
All `fetch`es that include `tags: ['posts']` are invalidated.

## Revalidate by path
```ts
revalidatePath('/posts');
revalidatePath('/posts/[id]', 'page');
```

## Static vs dynamic rendering
A route is **static** if every data access is cacheable. Reading from `cookies()` / `headers()` / `searchParams` / `noStore()` makes it **dynamic**.

```ts
import { noStore } from 'next/cache';
export default async function Page() {
  noStore();                                // force dynamic
  return <div>{Date.now()}</div>;
}
```

## React `cache()` (per-request memo)
```ts
import { cache } from 'react';
export const getUser = cache(async (id: string) => db.user.findUnique({ where: { id } }));
```
Same args inside one render → one call.

## Real World Usage
- Marketing pages: static + ISR every 5 min
- Personalized dashboards: dynamic + per-request memo
- Lists: cached with `revalidateTag('list-name')` triggered by mutations
- API proxy routes: tag both upstream and downstream
- Edge functions reading near-static data

## Common Mistakes
- Assuming everything dynamic by default — App Router defaults to static
- Forgetting to revalidate after a mutation → stale UI for the cache window
- Same tag on too many fetches → wide invalidation storms
- `cookies()` in a static page → build error
- Caching personalized responses across users

## Prerequisites
- [[Next.js App Router]] · [[React Server Components]] · [[Server Actions]]

## What To Learn Next
- [[Edge Runtime]] · [[Streaming and Suspense]]

## Best Learning Resources

### Official Documentation
- [Next.js — Caching](https://nextjs.org/docs/app/building-your-application/caching)
- [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)

### Best YouTube Resource
- [Lee Robinson — Caching in Next.js](https://www.youtube.com/@leerob)
- [Theo — caching layers](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Next.js Learn — caching chapters](https://nextjs.org/learn)

### Best Advanced Resource
- [Vercel blog — Cache deep dives](https://vercel.com/blog)

### Best Practice Project
Build a blog: static list page cached forever, but tagged. After publish action runs, `revalidateTag('posts')`. Verify zero stale reads after publish.

### Recommended Order to Learn
1. fetch defaults
2. `revalidate` + tags
3. `revalidatePath` / `revalidateTag` from actions
4. Static vs dynamic rendering
5. Router cache (client-side)
6. `unstable_cache` for non-fetch caching

## Interview Questions
**Q. Why does App Router cache by default?**
A. Perf — static rendering is fast and cheap to serve at edge. Opt out for user-scoped data.

**Q. Tag vs path revalidation?**
A. Tag invalidates everything sharing that tag (multi-route). Path invalidates one specific route.

**Q. What makes a route dynamic?**
A. Using `cookies()`, `headers()`, `searchParams`, `noStore()`, or any fetch with `no-store`.

## Related
- [[Next.js App Router]] · [[Server Actions]] · [[Edge Runtime]]
