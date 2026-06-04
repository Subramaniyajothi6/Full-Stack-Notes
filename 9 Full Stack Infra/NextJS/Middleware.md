---
tags: [nextjs, intermediate, routing]
---

# Middleware (Next.js)

> A function that runs *before* a route handler / page renders. Edge-runtime by default. Used for auth gates, redirects, rewrites, A/B routing.

## Setup
```ts
// middleware.ts at project root
import { NextRequest, NextResponse } from 'next/server';

export function middleware(req: NextRequest) {
  const token = req.cookies.get('at')?.value;
  if (!token && req.nextUrl.pathname.startsWith('/dashboard')) {
    const url = req.nextUrl.clone();
    url.pathname = '/login';
    return NextResponse.redirect(url);
  }
  const res = NextResponse.next();
  res.headers.set('x-request-id', crypto.randomUUID());
  return res;
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/protected/:path*'],
};
```

## What you can do
- **Redirect / rewrite** — `NextResponse.redirect`, `NextResponse.rewrite`
- **Set / read cookies** — `req.cookies` / `res.cookies`
- **Set headers** — request id, geo, A/B variant
- **Block** — `new Response('forbidden', { status: 403 })`
- **Pass through** — `NextResponse.next()`

## Constraints (edge runtime)
- No Node APIs (`fs`, `crypto.createHash` from `node:crypto`)
- No native modules
- 1 MB code size limit
- Stateless

For full Node, use a Route Handler instead.

## Real World Usage
- Auth gating for protected sections
- Geo-based redirects + locale routing
- Bot detection / rate limiting at the edge
- Feature-flag-based routing
- Setting tracing headers
- Rewriting to a different backend (A/B testing)

## Common Mistakes
- Heavy DB calls in middleware (runs on every match — slow)
- Forgetting `matcher` and running on every request (assets, images, etc.)
- Using Node-only APIs (must use Web APIs)
- Setting cookies on `res` then forgetting to return that response
- Tying business logic deep inside middleware — keep it edge-cheap

## Prerequisites
- [[Next.js App Router]] · [[Cross-Domain Cookies]]

## What To Learn Next
- [[Server Actions]] · [[Route Handlers]] · [[Caching and Revalidation]]

## Best Learning Resources

### Official Documentation
- [Next.js — Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware)
- [Edge runtime](https://nextjs.org/docs/app/api-reference/edge)

### Best YouTube Resource
- [Lee Robinson — middleware](https://www.youtube.com/@leerob)
- [Theo — middleware patterns](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Next.js Learn — middleware](https://nextjs.org/learn)

### Best Advanced Resource
- [Vercel blog — Edge Middleware](https://vercel.com/blog/edge-middleware)

### Best Practice Project
Add middleware that: (1) gates `/dashboard/*` with cookie check, (2) sets `x-request-id`, (3) redirects users from country X to a localized path. Verify edge runtime cold start ≤ 30ms.

### Recommended Order to Learn
1. `middleware.ts` + matcher
2. Redirects + rewrites
3. Cookies (read/write)
4. Header propagation
5. Edge runtime limits
6. Composing with Route Handlers

## Interview Questions
**Q. Middleware vs Route Handler?**
A. Middleware runs *before* matching a route — for cross-cutting concerns. Route Handlers *are* the route.

**Q. Why edge-only?**
A. Speed and ubiquity — runs near the user at every POP, so adding ms via middleware barely shows.

## Related
- [[Next.js App Router]] · [[Edge Computing]] · [[Route Handlers]]
