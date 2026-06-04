---
tags: [system-design, advanced, architecture]
---

# Message Queues

> Decouple producers from consumers via durable queues.

## Use cases
- Async tasks (email, image processing)
- Smoothing traffic spikes
- Cross-service events

## Tools
- RabbitMQ — flexible routing
- Redis Streams — lightweight
- Kafka — high-throughput, durable, log-based
- SQS — managed

## Patterns
- Work queue (one consumer per message)
- Pub/Sub fanout
- Retry with backoff + DLQ

## Related
- [[Pub Sub]] · [[Event-Driven Architecture]]

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
