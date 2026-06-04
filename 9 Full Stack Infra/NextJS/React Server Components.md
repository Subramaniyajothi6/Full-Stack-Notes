---
tags: [infra, frontend, advanced]
---

# React Server Components

> Components that run only on the server; their JS is never sent to the client. Async, data-fetching, composable with Client Components.

## Why it matters
Smaller bundles, faster TTFB, and the ability to colocate DB/API calls with the UI that uses them. They redefine the React mental model.

## Core ideas
- **Server-only by default** in frameworks like Next.js App Router
- Can `await` data directly — no `useEffect` for fetching
- **Cannot** use `useState`, `useEffect`, browser APIs, event handlers
- Can render Client Components (marked `'use client'`)
- **Boundary** — Server → Client allowed; Client → Server is via Server Actions or props
- **Serializable props** — what crosses the boundary must be JSON-friendly (no functions, no class instances)

## Example
```tsx
// server component
export default async function Posts() {
  const posts = await db.post.findMany();
  return (
    <ul>
      {posts.map(p => <PostCard key={p.id} post={p} />)}
    </ul>
  );
}
```

## Real World Usage
- Database-driven pages without API hop
- SEO-critical content with zero client JS
- Mixing static marketing sections with interactive widgets

## Common Mistakes
- Importing client-only libraries (e.g., `framer-motion`) into a server component → build error
- Passing functions across boundary (must be Server Action or rebuild as event handler in client)
- Reading cookies/headers without using the framework's helpers
- Forgetting that Server Components don't re-render on interaction — must convert to Client Component

## Prerequisites
- [[Components|Components]] · [[Lazy Loading and Suspense|Suspense]]

## What To Learn Next
- [[Next.js App Router]] · [[AI SDK by Vercel]] · [[Server Components|React Server Components (overview note)]]

## Best Learning Resources

### Official Documentation
- [React docs — Server Components](https://react.dev/reference/rsc/server-components)
- [Next.js — Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)

### Best YouTube Resource
- [Jack Herrington — RSC playlist](https://www.youtube.com/@jherr) — best architectural explanations
- [Theo — RSC & Server Actions](https://www.youtube.com/@t3dotgg)
- [Dan Abramov talks](https://www.youtube.com/results?search_query=dan+abramov+server+components) — historical context from a maintainer

### Best Free Course
- [Next.js Learn — RSC chapters](https://nextjs.org/learn)

### Best Advanced Resource
- [How React Server Components Work — Plasmic](https://www.plasmic.app/blog/how-react-server-components-work) — internals
- [RSC RFC](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md)

### Best Practice Project
Build a "pinboard" app where the home page renders 1000 server-component cards with zero client JS. Add a starred-toggle as a Client Component child. Profile bundle size before/after vs a SPA equivalent.

### Recommended Order to Learn
1. Why RSC exists (motivation)
2. Server vs Client boundary rules
3. Composition + serialization
4. Data fetching patterns
5. Server Actions
6. Streaming + Suspense

## Interview Questions
**Q. What can't a Server Component do?**
A. State, effects, refs, event handlers, browser APIs.

**Q. How does the server send a Server Component?**
A. Serialized component tree (RSC payload) — not HTML, not JSON — that the client React runtime reconciles.

**Q. Why do props need to be serializable?**
A. They cross the network boundary into the client tree.

**Q. RSC vs SSR?**
A. SSR = run client components on server, hydrate same tree on client. RSC = some components only ever run on server, no client JS at all.

## Related
- [[Next.js App Router]] · [[Server Components|Server Components (intro)]]
