---
tags: [react, beginner, concept]
---

# State in React

> Data owned by a component that changes over time and triggers re-render.

## Snapshot semantics
State during a render is a **snapshot**. Setters schedule a re-render with new state — they don't mutate the current one.

```jsx
const [count, setCount] = useState(0);
setCount(count + 1);
setCount(count + 1); // still 1, both saw count=0
setCount(c => c + 1);
setCount(c => c + 1); // 2, functional updates compose
```

## When to use functional updates
Whenever the new state depends on the previous state.

## Common mistakes
- **Mutating state** — `arr.push(x); setArr(arr)` won't re-render. Use `setArr([...arr, x])`.
- Storing derived data in state — derive from existing state during render
- Duplicating props in state — read from props directly

## Interview angle
- Why is state "snapshot" based?
- How does React batch state updates? (React 18 batches even in async callbacks)

## Related
- [[useState]] · [[useReducer]] · [[Lifting State Up]] · [[Props]]

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
