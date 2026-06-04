---
tags: [mongodb, advanced, performance]
---

# Compound Indexes

> Index over multiple fields. Order matters.

## Rule of thumb (ESR)
**E**quality fields first, then **S**ort, then **R**ange.

## Example
Query: `{ status: 'open', priority: { $gte: 3 } }, sort: { createdAt: -1 }`
Index: `{ status: 1, createdAt: -1, priority: 1 }`

## Prefix rule
A compound index `{ a, b, c }` can serve queries on `{ a }` or `{ a, b }` but not just `{ b }`.

## Related
- [[Indexes]] · [[Explain and Query Plans]]

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
