---
tags: [react, intermediate, pattern]
---

# Rules of Hooks

> 1. Only call hooks at the top level. 2. Only call hooks from React functions or other hooks.

## Why
React relies on call order to associate hook state with the right slot. Conditionals would scramble the slots.

## Bad
```js
if (cond) useEffect(...);  // ❌
```

## Good
```js
useEffect(() => { if (cond) doThing(); }, [cond]);  // ✅
```

## Tooling
The ESLint plugin `eslint-plugin-react-hooks` catches violations and missing deps.

## Related
- [[Custom Hooks]] · [[useState]] · [[useEffect]]

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
