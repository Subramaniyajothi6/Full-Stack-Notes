---
tags: [system-design, advanced, scale]
---

# Sharding and Partitioning

> Split a dataset across DBs/nodes.

## Strategies
- **Range** — by key range (e.g., A–M)
- **Hash** — hash(key) % n
- **Geographic** — by region
- **Directory-based** — explicit mapping

## Pitfalls
- Hot shards
- Cross-shard joins are expensive
- Resharding is hard — pick keys carefully

## Related
- [[Sharding|Sharding (MongoDB)]] · [[Replication in System Design]]

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
