---
tags: [postgresql, intermediate, syntax]
---

# CTEs and Window Functions

> Common Table Expressions (`WITH`) name a sub-query for reuse. Window functions compute values across row partitions without collapsing them.

## CTEs
```sql
WITH recent AS (
  SELECT * FROM orders WHERE created_at > now() - interval '7 days'
)
SELECT user_id, count(*) FROM recent GROUP BY user_id;
```

### Recursive CTE
```sql
WITH RECURSIVE descendants AS (
  SELECT id, parent_id FROM categories WHERE id = 5
  UNION ALL
  SELECT c.id, c.parent_id
  FROM categories c
  JOIN descendants d ON c.parent_id = d.id
)
SELECT * FROM descendants;
```
For tree traversal (orgs, comments, file trees).

### CTE materialization
Postgres 12+ inlines CTEs by default (faster). Force separation with `WITH x AS MATERIALIZED (...)` when you intend a hard fence.

## Window functions
Aggregate without `GROUP BY`:
```sql
SELECT user_id, total,
       sum(total) OVER (PARTITION BY user_id) AS user_total,
       row_number() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
FROM orders;
```

### Common windows
- `row_number()`, `rank()`, `dense_rank()`, `ntile(n)`
- `lag(col, n)`, `lead(col, n)`
- `sum / avg / min / max OVER (...)`
- `percent_rank()`, `cume_dist()`

### Top-N per group
```sql
WITH ranked AS (
  SELECT *, row_number() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
  FROM orders
)
SELECT * FROM ranked WHERE rn <= 3;       -- top 3 per user
```

## Real World Usage
- Reporting (running totals, moving averages)
- Top-N per group
- Tree / graph data with recursive CTEs
- Deduplication keeping latest
- Funnel analytics

## Common Mistakes
- Using subqueries everywhere when a CTE would clarify
- Recursive CTE without a termination — infinite loop
- Window function vs `GROUP BY` confusion — windows keep rows, groups collapse
- Forgetting `ORDER BY` inside `OVER` — order is undefined otherwise

## Prerequisites
- [[SQL Joins]] · [[PostgreSQL]]

## What To Learn Next
- [[EXPLAIN and Query Plans]] · [[JSONB]]

## Best Learning Resources

### Official Documentation
- [WITH (Common Table Expressions)](https://www.postgresql.org/docs/current/queries-with.html)
- [Window Functions](https://www.postgresql.org/docs/current/tutorial-window.html)

### Best YouTube Resource
- [Hussein Nasser — Window functions](https://www.youtube.com/@hnasr)

### Best Free Course
- [PostgreSQL Tutorial — Window functions](https://www.postgresqltutorial.com/postgresql-window-function/)
- [PostgreSQL Tutorial — CTEs](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-cte/)

### Best Advanced Resource
- ["Modern SQL" by Markus Winand](https://modern-sql.com/) — definitive SQL feature site

### Best Practice Project
Build an analytics view: daily active users, retention cohort, top-3 products per category. Use CTEs for clarity and window functions for the calculations.

### Recommended Order to Learn
1. CTE basics
2. Recursive CTE (tree traversal)
3. Aggregate window functions
4. Ranking windows (`row_number`, `rank`)
5. `lag` / `lead` for sequencing
6. Frame clauses (`ROWS BETWEEN ...`)

## Interview Questions
**Q. CTE vs subquery — performance?**
A. Since Postgres 12, CTEs are inlined by default — similar perf. Use whichever reads cleaner.

**Q. row_number vs rank vs dense_rank?**
A. row_number is unique sequential. rank skips on ties (1,1,3). dense_rank keeps tight (1,1,2).

**Q. Top-N per group — how?**
A. `row_number() OVER (PARTITION BY group ORDER BY x DESC)` then filter `<= N`.

## Related
- [[SQL Joins]] · [[EXPLAIN and Query Plans]] · [[PostgreSQL]]
