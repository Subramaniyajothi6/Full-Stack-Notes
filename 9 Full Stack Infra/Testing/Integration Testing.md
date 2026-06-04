---
tags: [infra, testing, intermediate]
---

# Integration Testing

> Test multiple units working together — usually a route handler + DB + middleware, or a React component tree.

## Why it matters
Most production bugs live at module boundaries. Integration tests catch them where unit tests can't.

## Approaches
- **API tests** — spin up Express + test DB, fire HTTP requests via supertest
- **Component tests** — render a React tree, fire events (React Testing Library)
- **Container tests** — testcontainers spin up real Postgres/Redis for tests
- **Contract tests** — Pact, ensure producer/consumer agree on schemas

## Example (Express + supertest + Vitest)
```ts
import request from 'supertest';
import { app } from '../src/app';
import { db } from '../src/db';

beforeEach(() => db.users.deleteMany({}));

it('creates user', async () => {
  const res = await request(app).post('/users').send({ email: 'a@b.c' });
  expect(res.status).toBe(201);
  const created = await db.users.findOne({ email: 'a@b.c' });
  expect(created).toBeTruthy();
});
```

## Real World Usage
- API endpoint suites
- DB layer (raw SQL or ORM with real DB)
- Auth flows
- React components reading from real-ish providers

## Common Mistakes
- Sharing state across tests → flakes
- Mocking the DB so much it's a unit test in disguise
- Slow suite from no parallelism (use schemas/databases per worker)
- Using prod DB or shared dev DB → corruption

## Prerequisites
- [[Unit Testing]] · [[Express MOC|Express]]

## What To Learn Next
- [[E2E Testing]] · [[Playwright]] · [[CI CD]]

## Best Learning Resources

### Official Documentation
- [Vitest Docs](https://vitest.dev/) — also runs integration suites
- [supertest GitHub](https://github.com/ladjs/supertest)
- [testcontainers-node](https://node.testcontainers.org/)

### Best YouTube Resource
- [The Net Ninja — Express testing](https://www.youtube.com/c/TheNetNinja)
- [Web Dev Simplified — testing series](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [Testing Library docs + tutorials](https://testing-library.com/docs/) — for component integration
- [Pact docs](https://docs.pact.io/) — contract testing intro

### Best Advanced Resource
- [Test Containers patterns](https://testcontainers.com/guides/) — real-DB testing
- [Kent C. Dodds — Testing Trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)

### Best Practice Project
Add a full integration suite to a MERN repo: per-test ephemeral Postgres via testcontainers, supertest hits Express, asserts DB state. Run in parallel via Vitest workers; ensure suite stays under 60s in CI.

### Recommended Order to Learn
1. supertest + in-memory DB
2. Real DB via testcontainers
3. Auth flows
4. Concurrency / parallelism strategy
5. Component integration with React Testing Library
6. Contract tests with Pact

## Interview Questions
**Q. Unit vs integration test?**
A. Unit isolates one piece with mocks. Integration runs multiple together with real-ish dependencies.

**Q. How do you keep tests independent?**
A. Reset DB between tests; per-worker schemas/DB; never depend on test order.

**Q. When use testcontainers?**
A. When mocking the dependency would lie (real DB has constraints, triggers, transactions a mock can't simulate).

## Related
- [[Unit Testing]] · [[E2E Testing]] · [[Vitest]]
