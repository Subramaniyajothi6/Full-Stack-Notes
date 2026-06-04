---
tags: [express, beginner, syntax]
---

# Static Files

```js
app.use(express.static('public'));        // serve /public/* at /*
app.use('/assets', express.static('dist'));
```

## Headers
- Set `Cache-Control` for far-future hashed assets
- Use a CDN for production

## Common mistakes
- Serving `node_modules`
- No cache headers → poor LCP
- Path traversal — express.static is safe but custom handlers often aren't

## Related
- [[CDN|CDN]]

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
