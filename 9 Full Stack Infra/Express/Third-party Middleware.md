---
tags: [express, intermediate, syntax]
---

# Third-party Middleware

## Common stack
- `cors` — see [[CORS]]
- `helmet` — security headers, see [[Helmet and Security]]
- `morgan` — request logs, see [[Logging with Morgan]]
- `compression` — gzip
- `cookie-parser` — populate `req.cookies`
- `express-session` — sessions, see [[Cookies and Sessions]]
- `multer` — file uploads, see [[File Uploads with Multer]]
- `express-rate-limit` — see [[Rate Limiting]]
- `passport` — auth strategies, see [[Passport]]

## Installation pattern
```js
app.use(helmet());
app.use(cors({ origin: 'https://app.com', credentials: true }));
app.use(express.json({ limit: '1mb' }));
app.use(morgan('combined'));
```

## Related
- [[Middleware]] · [[Built-in Middleware]]

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
