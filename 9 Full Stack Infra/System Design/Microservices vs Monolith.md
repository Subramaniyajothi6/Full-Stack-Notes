---
tags: [system-design, intermediate, architecture]
---

# Microservices vs Monolith

## Monolith pros
- Simple deploy + debug
- Fast iteration when small team
- One DB, easy transactions

## Microservices pros
- Independent deploys per team
- Tech freedom per service
- Fault isolation

## Microservices cons
- Distributed system tax — networking, eventual consistency, observability
- Schema changes across services
- Hard to start there

## Recommendation
Start monolith. Split when team or domain forces it.

## Related
- [[API Gateway]] · [[Message Queues]]

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
