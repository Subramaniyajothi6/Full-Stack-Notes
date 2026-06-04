---
tags: [moc, redis, database]
---

# Redis MOC

> In-memory data structure store. Cache, session store, queue, pub/sub, leaderboard, distributed lock — all in one tool.

## Overview
- [[Redis]] — what / why / when

## Data structures
- [[Redis Strings]] — strings, counters, locks
- [[Redis Hashes]] — field/value maps
- [[Redis Lists and Queues]] — push/pop, blocking pop
- [[Redis Sets]] — uniqueness, set algebra
- [[Redis Sorted Sets]] — leaderboards, time-series, sliding windows

## Messaging
- [[Redis Pub Sub vs Streams]] — choose your messaging model
- [[Redis Streams]] — consumer groups + durability

## Advanced
- [[Lua Scripting]] — atomic multi-key ops
- [[Eviction and Persistence]] — memory limits, RDB, AOF
- [[Cluster and HA]] — sharding, replicas, Sentinel

## Suggested order
1. [[Redis]] overview
2. [[Redis Strings]] → [[Redis Hashes]] → [[Redis Lists and Queues]]
3. [[Redis Sets]] → [[Redis Sorted Sets]]
4. [[Redis Pub Sub vs Streams]] → [[Redis Streams]]
5. [[Lua Scripting]]
6. [[Eviction and Persistence]] → [[Cluster and HA]]

## Roadmap to fill in
- [ ] Bitmaps + bit operations
- [ ] HyperLogLog (approximate uniques)
- [ ] Geo commands
- [ ] Redis JSON module
- [ ] Redis Search (FT.*)
- [ ] Client libraries comparison (ioredis vs node-redis)
- [ ] Memory analysis (`MEMORY USAGE`, `BIG_KEYS`)
- [ ] Latency monitoring + `slowlog`

## Related stacks
- [[System Design MOC]] — caching, message queues, pub/sub
- [[Express MOC]] — sessions, rate limiting
- [[NodeJS MOC]] — BullMQ workers
- [[MERN Stack MOC]] — [[Caching Layers]] · [[Background Jobs]] · [[Realtime with Socket.IO]]

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
