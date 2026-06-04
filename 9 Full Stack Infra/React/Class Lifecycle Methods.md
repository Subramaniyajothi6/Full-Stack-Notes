---
tags: [react, advanced, concept]
---

# Class Lifecycle Methods

> Legacy — still in some codebases.

## Order
1. `constructor`
2. `static getDerivedStateFromProps`
3. `render`
4. `componentDidMount`

On update:
1. `getDerivedStateFromProps`
2. `shouldComponentUpdate`
3. `render`
4. `getSnapshotBeforeUpdate`
5. `componentDidUpdate`

On unmount: `componentWillUnmount`.

## Deprecated (UNSAFE_)
`componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` — replaced.

## Functional equivalents
See [[React Lifecycle]] table.

## Related
- [[Functional vs Class Components]] · [[useEffect]]

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
