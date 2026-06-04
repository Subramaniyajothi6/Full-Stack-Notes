---
tags: [mern, integration, intermediate, security]
---

# Cross-Domain Cookies

> Sending cookies between a frontend on `app.example.com` and an API on `api.example.com` (or different domains entirely) — the spot where most "auth works in dev, breaks in prod" bugs live.

## The four levers
- **Cookie attributes** — `Domain`, `Path`, `SameSite`, `Secure`, `HttpOnly`
- **CORS headers** — `Access-Control-Allow-Origin`, `Access-Control-Allow-Credentials`
- **Client `credentials`** — `fetch(url, { credentials: 'include' })`
- **Browser policy** — third-party cookie restrictions, public-suffix list

## Decision tree

### Same site (subdomains under same eTLD+1)
- Client: `https://app.example.com`
- API: `https://api.example.com`
- Cookie: `Domain=.example.com; SameSite=Lax; Secure; HttpOnly`
- CORS: allow `https://app.example.com`, `credentials: true`
- Fetch: `credentials: 'include'`

### Cross site (different eTLD+1)
- Client: `https://app.com`
- API: `https://service.io`
- Cookie: `SameSite=None; Secure; HttpOnly` (must be Secure with None)
- CORS: explicit origin echo (`*` not allowed with credentials), `credentials: true`
- Fetch: `credentials: 'include'`
- Reality: many browsers now block third-party cookies by default → consider proxying API behind your domain instead

### Local dev
- Client: `http://localhost:5173`
- API: `http://localhost:3001`
- These are different origins. Use `SameSite=Lax` + matching CORS, or proxy via Vite dev server (`server.proxy`) to keep one origin.

## Quick reference
| Scenario              | Cookie SameSite | Secure | CORS allow-origin     | credentials |
|-----------------------|-----------------|--------|-----------------------|-------------|
| Same origin           | Lax (default)   | yes    | not needed            | implicit    |
| Same eTLD+1 subdomain | Lax             | yes    | echo origin, allow    | include     |
| Cross site            | None            | yes    | echo origin, allow    | include     |
| Localhost different ports | Lax         | no     | echo `http://localhost:5173` | include |

## Express snippet
```ts
import cors from 'cors';
const allowed = ['https://app.example.com', 'http://localhost:5173'];
app.use(cors({
  origin: (origin, cb) => cb(null, !origin || allowed.includes(origin)),
  credentials: true,
}));
```

## Real World Usage
- Multi-region SaaS where API is on a different domain
- Embedded widgets (cross-origin iframes — also need CSP frame-ancestors)
- Microservices behind separate subdomains
- Dev environments before they're proxied

## Common Mistakes
- `Access-Control-Allow-Origin: *` with `credentials: 'include'` → browser rejects
- Forgetting `Secure` when using `SameSite=None` → cookie ignored
- Setting `Domain=example.com` (leading-dot vs no-dot) inconsistencies — modern browsers normalize, but verify
- Forgetting `credentials: 'include'` → request goes anonymous, server sees no cookie
- Trusting `Origin` header on the server (it's set by the browser; server logic must still authorize)
- Cookie set but not sent because path mismatch (cookie on `/api/auth`, request to `/api/users`)

## Prerequisites
- [[CORS]] · [[Cookies and Sessions]] · [[Full-Stack Auth Flow]]

## What To Learn Next
- [[Helmet and Security]] · [[Deployment Architecture]]

## Best Learning Resources

### Official Documentation
- [MDN — Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
- [MDN — CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Web.dev — SameSite cookies](https://web.dev/articles/samesite-cookies-explained)

### Best YouTube Resource
- [Hussein Nasser — Cookies & SameSite](https://www.youtube.com/@hnasr)
- [Theo — CORS issues](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [web.dev — Privacy Sandbox / Third-party cookies](https://web.dev/articles/third-party-cookies)
- [Cloudflare Learning — CORS](https://www.cloudflare.com/learning/access-management/what-is-cors/)

### Best Advanced Resource
- [Public Suffix List](https://publicsuffix.org/) — what counts as the "site" for SameSite
- [Browser cookie evolution (Chromium blog)](https://blog.chromium.org/) — tracks restriction changes

### Best Practice Project
Set up a real cross-domain stack: Vercel-hosted frontend + Render-hosted API on different eTLDs. Make signup → cookie → authenticated `/me` work end-to-end. Document every CORS / cookie tweak.

### Recommended Order to Learn
1. Cookie attributes
2. CORS basics + preflight
3. Client `credentials` modes
4. Same-site vs cross-site distinction
5. Browser third-party cookie restrictions
6. Proxying as an alternative

## Interview Questions
**Q. Why does `SameSite=None` require `Secure`?**
A. Browser policy: cross-site cookies must travel over HTTPS only.

**Q. Wildcard origin with credentials — why blocked?**
A. CSRF protection: a misconfigured server with `*` would let any site send credentials. Browsers reject the combination.

**Q. Why might a cookie be set but not sent on the next request?**
A. Path mismatch, domain mismatch, missing `credentials: 'include'`, third-party cookie blocking, or cookie expired.

## Related
- [[CORS]] · [[Cookies and Sessions]] · [[Full-Stack Auth Flow]] · [[Helmet and Security]]
