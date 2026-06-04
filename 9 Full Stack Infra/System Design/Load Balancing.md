---
tags: [system-design, intermediate, scale]
---

# Load Balancing

> Distribute traffic across instances.

## Layers
- L4 — TCP/UDP (fast, no app awareness)
- L7 — HTTP-aware (path routing, headers, cookies)

## Algorithms
- Round-robin
- Least-connections
- Weighted
- Consistent hashing (sticky for sessions/sharding)

## Health checks
LB removes unhealthy instances based on probes (HTTP 200, custom path).

## Related
- [[Horizontal vs Vertical Scaling]] · [[API Gateway]]

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
