---
tags: [react, beginner, concept]
---

# Components

> Reusable, isolated pieces of UI. Functions (or classes) that return JSX.

## Two kinds
- **Functional** — plain functions, use [[useState|hooks]] for state. Modern default.
- **Class** — extend `React.Component`, use lifecycle methods. Legacy.

## Example
```jsx
function Greeting({ name }) {
  return <p>Hello, {name}</p>;
}

export default Greeting;
```

## Naming rule
PascalCase. Lowercase = treated as HTML tag.

## Common mistakes
- Defining a component inside another component's render — recreated every render, breaks state
- Forgetting to `export` it
- Mutating [[Props]] (props are read-only)

## Interview angle
- Functional vs class — see [[Functional vs Class Components]]
- What makes a component "pure"?

## Related
- [[Props]] · [[State in React]] · [[Component Composition]] · [[Functional vs Class Components]]

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
