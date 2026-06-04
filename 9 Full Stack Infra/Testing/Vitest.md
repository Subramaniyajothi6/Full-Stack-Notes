---
tags: [infra, testing, beginner]
---

# Vitest

> Fast, Vite-powered test runner. Jest-compatible API; best DX for modern TS/ESM projects.

## Why it matters
Replaces Jest in Vite-based projects with native ESM, instant HMR for tests, TS support out of the box.

## Core features
- Globs config, no babel
- `describe` / `it` / `expect` Jest-like API
- `vi.fn()` / `vi.mock()` for mocking
- Coverage via `c8`
- Watch + UI mode (browser test runner)
- Workspaces for monorepos

## Setup
```bash
npm i -D vitest @vitest/coverage-v8
```

```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'jsdom',          // or 'node'
    globals: true,                  // optional, no need to import describe/it
    coverage: { provider: 'v8' },
  },
});
```

```ts
// math.test.ts
import { add } from './math';
test('add', () => expect(add(1, 2)).toBe(3));
```

## Real World Usage
- Default runner for Vite-based React apps
- Replacing Jest in Node libs
- Testing Astro / SvelteKit / Solid

## Common Mistakes
- Forgetting `environment: 'jsdom'` for component tests
- Using `vi.useFakeTimers()` then forgetting to restore
- Mocking modules path mismatch — use absolute or vite alias
- No CI step running coverage thresholds

## Prerequisites
- [[Unit Testing]]

## What To Learn Next
- [[Integration Testing]] · [[Playwright]]

## Best Learning Resources

### Official Documentation
- [Vitest Docs](https://vitest.dev/) — examples + API ref
- [Vitest UI](https://vitest.dev/guide/ui)

### Best YouTube Resource
- [Anthony Fu (Vitest creator) talks](https://www.youtube.com/results?search_query=anthony+fu+vitest)
- [Web Dev Simplified — Vitest](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [Vitest Guide](https://vitest.dev/guide/) — official, suffices

### Best Advanced Resource
- [Vitest source on GitHub](https://github.com/vitest-dev/vitest)
- [Anthony Fu's blog](https://antfu.me/) — design notes

### Best Practice Project
Migrate a Jest project to Vitest: drop babel, keep tests; add `vitest --ui` to dev workflow; configure coverage thresholds; benchmark suite time before/after.

### Recommended Order to Learn
1. Basic config + first test
2. Mocking + spies
3. Snapshot testing
4. Coverage thresholds
5. UI + watch mode
6. Workspaces

## Interview Questions
**Q. Vitest vs Jest?**
A. Native ESM/TS, faster, Vite-aligned config, fewer babel issues. Jest still strong but slower in modern stacks.

**Q. How does Vitest mock modules?**
A. `vi.mock('module', factory)` with hoisting via Vite plugin. Path matching follows Vite resolve.

## Related
- [[Unit Testing]] · [[Integration Testing]]
