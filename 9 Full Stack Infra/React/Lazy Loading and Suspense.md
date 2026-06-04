---
tags: [react, advanced, performance]
---

# Lazy Loading and Suspense

> `lazy()` defers loading. `<Suspense>` shows a fallback while it (or data) is pending.

## Example
```jsx
const Editor = lazy(() => import('./Editor'));

<Suspense fallback={<p>Loading…</p>}>
  <Editor />
</Suspense>
```

## With data
React Query, Relay, and the new `use()` hook can suspend on data fetches too.

## Common mistakes
- Nested Suspense without coordinated fallbacks → flashes
- Throwing promises from regular code (must be inside a suspense-aware library)

## Related
- [[Code Splitting]] · [[Concurrent Rendering]]

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
