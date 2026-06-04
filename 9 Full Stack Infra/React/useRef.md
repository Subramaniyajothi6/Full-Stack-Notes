---
tags: [react, intermediate, hook]
---

# useRef

> Mutable container that persists across renders without triggering re-render.

## Two uses
1. **DOM access** — `<input ref={inputRef} />` then `inputRef.current.focus()`
2. **Mutable instance value** — store a timer id, previous value, etc.

## Example
```jsx
const prev = useRef();
useEffect(() => { prev.current = value; });
```

## Common mistakes
- Reading `ref.current` during render — refs are not reactive
- Treating ref like state — mutating it does **not** re-render
- Forwarding refs to functional components without `forwardRef`

## Edge cases
- `useRef(null)` is the typical DOM ref
- Refs survive re-renders but reset on unmount

## Interview angle
- Ref vs state — when to choose
- How does `forwardRef` work?

## Related
- [[useState]] · [[useEffect]] · [[Performance Optimization]]

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
