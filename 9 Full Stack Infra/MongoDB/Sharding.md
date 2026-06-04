---
tags: [mongodb, advanced, scale]
---

# Sharding

> Horizontal partitioning — distribute data across shards.

## Pieces
- **Shard** — a replica set
- **Mongos** — query router
- **Config servers** — cluster metadata

## Shard key
Choose carefully — drives all read/write distribution.
- High cardinality
- Even write distribution
- Aligns with common queries

## Bad shard keys
- `_id` (ObjectId is monotonic → write hotspots)
- Low-cardinality fields ("country" with 5 values)

## Related
- [[Replication]] · [[Sharding and Partitioning|Sharding (system design)]]

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
- https://www.mongodb.com/docs/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, MongoDB official

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
