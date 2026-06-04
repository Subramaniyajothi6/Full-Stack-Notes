---
tags: [react, intermediate, hook]
---

# useReducer

> Like useState but state transitions go through a reducer function. Good for complex state.

## Signature
```js
const [state, dispatch] = useReducer(reducer, initialState);
```

## Example
```js
function reducer(state, action) {
  switch (action.type) {
    case 'increment': return { count: state.count + 1 };
    case 'reset':     return { count: 0 };
    default: throw new Error();
  }
}
const [state, dispatch] = useReducer(reducer, { count: 0 });
dispatch({ type: 'increment' });
```

## When to prefer over useState
- Multiple sub-values that change together
- Next state depends on previous + action shape
- Want to test state logic in isolation (reducer is pure)

## Common mistakes
- Mutating state inside reducer — must return new object
- Putting effects inside reducer — reducer must be pure

## Interview angle
- useReducer vs Redux ([[Redux Toolkit]] is built on the same idea, scoped globally)
- Why must reducers be pure?

## Related
- [[useState]] · [[Redux Basics]] · [[useContext]]

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
