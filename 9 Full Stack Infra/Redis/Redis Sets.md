---
tags: [redis, intermediate, syntax]
---

# Redis Sets

> Unordered collection of unique members. O(1) add/remove/contains.

## Commands
```
SADD tags:post:1 mern redis nodejs
SREM tags:post:1 redis
SMEMBERS tags:post:1
SISMEMBER tags:post:1 nodejs
SCARD tags:post:1                  # size
SRANDMEMBER tags:post:1 3
SPOP tags:post:1                   # remove + return random
SINTER set1 set2                   # intersection
SUNION set1 set2
SDIFF set1 set2
SINTERSTORE dest set1 set2         # store result
```

## Idioms
- **Unique tracking** — `SADD page-viewers:home <userId>`; `SCARD` gives uniques
- **Tag system** — `SADD posts:tagged:mern <postId>`, then `SINTER` to AND tags
- **Permissions** — `SADD user:42:perms read write`
- **Friend list** — `SADD friends:42 5 7 9`, `SINTER friends:42 friends:7` → mutuals

## Real World Usage
- Unique visitor counting (small sets)
- Tag indexes
- Set algebra over user/feature lists
- Banned-list checks (`SISMEMBER`)

## Common Mistakes
- Using sets for ordering — they're unordered; use sorted sets
- Storing millions of members per set without sharding
- Forgetting `SISMEMBER` is O(1) — cheap; abuse it freely
- HyperLogLog (`PFADD`/`PFCOUNT`) is better for *huge* unique counts where small error is OK

## Prerequisites
- [[Redis]] · [[Redis Strings]]

## What To Learn Next
- [[Redis Sorted Sets]] · [[Redis Hashes]]

## Best Learning Resources

### Official Documentation
- [Redis Sets docs](https://redis.io/docs/data-types/sets/)
- [Redis HyperLogLog](https://redis.io/docs/data-types/probabilistic/hyperloglogs/)

### Best YouTube Resource
- [Hussein Nasser — Redis Sets](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU101](https://university.redis.com/)

### Best Advanced Resource
- [Redis source — t_set.c](https://github.com/redis/redis/blob/unstable/src/t_set.c)

### Best Practice Project
Build a "users who liked both X and Y" feature using `SINTER` over per-post like sets. Then compare memory to a HyperLogLog approximation.

### Recommended Order to Learn
1. SADD / SREM / SMEMBERS / SISMEMBER
2. SCARD / SRANDMEMBER / SPOP
3. SINTER / SUNION / SDIFF
4. *STORE variants
5. HyperLogLog for huge unique counts

## Interview Questions
**Q. Set vs Sorted Set?**
A. Sets are unordered + uniqueness. Sorted sets add a score for ordering and range queries.

**Q. When use HyperLogLog?**
A. Approximate unique counts over huge cardinality (~12 KB fixed; <1% error). Set is exact but memory-hungry.

## Related
- [[Redis Sorted Sets]] · [[Redis Hashes]] · [[Redis Strings]]
