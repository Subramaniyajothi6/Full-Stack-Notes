---
tags: [redis, advanced, scale]
---

# Cluster and HA

> Scaling Redis horizontally (cluster) and surviving failures (Sentinel or Cluster).

## Topologies
- **Standalone** — one node; no HA
- **Primary + replicas** — async replication; manual failover
- **Sentinel** — monitors primary + auto-failover among a primary/replica group
- **Cluster** — shards data across multiple primaries, each with replicas

## Sentinel
- Monitors primary, agrees on failure via quorum
- Promotes a replica to primary
- Updates clients via Sentinel discovery
- Use when: one primary is enough capacity, you just need HA

## Cluster
- Data partitioned into 16384 slots
- Each slot owned by one primary
- Each primary has replicas
- Client talks to any node, gets MOVED/ASK redirects
- Use when: a single instance can't hold your data or handle the write rate

## Hash tags
Multi-key commands must hash to the same slot. Use `{}` to force grouping:
```
SET {user42}:profile ...
SADD {user42}:friends 7 9
SINTER {user42}:friends {user42}:blocked    # both keys same slot
```

## Limits
- Pub/Sub by default goes to all nodes (since Redis 7, sharded pub/sub available)
- Lua scripts must operate on keys that hash to the same slot
- Cross-slot multi-key commands fail
- Atomicity weaker across slots

## Operational
- Sizing: `INFO memory`, `MEMORY USAGE`, `latency monitor`
- Backups + replication independent
- Avoid scaling too late; resharding is slow

## Real World Usage
- HA session store → Sentinel
- BullMQ at high throughput → Cluster
- Multi-region read-mostly → replicas in each region (eventual consistency)
- Global cache layer

## Common Mistakes
- Cross-slot transactions on Cluster (will fail)
- Sentinel without enough sentinel instances (need ≥3 for quorum)
- Forgetting hash tags on related keys → MOVED redirects on every op
- Treating replicas as read-after-write consistent (they're async)
- Single-node Redis for prod stateful workloads

## Prerequisites
- [[Redis]] · [[Eviction and Persistence]]

## What To Learn Next
- [[Backups and Restore]] · [[Sharding and Partitioning]]

## Best Learning Resources

### Official Documentation
- [Redis Cluster spec](https://redis.io/docs/management/scaling/)
- [Redis Sentinel](https://redis.io/docs/management/sentinel/)
- [Redis Replication](https://redis.io/docs/management/replication/)

### Best YouTube Resource
- [Hussein Nasser — Redis cluster & sentinel](https://www.youtube.com/@hnasr)

### Best Free Course
- [Redis University — RU301](https://university.redis.com/)

### Best Advanced Resource
- [Antirez — Cluster Design](http://antirez.com/news/107)
- [AWS ElastiCache architecture](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.html)

### Best Practice Project
Run a 6-node cluster in Docker (3 primaries, 3 replicas). Simulate a primary failure; verify automatic failover and zero data loss with WAL flush settings.

### Recommended Order to Learn
1. Replication basics
2. Sentinel quorum + failover
3. Cluster slots + hash tags
4. Resharding live
5. Multi-region patterns
6. Disaster recovery

## Interview Questions
**Q. Sentinel vs Cluster?**
A. Sentinel = HA for a single primary's data. Cluster = HA + horizontal sharding across many primaries.

**Q. Why hash tags?**
A. They force multiple keys into the same slot so multi-key commands and Lua scripts can run.

**Q. Are Redis replicas synchronous?**
A. No — async by default. Synchronous replication is opt-in (`WAIT` command) with caveats.

## Related
- [[Eviction and Persistence]] · [[Backups and Restore]] · [[Sharding and Partitioning]]
