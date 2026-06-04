---
tags: [react, intermediate, pattern]
---

# Forms in React

> Two approaches: controlled (React owns value) vs uncontrolled (DOM owns).

## Controlled
```jsx
const [name, setName] = useState('');
<input value={name} onChange={e => setName(e.target.value)} />
```

## Uncontrolled
```jsx
const ref = useRef();
<input defaultValue="" ref={ref} />
// read via ref.current.value
```

## Form libraries
- **React Hook Form** — uncontrolled by default, fast
- **Formik** — controlled, simpler API
- **Zod / Yup** — schema validation

## Common mistakes
- Switching between controlled/uncontrolled (warning: "input is changing from uncontrolled to controlled")
- Forgetting `e.preventDefault()` on submit
- Validating only on submit when realtime would help UX

## Related
- [[Controlled vs Uncontrolled Components]] · [[State in React]]

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
