---
tags: [react, intermediate, concept]
---

# Controlled vs Uncontrolled Components

> Controlled: state in React. Uncontrolled: state in DOM, accessed via ref.

## Controlled — single source of truth
```jsx
<input value={x} onChange={e => setX(e.target.value)} />
```

## Uncontrolled — DOM owns it
```jsx
<input defaultValue="hello" ref={ref} />
```

## When to use which
- Controlled: validation while typing, conditional fields, instant feedback
- Uncontrolled: simple forms, file inputs (always uncontrolled — `<input type="file" />`)

## Common mistakes
- Mixing `value` and `defaultValue` on the same element
- Setting `value` without `onChange` → input is read-only

## Related
- [[Forms in React]] · [[useRef]]

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
