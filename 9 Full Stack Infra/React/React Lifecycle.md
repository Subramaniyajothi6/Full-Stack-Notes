---
tags: [react, intermediate, concept]
---

# React Lifecycle

> Phases a component goes through: mount → update → unmount.

## Functional component mapping
| Phase   | Class                                | Functional                       |
| ------- | ------------------------------------ | -------------------------------- |
| Mount   | `componentDidMount`                  | `useEffect(fn, [])`              |
| Update  | `componentDidUpdate`                 | `useEffect(fn, [deps])`          |
| Unmount | `componentWillUnmount`               | cleanup returned from `useEffect`|

## Example
```js
useEffect(() => {
  console.log('mount or deps changed');
  return () => console.log('cleanup');
}, [deps]);
```

## Common mistakes
- Doing setup in render instead of effect
- Missing cleanup → memory leaks (timers, subscriptions)

## Related
- [[Class Lifecycle Methods]] · [[useEffect]] · [[Fiber Architecture]]

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
