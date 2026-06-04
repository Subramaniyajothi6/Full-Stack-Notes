---
tags: [react, beginner, concept]
---

# What is React

> A JavaScript library for building user interfaces by composing reusable components.

## Why it matters
React encodes the UI as a function of state. Re-render the whole tree mentally; React diffs and patches the DOM efficiently via the [[Virtual DOM]].

## Core ideas
- **Components** — small, reusable units of UI
- **Declarative** — describe *what* to render, not *how* to mutate the DOM
- **Unidirectional data flow** — props flow down, events flow up
- **Composition over inheritance** — see [[Component Composition]]

## Minimal example
```jsx
function Hello({ name }) {
  return <h1>Hello, {name}</h1>;
}
```

## Common mistakes
- Treating React as a framework — it's a library; routing, data fetching, etc. need extra packages
- Mutating state directly instead of using setters (see [[State in React]])

## Interview angle
- Why React over vanilla JS? Diffing, components, ecosystem
- Library vs framework distinction

## Related
- [[JSX]] · [[Virtual DOM]] · [[Components]] · [[React MOC]]

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
