---
tags: [mern, auth, intermediate]
---

# Full-Stack Auth Flow

> End-to-end session: signup → token issue → cookie storage → request authentication → refresh → logout.

## The standard recipe (cookie-based JWT with refresh)
```
1. POST /signup       (email + password, server hashes with bcrypt)
2. POST /login        (verify hash → issue access JWT + refresh JWT)
3. Set-Cookie: at=<JWT>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=900
   Set-Cookie: rt=<refresh>; HttpOnly; Secure; SameSite=Strict; Path=/api/auth; Max-Age=604800
4. Every request: server reads `at` cookie, verifies, attaches req.user
5. On 401 from access token expiry: client calls /api/auth/refresh
   → server verifies refresh, ROTATES it, returns new access cookie
6. POST /logout       (clear both cookies, mark refresh revoked in DB)
```

## Why this combination
- **httpOnly cookies** can't be read by JS → XSS-resistant
- **SameSite=Lax** blocks CSRF on cross-site requests
- **Short-lived access (15m)** + long-lived refresh (7d) → balance UX and revocation
- **Refresh rotation + DB record** → revoke compromised tokens

## Server side (Express)
```ts
function signTokens(user) {
  const at = jwt.sign({ sub: user.id }, ACCESS_SECRET, { expiresIn: '15m' });
  const rt = jwt.sign({ sub: user.id, jti: uuid() }, REFRESH_SECRET, { expiresIn: '7d' });
  return { at, rt };
}

app.post('/login', async (req, res) => {
  const u = await User.findOne({ email: req.body.email });
  if (!u || !(await bcrypt.compare(req.body.password, u.passwordHash))) {
    return res.status(401).json({ error: 'invalid credentials' });
  }
  const { at, rt } = signTokens(u);
  await RefreshToken.create({ userId: u.id, jti: jwt.decode(rt).jti });
  res.cookie('at', at, { httpOnly: true, secure: true, sameSite: 'lax', maxAge: 15*60*1000 });
  res.cookie('rt', rt, { httpOnly: true, secure: true, sameSite: 'strict', maxAge: 7*24*60*60*1000, path: '/api/auth' });
  res.json({ user: { id: u.id, email: u.email } });
});

function requireAuth(req, res, next) {
  const at = req.cookies.at;
  if (!at) return res.sendStatus(401);
  try { req.user = jwt.verify(at, ACCESS_SECRET); next(); }
  catch { res.sendStatus(401); }
}
```

## Client side (React)
```tsx
async function api(url, opts = {}) {
  let r = await fetch(url, { credentials: 'include', ...opts });
  if (r.status === 401) {
    const refreshed = await fetch('/api/auth/refresh', { method: 'POST', credentials: 'include' });
    if (refreshed.ok) r = await fetch(url, { credentials: 'include', ...opts });
  }
  return r;
}
```

## Real World Usage
- Internal dashboards
- B2B SaaS
- E-commerce checkout
- Any app where session length > 1 hour

## Common Mistakes
- Storing JWT in `localStorage` → any XSS exfiltrates it
- Same secret for access + refresh → can't independently rotate
- No refresh rotation → stolen refresh = forever access
- `SameSite=None` without need → opens CSRF surface
- Forgetting `credentials: 'include'` on the client fetch
- No revocation list → can't kick a compromised user
- Logging tokens (in pino, morgan formats) → leaks in observability stack

## Prerequisites
- [[JWT Authentication]] · [[Cookies and Sessions]] · [[Sessions vs JWT]] · [[Cross-Domain Cookies]]

## What To Learn Next
- [[Protected Routes End-to-End]] · [[OAuth Flow]] · [[Helmet and Security]]

## Best Learning Resources

### Official Documentation
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [MDN — HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

### Best YouTube Resource
- [Hussein Nasser — JWT pitfalls](https://www.youtube.com/@hnasr)
- [Web Dev Simplified — Refresh tokens](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [Auth.js (NextAuth) tutorials](https://authjs.dev/getting-started/introduction)
- [Lucia Auth docs](https://lucia-auth.com/) — minimal session lib

### Best Advanced Resource
- [The Copenhagen Book — auth patterns](https://thecopenhagenbook.com/) — modern session design
- [Clerk + Auth0 engineering blogs](https://clerk.com/blog) — production patterns

### Best Practice Project
Implement signup → login → refresh → logout in Express + React with real bcrypt, real refresh rotation, and a Redis revocation list. Then attempt to break it: open DevTools, look for tokens in JS, simulate XSS, simulate CSRF.

### Recommended Order to Learn
1. Hashing (bcrypt / argon2)
2. JWT structure + signing
3. Cookie attributes (httpOnly, secure, SameSite, path, domain)
4. Access vs refresh tokens
5. Refresh rotation + revocation
6. CSRF protection (SameSite, double-submit, anti-CSRF tokens)
7. OAuth as add-on

## Interview Questions
**Q. Why httpOnly cookies over localStorage?**
A. JS can't read httpOnly cookies — XSS can't exfiltrate.

**Q. Why short access + long refresh, not one long token?**
A. Short access limits damage if leaked. Refresh rotation lets you revoke without invalidating every active session.

**Q. CSRF with cookies — how do you stop it?**
A. SameSite=Lax/Strict default; add anti-CSRF tokens for sensitive POSTs if you must use SameSite=None.

**Q. What's a "refresh rotation"?**
A. Each refresh use returns a new refresh token; previous is invalidated. Detects token theft (replay = both holders see one rejection).

## Related
- [[JWT Authentication]] · [[Cookies and Sessions]] · [[Sessions vs JWT]] · [[Cross-Domain Cookies]] · [[Protected Routes End-to-End]]
