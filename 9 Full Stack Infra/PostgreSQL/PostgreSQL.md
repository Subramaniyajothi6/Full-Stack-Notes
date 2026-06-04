---
tags: [infra, database, intermediate]
---

# PostgreSQL

> The world's most advanced open-source relational database. ACID, rich types, extensions like [[pgvector]] and PostGIS.

## Why it matters
Default SQL choice for new apps. Predictable, fast, supports JSON, full-text search, vector search, and complex queries that document DBs struggle with.

## Core ideas
- **MVCC** — readers don't block writers, writers don't block readers
- **WAL** — write-ahead log enables crash recovery + replication
- **Indexes** — B-tree (default), hash, GIN, GiST, BRIN, IVFFlat/HNSW (via pgvector)
- **Transactions** — BEGIN / COMMIT / ROLLBACK; SAVEPOINTs
- **Roles & schemas** — granular permissions
- **Extensions** — pgvector, PostGIS, TimescaleDB, pg_stat_statements

## Quick reference
```sql
CREATE TABLE users (id BIGSERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, created_at TIMESTAMPTZ DEFAULT now());

EXPLAIN ANALYZE SELECT * FROM users WHERE email = $1;

CREATE INDEX users_email_idx ON users(email);

WITH recent AS (SELECT * FROM orders WHERE created_at > now() - interval '7 days')
SELECT user_id, count(*) FROM recent GROUP BY user_id;
```

## Real World Usage
- App data (users, orders, content)
- Search (full-text + trigram)
- Vector search (with pgvector)
- Analytics (with materialized views)
- Geospatial (with PostGIS)

## Common Mistakes
- Skipping `EXPLAIN ANALYZE` — guessing index plans
- Long-held transactions on busy tables → bloat
- Not using `pg_stat_statements` — flying blind on slow queries
- N+1 queries (especially with ORMs like Prisma/Sequelize)
- Storing JSONB blobs and forgetting GIN index for queries

## Prerequisites
- [[SQL vs NoSQL|SQL vs NoSQL]]
- Basic SQL

## What To Learn Next
- [[pgvector]] · [[Redis]] · [[Database Indexing|Database Indexing]]

## Best Learning Resources

### Official Documentation
- [PostgreSQL docs](https://www.postgresql.org/docs/) — extraordinarily complete
- [Postgres EXPLAIN visualizer](https://explain.dalibo.com/)

### Best YouTube Resource
- [Hussein Nasser — Postgres deep dives](https://www.youtube.com/@hnasr) — index types, MVCC, query planning
- [Software Engineering Daily — Postgres episodes](https://www.youtube.com/c/softwareengineeringdaily)

### Best Free Course
- [Use The Index, Luke!](https://use-the-index-luke.com/) — index-focused free book
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) — comprehensive

### Best Advanced Resource
- [Postgres internals (Egor Rogov)](https://postgrespro.com/blog/pgsql/5969985) — series on MVCC, WAL, etc.
- [Citus blog](https://www.citusdata.com/blog/) — performance + scaling

### Best Practice Project
Migrate a small Mongo app to Postgres: schemas, foreign keys, indexes, full-text search on a content column with `tsvector`, an analytics endpoint using a CTE + window function. Add `pg_stat_statements` and write a query report.

### Recommended Order to Learn
1. SQL fundamentals (joins, subqueries)
2. Indexes + EXPLAIN
3. Transactions + isolation levels
4. JSONB + full-text search
5. Replication + backups
6. Extensions: pgvector, PostGIS

## Interview Questions
**Q. What's MVCC?**
A. Multi-Version Concurrency Control. Each write creates a new row version; reads see a consistent snapshot. No reader-writer locking.

**Q. When does an index *not* help?**
A. Tiny tables, very low selectivity, queries that need most rows anyway.

**Q. Difference between `INNER JOIN` and `LEFT JOIN`?**
A. INNER returns rows matching both tables. LEFT returns all left-table rows; right side becomes NULL when no match.

**Q. JSONB vs JSON?**
A. JSONB is binary, indexable, slightly slower to insert, faster to query. Default to JSONB.

**Q. What is connection pooling and why does Postgres need it?**
A. Each Postgres connection = a process. Pool (PgBouncer/PgCat) sharing pre-warmed connections is essential under load.

## Related
- [[pgvector]] · [[Redis]] · [[Object Storage]]
