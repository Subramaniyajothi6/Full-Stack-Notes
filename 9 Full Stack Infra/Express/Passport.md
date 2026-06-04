---
tags: [express, intermediate, auth]
---

# Passport

> Pluggable auth via "strategies": local, JWT, Google OAuth, GitHub, etc.

## Local strategy
```js
import passport from 'passport';
import { Strategy as Local } from 'passport-local';

passport.use(new Local(async (username, password, done) => {
  const user = await User.findOne({ username });
  if (!user || !(await user.verifyPassword(password))) return done(null, false);
  return done(null, user);
}));

app.post('/login', passport.authenticate('local'), (req, res) => res.json({ ok: true }));
```

## OAuth
Each provider has its own strategy package: `passport-google-oauth20`, `passport-github2`, etc.

## Related
- [[JWT Authentication]] · [[OAuth in Express]] · [[Cookies and Sessions]]

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
