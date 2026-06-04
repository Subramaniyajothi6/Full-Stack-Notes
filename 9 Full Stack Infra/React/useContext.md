---
tags: [react, intermediate, hook]
---

# useContext

> Read a context value provided higher in the tree, avoiding prop drilling.

## Example
```jsx
const ThemeContext = createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Page />
    </ThemeContext.Provider>
  );
}

function Page() {
  const theme = useContext(ThemeContext);
  return <div className={theme} />;
}
```

## Common mistakes
- Putting frequently-changing values in context — every consumer re-renders. Split contexts by update frequency.
- Forgetting a Provider — falls back to default value
- Treating context as a state manager for everything (use [[Redux Toolkit]] / [[Zustand and Alternatives]] for complex state)

## Edge cases
- Memoize the value: `<Provider value={useMemo(() => ({a, b}), [a, b])}>`
- Multiple providers compose — order matters only for shadowing

## Interview angle
- Context vs Redux vs prop drilling
- Why does every consumer re-render on value change?

## Related
- [[Context API]] · [[useMemo]] · [[Redux Basics]]

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
