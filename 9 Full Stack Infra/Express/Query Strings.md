---
tags: [express, beginner, syntax]
---

# Query Strings

## Basics
`/search?q=foo&page=2` → `req.query` is `{ q: 'foo', page: '2' }`.

## Always strings
Coerce: `Number(req.query.page)`. Validate ranges.

## Arrays
`?tag=a&tag=b` → `req.query.tag = ['a','b']` (with `extended` parser).

## Common mistakes
- Skipping coercion → string compares
- Not validating → injection in DB queries
- Loose pagination defaults → huge result sets

## Related
- [[Pagination and Filtering]] · [[Validation]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://expressjs.com/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Web Dev Simplified, Traversy Media

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
