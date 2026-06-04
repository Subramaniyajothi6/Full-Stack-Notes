---
tags: [testing, intermediate, integration]
---

# Contract Testing

> Tests that verify the producer and consumer of an API agree on its shape. Catches contract drift early without running everything together.

## The problem
- Frontend tests its mocks (passes)
- Backend tests its own handlers (passes)
- Production: backend changes a field name → frontend breaks
- Integration / E2E tests catch it, but late + slow

## Pact pattern
1. **Consumer** records expected interactions while running tests against a Pact-recording mock
2. **Pact file** (JSON) describes "GET /users/1 returns { id, email }"
3. **Producer** replays the Pact against its real implementation
4. CI fails if shapes diverge

## Pact JS example (consumer)
```ts
import { PactV3 } from '@pact-foundation/pact';

const provider = new PactV3({ consumer: 'web', provider: 'api' });

test('GET /users/:id', async () => {
  provider
    .uponReceiving('a request for user 1')
    .withRequest({ method: 'GET', path: '/users/1' })
    .willRespondWith({ status: 200, body: { id: '1', email: 'a@b.c' } });

  await provider.executeTest(async (mockServer) => {
    const user = await getUser(mockServer.url + '/users/1');
    expect(user.email).toBe('a@b.c');
  });
});
```

## Alternative — OpenAPI as contract
- Spec lives in repo
- Codegen for both sides
- Validate runtime traffic against spec (Dredd, Schemathesis)

## When to use
- Multi-service systems where running everything together for every PR is slow
- Mobile clients pinned to API versions
- Public APIs with external consumers
- Microservices teams shipping independently

## Real World Usage
- Pact Broker shared between consumer / producer CI
- OpenAPI + codegen for type safety
- Schemathesis-driven property tests against producer
- Schema registries (Confluent for Kafka)

## Common Mistakes
- Testing irrelevant shapes (every field) → brittle contracts
- Skipping producer verification (consumer thinks it works; producer drifts)
- One big contract → bottleneck; prefer per-interaction contracts
- Treating contract as runtime validation — it's compile-time / test-time

## Prerequisites
- [[Integration Testing]] · [[API Contract]] · [[MSW]]

## What To Learn Next
- [[Visual Regression]] · [[Load Testing]]

## Best Learning Resources

### Official Documentation
- [Pact docs](https://docs.pact.io/)
- [OpenAPI spec](https://swagger.io/specification/)
- [Schemathesis](https://schemathesis.readthedocs.io/)

### Best YouTube Resource
- [Pactflow YouTube](https://www.youtube.com/c/Pactflow)

### Best Free Course
- [Pact getting started](https://docs.pact.io/5-minute-getting-started-guide)
- [Atlassian — Contract Testing](https://www.atlassian.com/continuous-delivery/software-testing/contract-testing)

### Best Advanced Resource
- [Martin Fowler — Contract Tests](https://martinfowler.com/bliki/ContractTest.html)

### Best Practice Project
Add Pact between a frontend and a Node service. Cause a breaking change in the producer; verify the consumer's CI fails. Then evolve the API additively to keep both green.

### Recommended Order to Learn
1. Pact consumer-side
2. Pact producer verification
3. Pact Broker setup
4. OpenAPI alternative
5. Property-based contract testing
6. Per-team workflow

## Interview Questions
**Q. Pact vs E2E?**
A. Pact tests the shape of interactions, fast + isolated. E2E tests user flows end-to-end, slow + holistic. Use both.

**Q. Who owns the contract?**
A. Consumer-driven Pact: the consumer records what it expects; the producer must satisfy it.

## Related
- [[Integration Testing]] · [[API Contract]] · [[Type Sharing]] · [[E2E Testing]]
