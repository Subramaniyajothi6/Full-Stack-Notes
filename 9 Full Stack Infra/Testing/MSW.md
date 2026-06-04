---
tags: [testing, intermediate, tooling]
---

# MSW

> Mock Service Worker — intercepts network requests at the network layer. Same handlers work for tests, dev, and Storybook.

## Why
Mocking `fetch` per test is brittle. MSW intercepts via a service worker (browser) or Node request hook — tests use real `fetch` and components don't know they're mocked.

## Setup
```ts
// mocks/handlers.ts
import { http, HttpResponse } from 'msw';

export const handlers = [
  http.get('/api/users/:id', ({ params }) =>
    HttpResponse.json({ id: params.id, email: 'a@b.c' })),
  http.post('/api/users', async ({ request }) => {
    const body = await request.json();
    return HttpResponse.json({ id: '1', ...body }, { status: 201 });
  }),
];

// mocks/server.ts (Node — for Vitest)
import { setupServer } from 'msw/node';
import { handlers } from './handlers';
export const server = setupServer(...handlers);

// test/setup.ts
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

## Per-test overrides
```ts
test('handles 500', async () => {
  server.use(http.get('/api/users/:id', () => new HttpResponse(null, { status: 500 })));
  render(<UserProfile />);
  expect(await screen.findByText(/error/i)).toBeInTheDocument();
});
```

## Dev mode
Browser worker handler intercepts in the running app — same handlers, no backend needed for frontend development.

## Real World Usage
- Component tests that fetch data
- Local dev when backend is unstable / not ready
- Storybook stories with realistic API responses
- E2E (Playwright/Cypress) against a stable mocked backend

## Common Mistakes
- `onUnhandledRequest: 'warn'` instead of `'error'` → silent leak when a real request slips through
- Not resetting handlers between tests → bleed-over
- Mocking too far from reality → tests pass; prod fails
- Editing handlers globally for one test (use `server.use(...)`)
- Forgetting to start MSW in the test setup file

## Prerequisites
- [[Unit Testing]] · [[React Testing Library]] · [[Vitest]]

## What To Learn Next
- [[E2E Testing]] · [[Contract Testing]]

## Best Learning Resources

### Official Documentation
- [MSW docs](https://mswjs.io/)
- [MSW v2 migration guide](https://mswjs.io/docs/migrations/1.x-to-2.x)

### Best YouTube Resource
- [Web Dev Cody — MSW + React](https://www.youtube.com/@WebDevCody)
- [Kent C. Dodds — Mocking with MSW](https://www.youtube.com/c/KentCDodds-vids)

### Best Free Course
- [Testing JavaScript — MSW chapter (free preview)](https://testingjavascript.com/)
- [TkDodo — Testing React Query with MSW](https://tkdodo.eu/blog/)

### Best Advanced Resource
- [MSW source on GitHub](https://github.com/mswjs/msw) — see how interception works

### Best Practice Project
Add MSW to a component test suite. Replace every `vi.mock('axios', ...)`-style hack with MSW handlers. Then enable MSW in dev mode for local-only screens.

### Recommended Order to Learn
1. Handlers + matchers
2. Node setup for Vitest
3. Per-test handler overrides
4. Browser worker for dev mode
5. Combining with Storybook
6. Generating handlers from OpenAPI

## Interview Questions
**Q. Why MSW over mocking `fetch`?**
A. Works at the network layer — components run unchanged; one set of mocks works for tests, dev, Storybook, E2E.

**Q. Risk of mocks drifting from real API?**
A. Yes — pair with contract tests (Pact) or generate handlers from the OpenAPI spec to stay in sync.

## Related
- [[Unit Testing]] · [[React Testing Library]] · [[E2E Testing]] · [[Contract Testing]]
