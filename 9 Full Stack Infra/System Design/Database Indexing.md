---
tags: [system-design, intermediate, performance]
---

# Database Indexing

> Data structure (usually B-tree) that maps a key to row pointer.

## Wins
- O(log n) lookups for indexed fields
- Range scans

## Costs
- Slows writes (every index updated)
- Disk + memory

## Tips
- Index columns used in WHERE, ORDER BY, JOIN
- Compound order: equality → sort → range
- Use covering indexes when possible
- Monitor unused indexes, drop them

## Related
- [[Indexes|Indexes (MongoDB)]] · [[Compound Indexes|Compound Indexes]]

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
