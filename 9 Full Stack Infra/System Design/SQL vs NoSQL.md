---
tags: [system-design, intermediate, concept]
---

# SQL vs NoSQL

| Dimension     | SQL (Postgres, MySQL)     | NoSQL (Mongo, DynamoDB, Cassandra)   |
| ------------- | ------------------------- | ------------------------------------- |
| Schema        | strict, evolves via migration | flexible per document             |
| Joins         | first-class               | limited / discouraged                  |
| Transactions  | ACID across rows          | usually single-doc; multi-doc possible |
| Scale         | vertical mostly; sharding harder | horizontal native                |
| Best for      | relational, complex queries | hierarchical, fast iterating        |

## Picking
Often you want both — relational for core entities, document for flexible content.

## Related
- [[CAP Theorem]] · [[Schema Design Patterns|Schema Design Patterns]]

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
