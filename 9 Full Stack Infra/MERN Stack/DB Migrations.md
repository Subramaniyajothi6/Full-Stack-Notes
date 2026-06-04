---
tags: [mern, deployment, intermediate]
---

# DB Migrations

> Versioned, repeatable, forward-only schema changes that run safely as part of deploys.

## Why a tool, not raw scripts
- **Versioned** — every schema change has an id; history is in git
- **Repeatable** — running twice is a no-op
- **Reviewable** — migrations are PRs
- **Reversible (carefully)** — most teams treat migrations as forward-only and roll forward instead of down

## Tools by stack
| Stack            | Tool                                |
| ---------------- | ----------------------------------- |
| Postgres + Node  | Prisma Migrate · Drizzle · Knex · TypeORM |
| MongoDB + Node   | migrate-mongo · `migrate` · custom  |
| Anything         | Sqitch · Liquibase · Flyway         |

## Pattern — additive migrations (zero-downtime)
1. **Add** new column with default (or nullable) — old code still works
2. **Backfill** in a job (chunked to avoid lock storms)
3. **Switch reads** in code to the new column
4. **Switch writes** dual-write briefly (defensive)
5. **Drop** old column in a later release

Never combine "rename" + "remove old" + "deploy code that uses new" in one step. Each step is a separate, deployable, revertable migration.

## Mongo example (`migrate-mongo`)
```js
// migrations/20260101-add-user-locale.js
module.exports = {
  async up(db) {
    await db.collection('users').updateMany(
      { locale: { $exists: false } },
      { $set: { locale: 'en' } }
    );
    await db.collection('users').createIndex({ locale: 1 });
  },
  async down(db) {
    await db.collection('users').dropIndex({ locale: 1 });
    await db.collection('users').updateMany({}, { $unset: { locale: '' } });
  },
};
```

## Migrations in CI/CD
```yaml
- run: npm run db:migrate
  env: { DATABASE_URL: ${{ secrets.STAGING_DATABASE_URL }} }
```
Run before app boot. Lock so concurrent deploys don't race (most tools use a `_migrations` table/collection with a row lock).

## Real World Usage
- Adding indexes to fix a slow query
- Splitting a `name` column into `first/last`
- Migrating from JSON blob to typed columns
- Adding tenant scoping to existing rows
- Backfilling computed/denormalized fields

## Common Mistakes
- Doing breaking renames in one shot → app deployed against old schema crashes
- Backfilling unbatched → table-locking sweep that times out
- No `_migrations` lock → two deploys try to run the same migration concurrently
- Migrations that read from production data without limits → runaway memory
- Treating Mongo as "no migrations needed" — schema-on-read still drifts; you need versioned data fixes
- Down migrations that lose data — generally unsafe; prefer forward-only

## Prerequisites
- [[Full-Stack CI CD]] · [[MongoDB]] · [[PostgreSQL]] · [[Deployment Architecture]]

## What To Learn Next
- [[Backups and Restore]] · [[Multi-Tenant Patterns]]

## Best Learning Resources

### Official Documentation
- [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate)
- [Drizzle Migrations](https://orm.drizzle.team/docs/migrations)
- [migrate-mongo](https://github.com/seppevs/migrate-mongo)
- [Sqitch](https://sqitch.org/) — the rigorous one

### Best YouTube Resource
- [Hussein Nasser — schema migration patterns](https://www.youtube.com/@hnasr)
- [Theo — Drizzle vs Prisma](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Atlas migrations docs (free open-source)](https://atlasgo.io/getting-started)
- [PlanetScale schema deploy guide](https://planetscale.com/docs/concepts/branching)

### Best Advanced Resource
- [Designing Data-Intensive Applications — schema evolution chapters](https://dataintensive.net/)
- [Strong Migrations (Rails ecosystem, principles transfer)](https://github.com/ankane/strong_migrations)

### Best Practice Project
On a sample MERN app, add three migrations: (1) add a column with default, (2) backfill in a chunked script, (3) drop an old column. Run each as a separate PR with separate deploys. Verify the app stays up across all three.

### Recommended Order to Learn
1. Why migrations exist (drift, vs ad-hoc)
2. Tool of choice for your DB
3. Forward-only philosophy
4. Additive multi-step rename pattern
5. Backfill jobs (chunked + idempotent)
6. Locking + concurrent deploys
7. Production cutover plans

## Interview Questions
**Q. Why forward-only?**
A. Down migrations risk data loss and assume reversibility that rarely holds in production.

**Q. How do you do a zero-downtime column rename?**
A. Add new column → dual-write → backfill → switch reads → switch writes → drop old. Multiple deploys.

**Q. Mongo — schemaless, so no migrations?**
A. The schema lives in app code. You still need versioned data migrations (e.g., backfilling new fields).

## Related
- [[MongoDB]] · [[PostgreSQL]] · [[Full-Stack CI CD]] · [[Backups and Restore]]
