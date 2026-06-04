---
tags: [react, beginner, pattern]
---

# Lists and Keys

> Use `.map()` to render arrays. Each item needs a stable, unique `key`.

## Example
```jsx
{items.map(item => <Row key={item.id} data={item} />)}
```

## Why keys matter
React uses keys to match items across renders. Wrong keys = wrong DOM reuse = bugs (input loses focus, animations restart).

## Common mistakes
- **Index as key** when items reorder, insert, or delete from the middle
- Math.random() — changes every render, defeats the purpose
- Duplicate keys — undefined behavior

## Edge cases
- Stable index is fine for static lists that never reorder

## Interview angle
- Why does index-as-key break reorderable lists?
- Are keys passed as props? (No — special prop, only React reads them)

## Related
- [[Reconciliation and Diffing]] · [[Conditional Rendering]]

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
