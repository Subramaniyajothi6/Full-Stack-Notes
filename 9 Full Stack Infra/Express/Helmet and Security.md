---
tags: [express, intermediate, security]
---

# Helmet and Security

> Set security-related HTTP headers.

## Setup
```js
import helmet from 'helmet';
app.use(helmet());
```

## What it sets
- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy`
- `Cross-Origin-Resource-Policy`

## Other practices
- Disable `x-powered-by` (helmet does this)
- HTTPS only (TLS at proxy)
- Validate + sanitize all input
- Use parameterized queries (Mongoose handles this for you)
- Hash passwords with **bcrypt** or **argon2**

## Related
- [[Rate Limiting]] · [[HTTP and HTTPS|HTTP and HTTPS]]

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
