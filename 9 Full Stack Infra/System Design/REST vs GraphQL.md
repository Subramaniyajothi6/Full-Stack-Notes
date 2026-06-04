---
tags: [system-design, intermediate, concept]
---

# REST vs GraphQL

| Aspect           | REST                              | GraphQL                                |
| ---------------- | --------------------------------- | -------------------------------------- |
| Endpoint         | many                              | one                                     |
| Shape control    | server                            | client                                  |
| Over/under fetch | common                            | mitigated                               |
| Caching          | HTTP cache works                  | needs custom cache                      |
| Tooling          | mature                            | rich (codegen, devtools)                 |
| Versioning       | URL/header                        | schema deprecation                      |
| Real-time        | SSE/WebSocket                     | subscriptions                           |

## Choose REST
Simple CRUD, public APIs, heavy CDN caching.

## Choose GraphQL
Many clients with different needs, deep nested fetches, fast iteration.

## Related
- [[REST API Design|REST API Design]] · [[Caching]]

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
- https://aws.amazon.com/architecture/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. ByteByteGo, Hussein Nasser

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
