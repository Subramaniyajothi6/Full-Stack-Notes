---
tags: [redis, intermediate, pattern]
---

# Redis Sorted Sets

> Set with a score per member. Ordered by score; supports range queries. Foundation of leaderboards and time-series storage.

## Commands
```
ZADD scores 100 alice 90 bob 120 carol
ZRANGE scores 0 -1 WITHSCORES        # ascending
ZREVRANGE scores 0 9 WITHSCORES      # top 10
ZRANGEBYSCORE scores 80 110          # score range
ZRANGEBYLEX names "[a" "[m"          # lexicographic range
ZRANK scores bob                     # 0-based rank
ZREVRANK scores bob                  # rank descending
ZINCRBY scores 5 alice
ZREM scores bob
ZCARD scores
ZPOPMIN / ZPOPMAX scores
```

## Idioms

### Leaderboard
```
ZADD leaderboard 1000 player:42
ZINCRBY leaderboard 25 player:42
ZREVRANGE leaderboard 0 9 WITHSCORES    # top 10
ZREVRANK leaderboard player:42          # my rank
```

### Time-bucketed events
Score = unix timestamp; range queries cover time windows:
```
ZADD events:user:42 1715800000 "login"
ZRANGEBYSCORE events:user:42 1715000000 1716000000
```

### Sliding-window rate limit
```
ZADD reqs:user:42 <now> <uuid>
ZREMRANGEBYSCORE reqs:user:42 -inf <now - 60s>
ZCARD reqs:user:42                       # request count in last 60s
```

## Real World Usage
- Game leaderboards
- Recent items (`score = timestamp`)
- Sliding-window rate limits
- Priority queues
- Auto-complete via lex ranges (with [[Redis Hashes]] for metadata)

## Common Mistakes
- Using `ZRANGE` when you want descending (use `ZREVRANGE` or `ZRANGE ... REV`)
- Forgetting `WITHSCORES` when you need them
- Treating scores as integers when float drift exists
- Unbounded growth — combine with `ZREMRANGEBYRANK` to trim

## Prerequisites
- [[Redis]] · [[Redis Sets]]

## What To Learn Next
- [[Lua Scripting]] · [[Redis Streams]] · [[Rate Limiting]]

## Best Learning Resources

### Official Documentation
- [Redis Sorted Sets docs](https://redis.io/docs/data-types/sorted-sets/)

### Best YouTube Resource
- [Hussein Nasser — Sorted Sets](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU101](https://university.redis.com/)

### Best Advanced Resource
- [Skip list internals (Wikipedia)](https://en.wikipedia.org/wiki/Skip_list) — Redis uses skip lists for sorted sets

### Best Practice Project
Build a global leaderboard + per-country leaderboards + a "near my rank" view (5 above / 5 below) using `ZREVRANK` + `ZREVRANGE`.

### Recommended Order to Learn
1. ZADD + ZRANGE
2. ZREVRANGE + WITHSCORES
3. ZRANGEBYSCORE (range queries)
4. ZRANK / ZREVRANK
5. ZREMRANGEBYRANK / SCORE for cleanup
6. Sliding-window rate limiter

## Interview Questions
**Q. Sorted Set time complexity?**
A. ZADD/ZSCORE/ZRANK: O(log N). ZRANGE: O(log N + M).

**Q. Why skip list?**
A. Probabilistic balanced ordering with simpler implementation than red-black trees, better for in-memory.

## Related
- [[Redis Sets]] · [[Lua Scripting]] · [[Rate Limiting]]
