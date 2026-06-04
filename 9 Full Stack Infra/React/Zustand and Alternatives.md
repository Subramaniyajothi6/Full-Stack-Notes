---
tags: [react, intermediate, state-management]
---

# Zustand and Alternatives

> Lightweight stores. Smaller API than Redux for app-level state.

## Zustand
```js
import { create } from 'zustand';
const useStore = create(set => ({
  count: 0,
  inc: () => set(s => ({ count: s.count + 1 }))
}));

// in component
const count = useStore(s => s.count);
```

## When to choose
- Zustand — minimalist, no provider
- Jotai — atomic state
- Recoil — derived selectors, atoms
- Redux Toolkit — strict, devtools-rich
- TanStack Query / SWR — server state caching (use alongside)

## Related
- [[Redux Toolkit]] · [[Context API]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Common Mistakes
- TODO: pitfalls and edge cases

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
