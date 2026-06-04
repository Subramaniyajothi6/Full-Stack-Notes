---
tags: [react, advanced, hook, performance]
---

# useCallback

> Cache a function reference across renders.

## Signature
```js
const handleClick = useCallback(() => doThing(id), [id]);
```

## When to use
- Passing callback to a memoized child (`React.memo`)
- Used as dep in [[useEffect]] / [[useMemo]]

## Common mistakes
- Wrapping every function — useless without `React.memo` consumer
- Wrong deps causing stale closures

## Interview angle
- `useCallback(fn, deps)` ≡ `useMemo(() => fn, deps)`
- Why does it matter for child re-renders?

## Related
- [[useMemo]] · [[Memoization in React]] · [[Performance Optimization]]

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
