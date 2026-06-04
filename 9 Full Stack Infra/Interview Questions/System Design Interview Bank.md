---
tags: [interview, system-design]
---

# System Design Interview Bank

## Walkthrough framework
1. Clarify scope + scale (RPS, data size, latency)
2. Define APIs
3. High-level architecture (LB → app → DB → cache)
4. Data model
5. Deep dive on one part (caching, sharding, queueing)
6. Bottlenecks + tradeoffs
7. Failure modes

## Common questions
**Q. Design URL shortener.**
- Hash or counter → base62 short code
- DB: KV (DynamoDB) or Mongo
- Read-heavy → cache + CDN
- Analytics async via [[Message Queues]]

**Q. Design Twitter feed.**
- Push (fanout-on-write): cheap reads, costly writes for celebrities
- Pull (fanout-on-read): cheap writes, costly reads
- Hybrid: pull for celebs, push for normals

**Q. Design WhatsApp.**
- WebSockets + Redis pub/sub
- Message store with composite key (chat, ts)
- Delivery receipts via ack pipeline
- E2E encryption — key exchange via Signal protocol

**Q. Design rate limiter.**
- Token bucket in Redis with atomic Lua
- See [[Rate Limiting in System Design]]

**Q. Design notification service.**
- Producers → queue → workers → channels (push/email/SMS)
- Idempotency, retries, DLQ

## Concepts to know cold
- [[CAP Theorem]] / PACELC
- [[Caching]] — strategies, stampedes
- [[Sharding and Partitioning]]
- [[Replication in System Design]]
- [[Message Queues]] · [[Pub Sub]]
- [[Indexes|Indexes]]
- [[Sessions vs JWT]] · [[OAuth Flow]]
- Idempotency keys
- Retries with exponential backoff + jitter

## Tradeoff phrases to use
- "We trade consistency for availability here"
- "We can tolerate eventual consistency for the feed but not the wallet"
- "Cache hit ratio target …; cold start mitigation via …"
