---
tags: [infra, performance, intermediate]
---

# Edge Computing

> Run code at hundreds of points-of-presence (POPs) close to users. Cuts round-trip latency dramatically.

## Why it matters
A request from Tokyo to a US-East server takes ~150ms RTT before any logic runs. Edge moves the function to a Tokyo POP — single-digit ms.

## Core ideas
- **POPs** — datacenters near users worldwide
- **Cold starts** — must be tiny; common runtimes are V8 isolates or WASM
- **Stateless** — limited memory/CPU; ephemeral
- **Replicated data** — read locally (D1, Hyperdrive, KV, Durable Objects)
- **Streaming** — flush HTML / SSE from edge

## Platforms
- Cloudflare Workers (V8 isolates) — biggest network
- Vercel Edge Functions (V8 isolates)
- Deno Deploy
- AWS Lambda@Edge / CloudFront Functions
- Fastly Compute@Edge (WASM)

## Real World Usage
- A/B testing + feature flags at edge
- Auth checks before hitting origin
- Image optimization, header rewrites
- Edge-rendered Next.js pages
- Rate limiting + bot detection
- Geo-aware redirects

## Common Mistakes
- Treating edge as long-running Node — different runtime, no `fs`/full Node API
- Heavy CPU work in edge (cold start budgets)
- Reading from a US DB on every request — defeats the purpose; use replicated edge stores
- Ignoring streaming — render at edge means flush early

## Prerequisites
- [[CDN|CDN]] · [[HTTP and HTTPS|HTTP & HTTPS]] · [[Sandboxing]]

## What To Learn Next
- [[WASM]] · [[Convex]] · [[AWS]]

## Best Learning Resources

### Official Documentation
- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/) — best edge dev experience
- [Vercel Edge Functions](https://vercel.com/docs/functions/edge-functions)
- [Deno Deploy](https://docs.deno.com/deploy/)

### Best YouTube Resource
- [Cloudflare Developers (channel)](https://www.youtube.com/c/CloudflareTV) — official deep dives
- [Theo — edge talks](https://www.youtube.com/@t3dotgg)
- [Hussein Nasser — edge architecture](https://www.youtube.com/@hnasr)

### Best Free Course
- [Cloudflare Workers Quickstart](https://developers.cloudflare.com/workers/get-started/) — official, fast
- [Build with Workers (Cloudflare)](https://workers.cloudflare.com/built-with) — examples

### Best Advanced Resource
- [Cloudflare blog — Workers internals](https://blog.cloudflare.com/) — V8 isolates posts
- [Fly.io blog](https://fly.io/blog/) — alternative edge model (microVMs near users)

### Best Practice Project
Build a global URL shortener: Workers + KV for storage, redirect at edge, analytics streamed to a queue. Compare cold/warm latency from 5 regions vs the same hosted on a single AWS US-East server.

### Recommended Order to Learn
1. Single Worker + KV
2. Routing + middleware
3. Durable Objects (single-instance globals)
4. Edge data: D1, Hyperdrive
5. Limits: CPU, memory, time
6. Hybrid edge + origin patterns

## Interview Questions
**Q. Edge functions vs Lambda?**
A. Edge runs in many POPs near users (low latency, tiny cold start). Lambda runs in regions (richer runtime, longer cold starts). Different sweet spots.

**Q. Why V8 isolates over containers?**
A. Microsecond start-up vs ~100ms for containers — essential for per-request edge invocation.

**Q. What's a Durable Object?**
A. A globally-unique single-instance Worker with persistent state — useful for coordination (rooms, counters).

## Related
- [[CDN|CDN]] · [[WASM]] · [[Sandboxing]]
