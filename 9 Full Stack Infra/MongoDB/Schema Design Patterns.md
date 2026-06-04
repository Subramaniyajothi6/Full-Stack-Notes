---
tags: [mongodb, advanced, design]
---

# Schema Design Patterns

> Design driven by **how the app reads** the data.

## Common patterns
- **Embedded** — sub-doc lives inside parent (1:few)
- **Referenced** — `ObjectId` points to another doc (1:many, M:N)
- **Bucket** — group time-series points by hour/day
- **Computed** — pre-compute aggregates and update on writes
- **Outlier** — handle "the one user with 1M orders" specially
- **Polymorphic** — multiple shapes in one collection (`type` field)

## Anti-patterns
- Massive arrays growing unbounded
- "Just like SQL" full normalization
- 1 collection per user

## Related
- [[Embedded vs Referenced]] · [[Denormalization Tradeoffs]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Common Mistakes
- TODO: pitfalls and edge cases

## Best Learning Resources

### Official Documentation
- https://www.mongodb.com/docs/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, MongoDB official

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
