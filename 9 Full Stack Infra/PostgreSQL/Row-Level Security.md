---
tags: [postgresql, advanced, security]
---

# Row-Level Security

> Postgres-enforced filter on every query against a table. Prevents tenant or per-user data leaks even if app code is buggy.

## Enable
```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
ALTER TABLE orders FORCE ROW LEVEL SECURITY;   -- enforce on table owner too
```

## Policy
```sql
CREATE POLICY tenant_isolation ON orders
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant')::uuid);
```

## Set the context per request
```sql
SET LOCAL app.current_tenant = '11111111-1111-1111-1111-111111111111';
SELECT * FROM orders;     -- only this tenant's rows visible
```

In your Node code:
```ts
await client.query("SET LOCAL app.current_tenant = $1", [req.tenant.id]);
const result = await client.query("SELECT * FROM orders WHERE id = $1", [orderId]);
```

## Use cases
- Multi-tenant SaaS where ORM-level filters are easy to forget
- Supabase / PostgREST — RLS is the only auth boundary
- Read-only / write-restricted views per role

## Policies on operations
```sql
CREATE POLICY orders_read  ON orders FOR SELECT USING (...);
CREATE POLICY orders_write ON orders FOR INSERT WITH CHECK (...);
```
- `USING` — controls visibility (read + filter on update)
- `WITH CHECK` — controls what new/updated rows are allowed

## Real World Usage
- Supabase + Postgres + RLS (the canonical stack)
- Multi-tenant ORMs as a safety net
- Per-org or per-team data partitioning
- Compliance-heavy apps (HIPAA, GDPR)

## Common Mistakes
- Forgetting `FORCE ROW LEVEL SECURITY` — table owner bypasses unless forced
- Using `current_user` instead of an app setting → DB users != app users
- Performance — RLS = extra WHERE on every query; ensure good indexes
- Not testing with a real non-superuser role
- Mixing RLS with `BYPASSRLS` roles unintentionally

## Prerequisites
- [[PostgreSQL]] · [[Multi-Tenant Patterns]] · [[Protected Routes End-to-End]]

## What To Learn Next
- [[Replication and Failover]] · [[Backups and Restore]]

## Best Learning Resources

### Official Documentation
- [Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)

### Best YouTube Resource
- [Hussein Nasser — Postgres RLS](https://www.youtube.com/@hnasr)
- [Supabase — RLS deep dives](https://www.youtube.com/@Supabase)

### Best Free Course
- [Supabase RLS docs + tutorials](https://supabase.com/docs/guides/auth/row-level-security)

### Best Advanced Resource
- [Crunchy Data — RLS patterns](https://www.crunchydata.com/blog/)
- [PostgresPro — RLS internals](https://postgrespro.com/)

### Best Practice Project
Add RLS to an existing multi-tenant Postgres app. Verify cross-tenant access is denied even when the app code "forgets" the WHERE. Measure performance impact under load.

### Recommended Order to Learn
1. ENABLE ROW LEVEL SECURITY + simple policy
2. Setting context via `SET LOCAL`
3. SELECT vs INSERT/UPDATE policies (`USING` vs `WITH CHECK`)
4. FORCE RLS
5. Performance (indexing the predicate columns)
6. Combining with Supabase JWT claims

## Interview Questions
**Q. RLS vs application-level filtering?**
A. RLS enforces in the DB — the app can't forget. App-level is faster (one filter) but bug-prone.

**Q. Why `SET LOCAL`?**
A. Scopes the setting to the current transaction; resets after commit.

**Q. How does Supabase use RLS?**
A. JWT claims (`auth.uid()`, `auth.role()`) drive policies — PostgREST exposes the DB directly; RLS is the only auth.

## Related
- [[Multi-Tenant Patterns]] · [[Protected Routes End-to-End]] · [[PostgreSQL]]
