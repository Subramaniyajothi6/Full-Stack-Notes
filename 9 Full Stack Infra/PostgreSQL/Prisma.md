---
tags: [postgresql, orm, intermediate, syntax]
---

# Prisma

> Type-safe Node ORM. Schema-first; generates a fully-typed client from `schema.prisma`.

## Why
- Single source of truth schema → typed client
- Solid migration tooling (Prisma Migrate)
- Multi-DB support (Postgres, MySQL, MongoDB, SQLite, SQL Server, CockroachDB)
- Great DX in IDE

## Schema
```prisma
generator client { provider = "prisma-client-js" }
datasource db    { provider = "postgresql"; url = env("DATABASE_URL") }

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  posts     Post[]
  createdAt DateTime @default(now())
}

model Post {
  id       String  @id @default(cuid())
  title    String
  body     String
  author   User    @relation(fields: [authorId], references: [id])
  authorId String
}
```

## Client
```ts
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

const user = await prisma.user.create({
  data: { email: 'a@b.c', posts: { create: [{ title: 'Hi', body: '...' }] } },
});

const recent = await prisma.post.findMany({
  where: { author: { email: 'a@b.c' } },
  orderBy: { createdAt: 'desc' },
  take: 10,
  include: { author: true },
});
```

## Migrations
```bash
npx prisma migrate dev --name init      # dev: create + apply
npx prisma migrate deploy               # CI/prod: apply only
npx prisma db push                      # prototyping (no migration files)
```

## Prisma vs Drizzle
| Aspect            | Prisma                        | Drizzle                  |
|-------------------|-------------------------------|--------------------------|
| API style         | Object query builder          | SQL-like, closer to wire |
| Bundle size       | Larger (engine binary)        | Tiny                     |
| Edge runtime      | Needs Accelerate / Driver Adapter | Native              |
| Migrations        | Built-in, mature              | Drizzle Kit              |
| Raw SQL           | `$queryRaw`                   | First-class              |

## Real World Usage
- Type-safe internal APIs
- Next.js + Prisma + PostgreSQL stack
- Multi-tenant apps (with row filters in middleware)
- Replacing Mongoose for Mongo-on-Atlas

## Common Mistakes
- `findMany` without `take` on huge tables
- N+1 from `findUnique` in a loop (use `findMany` + `where: { id: { in: ids } }`)
- Forgetting `prisma.$disconnect()` in scripts
- Default `PrismaClient` creating new instances per HMR refresh — singleton pattern in dev
- Edge runtime without Accelerate/Driver Adapter → "engine not found"
- Generating client from prod DB host (use shadow DB)

## Prerequisites
- [[PostgreSQL]] · [[TypeScript]] · [[DB Migrations]]

## What To Learn Next
- [[Indexes in PostgreSQL]] · [[Connection Pooling]] · [[Row-Level Security]]

## Best Learning Resources

### Official Documentation
- [Prisma docs](https://www.prisma.io/docs)
- [Prisma Schema Reference](https://www.prisma.io/docs/orm/reference/prisma-schema-reference)

### Best YouTube Resource
- [Web Dev Simplified — Prisma](https://www.youtube.com/c/WebDevSimplified)
- [Theo — Prisma vs Drizzle](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Prisma getting started](https://www.prisma.io/docs/getting-started)
- [create-t3-app](https://create.t3.gg/) — opinionated Next + Prisma starter

### Best Advanced Resource
- [Prisma engineering blog](https://www.prisma.io/blog)
- [Prisma Driver Adapters](https://www.prisma.io/docs/orm/overview/databases/database-drivers)

### Best Practice Project
Migrate a MongoDB+Mongoose app to Postgres+Prisma. Define schema; run `migrate dev`; rewrite queries; verify type safety throughout.

### Recommended Order to Learn
1. Schema + first migration
2. CRUD via client
3. Relations + nested writes
4. Transactions (`$transaction`)
5. Middleware / extensions
6. Performance (`include` vs `select`, indexes)
7. Edge with Driver Adapters

## Interview Questions
**Q. Prisma vs Drizzle?**
A. Prisma = high-level query builder + mature migrations + larger runtime. Drizzle = SQL-close, tiny, edge-native. Prisma DX wins for many teams; Drizzle wins for perf and edge.

**Q. Why does Prisma generate types?**
A. The schema is the contract; the generated client guarantees compile-time correctness for all field selections + relations.

## Related
- [[PostgreSQL]] · [[DB Migrations]] · [[Connection Pooling]] · [[TypeScript]]
