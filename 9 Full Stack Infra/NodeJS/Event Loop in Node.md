---
tags: [nodejs, intermediate, concept]
---

# Event Loop in Node

> Multi-phase loop that processes callbacks. Different from the browser loop.

## Phases (in order)
1. **Timers** — `setTimeout`, `setInterval` callbacks
2. **Pending callbacks** — some system errors
3. **Idle, prepare** — internal
4. **Poll** — retrieve new I/O events; execute their callbacks
5. **Check** — `setImmediate` callbacks
6. **Close** — `socket.on('close')`

Between every phase: process **microtasks** (resolved promises, `queueMicrotask`) and `process.nextTick` queue.

## nextTick vs setImmediate
- `process.nextTick` runs **before** the next phase (highest priority — can starve loop)
- `setImmediate` runs in **check** phase (after I/O)

## Common mistakes
- Recursive `process.nextTick` → starves event loop
- Mixing CPU-heavy work into request handlers

## Interview angle
- Order of: `setTimeout(fn, 0)`, `setImmediate(fn)`, `Promise.resolve().then(fn)`, `process.nextTick(fn)` — try it!

## Related
- [[Async Patterns in Node]] · [[Event Loop|Event Loop (browser)]]

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
