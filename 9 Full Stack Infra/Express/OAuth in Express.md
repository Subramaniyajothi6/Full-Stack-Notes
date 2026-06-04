---
tags: [express, advanced, auth]
---

# OAuth in Express

> Standard for delegated auth — users log in via a third party.

## Flow (auth code)
1. Browser → `/auth/google` → redirect to Google
2. Google → callback URL with code
3. Server exchanges code for access + ID token
4. Server creates session / JWT, redirects to app

## With Passport
```js
passport.use(new GoogleStrategy({
  clientID, clientSecret, callbackURL: '/auth/google/callback'
}, (accessToken, refreshToken, profile, done) => {
  // upsert user, return done(null, user)
}));

app.get('/auth/google', passport.authenticate('google', { scope: ['profile', 'email'] }));
app.get('/auth/google/callback', passport.authenticate('google', { successRedirect: '/', failureRedirect: '/login' }));
```

## Common mistakes
- Hardcoding callback URLs
- Trusting profile email without verification flag
- Skipping state/PKCE → CSRF risk

## Related
- [[Passport]] · [[OAuth Flow|OAuth Flow]]

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
