---
tags: [system-design, advanced, concept]
---

# Consistency Models

- **Strong / Linearizable** — reads return the latest write
- **Sequential** — operations seen in same order by all nodes
- **Causal** — preserves cause/effect order
- **Eventual** — reads converge over time

## In practice
- DynamoDB: eventual by default, strong on demand
- MongoDB: causal sessions; readConcern majority for stronger
- Cassandra: tunable per query

## Related
- [[CAP Theorem]] · [[Replication in System Design]]

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
