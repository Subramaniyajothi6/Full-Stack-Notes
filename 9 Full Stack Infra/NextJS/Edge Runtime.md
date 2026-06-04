---
tags: [nextjs, advanced, performance]
---

# Edge Runtime

> Next.js routes (middleware, route handlers, server components) can opt into running on V8 isolates at edge POPs.

## How to opt in
```ts
export const runtime = 'edge';     // or 'nodejs' (default)
```
Set on a Route Handler, Server Component, Middleware, or `layout.tsx`.

## What you get
- Cold start ~5–30 ms (vs ~100–500 ms for Node serverless)
- Globally distributed
- Streaming-friendly
- Cheaper per-request

## What you lose
- No Node-only APIs (`fs`, `child_process`, `node:crypto.createHash` API surface limited)
- No native modules
- Code size limit (typically 1–4 MB)
- Limited DB drivers (need HTTP-based / Web-compatible — Neon HTTP, PlanetScale Database-JS, Upstash REST, Convex)
- Memory limits (~128 MB)

## Compatible DB / KV
- **Neon** — HTTP serverless driver
- **PlanetScale** — Database.js
- **Upstash Redis** — REST API
- **Cloudflare D1 / KV / R2**
- **Convex** — see [[Convex]]
- **Vercel Postgres** — pooled
- **MongoDB Atlas Data API** (REST)

## When to choose edge
- Personalization / A/B at edge → middleware
- Geo-aware redirects → middleware
- Static-ish API with simple data → edge route handlers
- AI streaming responses (LLM provider clients are Web-compatible)
- Latency-sensitive paths with low DB needs

## When to stay on Node
- Heavy DB drivers (Prisma classic, native Mongo driver with TCP)
- File system access
- Long CPU work (image processing, server-side PDF gen)
- Large binary deps (FFmpeg, sharp)

## Real World Usage
- Vercel AI SDK chat endpoints → edge (LLM streaming)
- Auth + geo middleware → edge
- Image transformations → edge runtime + Cloudflare-style
- Webhook receivers that just enqueue → edge

## Common Mistakes
- Importing a Node-only lib accidentally (build failure)
- Hitting code-size limit with big deps
- Using `process.env` reads at module-level (some don't propagate to edge unless declared)
- Using a TCP Postgres client at edge — must use HTTP / pooled
- Long-running CPU tasks (timeouts are tighter)

## Prerequisites
- [[Edge Computing]] · [[Sandboxing]] · [[Next.js App Router]]

## What To Learn Next
- [[Streaming and Suspense]] · [[Caching and Revalidation]]

## Best Learning Resources

### Official Documentation
- [Next.js — Edge runtime](https://nextjs.org/docs/app/api-reference/edge)
- [Vercel Edge Functions](https://vercel.com/docs/functions/edge-functions)

### Best YouTube Resource
- [Theo — Edge vs Node tradeoffs](https://www.youtube.com/@t3dotgg)
- [Lee Robinson — Edge perf](https://www.youtube.com/@leerob)

### Best Free Course
- [Next.js Learn](https://nextjs.org/learn)
- [Cloudflare Workers docs](https://developers.cloudflare.com/workers/)

### Best Advanced Resource
- [Vercel blog — runtime selection](https://vercel.com/blog)
- [Cloudflare blog — V8 isolates](https://blog.cloudflare.com/)

### Best Practice Project
Build the same API two ways: Node runtime with Prisma, edge runtime with Neon HTTP driver. Compare cold/warm latency from 3 regions; measure cost.

### Recommended Order to Learn
1. `runtime` directive
2. Web Request / Response APIs
3. Edge-compatible DB drivers
4. Streaming with `ReadableStream`
5. Cold start budgets
6. Production decision: edge vs Node per route

## Interview Questions
**Q. Edge runtime vs Node runtime in Next.js?**
A. Edge runs on V8 isolates near users — tiny cold start, Web API only. Node runs Node serverless — slower cold start, full API surface.

**Q. Why might Prisma not work at edge?**
A. The default driver uses TCP and a Node engine; edge needs HTTP-based / Web-compatible drivers (Prisma Accelerate, Neon HTTP, PlanetScale Database.js).

## Related
- [[Next.js App Router]] · [[Edge Computing]] · [[Middleware]] · [[Streaming and Suspense]]
