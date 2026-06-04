---
tags: [redis, intermediate, syntax]
---

# Redis Hashes

> Map of fields → values inside one key. Cheaper than many string keys when the fields share a prefix.

## Commands
```
HSET user:1 name "A" email "a@b.c" age 30
HGET user:1 email
HMGET user:1 name age
HGETALL user:1
HDEL user:1 age
HINCRBY user:1 logins 1
HEXISTS user:1 email
HKEYS user:1
HVALS user:1
HLEN user:1
HSETNX user:1 name "A"    # set only if field missing
```

## Why hashes over strings
- Update one field without rewriting the whole blob
- Smaller memory footprint (ziplist / listpack encoding for small hashes)
- Atomic per-field increments (`HINCRBY`)
- Cleaner pattern than `user:1:name`, `user:1:email`, ...

## Idiom — partial cache update
```
HSET user:1 email "new@x.com"     # one field
EXPIRE user:1 3600
```

## Real World Usage
- User profiles, session data
- Per-entity counters (`HINCRBY metrics:posts:42 views 1`)
- Light "document" store
- Configuration objects

## Common Mistakes
- Storing huge hashes (>10k fields) — slower commands, encoding switches; consider sharding
- Forgetting `HSET` overwrites a field but keeps others (often desired; sometimes surprising)
- Using hash when a sorted set or list is the right shape
- Treating `HGETALL` on big hashes as cheap

## Prerequisites
- [[Redis]] · [[Redis Strings]]

## What To Learn Next
- [[Redis Lists and Queues]] · [[Redis Sets]] · [[Redis Sorted Sets]]

## Best Learning Resources

### Official Documentation
- [Redis Hashes docs](https://redis.io/docs/data-types/hashes/)
- [Redis memory optimization](https://redis.io/docs/management/optimization/memory-optimization/)

### Best YouTube Resource
- [Hussein Nasser — Redis data structures](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU101](https://university.redis.com/)

### Best Advanced Resource
- [Redis source — t_hash.c](https://github.com/redis/redis/blob/unstable/src/t_hash.c)

### Best Practice Project
Migrate a user-session cache from JSON-in-string to a Hash. Compare memory usage and update latency for changing just one field.

### Recommended Order to Learn
1. HSET / HGET / HGETALL
2. HMGET / HMSET
3. HINCRBY for counters
4. Encoding (ziplist threshold)
5. Sharding very large hashes

## Interview Questions
**Q. When prefer hash over multiple string keys?**
A. Entities with multiple fields you'll often read together — saves keyspace overhead and gives atomic per-field updates.

**Q. Why is `HGETALL` on a 100k-field hash a bad idea?**
A. Blocks the single-threaded loop while serializing the whole hash; can stall other commands.

## Related
- [[Redis Strings]] · [[Redis Lists and Queues]] · [[Eviction and Persistence]]
