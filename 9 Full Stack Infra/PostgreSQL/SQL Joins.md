---
tags: [postgresql, sql, beginner, concept]
---

# SQL Joins

> Combine rows from two or more tables based on a related column.

## The four
| Join | Returns |
|---|---|
| `INNER JOIN` | Rows matching in both tables |
| `LEFT JOIN`  | All left rows + matching right (NULL if no match) |
| `RIGHT JOIN` | All right rows + matching left |
| `FULL JOIN`  | All rows from both; NULLs where unmatched |

## Examples
```sql
-- Inner: only users with at least one order
SELECT u.id, u.email, o.total
FROM users u
INNER JOIN orders o ON o.user_id = u.id;

-- Left: every user, with their order count (0 if none)
SELECT u.id, count(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id;

-- Self join: employees + their manager
SELECT e.name, m.name AS manager
FROM employees e
LEFT JOIN employees m ON m.id = e.manager_id;
```

## Cross / lateral / using
```sql
SELECT * FROM a CROSS JOIN b;                         -- cartesian product
SELECT * FROM users u, lateral most_recent_order(u.id) o;  -- per-row subquery
SELECT * FROM a JOIN b USING (user_id);               -- short form when columns match
```

## Real World Usage
- Listing related entities (orders + users)
- Reports across multiple tables
- "Who hasn't done X" via `LEFT JOIN ... WHERE x IS NULL`
- Hierarchical data via self-joins
- Anti-joins for finding missing matches

## Common Mistakes
- Forgetting `GROUP BY` after aggregating with a join
- `LEFT JOIN` then filtering with `WHERE` on the right side → effectively becomes inner join (use `AND` in `ON` instead)
- Cartesian explosion from missing join condition
- Mixing implicit join (comma) with explicit JOIN syntax
- Returning duplicated left-side rows when right side has multiple matches without aggregation

## Prerequisites
- [[PostgreSQL]] · [[SQL vs NoSQL]]

## What To Learn Next
- [[Indexes in PostgreSQL]] · [[CTEs and Window Functions]] · [[EXPLAIN and Query Plans]]

## Best Learning Resources

### Official Documentation
- [PostgreSQL JOIN syntax](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-JOIN)

### Best YouTube Resource
- [Hussein Nasser — SQL joins](https://www.youtube.com/@hnasr)

### Best Free Course
- [PostgreSQL Tutorial — Joins](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/)
- [SQLBolt (interactive)](https://sqlbolt.com/)

### Best Advanced Resource
- [Use The Index, Luke! — joins chapter](https://use-the-index-luke.com/sql/join)

### Best Practice Project
Take any schema with 3+ related tables; write 10 queries: inner, left, right, full, self, anti-join, semi-join, cross, lateral, and a 4-table join. Read `EXPLAIN ANALYZE` for each.

### Recommended Order to Learn
1. INNER + LEFT JOIN
2. RIGHT + FULL
3. Self joins
4. USING vs ON
5. LATERAL
6. Anti / semi joins

## Interview Questions
**Q. INNER vs LEFT?**
A. INNER keeps only matched pairs. LEFT keeps all left-table rows; NULLs fill the right side when unmatched.

**Q. Why does `LEFT JOIN ... WHERE right_col = X` behave like INNER?**
A. The filter rejects NULL rows; predicate belongs in `ON ... AND right_col = X` instead.

**Q. What's a LATERAL join?**
A. The right side can reference columns from earlier in the FROM clause — like a per-row subquery.

## Related
- [[Indexes in PostgreSQL]] · [[CTEs and Window Functions]] · [[EXPLAIN and Query Plans]]
