---
tags: [moc, postgresql, database]
---

# PostgreSQL MOC

> Open-source relational database. Default SQL choice for new apps; supports JSON, full-text search, and vector via [[pgvector]].

## Overview
- [[PostgreSQL]] — what / why / when

## Querying
- [[SQL Joins]] — inner / left / right / full / self / lateral
- [[CTEs and Window Functions]] — WITH, recursive, ranking, running totals
- [[JSONB]] — semi-structured data inside Postgres
- [[Full-Text Search]] — tsvector / tsquery / pg_trgm

## Performance
- [[Indexes in PostgreSQL]] — B-tree, GIN, BRIN, partial, expression, covering
- [[EXPLAIN and Query Plans]] — diagnose any slow query
- [[Connection Pooling]] — PgBouncer, app-side pools, serverless

## Reliability
- [[Transactions and Isolation]] — ACID, isolation levels, MVCC, locking
- [[Replication and Failover]] — streaming, sync vs async, logical
- [[Row-Level Security]] — DB-enforced tenant isolation

## Extensions
- [[pgvector]] — semantic search via vector embeddings

## Suggested order
1. [[PostgreSQL]] (overview) → [[SQL Joins]]
2. [[Indexes in PostgreSQL]] → [[EXPLAIN and Query Plans]]
3. [[Transactions and Isolation]]
4. [[CTEs and Window Functions]] → [[JSONB]] → [[Full-Text Search]]
5. [[Connection Pooling]]
6. [[Replication and Failover]] → [[Row-Level Security]]
7. [[pgvector]] (when adding semantic search)

## Roadmap to fill in
- [ ] Constraints (CHECK, UNIQUE, EXCLUDE)
- [ ] Triggers + stored procedures
- [ ] Partitioning (declarative + inheritance)
- [ ] Materialized views
- [ ] Advisory locks
- [ ] `LISTEN`/`NOTIFY` for pub/sub
- [ ] PostGIS for geospatial
- [ ] Sharding strategies (Citus, partitioning)

## Related stacks
- [[MongoDB MOC]] — NoSQL alternative
- [[Redis MOC]] — caching + queue partner
- [[AI Engineering MOC]] — pgvector for RAG
- [[System Design MOC]] — SQL vs NoSQL, indexing
- [[MERN Stack MOC]] — [[Backups and Restore]] · [[DB Migrations]] · [[Multi-Tenant Patterns]]

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
