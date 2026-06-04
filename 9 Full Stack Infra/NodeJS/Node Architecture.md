---
tags: [nodejs, intermediate, concept]
---

# Node Architecture

> Single-threaded JS + multi-threaded I/O via libuv's thread pool.

## Layers
1. **Your JS** — runs on main thread
2. **Node bindings** — C++ glue
3. **[[V8 Engine]]** — executes JS
4. **[[libuv]]** — event loop, thread pool, async I/O

## Key consequence
JS runs on **one thread**. Long synchronous code blocks all requests. Offload via:
- async I/O (already non-blocking)
- [[Cluster and Worker Threads]] for CPU work
- [[Child Process]] for separate processes

## Related
- [[Event Loop in Node]] · [[V8 Engine]] · [[libuv]]

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
