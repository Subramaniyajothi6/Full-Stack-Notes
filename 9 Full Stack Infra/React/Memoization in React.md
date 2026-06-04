---
tags: [react, advanced, performance]
---

# Memoization in React

> Three tools: `React.memo`, `useMemo`, `useCallback`.

## React.memo
Wrap a component to skip render if props are shallow-equal.
```js
export default React.memo(MyComponent);
```

## useMemo
Cache a value:
```js
const sorted = useMemo(() => list.sort(cmp), [list]);
```

## useCallback
Cache a function:
```js
const onClick = useCallback(() => x(id), [id]);
```

## Custom equality
`React.memo(Comp, (prev, next) => boolean)`.

## Common mistakes
- React.memo wrapping a component whose parent always passes new props (no benefit)
- Memoizing primitives — equality is already cheap

## Related
- [[useMemo]] · [[useCallback]] · [[Performance Optimization]]

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
