---
tags: [express, beginner, syntax]
---

# Body Parsing

```js
app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: true, limit: '1mb' }));
```

## Why limits matter
Unbounded body = DoS. Set sensible limits per route.

## Multipart (file uploads)
Use [[File Uploads with Multer|Multer]] — `express.json` does not parse multipart.

## Common mistakes
- Body parser after routes — `req.body` is undefined
- Reading streams twice
- No content-type → silent empty body

## Related
- [[Built-in Middleware]] · [[Validation]] · [[File Uploads with Multer]]

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
