---
tags: [react, beginner, hook]
---

# useState

> Hook that adds local state to a function component.

## Signature
```js
const [value, setValue] = useState(initialValue);
```

## Lazy initial state
If init is expensive, pass a function — runs only on first render.
```js
const [data] = useState(() => expensiveCompute());
```

## Functional updates
Use when new state depends on previous:
```js
setCount(prev => prev + 1);
```

## Common mistakes
- Calling setter in render → infinite loop
- Using objects without spreading: `setUser({ name: 'a' })` overwrites entire object — use `setUser(u => ({ ...u, name: 'a' }))`
- Storing JSX or functions in state when a derived value would do

## Edge cases
- React bails out when next === current (Object.is)
- Updates inside async callbacks are batched in React 18

## Interview angle
- Why prefer functional updates?
- How is initial state stored across renders?

## Related
- [[State in React]] · [[useReducer]] · [[Rules of Hooks]]

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
