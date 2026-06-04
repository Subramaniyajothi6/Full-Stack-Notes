---
tags: [react, intermediate, hook]
---

# useEffect

> Run side effects after render — data fetching, subscriptions, DOM manipulation.

## Signature
```js
useEffect(() => {
  // effect
  return () => {
    // cleanup (runs before next effect or on unmount)
  };
}, [deps]);
```

## Dep array semantics
- `[]` — run once after mount, cleanup on unmount
- `[a, b]` — run when `a` or `b` changes (Object.is comparison)
- omitted — run after every render

## Example — subscription
```js
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);
}, []);
```

## Common mistakes
- **Missing deps** — leads to stale closures (capture old state values)
- **Object/array deps** — they change identity each render; memoize with [[useMemo]]
- Setting state in effect without a guard — infinite loop
- Using effects for derived data — compute during render instead

## Edge cases
- Effects run twice in StrictMode (dev only) to catch impurities
- Cleanup runs **before** the next effect, not after

## Interview angle
- Effect vs layout effect (`useLayoutEffect` runs synchronously after DOM mutation, before paint — used for measuring layout)
- Why do effects run after paint?

## Related
- [[useState]] · [[useRef]] · [[Custom Hooks]] · [[Rules of Hooks]]

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
