---
tags: [redis, intermediate, pattern]
---

# Redis Lists and Queues

> Linked lists with push/pop at both ends. The basis for simple job queues and timelines.

## Commands
```
LPUSH q job1                 # left push
RPUSH q job2                 # right push
LPOP q                       # left pop
RPOP q
LLEN q
LRANGE q 0 9                 # peek first 10
LREM q 0 value               # remove all matches
BLPOP q 5                    # blocking left pop (5s timeout)
BRPOP q 5                    # blocking right pop
BRPOPLPUSH src dst 5         # reliable queue pattern
LMOVE src dst LEFT RIGHT     # modern replacement
```

## Reliable work queue pattern
```
worker:
  job = BRPOPLPUSH q processing 0
  do(job)
  LREM processing 0 job        # ack
```
Crashes leave the job in `processing` for recovery — at-least-once.

## Capped log
```
LPUSH log:user:1 entry
LTRIM log:user:1 0 999       # keep last 1000
```

## Real World Usage
- Background job queue (when BullMQ is overkill)
- Recent-N feed (timeline of last 100 events)
- Audit logs with capped size
- Producer/consumer with backpressure

## Common Mistakes
- Polling with `LPOP` in a tight loop — use `BLPOP` for blocking
- Forgetting `LTRIM` → unbounded list
- Treating `LPOP` as ack — it's already gone if the worker crashes; use the move pattern
- Big `LRANGE 0 -1` on huge lists — blocking

## Prerequisites
- [[Redis]] · [[Redis Strings]]

## What To Learn Next
- [[Redis Streams]] · [[Redis Pub Sub vs Streams]] · [[Background Jobs]]

## Best Learning Resources

### Official Documentation
- [Redis Lists docs](https://redis.io/docs/data-types/lists/)

### Best YouTube Resource
- [Hussein Nasser — Redis queues](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU101](https://university.redis.com/)

### Best Advanced Resource
- [Redis docs — Patterns: Reliable queue](https://redis.io/docs/manual/patterns/distributed-locks/)
- [BullMQ source (built on Lua + lists/streams)](https://github.com/taskforcesh/bullmq)

### Best Practice Project
Build a reliable job queue: `BRPOPLPUSH q processing` + ack via `LREM`, plus a janitor that re-queues processing items older than N seconds.

### Recommended Order to Learn
1. LPUSH / RPUSH / LPOP / RPOP
2. BLPOP for blocking
3. LMOVE / BRPOPLPUSH reliable queue
4. LTRIM capped list
5. When to graduate to Streams

## Interview Questions
**Q. Why use `BLPOP` instead of polling `LPOP`?**
A. Polling burns CPU and adds latency; `BLPOP` blocks server-side until a job arrives.

**Q. Streams vs Lists for queues?**
A. Streams add consumer groups, replay, offsets, and durability semantics. Lists are simpler for single-consumer FIFO.

## Related
- [[Redis Streams]] · [[Background Jobs]] · [[Redis Pub Sub vs Streams]]
