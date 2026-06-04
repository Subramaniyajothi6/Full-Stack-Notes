---
tags: [react, intermediate, concept]
---

# Context API

> Built-in mechanism to pass values through the tree without prop drilling.

## Setup
```jsx
const AuthCtx = createContext(null);

<AuthCtx.Provider value={{ user, logout }}>
  <App />
</AuthCtx.Provider>
```

## Consume
```jsx
const { user } = useContext(AuthCtx);
```

## Performance
Every consumer re-renders when value identity changes. Mitigations:
- Memoize value with [[useMemo]]
- Split into multiple contexts by update frequency
- Use selector libraries (use-context-selector)

## When NOT to use
- Frequently changing global state → [[Redux Toolkit]] / [[Zustand and Alternatives]]
- Server state → React Query / SWR

## Related
- [[useContext]] · [[Redux Basics]] · [[Performance Optimization]]

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
