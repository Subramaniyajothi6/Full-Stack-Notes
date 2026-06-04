---
tags: [express, beginner, concept]
---

# Middleware

> Functions with `(req, res, next)` that run sequentially. Foundation of Express.

## Anatomy
```js
function logger(req, res, next) {
  console.log(req.method, req.url);
  next();        // hand off to next middleware
}
app.use(logger);
```

## Three behaviors
1. Pass through — `next()`
2. End response — `res.send/.json/.end`
3. Error — `next(err)` (skips to error handlers)

## Order matters
- Body parser before routes that need `req.body`
- Auth before protected routes
- Error handler **last**

## Common mistakes
- Forgetting `next()` → request hangs
- Mutating `req` with surprising shapes
- Multiple responses (call `next` after `res.send`)

## Related
- [[Built-in Middleware]] · [[Third-party Middleware]] · [[Error Handling Middleware]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://expressjs.com/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Web Dev Simplified, Traversy Media

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
