---
tags: [express, intermediate, auth]
---

# JWT Authentication

> Stateless tokens. Server signs payload, client sends back on each request.

## Issue
```js
import jwt from 'jsonwebtoken';
const token = jwt.sign({ sub: user.id }, process.env.JWT_SECRET, { expiresIn: '15m' });
```

## Verify middleware
```js
function auth(req, res, next) {
  const t = req.headers.authorization?.split(' ')[1];
  if (!t) return res.sendStatus(401);
  try { req.user = jwt.verify(t, process.env.JWT_SECRET); next(); }
  catch { res.sendStatus(401); }
}
```

## Refresh tokens
- Short access token (15m)
- Long-lived refresh token in **httpOnly cookie**
- Refresh endpoint rotates and revokes

## Common mistakes
- Storing JWT in localStorage → XSS exfiltration
- No revocation strategy
- Long-lived access tokens
- Putting sensitive data in JWT (it's base64, not encrypted)

## Related
- [[Cookies and Sessions]] · [[Sessions vs JWT|Sessions vs JWT]]

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
