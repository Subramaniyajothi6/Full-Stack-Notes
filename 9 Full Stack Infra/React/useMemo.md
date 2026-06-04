---
tags: [react, advanced, hook, performance]
---

# useMemo

> Cache an expensive computation between renders.

## Signature
```js
const result = useMemo(() => expensive(a, b), [a, b]);
```

## When to use
- Heavy computations (filtering huge lists, parsing)
- Stable object/array references for memoized children or [[useEffect]] deps

## Common mistakes
- **Premature memoization** — adds overhead for trivial work
- Wrong dep array — stale results
- Treating it as a guarantee — React may discard the cache

## Interview angle
- Difference vs [[useCallback]] (memo a value vs memo a function)
- Why isn't memoization free?

## Related
- [[useCallback]] · [[Memoization in React]] · [[Performance Optimization]]

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
