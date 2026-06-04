---
tags: [express, beginner, tooling]
---

# Logging with Morgan

```js
import morgan from 'morgan';
app.use(morgan('combined'));   // production-style
// or 'tiny', 'dev', 'short'
```

## Stream into structured logger
```js
app.use(morgan('combined', {
  stream: { write: (msg) => logger.info(msg.trim()) }
}));
```

## Related
- [[Logging in Node|Logging in Node]]

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
