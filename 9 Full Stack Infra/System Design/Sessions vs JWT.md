---
tags: [system-design, intermediate, concept]
---

# Sessions vs JWT

| Aspect            | Sessions (cookie)              | JWT                          |
| ----------------- | ------------------------------ | ---------------------------- |
| State             | server (Redis/DB)              | self-contained               |
| Revocation        | easy (delete server side)      | hard — needs deny-list       |
| Scaling           | needs shared store             | stateless                    |
| Size              | small id                       | larger payload               |
| Storage on client | httpOnly cookie                | cookie or localStorage(risky)|

## Practical recipe
- Web app: short-lived JWT in **httpOnly cookie** + refresh token. Server-side rotation.
- Mobile/native: bearer JWT in secure storage.

## Related
- [[Authentication vs Authorization]] · [[JWT Authentication|JWT Authentication]] · [[Cookies and Sessions|Cookies and Sessions]]

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
