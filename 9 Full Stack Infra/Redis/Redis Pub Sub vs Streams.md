---
tags: [redis, intermediate, concept]
---

# Redis Pub Sub vs Streams

> Two messaging primitives. Pub/Sub is fire-and-forget. Streams are durable Kafka-lite.

## Pub/Sub
```
SUBSCRIBE channel:chat
PUBLISH channel:chat "hello"
```
- Fan-out to all subscribers
- No durability — messages while no one's listening are lost
- No replay
- Good for: presence, live notifications where loss is tolerable

## Streams
```
XADD stream:events * type signup userId 42
XREAD BLOCK 0 STREAMS stream:events $
XLEN stream:events
XRANGE stream:events - +
XGROUP CREATE stream:events grp1 $ MKSTREAM
XREADGROUP GROUP grp1 worker1 BLOCK 0 COUNT 10 STREAMS stream:events >
XACK stream:events grp1 <id>
```
- Append-only durable log
- Consumer groups (each message processed by one worker in the group)
- Replay from any id
- Acknowledgment + pending entries list
- Good for: event sourcing, reliable async work, audit trails

## When to use which
| Need                         | Pick     |
|------------------------------|----------|
| Live UI notifications        | Pub/Sub  |
| At-least-once async work     | Streams  |
| Replay last hour of events   | Streams  |
| Lowest latency, lossy        | Pub/Sub  |
| Audit log                    | Streams  |

## Real World Usage
- Pub/Sub: Socket.IO multi-instance adapter, chat presence
- Streams: BullMQ alternative, event sourcing, CDC pipelines
- Combine: Streams for durability, Pub/Sub-fanned-out cache invalidation

## Common Mistakes
- Assuming Pub/Sub messages persist → silent data loss
- Using Streams without consumer groups when fan-out was intended
- Unbounded Stream growth — use `XADD ... MAXLEN ~ 1000000`
- Forgetting `XACK` → pending list grows; reprocessed-on-restart confusion

## Prerequisites
- [[Redis]] · [[Redis Lists and Queues]]

## What To Learn Next
- [[Background Jobs]] · [[Realtime with Socket.IO]] · [[Message Queues]]

## Best Learning Resources

### Official Documentation
- [Redis Pub/Sub docs](https://redis.io/docs/manual/pubsub/)
- [Redis Streams docs](https://redis.io/docs/data-types/streams/)

### Best YouTube Resource
- [Hussein Nasser — Streams + Pub/Sub](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU202 (Streams)](https://university.redis.com/)

### Best Advanced Resource
- [Antirez (Redis creator) — Streams design](http://antirez.com/news/114) — origin story

### Best Practice Project
Build the same notification system twice: once with Pub/Sub (lossy), once with Streams + consumer group (reliable). Kill a worker mid-message and observe behavior.

### Recommended Order to Learn
1. Pub/Sub basics
2. Stream `XADD` + `XREAD`
3. Consumer groups (`XREADGROUP`, `XACK`)
4. Pending entries + claim
5. `MAXLEN` for retention
6. Cross-process patterns

## Interview Questions
**Q. Why is Pub/Sub fire-and-forget?**
A. No persistence layer; if a subscriber isn't connected, the message is gone.

**Q. Streams consumer group — what guarantees?**
A. Each message in the stream is delivered to one worker in the group. Workers must `XACK` or messages remain in the pending list for claim/retry.

## Related
- [[Redis Lists and Queues]] · [[Message Queues]] · [[Background Jobs]] · [[Realtime with Socket.IO]]
