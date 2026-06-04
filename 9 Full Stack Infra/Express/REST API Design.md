---
tags: [express, intermediate, design]
---

# REST API Design

## Resource URLs
- `GET    /users`       — list
- `POST   /users`       — create
- `GET    /users/:id`   — read
- `PUT    /users/:id`   — replace
- `PATCH  /users/:id`   — partial update
- `DELETE /users/:id`   — remove
- Nested: `GET /users/:id/posts`

## Status codes
- `200` OK, `201` Created, `204` No Content
- `400` Bad Request, `401` Unauthorized, `403` Forbidden, `404` Not Found, `409` Conflict, `422` Unprocessable
- `429` Too Many Requests
- `500` Server, `502/503/504` upstream

## Rules
- Plural nouns
- Use HTTP verbs, not action names in URL
- Return JSON consistently shaped
- Use proper headers (`Location` on create)
- Document with OpenAPI

## Related
- [[API Versioning]] · [[Pagination and Filtering]] · [[REST vs GraphQL|REST vs GraphQL]]

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
