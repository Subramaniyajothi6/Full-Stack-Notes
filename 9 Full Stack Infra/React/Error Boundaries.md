---
tags: [react, intermediate, pattern]
---

# Error Boundaries

> Catch render-time errors in a subtree and show a fallback UI.

## Example (class only — no hook equivalent yet)
```jsx
class Boundary extends React.Component {
  state = { error: null };
  static getDerivedStateFromError(error) { return { error }; }
  componentDidCatch(error, info) { logError(error, info); }
  render() {
    return this.state.error ? <Fallback /> : this.props.children;
  }
}
```

## What they don't catch
- Event handlers (use try/catch)
- Async code
- Server-side rendering errors
- Errors in the boundary itself

## Common mistakes
- One global boundary — losing all of UI on a tiny error
- Forgetting to log errors

## Related
- [[React Lifecycle]] · [[Components]]

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
