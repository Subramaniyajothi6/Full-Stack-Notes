---
tags: [system-design, intermediate, concept]
---

# WebSockets

> Persistent, full-duplex TCP channel between client and server.

## When to use
- Chat, presence, multiplayer games, live dashboards
- Server-pushed updates beyond what SSE can handle

## Libraries
- **ws** — minimal Node WebSocket
- **Socket.IO** — adds rooms, ack, fallback

## Scaling
- Sticky sessions or shared adapter (Redis pub/sub) when running multiple instances
- Load balancer must support WebSocket upgrade

## Related
- [[Server-Sent Events]] · [[Pub Sub]] · [[6 Real-time Chat|Real-time Chat]]

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
