---
tags: [express, intermediate, pattern]
---

# Error Handling Middleware

> Special signature: 4 args `(err, req, res, next)`. Express recognizes this and routes errors here.

## Pattern
```js
// custom error class
class HttpError extends Error {
  constructor(status, msg) { super(msg); this.status = status; }
}

// throw / next from any handler
app.get('/x', (req, res, next) => next(new HttpError(404, 'not found')));

// last middleware
app.use((err, req, res, next) => {
  const status = err.status ?? 500;
  res.status(status).json({ error: err.message });
});
```

## Async handlers
Wrap to forward rejections:
```js
const asyncH = fn => (req, res, next) => Promise.resolve(fn(req, res, next)).catch(next);
app.get('/x', asyncH(async (req, res) => { ... }));
```
Or use `express-async-errors`.

## Common mistakes
- Forgetting 4-arg signature
- Leaking stack traces in production
- Sending different shapes for different errors

## Related
- [[Middleware]] · [[Error Handling in Node|Error Handling in Node]]

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
