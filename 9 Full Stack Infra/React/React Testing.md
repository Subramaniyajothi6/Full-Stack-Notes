---
tags: [react, intermediate, testing]
---

# React Testing

> Test behavior, not implementation. Use React Testing Library.

## Stack
- **Vitest / Jest** — runner
- **React Testing Library** — render + query
- **MSW** — mock network

## Example
```js
import { render, screen, fireEvent } from '@testing-library/react';

test('increments', () => {
  render(<Counter />);
  fireEvent.click(screen.getByRole('button', { name: /add/i }));
  expect(screen.getByText('1')).toBeInTheDocument();
});
```

## Query priority
1. `getByRole` — accessible
2. `getByLabelText` — forms
3. `getByText` — non-interactive
4. avoid `getByTestId` unless necessary

## Common mistakes
- Testing implementation details (state shape, internal methods)
- Ignoring `act` warnings
- Querying with brittle selectors

## Related
- [[Performance Optimization]] · [[Components]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://react.dev/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Jack Herrington, Theo, Web Dev Simplified

### Best Free Course
- TODO

### Best Advanced Resource
- TODO

### Best Practice Project
- TODO: 1-paragraph project idea

### Recommended Order to Learn
1. TODO
2. TODO
3. TODO

## Interview Questions
**Q. TODO** — A. ...

**Q. TODO** — A. ...
