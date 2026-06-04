---
tags: [react, intermediate, concept]
---

# Virtual DOM

> An in-memory tree of plain JS objects representing the UI. React diffs old vs new VDOM and patches only what changed.

## Why it matters
Direct DOM mutations are expensive (layout, repaint). VDOM batches and minimizes them.

## Flow
1. State changes → component re-renders
2. New VDOM tree is created
3. [[Reconciliation and Diffing|Diffing algorithm]] compares with previous tree
4. Only changed nodes are committed to the real DOM

## Common mistakes
- Believing VDOM is "always faster" — for small UIs, vanilla DOM may be faster. The win is at scale and developer ergonomics.
- Confusing VDOM with [[Fiber Architecture|Fiber]] (Fiber is the reconciler implementation, VDOM is the data structure).

## Interview angle
- What is the VDOM and why?
- VDOM vs real DOM vs Shadow DOM (Shadow DOM = browser encapsulation, not React)

## Related
- [[Reconciliation and Diffing]] · [[Fiber Architecture]] · [[Performance Optimization]]

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
