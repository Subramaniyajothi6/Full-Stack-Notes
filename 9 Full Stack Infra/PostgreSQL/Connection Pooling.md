---
tags: [postgresql, intermediate, deployment]
---

# Connection Pooling

> Every Postgres connection is a forked process — expensive. A pool shares a small set across many app workers.

## Why it matters
- Postgres connection limit (~100s)
- Each backend uses memory (~10MB)
- Node + many workers + serverless → thousands of would-be connections
- Pool throttles + reuses

## Tools
- **PgBouncer** — battle-tested, lightweight
- **Pgpool-II** — heavier, adds load balancing
- **PgCat** — Rust replacement, gaining traction
- **Cloud-managed** — RDS Proxy, Supabase Pooler, Neon Pooler

## PgBouncer modes
- **Session pooling** — connection held for the whole client session (default; safest)
- **Transaction pooling** — connection released after each txn (great for short, stateless txns; breaks features that need per-session state like `LISTEN`, prepared statements with names, server-side cursors)
- **Statement pooling** — released after each statement (very specialized)

Transaction pooling is the default for most modern apps.

## Application-side pool
Even with PgBouncer, your app driver (`pg`, `node-postgres`) has its own pool:
```ts
import { Pool } from 'pg';
const pool = new Pool({ max: 10, idleTimeoutMillis: 30_000 });
const { rows } = await pool.query('SELECT * FROM users WHERE id = $1', [id]);
```

## Serverless caveats
Lambda + Postgres ⇒ many cold-start connections. Use a pooler in front (RDS Proxy, Supavisor) or driver-level retry/backoff.

## Real World Usage
- High-traffic APIs (thousands of req/s, hundreds of workers)
- Serverless functions
- Multi-tenant SaaS
- Job queues hitting the DB heavily

## Common Mistakes
- Letting each Lambda open a fresh PG connection (exhausts limit)
- Using transaction pooling while relying on session-scoped features (`SET search_path` for a session, named prepared statements)
- App pool `max` × instances > Postgres limit → connection storm
- No `idle_in_transaction_session_timeout` → leaked txn holds locks forever
- Not pooling on the app side, only at PgBouncer — round-trip per query

## Prerequisites
- [[PostgreSQL]] · [[Transactions and Isolation]]

## What To Learn Next
- [[Replication and Failover]] · [[EXPLAIN and Query Plans]]

## Best Learning Resources

### Official Documentation
- [PgBouncer docs](https://www.pgbouncer.org/usage.html)
- [PgCat docs](https://github.com/postgresml/pgcat)
- [AWS RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)

### Best YouTube Resource
- [Hussein Nasser — Connection pooling deep dive](https://www.youtube.com/@hnasr)

### Best Free Course
- [PostgreSQL Tutorial — Connections + pgbouncer (community)](https://www.postgresqltutorial.com/)

### Best Advanced Resource
- [Crunchy Data — PgBouncer in production](https://www.crunchydata.com/blog/)
- [Heap — How we tuned PgBouncer](https://www.heap.io/blog) — engineering deep dive

### Best Practice Project
Add PgBouncer in transaction mode in front of Postgres. Load-test the app at 1k req/s; compare connection counts and tail latency vs no pooler.

### Recommended Order to Learn
1. Connection vs process model
2. App-side pool (`pg`, knex)
3. PgBouncer session vs transaction mode
4. Limits at every layer (app × instances × pooler × Postgres)
5. Serverless patterns (RDS Proxy, Supavisor)
6. Monitoring (idle, active, waiting)

## Interview Questions
**Q. Why is a connection in Postgres expensive?**
A. Each is a fork()'d process with ~10MB RAM and startup cost.

**Q. Transaction pooling drawbacks?**
A. Features needing session state (LISTEN/NOTIFY, named prepared statements) don't work — connection switches between txns.

**Q. App pool + PgBouncer pool — redundant?**
A. No. App pool minimizes per-query round-trip + serialization. PgBouncer multiplexes many app pools across few Postgres backends.

## Related
- [[PostgreSQL]] · [[Transactions and Isolation]] · [[Deployment Architecture]]
