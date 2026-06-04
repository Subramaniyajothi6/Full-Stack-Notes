---
tags: [system-design, beginner, concept]
---

# Authentication vs Authorization

- **Authentication (AuthN)** — who are you?
- **Authorization (AuthZ)** — what can you do?

## Patterns
- AuthN: passwords + MFA, OAuth, magic links, passkeys
- AuthZ: RBAC (roles), ABAC (attributes), policy engines (OPA, Cedar)

## Common mistakes
- Putting permission checks only in UI
- Trusting client-claimed roles
- IDOR — `/orders/123` accessible without ownership check

## Related
- [[Sessions vs JWT]] · [[OAuth Flow]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

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
