---
tags: [redis, beginner, syntax]
---

# Redis Strings

> The simplest Redis type. Stores text or binary up to 512 MB per key. Supports atomic counters.

## Core commands
```
SET key value [EX seconds] [NX]
GET key
INCR key                 # atomic +1
INCRBY key 5
DECR key
APPEND key " more"
GETSET key newvalue      # set + return old
MGET k1 k2 k3            # batch read
MSET k1 v1 k2 v2         # batch write
SETNX key value          # set only if not exists (lock primitive)
```

## TTL
```
SET key v EX 60          # expire in 60s
EXPIRE key 60
PEXPIRE key 60000        # ms
TTL key
PERSIST key              # remove TTL
```

## Idioms
- **Counter** — page views, rate limiter: `INCR counter:home`
- **Cache** — `SET user:1 <json> EX 300`
- **Distributed lock** — `SET lock:job NX EX 30` (acquire if not held, auto-expire)
- **Sequence** — `INCR seq:order` returns next monotonic id

## Real World Usage
- Counters (likes, views)
- Cache layer (with TTL)
- Single-use tokens (SETNX + EX)
- Feature flag (`GET flag:new-ui`)

## Common Mistakes
- Using strings to store rich JSON when [[Redis Hashes]] would let you update fields atomically
- No TTL on cache keys → memory leak
- Race on `GET-modify-SET` (use `INCR`, `INCRBY`, or Lua)
- Storing >512 MB (split into chunks or use a different store)

## Prerequisites
- [[Redis]]

## What To Learn Next
- [[Redis Hashes]] · [[Redis Lists and Queues]] · [[Lua Scripting]]

## Best Learning Resources

### Official Documentation
- [Redis Strings docs](https://redis.io/docs/data-types/strings/)
- [Redis command reference](https://redis.io/commands/)

### Best YouTube Resource
- [Hussein Nasser — Redis internals](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU101](https://university.redis.com/)
- [Try Redis (interactive)](https://try.redis.io/)

### Best Advanced Resource
- [Redis source — t_string.c](https://github.com/redis/redis/blob/unstable/src/t_string.c)

### Best Practice Project
Build a per-IP rate limiter with `INCR` + `EXPIRE` Lua atomicity. Confirm correctness under concurrent load with `redis-benchmark`.

### Recommended Order to Learn
1. SET / GET / DEL
2. INCR family
3. TTL + expiration
4. SETNX for locks
5. MGET / MSET for batching

## Interview Questions
**Q. Why use `SET key v NX EX 30` for locks?**
A. NX makes it acquire-only-if-missing; EX adds auto-expiration so a crashed holder doesn't deadlock.

**Q. INCR is atomic — what does that buy?**
A. No race when multiple clients increment the same counter; the single-threaded event loop serializes commands.

## Related
- [[Redis]] · [[Redis Hashes]] · [[Lua Scripting]] · [[Caching]]
