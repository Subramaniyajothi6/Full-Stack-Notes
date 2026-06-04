---
tags: [redis, advanced, concept]
---

# Redis Streams

> Append-only log inside Redis. Consumer groups, replay, retention — a small Kafka.

## Add and read
```
XADD stream * field1 v1 field2 v2     # * = auto id
XLEN stream
XRANGE stream - +                     # all entries
XREAD COUNT 10 BLOCK 0 STREAMS stream $   # tail from now
```

## Consumer groups
```
XGROUP CREATE stream grp1 $ MKSTREAM
XREADGROUP GROUP grp1 worker1 BLOCK 0 COUNT 10 STREAMS stream >
# process message
XACK stream grp1 <id>
```
- `>` means "new messages I haven't seen"
- Pending list per consumer until ACK
- `XCLAIM` to reassign stuck messages from a dead worker

## Capped stream
```
XADD stream MAXLEN ~ 1000000 * type signup ...
```
`~` means "approximately" — much faster than exact.

## Inspect
```
XINFO STREAM stream
XINFO GROUPS stream
XPENDING stream grp1
```

## Real World Usage
- Reliable async work queues
- Event sourcing
- Audit trails
- Change Data Capture (CDC) ingestion
- Activity feeds with replay

## Common Mistakes
- Forgetting `MAXLEN` → unbounded growth
- Not ACKing → pending list grows; reprocessing storms on restart
- Using Streams when Lists would do (simpler FIFO, no groups needed)
- Treating IDs as plain integers (they're `ms-seq` strings)
- Missing `XCLAIM` for dead-worker recovery

## Prerequisites
- [[Redis]] · [[Redis Lists and Queues]] · [[Redis Pub Sub vs Streams]]

## What To Learn Next
- [[Background Jobs]] · [[Message Queues]] · [[Cluster and HA]]

## Best Learning Resources

### Official Documentation
- [Redis Streams docs](https://redis.io/docs/data-types/streams/)
- [Streams tutorial](https://redis.io/docs/data-types/streams-tutorial/)

### Best YouTube Resource
- [Hussein Nasser — Redis Streams deep dive](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU202](https://university.redis.com/)

### Best Advanced Resource
- [Antirez — Streams introduction post](http://antirez.com/news/114)

### Best Practice Project
Build a webhook delivery pipeline: producers `XADD`, workers in a consumer group fetch, deliver with retry, ACK on success or `XCLAIM` after timeout. Compare to a List-based equivalent.

### Recommended Order to Learn
1. XADD / XREAD
2. Consumer groups + XACK
3. XPENDING / XCLAIM
4. MAXLEN retention
5. Sharded streams across cluster
6. Stream + Sentinel/Cluster ops

## Interview Questions
**Q. Streams vs Pub/Sub?**
A. Streams are durable, replayable, ACK-based, with consumer groups. Pub/Sub is fire-and-forget.

**Q. What happens to messages of a crashed worker?**
A. They sit in the pending entries list; another worker can `XCLAIM` after a timeout.

## Related
- [[Redis Lists and Queues]] · [[Redis Pub Sub vs Streams]] · [[Background Jobs]] · [[Message Queues]]
