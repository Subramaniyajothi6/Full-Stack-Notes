---
tags: [react, beginner, concept]
---

# Props

> Read-only inputs to a component, passed from parent.

## Example
```jsx
function Avatar({ url, size = 40 }) {
  return <img src={url} width={size} />;
}

<Avatar url="/me.png" size={64} />
```

## Rules
- Immutable — never assign to `props.x`
- Children are passed via the special `children` prop
- Default values via destructuring or `defaultProps` (legacy)

## Patterns
- **Spread** — `<Child {...props} />`
- **Render props** — pass a function as a child or prop. See [[Render Props]].

## Common mistakes
- Mutating props
- Passing entire objects when you only need one field — causes unnecessary re-renders
- Forgetting that arrow functions in props recreate every render — use [[useCallback]]

## Interview angle
- Why are props immutable?
- Props vs state — props are external, state is internal

## Related
- [[State in React]] · [[Component Composition]] · [[useCallback]]

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
