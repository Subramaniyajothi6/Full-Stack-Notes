---
tags: [postgresql, intermediate, performance]
---

# EXPLAIN and Query Plans

> The Postgres planner's view of your query. Read it to find the bottleneck.

## Basics
```sql
EXPLAIN          SELECT * FROM users WHERE email = $1;
EXPLAIN ANALYZE  SELECT * FROM users WHERE email = $1;   -- actually runs
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, FORMAT JSON) SELECT ...;
```

`ANALYZE` runs the query (don't use on huge DELETEs casually). `BUFFERS` shows cache vs disk reads.

## What to look for
- **Seq Scan** vs **Index Scan** — sequential = table walk
- **Rows estimated** vs **rows actual** — large divergence = bad stats, run `ANALYZE`
- **Loops** — multiplier for actual cost
- **Total time** — actual ms
- **Hash Join** vs **Nested Loop** vs **Merge Join** — strategy
- **Index Only Scan** — best case (covering index)

## Annotated example
```
Index Scan using idx_users_email on users  (cost=0.42..8.44 rows=1 width=64)
                                            (actual time=0.020..0.021 rows=1 loops=1)
  Index Cond: (email = 'a@b.c'::text)
Planning Time: 0.150 ms
Execution Time: 0.045 ms
```

## Visualizers
- [explain.dalibo.com](https://explain.dalibo.com/) — paste plan, see flame-tree
- [explain.depesz.com](https://explain.depesz.com/) — color-coded

## When the planner gets it wrong
- Stats stale → `ANALYZE table_name`
- Correlated columns → `CREATE STATISTICS`
- Use `pg_stat_statements` for top-N slow queries
- Hints — Postgres doesn't have them by design; rewrite the query instead

## Real World Usage
- Diagnosing prod slow queries
- Validating an index actually gets used
- Comparing two query rewrites
- Tracking regressions across deploys

## Common Mistakes
- Reading EXPLAIN without ANALYZE → only estimates, not real times
- Ignoring "rows actual vs estimated" divergence
- Adding an index without confirming the plan changes
- Running `EXPLAIN ANALYZE` on write queries without `BEGIN; ROLLBACK;`
- Treating high cost as "must optimize" — it's relative; actual time matters

## Prerequisites
- [[PostgreSQL]] · [[Indexes in PostgreSQL]]

## What To Learn Next
- [[Transactions and Isolation]] · [[Connection Pooling]]

## Best Learning Resources

### Official Documentation
- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html)
- [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)

### Best YouTube Resource
- [Hussein Nasser — EXPLAIN tutorial](https://www.youtube.com/@hnasr)

### Best Free Course
- [Use The Index, Luke! — Execution Plans](https://use-the-index-luke.com/sql/explain-plan/postgresql/getting-an-execution-plan)
- [Depesz EXPLAIN articles](https://www.depesz.com/tag/explain/)

### Best Advanced Resource
- [Egor Rogov — Postgres internals series](https://postgrespro.com/blog/pgsql/5969985)

### Best Practice Project
Set up `pg_stat_statements`. Find the top 10 slowest queries. For each, run `EXPLAIN ANALYZE`, identify the bottleneck (missing index? bad plan? lock contention?), and fix.

### Recommended Order to Learn
1. EXPLAIN basics
2. EXPLAIN ANALYZE + BUFFERS
3. Reading plan trees
4. Recognizing scan types + join strategies
5. Stats with `ANALYZE` + `CREATE STATISTICS`
6. `pg_stat_statements` for prod

## Interview Questions
**Q. Why might Postgres prefer a Seq Scan over an Index Scan?**
A. Small table, low selectivity, or stats suggest fetching the index + table costs more than the scan.

**Q. What's an Index-Only Scan?**
A. All needed columns are in the index (covering); no heap fetch.

**Q. How to fix wildly wrong row estimates?**
A. `ANALYZE table`; for correlated columns, `CREATE STATISTICS (dependencies, ndistinct) ON (col1, col2) FROM tbl`.

## Related
- [[Indexes in PostgreSQL]] · [[Transactions and Isolation]]
