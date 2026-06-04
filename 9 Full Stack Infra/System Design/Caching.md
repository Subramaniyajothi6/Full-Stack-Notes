---
tags: [system-design, intermediate, performance]
---

# Caching

> Store hot data closer to consumer. Trade staleness for latency.

## Layers
- Browser cache (Cache-Control)
- CDN edge — see [[CDN]]
- Reverse proxy (Varnish, Nginx)
- App-level (in-memory LRU)
- Distributed (Redis, Memcached)
- DB query cache

## Patterns
- **Cache-aside (lazy)** — read miss → load → cache
- **Write-through** — write to cache + DB together
- **Write-behind** — write to cache, async to DB
- **TTL + stale-while-revalidate**

## Pitfalls
- Cache stampede — many misses hit DB at once. Mitigate with locks, jittered TTLs, request coalescing.
- Cache invalidation — "the second hardest thing"
- Caching personalized responses on shared CDN

## Related
- [[CDN]] · [[Database Indexing]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Common Mistakes
- TODO: pitfalls and edge cases

## Best Learning Resources

### Official Documentation
- https://aws.amazon.com/architecture/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. ByteByteGo, Hussein Nasser

### Best Free Course
- TODO

### Best Advanced Resource
- TODO

### Best Practice Project
- TODO: 1-paragraph project idea

### Recommended Order to Learn
1. TODO
2. TODO
3. TODO

## Interview Questions
**Q. TODO** — A. ...

**Q. TODO** — A. ...
