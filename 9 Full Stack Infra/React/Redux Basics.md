---
tags: [react, intermediate, state-management]
---

# Redux Basics

> Predictable state container: single store, pure reducers, dispatched actions.

## Core concepts
- **Store** — single object holding the entire state
- **Action** — `{ type, payload }`
- **Reducer** — `(state, action) => newState`, pure
- **Dispatch** — `store.dispatch(action)`
- **Selector** — function reading from state

## Flow
View → dispatch(action) → reducer → new state → re-render

## When to use
Truly global state shared across many far-apart components, time-travel debugging, complex transitions.

## Modern Redux
Use [[Redux Toolkit]] — eliminates boilerplate.

## Related
- [[Redux Toolkit]] · [[useReducer]] · [[Context API]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Common Mistakes
- TODO: pitfalls and edge cases

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
