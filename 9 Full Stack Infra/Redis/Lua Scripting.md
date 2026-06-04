---
tags: [redis, advanced, pattern]
---

# Lua Scripting

> Run a Lua script atomically on the Redis server. The way to do multi-key transactions safely.

## Why
Multiple Redis commands aren't atomic by default. `EVAL` runs a Lua block as a single command — perfect for read-modify-write across keys.

## EVAL signature
```
EVAL "script" numKeys key1 key2 ... arg1 arg2 ...
```
Inside Lua: `KEYS[i]` and `ARGV[i]` arrays.

## Sliding-window rate limit
```lua
-- KEYS[1]=key, ARGV[1]=now ms, ARGV[2]=window ms, ARGV[3]=max
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local max = tonumber(ARGV[3])

redis.call('ZREMRANGEBYSCORE', key, 0, now - window)
local count = redis.call('ZCARD', key)
if count >= max then
  return 0
end
redis.call('ZADD', key, now, now .. '-' .. math.random())
redis.call('PEXPIRE', key, window)
return 1
```

## Caching scripts — `EVALSHA`
```
SCRIPT LOAD "script" → returns sha
EVALSHA <sha> numKeys ...
```
Server caches the script; clients send the sha to avoid resending source.

## Real World Usage
- Atomic rate limiters
- Reliable counter + ttl
- "Compare-and-swap" semantics
- Lock release that checks ownership
- Sliding-window leaderboards

## Common Mistakes
- Long-running scripts block the single-threaded loop (cap iteration; consider Redis Functions for newer Redis)
- Forgetting `redis.call` errors raise — wrap in `pcall` if you need to handle them
- Putting blocking commands (`BLPOP`) inside scripts (not allowed)
- Hard-coding key names instead of passing them as KEYS (breaks Redis Cluster routing)

## Prerequisites
- [[Redis]] · [[Redis Sorted Sets]]

## What To Learn Next
- [[Redis Streams]] · [[Cluster and HA]]

## Best Learning Resources

### Official Documentation
- [Redis EVAL docs](https://redis.io/docs/manual/programmability/eval-intro/)
- [Redis Functions (newer alternative)](https://redis.io/docs/manual/programmability/functions-intro/)

### Best YouTube Resource
- [Hussein Nasser — Redis scripting](https://www.youtube.com/@hnasr)

### Best Free Course
- [Lua in 15 Minutes](https://learnxinyminutes.com/docs/lua/) — Lua basics

### Best Advanced Resource
- [Redis Best Practices — Lua patterns](https://redis.io/docs/manual/programmability/lua-api/)
- [BullMQ source code — heavy Lua usage](https://github.com/taskforcesh/bullmq)

### Best Practice Project
Replace a hand-rolled `MULTI`/`EXEC` rate-limit attempt with a Lua script. Verify correctness under concurrent abuse with a k6 load test.

### Recommended Order to Learn
1. EVAL basics
2. KEYS vs ARGV
3. SCRIPT LOAD + EVALSHA
4. Common scripts (rate limit, lock release)
5. Redis Functions (Redis 7+)

## Interview Questions
**Q. Why is Lua atomic in Redis?**
A. The single-threaded server runs the script as one command — no other client can interleave.

**Q. KEYS vs ARGV — why both?**
A. KEYS lets Redis Cluster route the script correctly (all keys must hash to same slot); ARGV is plain data.

## Related
- [[Redis Sorted Sets]] · [[Redis Streams]] · [[Rate Limiting]]
