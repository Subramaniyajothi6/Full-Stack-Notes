---
tags: [postgresql, intermediate, performance]
---

# Indexes in PostgreSQL

> The single biggest perf lever. Postgres has B-tree (default), Hash, GIN, GiST, BRIN, and SP-GiST.

## Types and when to use them
| Type   | Use case                                      |
| ------ | --------------------------------------------- |
| B-tree | Default; equality, range, ORDER BY            |
| Hash   | Pure equality (rarely better than B-tree)     |
| GIN    | Composite values (arrays, JSONB, full-text)   |
| GiST   | Geometric, ranges, custom types               |
| BRIN   | Huge append-mostly tables ordered by inserted-at |
| SP-GiST| Non-balanced trees (specific data types)      |

## Creating
```sql
CREATE INDEX idx_users_email ON users(email);
CREATE UNIQUE INDEX idx_users_email_unq ON users(email);
CREATE INDEX idx_orders_user_created ON orders(user_id, created_at DESC);  -- compound
CREATE INDEX idx_posts_tags ON posts USING GIN (tags);                      -- array col
CREATE INDEX idx_logs_time ON logs USING BRIN (created_at);                 -- time-series
```

## Concurrent index — no table lock
```sql
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
```
Slower; safer in production.

## Partial index — only some rows
```sql
CREATE INDEX idx_active_users_email ON users(email) WHERE is_active;
```

## Expression index — index a function
```sql
CREATE INDEX idx_users_lower_email ON users(lower(email));
SELECT * FROM users WHERE lower(email) = 'a@b.c';
```

## Covering index — INCLUDE non-key cols
```sql
CREATE INDEX idx_orders_user_inc ON orders(user_id) INCLUDE (total, created_at);
```
Index-only scans without hitting the table.

## Real World Usage
- Foreign key columns (almost always need an index)
- WHERE / ORDER BY / JOIN columns
- Tenant scoping (`tenant_id` first)
- JSONB attribute access via GIN
- BRIN for log tables ordered by time

## Common Mistakes
- Indexing every column — slow writes, bloat
- Wrong column order on compound (E-S-R: Equality, Sort, Range)
- Function-on-column in WHERE without expression index (`lower(email)`)
- Not running `ANALYZE` after bulk loads → planner uses stale stats
- Creating a duplicate index that subsumes / is subsumed
- Forgetting `CONCURRENTLY` in prod → table lock

## Prerequisites
- [[PostgreSQL]] · [[Database Indexing]]

## What To Learn Next
- [[EXPLAIN and Query Plans]] · [[Transactions and Isolation]] · [[Connection Pooling]]

## Best Learning Resources

### Official Documentation
- [PostgreSQL Indexes](https://www.postgresql.org/docs/current/indexes.html)

### Best YouTube Resource
- [Hussein Nasser — Postgres indexes](https://www.youtube.com/@hnasr)

### Best Free Course
- [Use The Index, Luke!](https://use-the-index-luke.com/) — best free index book
- [PostgreSQL Tutorial — Indexes](https://www.postgresqltutorial.com/postgresql-indexes/)

### Best Advanced Resource
- [Egor Rogov — Postgres index types deep dive (Postgres Pro blog)](https://postgrespro.com/blog/pgsql/4161264)
- [Pavlo course — Indexing chapter (CMU)](https://15445.courses.cs.cmu.edu/fall2024/)

### Best Practice Project
Pick a slow query; run `EXPLAIN ANALYZE`; add an index; measure again. Try a partial, expression, and covering index; document gain/cost per change.

### Recommended Order to Learn
1. B-tree default
2. Compound + column order (ESR)
3. Partial + expression
4. Covering (INCLUDE)
5. GIN for JSONB + arrays
6. BRIN for time-series
7. `CREATE INDEX CONCURRENTLY` in prod

## Interview Questions
**Q. Why is GIN better than B-tree for JSONB?**
A. GIN indexes each token (key/value path); B-tree indexes the whole value as a unit.

**Q. Compound index column order — what rule?**
A. Equality columns first, then sort, then range. Queries can use a prefix of the index keys.

**Q. Cost of indexes?**
A. Every write updates them; they consume RAM/disk. Don't over-index.

## Related
- [[EXPLAIN and Query Plans]] · [[PostgreSQL]] · [[Database Indexing]]
