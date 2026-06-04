---
tags: [express, intermediate, design]
---

# API Versioning

## Strategies
- **URL** — `/v1/users` (most common, easiest)
- **Header** — `Accept: application/vnd.api.v2+json`
- **Query** — `?v=2` (avoid)

## When to bump
Breaking changes only. Additive changes (new optional fields) don't need a new version.

## Deprecation
- Announce in advance
- Add `Deprecation` and `Sunset` headers
- Maintain old version until traffic drains

## Related
- [[REST API Design]]

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
