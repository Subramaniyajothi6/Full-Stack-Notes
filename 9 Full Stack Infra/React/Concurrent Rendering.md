---
tags: [react, advanced, modern]
---

# Concurrent Rendering

> Rendering can be paused, resumed, or abandoned. Powered by [[Fiber Architecture|Fiber]].

## APIs
- `useTransition` — mark updates as non-urgent
- `useDeferredValue` — derive a delayed copy of a value
- `<Suspense>` — coordinate loading states

## Example
```js
const [isPending, startTransition] = useTransition();
startTransition(() => setQuery(input));
```

## Common mistakes
- Wrapping urgent updates (typing) in transition
- Expecting transitions to debounce — they prioritize, not delay

## Related
- [[Fiber Architecture]] · [[Lazy Loading and Suspense]]

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
