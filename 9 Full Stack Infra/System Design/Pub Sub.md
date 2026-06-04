---
tags: [system-design, advanced, architecture]
---

# Pub Sub

> Publishers emit events; subscribers receive copies.

## Tools
- Redis Pub/Sub — simple, no durability
- Kafka, NATS — durable, replayable
- Cloud — Google Pub/Sub, AWS SNS

## Vs queue
- Queue: each message goes to one consumer
- Pub/Sub: each subscriber gets every message

## Related
- [[Message Queues]] · [[WebSockets]]

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
