---
tags: [testing, intermediate, syntax]
---

# React Testing Library

> Render React, find elements like a user would, assert behavior. Pairs with [[Vitest]] (or Jest).

## Philosophy
"The more your tests resemble the way your software is used, the more confidence they give you." — Kent C. Dodds

## Setup
```ts
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
export default defineConfig({
  plugins: [react()],
  test: { environment: 'jsdom', setupFiles: './test/setup.ts' },
});

// test/setup.ts
import '@testing-library/jest-dom/vitest';
```

## Anatomy
```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('increments counter', async () => {
  render(<Counter />);
  const user = userEvent.setup();

  expect(screen.getByText(/0/)).toBeInTheDocument();
  await user.click(screen.getByRole('button', { name: /add/i }));
  expect(screen.getByText(/1/)).toBeInTheDocument();
});
```

## Query priority (most → least preferred)
1. `getByRole` (accessible)
2. `getByLabelText` (form fields)
3. `getByPlaceholderText`
4. `getByText`
5. `getByDisplayValue`
6. `getByAltText` / `getByTitle`
7. `getByTestId` (last resort)

## Variants
- `getBy*` — throws if missing
- `queryBy*` — null if missing (assert non-existence)
- `findBy*` — async, waits for it to appear

## Mocking
- Network: [[MSW]]
- Modules: `vi.mock('./api')`
- Timers: `vi.useFakeTimers()`

## Real World Usage
- Component-level integration tests
- Hook tests via `renderHook`
- Form validation flows
- Routing assertions
- Error boundary fallbacks

## Common Mistakes
- Selecting by class name or DOM structure (brittle)
- Testing implementation details (`expect(component.state.x)`)
- `act()` warnings ignored — usually means missing await
- Asserting `expect(...).toBeTruthy()` instead of `.toBeInTheDocument()`
- Not awaiting `user.click` (it's async)
- Wrapping every test in a custom render without `userEvent.setup()`

## Prerequisites
- [[Unit Testing]] · [[Vitest]] · [[React MOC]]

## What To Learn Next
- [[MSW]] · [[Visual Regression]] · [[E2E Testing]]

## Best Learning Resources

### Official Documentation
- [Testing Library docs](https://testing-library.com/)
- [user-event v14](https://testing-library.com/docs/user-event/intro)

### Best YouTube Resource
- [Kent C. Dodds — Testing](https://www.youtube.com/c/KentCDodds-vids)
- [Web Dev Simplified — RTL](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [Testing JavaScript (free intro)](https://testingjavascript.com/)
- [Testing Library Cheatsheet](https://testing-library.com/docs/dom-testing-library/cheatsheet/)

### Best Advanced Resource
- [Kent C. Dodds blog](https://kentcdodds.com/blog) — testing patterns

### Best Practice Project
Take an under-tested component (form with validation, list with filter). Write tests covering: happy path, validation errors, empty state, loading state. Assert via queries that match real user actions.

### Recommended Order to Learn
1. `render` + `screen.getByRole`
2. `userEvent` for clicks/typing
3. `findBy*` for async UIs
4. Module mocks
5. MSW for network mocking
6. `renderHook` for custom hooks

## Interview Questions
**Q. Why `getByRole` over `getByTestId`?**
A. Role queries also verify accessibility — if a screen reader can't find it, your test fails too. Test IDs are a last-resort escape hatch.

**Q. `queryBy*` vs `getBy*`?**
A. `getBy` throws on absence; `queryBy` returns null. Use `queryBy` to assert "shouldn't be there."

## Related
- [[Vitest]] · [[MSW]] · [[Unit Testing]] · [[React MOC]]
