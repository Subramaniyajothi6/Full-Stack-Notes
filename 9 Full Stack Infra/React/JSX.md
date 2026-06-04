---
tags: [react, beginner, syntax]
---

# JSX

> Syntactic sugar over `React.createElement` calls. Looks like HTML, compiles to JS.

## Why it matters
JSX makes component trees readable. Babel transpiles it to function calls.

## Example
```jsx
const el = <h1 className="title">Hi</h1>;
// compiles to
const el = React.createElement('h1', { className: 'title' }, 'Hi');
```

## Rules
- Single root element (or use `<>...</>` fragment)
- `className` not `class`, `htmlFor` not `for`
- Curly braces `{ }` to embed JS expressions
- Self-close tags: `<img />`, `<br />`

## Common mistakes
- Forgetting to capitalize component names — lowercase = HTML element
- Returning multiple elements without a fragment
- Using `if/else` directly inside JSX (use ternary or `&&`)

## Edge cases
- `false`, `null`, `undefined` render nothing; `0` renders as text "0"
- Boolean attributes: `<input disabled />` ≡ `disabled={true}`

## Interview angle
- What does JSX compile to? `React.createElement(type, props, ...children)`
- Why must components start with a capital letter?

## Related
- [[What is React]] · [[Components]] · [[Conditional Rendering]]

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
