---
tags: [infra, database, intermediate]
---

# Redis

> In-memory data structure store. Key-value with rich types: strings, hashes, lists, sets, sorted sets, streams, geo, bitmaps.

## Why it matters
The Swiss army knife of backend. Cache, session store, rate limiter, queue, leaderboard, pub/sub, distributed lock — all in one tool.

## Core ideas
- **Single-threaded command loop** — atomic ops by default
- **Persistence** — RDB (snapshot) + AOF (append-only log)
- **Replication** — primary → replicas (async)
- **Cluster** — sharded across nodes (slot-based)
- **Sentinel** — HA monitoring + failover
- **Lua scripts** — atomic multi-key ops
- **Eviction policies** — LRU, LFU, allkeys-random, etc.

## Cheat sheet
```
SET k v EX 60         # cache with TTL
INCR counter
LPUSH q "job"
RPOPLPUSH q processing  # reliable queue pattern
HSET user:1 name "A"
ZADD leaderboard 100 "alice"
PUBLISH chan "msg"
EVAL "return redis.call(...)" 0  # atomic Lua
```

## Real World Usage
- Cache (read-through, write-through)
- Session store
- Rate limiter (token bucket via Lua)
- Job queue (BullMQ, Sidekiq)
- Pub/Sub (Socket.IO scaling)
- Leaderboards via sorted sets
- Distributed locks (Redlock — debated, see Kleppmann)

## Common Mistakes
- Using `KEYS *` in production (blocks) — use `SCAN`
- No `maxmemory` + eviction policy → OOM
- Treating Pub/Sub as durable (it's fire-and-forget; use Streams for durability)
- Storing large blobs (Redis is in-memory — costly)
- Forgetting to set TTL on cache keys → memory leak

## Prerequisites
- [[Caching|Caching]]

## What To Learn Next
- [[Message Queues|Message Queues]] · [[Pub Sub|Pub/Sub]] · [[Vector Databases]]

## Best Learning Resources

### Official Documentation
- [Redis docs](https://redis.io/docs/) — clear examples per command
- [Redis University](https://university.redis.com/) — free official courses

### Best YouTube Resource
- [Hussein Nasser — Redis internals](https://www.youtube.com/@hnasr)
- [ByteByteGo — Redis system design](https://www.youtube.com/c/ByteByteGo)

### Best Free Course
- [Redis University — RU101: Intro to Redis](https://university.redis.com/) — official, free
- [Try Redis](https://try.redis.io/) — interactive

### Best Advanced Resource
- [Redis Best Practices](https://redis.io/docs/manual/patterns/) — official patterns
- [Aphyr / Kyle Kingsbury — distributed systems analyses](https://aphyr.com/) — Redlock and consistency

### Best Practice Project
Add Redis to an existing app for: response caching with TTL, a sliding-window rate limiter via Lua, a BullMQ background job queue, and Socket.IO scaling via Redis adapter. Document hit ratios and queue throughput.

### Recommended Order to Learn
1. String + hash basics
2. Lists + sets + sorted sets
3. TTL + eviction
4. Pub/Sub vs Streams
5. Lua scripting
6. Replication, cluster, persistence

## Interview Questions
**Q. Why is Redis fast?**
A. In-memory, single-threaded loop, optimized C, zero-copy networking, simple data structures.

**Q. Pub/Sub vs Streams?**
A. Pub/Sub is fire-and-forget — no replay, no offsets. Streams are durable log-like with consumer groups (Kafka-lite).

**Q. How would you implement a rate limiter?**
A. Sliding window: Lua script using ZSET with timestamps; remove old entries; check count.

**Q. What does `EXPIRE` actually do?**
A. Marks TTL; key is lazily evicted on access OR proactively by background expiration sampling.

**Q. Risks with `KEYS *`?**
A. Blocks the single-threaded loop on large datasets — production outage.

## Related
- [[Caching|Caching]] · [[Message Queues|Message Queues]]
