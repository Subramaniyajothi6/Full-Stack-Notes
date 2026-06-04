---
tags: [system-design, intermediate, scale]
---

# Replication (system design)

> Copy data to multiple nodes for HA + read scaling.

## Modes
- **Sync** — primary waits for replicas (strong durability, higher latency)
- **Async** — primary commits then propagates (low latency, possible loss on failover)
- **Multi-leader** — accept writes anywhere, conflict resolution required

## Read replicas
Route reads to followers; writes to leader. Beware replication lag.

## Related
- [[Replication|Replication (Mongo)]] · [[CAP Theorem]]

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
