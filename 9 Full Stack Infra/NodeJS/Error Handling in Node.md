---
tags: [nodejs, intermediate, pattern]
---

# Error Handling in Node

> Many failure modes: thrown errors, rejected promises, emitted `error` events.

## Surfaces
```js
process.on('uncaughtException', err => { log(err); process.exit(1); });
process.on('unhandledRejection', err => { log(err); process.exit(1); });

emitter.on('error', err => { /* handle */ });
```

## Async/await
```js
try {
  await db.query(...);
} catch (e) {
  next(e);   // pass to Express error middleware
}
```

## Operational vs programmer errors
- Operational — expected (network down, validation) → handle gracefully
- Programmer — bugs (TypeError) → crash + restart with PM2/systemd

## Common mistakes
- Catching and swallowing errors
- Not crashing on programmer errors — leaves process in bad state
- Logging without context (no request id)

## Related
- [[Error Handling Middleware|Error Handling Middleware]] · [[Logging in Node]]

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
