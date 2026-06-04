---
tags: [react, beginner, concept]
---

# Functional vs Class Components

> Functional + hooks is the modern default. Classes still work but rarely used in new code.

## Comparison
| Aspect          | Functional + Hooks       | Class                          |
| --------------- | ------------------------ | ------------------------------ |
| Syntax          | function                 | `class extends Component`      |
| State           | `useState`, `useReducer` | `this.state`, `setState`       |
| Side effects    | `useEffect`              | `componentDidMount`, etc.      |
| `this`          | not used                 | required, easy to mis-bind     |
| Code reuse      | Custom hooks             | HOCs, render props             |

## Why functional won
- No `this` confusion (see [[Call Apply Bind]])
- Easier to extract logic into [[Custom Hooks]]
- Less boilerplate

## Common mistakes
- Mixing — calling hooks inside a class (illegal)
- Using class lifecycle when an `useEffect` would do

## Related
- [[Components]] · [[useState]] · [[useEffect]] · [[React Lifecycle]] · [[Class Lifecycle Methods]]

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
