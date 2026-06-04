---
tags: [mern, performance, intermediate]
---

# Caching Layers

> A request can be served from many places before reaching the DB. Each layer cuts latency and load.

## The cache hierarchy (closest to user → furthest)
```
Browser cache       (100% local, ~0ms)
   ↓ miss
CDN edge            (regional, 5–30ms)
   ↓ miss
Reverse proxy       (Varnish / nginx, ~1ms intra-DC)
   ↓ miss
App-level cache     (in-process LRU, microseconds)
   ↓ miss
Distributed cache   (Redis / Memcached, 1–3ms)
   ↓ miss
DB query cache      (Postgres shared buffers / Mongo WiredTiger)
   ↓ miss
DB on disk          (worst case)
```

Aim to push hits as far up the chain as you can.

## Browser + CDN (HTTP cache)
```
Cache-Control: public, max-age=31536000, immutable    ← hashed JS bundle
Cache-Control: public, max-age=300, s-maxage=3600     ← API list response
Cache-Control: private, no-store                      ← personalized data
ETag: "abc123"                                        ← conditional GET
```

`stale-while-revalidate`: serve stale immediately, refresh in background.

## Reverse-proxy cache
nginx `proxy_cache` or Varnish in front of the API caches GETs by URL+headers. Useful for unauth endpoints that change slowly.

## App-level cache (in-process)
```ts
import { LRUCache } from 'lru-cache';
const cache = new LRUCache<string, any>({ max: 1000, ttl: 60_000 });

async function getUser(id: string) {
  const hit = cache.get(id);
  if (hit) return hit;
  const u = await User.findById(id);
  cache.set(id, u);
  return u;
}
```
Per-instance — fast but inconsistent across replicas. Good for read-mostly hot keys.

## Distributed cache (Redis)
```ts
import Redis from 'ioredis';
const r = new Redis(process.env.REDIS_URL);

async function getUser(id: string) {
  const k = `user:${id}`;
  const cached = await r.get(k);
  if (cached) return JSON.parse(cached);
  const u = await User.findById(id);
  await r.set(k, JSON.stringify(u), 'EX', 300);  // 5-min TTL
  return u;
}
```
Shared across instances; consistent; survives restarts.

## Cache-aside vs write-through vs write-behind
- **Cache-aside (lazy)** — read miss → load → cache. Most common.
- **Write-through** — every write goes to DB + cache. Strong consistency, slower writes.
- **Write-behind** — write to cache, async to DB. Risk of loss; rare in CRUD apps.

## Invalidation patterns
- **TTL-only** — accept staleness up to TTL
- **Explicit invalidate on write** — `await r.del('user:' + id)` on update
- **Event-driven** — DB change stream → publish → subscribers invalidate
- **Tag-based** — group related keys; invalidate by tag

## Cache stampede
Many cache misses hit DB simultaneously when a hot key expires:
- **Lock + recompute** — first miss locks; others wait
- **Jittered TTL** — `ttl + random(jitter)` so keys don't expire together
- **Stale-while-revalidate** — serve stale; refresh in background
- **Probabilistic early refresh** — refresh before expiry with rising probability

## Real World Usage
- Static assets (CDN, very long max-age)
- Public API responses (s-maxage at CDN)
- User profile lookups (Redis, short TTL)
- Computed aggregates (per-tenant dashboards)
- Search autocompletion
- Session storage

## Common Mistakes
- Caching personalized responses on a shared CDN (data leak between users)
- TTL too long → users see stale data
- TTL too short → cache hit rate near zero
- No invalidation on writes → permanent staleness
- Caching everything (premature optimization; many endpoints are fast enough)
- Forgetting to vary cache key by auth context (user-scoped responses cached globally)
- Cache key collisions (key the version/schema in)
- No metrics → can't measure hit ratio

## Prerequisites
- [[Caching]] · [[CDN]] · [[Redis]]

## What To Learn Next
- [[Realtime with Socket.IO]] · [[Background Jobs]]

## Best Learning Resources

### Official Documentation
- [MDN — HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
- [Cloudflare — Cache control](https://developers.cloudflare.com/cache/concepts/cache-control/)
- [Redis caching patterns](https://redis.io/docs/manual/patterns/)
- [Varnish documentation](https://varnish-cache.org/)

### Best YouTube Resource
- [Hussein Nasser — Caching internals](https://www.youtube.com/@hnasr)
- [ByteByteGo — Caching strategies](https://www.youtube.com/c/ByteByteGo)

### Best Free Course
- [Cloudflare Learning Center — caching](https://www.cloudflare.com/learning/cache/)
- [High Performance Browser Networking — Ilya Grigorik (free)](https://hpbn.co/)

### Best Advanced Resource
- [DDIA — Caching chapters](https://dataintensive.net/)
- [Engineering blogs from Stack Overflow / Discord / Shopify](https://stackoverflow.blog/) — real cache stories

### Best Practice Project
Pick a slow endpoint in your app. Measure baseline p50/p95. Add app-level LRU → measure. Promote to Redis → measure. Add CDN cache headers → measure. Document hit ratio + latency at each layer.

### Recommended Order to Learn
1. HTTP cache headers
2. CDN caching for static + APIs
3. App-level LRU
4. Redis cache-aside
5. Invalidation patterns
6. Cache stampede mitigation
7. Observability (hit ratio dashboards)

## Interview Questions
**Q. What's a cache stampede?**
A. Many simultaneous misses on a hot key all stampede the DB. Mitigate with locks, jittered TTL, or stale-while-revalidate.

**Q. Why is cache invalidation hard?**
A. Producing the right invalidation set on every write is correlated with all read paths — easy to miss one. TTL is a forgiveness mechanism.

**Q. CDN vs Redis — when which?**
A. CDN: edge-cacheable HTTP responses for many users. Redis: dynamic per-user-scoped data inside the data center.

## Related
- [[Caching]] · [[CDN]] · [[Redis]] · [[Realtime with Socket.IO]] · [[Background Jobs]]
