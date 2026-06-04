---
tags: [infra, testing, beginner]
---

# Unit Testing

> Test the smallest pieces of your code (a function, a module) in isolation.

## Why it matters
Fast feedback loop, catches regressions, documents intent. Foundation of the test pyramid.

## Core ideas
- **AAA** — Arrange, Act, Assert
- **Isolation** — mock external deps (network, DB, time)
- **Determinism** — same input → same result, no flakes
- **Coverage** — useful as a smell, harmful as a target

## Example (Vitest)
```ts
import { describe, it, expect } from 'vitest';
import { add } from './math';

describe('add', () => {
  it('adds positives', () => expect(add(2, 3)).toBe(5));
  it('handles zero', () => expect(add(0, 5)).toBe(5));
});
```

## Real World Usage
- Pure utility functions (formatters, validators)
- Reducers / state-machine transitions
- Domain logic (pricing, eligibility)
- Pre-commit gating in CI

## Common Mistakes
- Mocking too much → tests pass, real code fails
- Asserting implementation details, not behavior
- Coverage chasing → "tests" that don't assert
- Slow unit tests (network/DB inside) — that's integration

## Prerequisites
- [[Functions Basics|Functions]]

## What To Learn Next
- [[Vitest]] · [[Integration Testing]] · [[E2E Testing]]

## Best Learning Resources

### Official Documentation
- [Vitest Docs](https://vitest.dev/)
- [Jest Docs](https://jestjs.io/)
- [Testing Library — guiding principles](https://testing-library.com/docs/guiding-principles/)

### Best YouTube Resource
- [Web Dev Simplified — Testing](https://www.youtube.com/c/WebDevSimplified)
- [Kent C. Dodds (testing philosophy)](https://www.youtube.com/c/KentCDodds-vids)

### Best Free Course
- [Testing JavaScript by Kent C. Dodds (free intro)](https://testingjavascript.com/) — paid full
- [Vitest tutorial in docs](https://vitest.dev/guide/)

### Best Advanced Resource
- [Kent Beck — Test Driven Development](https://www.oreilly.com/library/view/test-driven-development/0321146530/)
- [Martin Fowler — Test Pyramid + Testing strategies](https://martinfowler.com/articles/practical-test-pyramid.html)

### Best Practice Project
Take a function-rich module in your project (validators, parsers). Add 100% behavioral test coverage with Vitest. Use `vi.fn()` to mock callbacks; cover edge cases (empty, nulls, large inputs).

### Recommended Order to Learn
1. Test runner basics (Vitest/Jest)
2. Mocking + spying
3. Snapshot testing (use sparingly)
4. Test doubles (stubs, mocks, fakes)
5. TDD cycle

## Interview Questions
**Q. What makes a good unit test?**
A. Fast, deterministic, isolated, asserts behavior, single reason to fail.

**Q. Mocks vs stubs?**
A. Stub = canned return. Mock = stub + assertion ("was it called with X?").

**Q. Why is 100% coverage a bad target?**
A. Forces useless tests on trivial code; doesn't measure assertion quality.

## Related
- [[Vitest]] · [[Integration Testing]] · [[E2E Testing]]
