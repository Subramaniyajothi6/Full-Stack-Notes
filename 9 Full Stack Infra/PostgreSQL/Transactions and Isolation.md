---
tags: [postgresql, intermediate, concept]
---

# Transactions and Isolation

> ACID: Atomicity, Consistency, Isolation, Durability. Isolation levels control how concurrent transactions see each other.

## Basics
```sql
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;       -- or ROLLBACK on failure
```

## Isolation levels
| Level                 | Prevents                                     |
|-----------------------|----------------------------------------------|
| Read Uncommitted      | (Postgres treats same as Read Committed)     |
| Read Committed (default) | Dirty reads                                 |
| Repeatable Read       | + Non-repeatable reads                       |
| Serializable          | + Phantom reads + write skew                 |

```sql
BEGIN ISOLATION LEVEL SERIALIZABLE;
```

### Anomalies cheat-sheet
- **Dirty read** — see uncommitted data from another txn
- **Non-repeatable read** — same row reads differently in same txn
- **Phantom read** — `SELECT ... WHERE` returns different rows on repeat
- **Write skew** — two txns each read state, decide based on it, both write — final state inconsistent

## Savepoints
```sql
BEGIN;
  ...
  SAVEPOINT s1;
  UPDATE ...;
  ROLLBACK TO s1;     -- partial undo
COMMIT;
```

## Row locking
```sql
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;       -- lock until commit
SELECT * FROM accounts WHERE id = 1 FOR UPDATE SKIP LOCKED;  -- queue worker pattern
```

## MVCC under the hood
Postgres keeps multiple row versions. Readers don't block writers; writers don't block readers. `VACUUM` cleans dead tuples.

## Real World Usage
- Money transfers (transactional debit + credit)
- Inventory + order placement
- Multi-row state changes
- Job queues (`FOR UPDATE SKIP LOCKED`)
- Bulk imports (single big transaction or chunked)

## Common Mistakes
- Long-running transactions → table bloat, locks held
- Mixing read + transactional intent on a single connection without commits
- Using Repeatable Read when Read Committed suffices (or vice versa)
- Ignoring serialization failures in client code (must retry)
- DDL inside huge txn → schema lock

## Prerequisites
- [[PostgreSQL]] · [[SQL Joins]]

## What To Learn Next
- [[Connection Pooling]] · [[Indexes in PostgreSQL]] · [[Backups and Restore]]

## Best Learning Resources

### Official Documentation
- [Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [Explicit Locking](https://www.postgresql.org/docs/current/explicit-locking.html)

### Best YouTube Resource
- [Hussein Nasser — Isolation levels](https://www.youtube.com/@hnasr)

### Best Free Course
- [Use The Index, Luke! — Transactions](https://use-the-index-luke.com/)
- [PostgreSQL Tutorial — Transactions](https://www.postgresqltutorial.com/postgresql-administration/)

### Best Advanced Resource
- [DDIA — Transactions chapter](https://dataintensive.net/)
- [Aphyr — Postgres isolation analyses](https://aphyr.com/tags/jepsen)

### Best Practice Project
Implement a money-transfer service using `BEGIN; ... COMMIT;` and validate via concurrent tests that no money is lost or duplicated. Try at Read Committed and Serializable; observe retries.

### Recommended Order to Learn
1. BEGIN / COMMIT / ROLLBACK
2. Read Committed default
3. Repeatable Read
4. Serializable + retry pattern
5. Savepoints
6. Row-level locks + SKIP LOCKED
7. MVCC + VACUUM

## Interview Questions
**Q. Default isolation level in Postgres?**
A. Read Committed.

**Q. What's write skew?**
A. Two txns each read state, write back based on it, both succeed under weaker isolation; final state violates an invariant. Fixed by Serializable.

**Q. Why use `FOR UPDATE SKIP LOCKED`?**
A. Worker pattern — each worker grabs a different row to process; locked rows are skipped instead of blocking.

## Related
- [[Indexes in PostgreSQL]] · [[Connection Pooling]] · [[Caching Layers]]
