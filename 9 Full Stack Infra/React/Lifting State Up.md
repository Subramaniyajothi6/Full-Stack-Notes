---
tags: [react, beginner, pattern]
---

# Lifting State Up

> When two siblings need the same state, move it to their nearest common parent.

## Example
```
       App (holds query)
      /        \
   Search      Results
   (sets)      (reads)
```

## Why
Single source of truth — avoids state desync between components.

## When to lift further
If many distant components need the same state, lift to context or a state manager (see [[Context API]], [[Redux Basics]]).

## Common mistakes
- Lifting too eagerly — keep state local until shared
- Lifting too far — causes unrelated re-renders

## Related
- [[State in React]] · [[Props]] · [[Context API]]

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
