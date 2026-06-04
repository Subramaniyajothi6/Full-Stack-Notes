---
tags: [system-design, intermediate, performance]
---

# CDN

> Content Delivery Network — geographically distributed caches that serve static (and increasingly dynamic) content from near the user.

## Wins
- Lower latency — TLS termination at edge
- Lower origin load
- DDoS mitigation, WAF
- Edge compute

## Cache headers
`Cache-Control: public, max-age=31536000, immutable` for hashed assets.

## Related
- [[Caching]] · [[Static Files|Static Files]]

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
