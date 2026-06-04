---
tags: [system-design, intermediate, security]
---

# Rate Limiting (system design)

## Algorithms
- **Fixed window** — simple, but boundary spikes
- **Sliding window** — smoother
- **Token bucket** — bursts allowed up to bucket size, refills at rate
- **Leaky bucket** — fixed outflow rate

## Where to enforce
- Edge (CDN/API gateway)
- App layer (per user/IP/key)
- Per resource (login, OTP)

## Distributed counters
Redis with atomic `INCR` + TTL, or Lua scripts for sliding windows.

## Related
- [[Rate Limiting|Rate Limiting (Express)]]

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
