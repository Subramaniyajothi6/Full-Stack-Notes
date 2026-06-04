---
tags: [nextjs, intermediate, syntax]
---

# Route Handlers

> Files at `app/.../route.ts` exporting HTTP methods. Replace `pages/api/*` in the App Router; full Web Request/Response.

## Anatomy
```ts
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(req: NextRequest) {
  const users = await db.user.findMany();
  return NextResponse.json(users);
}

export async function POST(req: NextRequest) {
  const body = await req.json();
  const user = await db.user.create({ data: body });
  return NextResponse.json(user, { status: 201 });
}

// Dynamic
// app/api/users/[id]/route.ts
export async function GET(req: NextRequest, { params }: { params: { id: string } }) {
  ...
}
```

## When to use Route Handlers vs Server Actions
| Route Handler                          | Server Action                          |
| -------------------------------------- | -------------------------------------- |
| External callers (mobile, 3rd-party)   | Same-app mutations                      |
| Webhooks (Stripe, GitHub)              | Form submits                            |
| Streaming / SSE responses              | Form / state mutations                  |
| File downloads                          | Optimistic updates                      |
| OAuth callbacks                         | When you want zero boilerplate          |

## Runtimes
```ts
export const runtime = 'edge';   // or 'nodejs' (default)
```
Edge: smaller cold start, no Node APIs. Node: full Node, larger cold start.

## Caching
Route Handlers cache `GET`s by default in production. Opt out:
```ts
export const dynamic = 'force-dynamic';
// or
export const revalidate = 60;
```

## Streaming response
```ts
export async function GET() {
  const stream = new ReadableStream({
    start(controller) {
      controller.enqueue('hello');
      setTimeout(() => { controller.enqueue(' world'); controller.close(); }, 500);
    },
  });
  return new Response(stream);
}
```

## Real World Usage
- REST/JSON APIs for mobile + 3rd-party
- Stripe / GitHub webhooks (need raw body — see Webhooks note)
- OAuth callbacks
- SSE streams
- File uploads (signed URL generators)
- Public APIs with rate limiting

## Common Mistakes
- Returning plain objects (must be `Response` / `NextResponse`)
- Forgetting that `GET` caches by default in prod → stale lists
- Mixing Edge runtime with Node-only libraries (will fail at deploy)
- Reading `req.body` twice (it's a stream)
- Not validating input — public endpoints

## Prerequisites
- [[Next.js App Router]] · [[Middleware]] · [[REST API Design]]

## What To Learn Next
- [[Server Actions]] · [[Caching and Revalidation]] · [[Edge Runtime]]

## Best Learning Resources

### Official Documentation
- [Next.js — Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)

### Best YouTube Resource
- [Lee Robinson — Route Handlers](https://www.youtube.com/@leerob)
- [Theo — when to use API routes](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Next.js Learn](https://nextjs.org/learn)

### Best Advanced Resource
- [Next.js examples repo](https://github.com/vercel/next.js/tree/canary/examples)

### Best Practice Project
Add a `/api/webhooks/stripe/route.ts` route that consumes raw body, verifies signature, dedups events. Then add `/api/users/[id]/route.ts` with GET/PATCH/DELETE protected by middleware.

### Recommended Order to Learn
1. GET + POST handlers
2. Dynamic `[param]/route.ts`
3. Validation with Zod
4. Caching directives (`dynamic`, `revalidate`)
5. Edge vs Node runtime
6. Streaming + SSE
7. Webhooks (raw body)

## Interview Questions
**Q. Route Handler vs Server Action?**
A. Route Handlers expose HTTP; useful for external consumers. Server Actions are RPC for the same app — simpler but tied to Next.

**Q. Why are GETs cached by default in prod?**
A. Performance — Next assumes pure GETs. Use `dynamic = 'force-dynamic'` for user-scoped data.

## Related
- [[Next.js App Router]] · [[Server Actions]] · [[Middleware]] · [[Webhooks]]
