---
tags: [react, advanced, concept]
---

# Fiber Architecture

> React 16+ rewrite of the reconciler enabling interruptible, prioritized rendering.

## Why it matters
Pre-Fiber React rendered synchronously and could block the main thread. Fiber splits work into units and can pause/resume — this enables [[Concurrent Rendering]] and [[Lazy Loading and Suspense|Suspense]].

## Key ideas
- **Fiber node** = unit of work (one per component instance)
- **Phases**: render (interruptible) and commit (synchronous)
- **Priorities**: urgent updates (typing) outrank non-urgent (data refresh)

## Common mistakes
- Assuming render phase mutates DOM — it doesn't, only commit does
- Side effects in render — must go in `useEffect` so they run after commit

## Interview angle
- Why was Fiber introduced?
- Render vs commit phase — when do effects fire?

## Related
- [[Concurrent Rendering]] · [[useEffect]] · [[Reconciliation and Diffing]]

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
