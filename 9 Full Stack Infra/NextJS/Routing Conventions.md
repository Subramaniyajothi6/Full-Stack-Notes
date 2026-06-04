---
tags: [nextjs, beginner, routing]
---

# Routing Conventions

> File and folder names inside `app/` define routes. Special filenames have special meaning.

## Special files
| File              | Role                                                     |
|-------------------|----------------------------------------------------------|
| `page.tsx`        | The route's UI                                            |
| `layout.tsx`      | Wraps `page.tsx` + child routes; persists across nav      |
| `loading.tsx`     | Suspense fallback for the segment                          |
| `error.tsx`       | Error boundary                                             |
| `not-found.tsx`   | UI for `notFound()`                                        |
| `template.tsx`    | Like layout but new instance per navigation                |
| `route.ts`        | HTTP handlers (no UI)                                      |
| `default.tsx`     | Fallback for parallel routes                                |

## Dynamic segments
```
app/users/[id]/page.tsx              ← /users/123
app/posts/[...slug]/page.tsx         ← /posts/a/b/c    (catch-all)
app/files/[[...path]]/page.tsx       ← optional catch-all (also matches /files)
```

## Route groups (`(group)`)
```
app/(marketing)/about/page.tsx       ← /about     — group doesn't affect URL
app/(marketing)/pricing/page.tsx     ← /pricing
app/(app)/dashboard/page.tsx         ← /dashboard
```
Use to group layouts without affecting URLs.

## Private folders (`_folder`)
```
app/_components/Button.tsx           ← never a route, shared util
```

## Parallel routes (`@slot`)
```
app/dashboard/layout.tsx
app/dashboard/@chart/page.tsx        ← rendered as a named slot
app/dashboard/@list/page.tsx
```
Render multiple pages in one layout (modals, side panels).

## Intercepting routes
`(.)`, `(..)`, `(...)` — render another route's content within the current segment (e.g., photo modal over a feed).

## Real World Usage
- Marketing vs app group layouts in same project
- Dashboard with parallel sections (sidebar nav + main + side-panel)
- Modal overlays via intercepting routes
- Catch-all routes for docs / wiki / CMS-driven pages

## Common Mistakes
- Forgetting `page.tsx` makes a folder route-less
- Putting shared components in route folders (use `_components`)
- Overusing route groups → confusing structure
- Dynamic segment shadowing static (`[id]` matches `'login'`)
- Catch-all collision with deeper routes

## Prerequisites
- [[Next.js App Router]]

## What To Learn Next
- [[Middleware]] · [[Server Actions]] · [[Streaming and Suspense]]

## Best Learning Resources

### Official Documentation
- [Next.js — Routing Fundamentals](https://nextjs.org/docs/app/building-your-application/routing)
- [File conventions](https://nextjs.org/docs/app/api-reference/file-conventions)

### Best YouTube Resource
- [Lee Robinson — App Router routing](https://www.youtube.com/@leerob)
- [Jack Herrington — Routing conventions](https://www.youtube.com/@jherr)

### Best Free Course
- [Next.js Learn — Routing](https://nextjs.org/learn)

### Best Advanced Resource
- [Vercel examples on GitHub](https://github.com/vercel/next.js/tree/canary/examples)

### Best Practice Project
Build an app with: `(marketing)` group for landing/about, `(app)` group with auth-required dashboard, parallel routes for sidebar + main, an intercepting route for a "view photo" modal.

### Recommended Order to Learn
1. `page.tsx` + `layout.tsx`
2. Dynamic + catch-all
3. `loading.tsx` + `error.tsx`
4. Route groups + private folders
5. Parallel routes
6. Intercepting routes
7. Route Handlers (`route.ts`)

## Interview Questions
**Q. Why route groups?**
A. Group routes that share a layout without affecting the URL.

**Q. Layout vs Template?**
A. Layout persists state across navigations. Template recreates state — like a fresh mount.

## Related
- [[Next.js App Router]] · [[Pages Router]] · [[Middleware]] · [[Streaming and Suspense]]
