---
tags: [mongodb, advanced, scale]
---

# Replication

> Replica set: Primary + Secondaries (+ Arbiter). Provides HA.

## How it works
- Writes go to primary
- Secondaries replicate via oplog
- Election picks new primary on failure

## Read preferences
- `primary` (default)
- `primaryPreferred`
- `secondary` — eventual consistency
- `nearest`

## Related
- [[Sharding]] · [[Replication in System Design|Replication (system design)]]

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
