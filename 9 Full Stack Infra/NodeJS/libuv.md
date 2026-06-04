---
tags: [nodejs, advanced, concept]
---

# libuv

> Cross-platform C library that provides Node's event loop, async I/O, and thread pool.

## Provides
- Event loop
- Async TCP/UDP, DNS, file I/O
- Default 4-worker **thread pool** (configurable via `UV_THREADPOOL_SIZE`)
- Timers and signals

## Thread pool offloads
- File system (`fs`) operations
- DNS lookups (`dns.lookup`)
- Crypto (`pbkdf2`, `randomBytes`)
- User C++ addons that opt in

## Common mistakes
- Assuming all I/O uses thread pool — network sockets are kernel async, no pool
- Saturating pool with crypto/zlib — bump pool size or move to workers

## Related
- [[Event Loop in Node]] · [[Cluster and Worker Threads]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://nodejs.org/en/docs — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, TechWorld with Nana, Traversy Media

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
