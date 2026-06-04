---
tags: [redis, intermediate, concept]
---

# Eviction and Persistence

> Two orthogonal concerns: how Redis frees memory when full (eviction) and how it survives restarts (persistence).

## Eviction policies
Set `maxmemory` + `maxmemory-policy`:
| Policy            | Behavior                                         |
|-------------------|--------------------------------------------------|
| `noeviction`      | Writes fail when memory full                     |
| `allkeys-lru`     | Evict least-recently-used across all keys        |
| `allkeys-lfu`     | Evict least-frequently-used (Redis 4+)           |
| `allkeys-random`  | Random key                                       |
| `volatile-lru`    | LRU among keys with TTL                          |
| `volatile-lfu`    | LFU among keys with TTL                          |
| `volatile-random` | Random key with TTL                              |
| `volatile-ttl`    | Shortest TTL first                               |

For caches: `allkeys-lru` or `allkeys-lfu`. For persistent data: `noeviction` (or use a different store entirely).

## Persistence — RDB (snapshots)
- Periodic point-in-time dump (`dump.rdb`)
- Fast restore
- Small data loss possible (since last snapshot)
- Configure: `save 900 1` (1 change in 15 min) etc.

## Persistence — AOF (append-only file)
- Logs every write
- `fsync` policy: `always` / `everysec` (default) / `no`
- Larger files; slower restart; less data loss

## Hybrid (recommended)
RDB + AOF together gives fast restart + minimal data loss.

## Replication interaction
- Replicas can be configured to write AOF / RDB too
- Diskless replication available for fast spin-up

## Real World Usage
- Pure cache → no persistence + `allkeys-lru`
- Sessions → AOF + `noeviction` + Sentinel for HA
- Queue store (BullMQ) → AOF + replication, never evict

## Common Mistakes
- Using Redis as a primary DB with `allkeys-lru` (silent data loss)
- AOF `appendfsync always` in latency-sensitive paths (slow)
- No `maxmemory` set → OS killer
- Disabling persistence on a queue → durable until next restart
- Backups stored on the same instance disk

## Prerequisites
- [[Redis]]

## What To Learn Next
- [[Cluster and HA]] · [[Backups and Restore]]

## Best Learning Resources

### Official Documentation
- [Redis Persistence](https://redis.io/docs/management/persistence/)
- [Redis maxmemory + policy](https://redis.io/docs/reference/eviction/)

### Best YouTube Resource
- [Hussein Nasser — Redis persistence](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU301 (operations)](https://university.redis.com/)

### Best Advanced Resource
- [Antirez — RDB + AOF design notes](http://antirez.com/news/)

### Best Practice Project
Set up a Redis with RDB+AOF on Docker. Kill the container during writes; restart; verify how much data is lost vs what's recovered. Compare to AOF-only.

### Recommended Order to Learn
1. maxmemory + LRU
2. RDB snapshots
3. AOF + fsync policies
4. Hybrid persistence
5. Backups to S3
6. Production tuning

## Interview Questions
**Q. RDB vs AOF — when which?**
A. RDB: smaller, faster restart, possible data loss between snapshots. AOF: fewer losses, larger files, slower restart. Most prod uses both.

**Q. Why is `allkeys-lru` dangerous for non-cache data?**
A. Redis silently drops keys to make room; permanent data quietly disappears.

## Related
- [[Cluster and HA]] · [[Backups and Restore]] · [[Caching]]
