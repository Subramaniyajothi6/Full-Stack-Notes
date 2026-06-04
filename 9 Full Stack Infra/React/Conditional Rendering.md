---
tags: [react, beginner, pattern]
---

# Conditional Rendering

> Show different UI based on state/props.

## Patterns
```jsx
// ternary
{isLoggedIn ? <Dashboard /> : <Login />}

// short-circuit
{error && <Error msg={error} />}

// early return
if (!data) return <Spinner />;

// switch via lookup
const views = { list: <List/>, edit: <Edit/> };
return views[mode];
```

## Common mistakes
- `{count && <X />}` — when `count = 0`, renders "0" instead of nothing. Use `count > 0 && <X />`.
- Returning `false` from JSX — fine, renders nothing
- Nested ternaries — refactor to early returns

## Related
- [[JSX]] · [[Lists and Keys]]

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
