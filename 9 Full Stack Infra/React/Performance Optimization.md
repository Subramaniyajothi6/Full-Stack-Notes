---
tags: [react, advanced, performance]
---

# Performance Optimization

> Measure first. Optimize the bottleneck. Don't memoize everything.

## Tools
- React DevTools Profiler
- `<Profiler>` API
- Browser perf timeline

## Common wins
- **List virtualization** — react-window for 1000+ rows
- **Code split** — see [[Code Splitting]]
- **Memoize** heavy children with `React.memo` + stable props ([[useCallback]], [[useMemo]])
- Avoid passing fresh objects/arrays as props each render
- Move state down — keep updates local

## Common mistakes
- Memoizing trivial components — overhead exceeds savings
- Re-rendering whole app on every keystroke (state too high)
- Forgetting that React.memo only does shallow compare

## Related
- [[Memoization in React]] · [[Code Splitting]] · [[Lazy Loading and Suspense]]

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
