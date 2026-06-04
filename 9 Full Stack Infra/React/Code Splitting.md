---
tags: [react, advanced, performance]
---

# Code Splitting

> Break your bundle into chunks loaded on demand.

## Route-level
```jsx
const Settings = lazy(() => import('./Settings'));

<Suspense fallback={<Spinner />}>
  <Settings />
</Suspense>
```

## Component-level
Lazy-load heavy components (charts, editors).

## Tools
- Vite, webpack — built-in chunk splitting
- Bundle analyzer — find offenders

## Common mistakes
- Splitting too aggressively — many tiny chunks = many requests
- Forgetting Suspense boundary
- Splitting code on the critical path (visible immediately)

## Related
- [[Lazy Loading and Suspense]] · [[Performance Optimization]]

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
