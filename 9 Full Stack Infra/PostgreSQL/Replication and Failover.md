---
tags: [postgresql, advanced, scale]
---

# Replication and Failover

> Primary + replicas. Async streaming of WAL. Read scaling + HA via failover.

## Streaming replication
- Primary writes WAL
- Replicas tail it and apply
- **Async** (default) — small replication lag, possible data loss on failover
- **Synchronous** — primary waits for at least one replica; durability + latency cost

```conf
# postgresql.conf
wal_level = replica
max_wal_senders = 10
synchronous_standby_names = '*'   # for sync replication
```

## Failover
- Manual: promote a replica with `pg_ctl promote`
- Automatic: Patroni / repmgr / Stolon manage leader election + DNS / VIP
- Cloud: RDS Multi-AZ, Aurora handle this transparently

## Read replicas
- Route read traffic to replicas
- Beware of **replication lag** — reads may be slightly stale
- Use primary for reads-after-write paths

## Logical replication (vs physical)
- Physical: byte-for-byte WAL ship
- Logical: row-level changes; different schemas; cross-version
- Used for CDC pipelines (Debezium), upgrades, partial mirror

## Backup vs replication
Replication is **not a backup** — it propagates `DROP TABLE`. PITR + off-site snapshots are needed too. See [[Backups and Restore]].

## Real World Usage
- HA: Aurora / RDS Multi-AZ / Patroni cluster
- Read scaling: route reports / analytics to replicas
- Zero-downtime upgrades via logical replication
- CDC to Kafka / Snowflake / data lake

## Common Mistakes
- Treating async replicas as instantly consistent
- Replication lag causes "user just wrote, now reads stale" bugs (route writes + reads-after-write to primary)
- Synchronous replication on a single sync standby that's down → primary stalls
- Forgetting backups because "we have replicas"
- Failover that doesn't promote ahead of slow replicas

## Prerequisites
- [[PostgreSQL]] · [[Transactions and Isolation]] · [[Connection Pooling]]

## What To Learn Next
- [[Backups and Restore]] · [[Sharding and Partitioning]]

## Best Learning Resources

### Official Documentation
- [Streaming Replication](https://www.postgresql.org/docs/current/runtime-config-replication.html)
- [Logical Replication](https://www.postgresql.org/docs/current/logical-replication.html)
- [Patroni docs](https://patroni.readthedocs.io/)

### Best YouTube Resource
- [Hussein Nasser — Postgres replication](https://www.youtube.com/@hnasr)

### Best Free Course
- [PostgreSQL Tutorial — Replication](https://www.postgresqltutorial.com/postgresql-administration/postgresql-replication/)

### Best Advanced Resource
- [PostgresPro — replication internals](https://postgrespro.com/blog/)
- [Citus / Crunchy blogs on HA patterns](https://www.crunchydata.com/blog/)

### Best Practice Project
Spin up primary + replica via Docker Compose. Write to primary, read from replica, kill primary, promote replica. Measure data loss and downtime under async vs sync configs.

### Recommended Order to Learn
1. Streaming replication (async)
2. Promotion / failover steps
3. Synchronous replication tradeoffs
4. Logical replication
5. Cluster managers (Patroni)
6. Cloud HA (RDS, Aurora)

## Interview Questions
**Q. Async vs synchronous replication?**
A. Async: low latency, can lose data on failover. Sync: zero loss, primary waits → higher latency, can stall if standby down.

**Q. Why isn't replication a backup?**
A. `DROP TABLE` propagates instantly. Backups give you a point-in-time recovery target.

**Q. Replication lag — how to measure?**
A. `SELECT now() - pg_last_xact_replay_timestamp();` on the replica.

## Related
- [[Backups and Restore]] · [[Connection Pooling]] · [[Sharding and Partitioning]]
