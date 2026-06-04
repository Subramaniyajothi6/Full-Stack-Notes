---
tags: [express, intermediate, design]
---

# Pagination and Filtering

## Offset/limit
`/users?limit=20&offset=40` — simple but slow for deep pages.

## Cursor
`/users?limit=20&cursor=ENCODED` — stable when data changes, scales.

## Filters
`/users?role=admin&status=active&q=ali`

## Sorting
`/users?sort=-createdAt,name`

## Always
- Cap `limit` (e.g. 100)
- Validate filter fields against allowlist
- Return total count or next cursor consistently

## Related
- [[REST API Design]] · [[Indexes|Indexes]]

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
