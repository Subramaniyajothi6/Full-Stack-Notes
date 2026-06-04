---
tags: [react, advanced, concept]
---

# Reconciliation and Diffing

> The algorithm React uses to figure out which DOM updates are needed.

## Heuristics
1. **Different element types** → tear down whole subtree
2. **Same type** → keep DOM node, update changed props
3. **Lists** → use `key` to match elements across renders

## Example — why keys matter
```jsx
// Without keys, React may misidentify items on reorder
items.map(i => <Row data={i} />)

// With keys, React can match by identity
items.map(i => <Row key={i.id} data={i} />)
```

## Common mistakes
- Using array index as key when items reorder — see [[Lists and Keys]]
- Expecting React to deeply compare props (it uses `Object.is` reference checks)

## Interview angle
- O(n) heuristic vs theoretical O(n³) tree diff
- Why keys must be stable, unique, and predictable

## Related
- [[Virtual DOM]] · [[Fiber Architecture]] · [[Lists and Keys]]

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
