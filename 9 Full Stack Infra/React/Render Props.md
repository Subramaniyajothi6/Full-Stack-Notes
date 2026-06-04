---
tags: [react, advanced, pattern]
---

# Render Props

> Pass a function as a prop (or child) to share rendering logic.

## Example
```jsx
<MouseTracker render={({ x, y }) => <h1>{x},{y}</h1>} />
```

## Modern alternative
[[Custom Hooks]] solve the same problem more elegantly:
```js
const { x, y } = useMouse();
```

## Related
- [[Higher Order Components]] · [[Custom Hooks]]

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
