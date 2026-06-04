---
tags: [react, intermediate, pattern]
---

# Custom Hooks

> A function that starts with `use` and may call other hooks. Extracts reusable stateful logic.

## Example — useLocalStorage
```js
function useLocalStorage(key, initial) {
  const [v, setV] = useState(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initial;
  });
  useEffect(() => localStorage.setItem(key, JSON.stringify(v)), [key, v]);
  return [v, setV];
}
```

## Rules
- Name must start with `use`
- Same call order every render — see [[Rules of Hooks]]
- Returns whatever shape is convenient: tuple, object, value

## Common mistakes
- Skipping the `use` prefix — lint rule won't fire
- Hook calls inside conditionals
- Sharing state between components by importing the hook — each call creates fresh state

## Related
- [[useState]] · [[useEffect]] · [[Rules of Hooks]]

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
