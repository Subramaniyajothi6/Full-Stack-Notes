---
tags: [infra, frontend, intermediate]
---

# TanStack Query

> Async server-state manager for React. Caching, deduping, background refetch, mutations, infinite scroll — out of the box.

## Why it matters
Most state in apps is *server* state, not client state. TanStack Query (formerly React Query) handles loading, caching, retries, and invalidation so you don't write `useEffect + setState + abortController` every time.

## Core ideas
- **`queryKey`** — uniquely identifies cached data (`['posts', id]`)
- **`queryFn`** — async fetcher
- Built-ins: stale time, cache time, retries, refetch on focus/reconnect
- **Mutations** — `useMutation` for writes, with `invalidateQueries` to refresh
- **Optimistic updates** — set cache before server confirms, roll back on error
- **Suspense mode** — integrate with React Suspense

## Example
```tsx
const { data, isLoading } = useQuery({
  queryKey: ['post', id],
  queryFn: () => fetch(`/api/posts/${id}`).then(r => r.json()),
  staleTime: 60_000,
});

const qc = useQueryClient();
const { mutate } = useMutation({
  mutationFn: updatePost,
  onSuccess: () => qc.invalidateQueries({ queryKey: ['post', id] }),
});
```

## Real World Usage
- API-heavy dashboards
- Infinite scroll (`useInfiniteQuery`)
- Optimistic mutation UX (likes, todos)
- Pairing with [[Next.js App Router]] for client islands

## Common Mistakes
- Stuffing TanStack Query state in Redux/Zustand too — duplicate sources of truth
- Missing query keys when params change → stale data
- Using as a global state replacement
- Refetch storms when many components mount with same key (it dedupes — verify)

## Prerequisites
- [[Promises|Promises]] · [[Fetch API|Fetch API]] · [[useEffect|useEffect]]

## What To Learn Next
- [[Zustand]] · [[Next.js App Router]] · [[AI SDK by Vercel]]

## Best Learning Resources

### Official Documentation
- [TanStack Query docs](https://tanstack.com/query/latest) — best-in-class
- [Examples gallery](https://tanstack.com/query/latest/docs/react/examples)

### Best YouTube Resource
- [Jack Herrington — TanStack Query](https://www.youtube.com/@jherr) — patterns
- [TkDodo on YouTube/blog](https://tkdodo.eu/blog) — TanStack Query maintainer; gold-tier writeups

### Best Free Course
- [Official tutorial — Tanstack Query Course](https://query.gg/) — by maintainers (paid full, free intro)
- [TkDodo's "Practical React Query" blog series](https://tkdodo.eu/blog/practical-react-query)

### Best Advanced Resource
- TkDodo's deep posts: caching, render optimisations, testing
- [TanStack Query + Suspense + RSC patterns](https://tanstack.com/query/latest/docs/react/guides/suspense)

### Best Practice Project
Rebuild a CRUD app you already have to remove every manual `fetch + useState`. Add optimistic updates, infinite scroll, query invalidation, and offline support via persistence plugin.

### Recommended Order to Learn
1. `useQuery` + key + fetcher
2. Stale/cache time semantics
3. Mutations + invalidations
4. Optimistic updates + rollback
5. Infinite queries + pagination
6. Persistence + Suspense

## Interview Questions
**Q. What is "stale time"?**
A. How long data is considered fresh; while fresh, no automatic refetch.

**Q. Difference between cacheTime (gcTime) and staleTime?**
A. staleTime = freshness window. gcTime = how long unused data lingers in cache before garbage collection.

**Q. How do mutations invalidate?**
A. `queryClient.invalidateQueries({ queryKey })` marks them stale; next observer triggers refetch.

**Q. When NOT to use TanStack Query?**
A. Pure UI/local state; tiny apps; environments where you'd rather use a framework's built-in fetch cache (Next.js App Router).

## Related
- [[Zustand]] · [[Next.js App Router]] · [[useEffect|useEffect]]
