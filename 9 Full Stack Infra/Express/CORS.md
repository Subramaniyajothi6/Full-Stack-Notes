---
tags: [express, intermediate, security]
---

# CORS

> Cross-Origin Resource Sharing. Browsers block cross-origin requests by default.

## Setup
```js
import cors from 'cors';
app.use(cors({
  origin: ['https://app.com', 'https://admin.app.com'],
  credentials: true,            // allow cookies
  methods: ['GET','POST','PUT','PATCH','DELETE'],
  allowedHeaders: ['Content-Type','Authorization']
}));
```

## Preflight
Browser sends `OPTIONS` first for non-simple requests.

## Common mistakes
- `origin: '*'` with credentials — invalid combo, browser rejects
- Forgetting OPTIONS handler on custom routers
- CORS errors that are actually network errors

## Related
- [[Helmet and Security]]

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
