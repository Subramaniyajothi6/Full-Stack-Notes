---
tags: [mern, auth, intermediate]
---

# Auth.js and Clerk

> Pre-built auth for modern stacks. Auth.js (open-source) and Clerk (hosted) — pick by ops appetite.

## Quick comparison
| Feature              | Auth.js (NextAuth)               | Clerk                                 |
|----------------------|----------------------------------|---------------------------------------|
| Hosting              | Self-hosted (in your app)        | Managed                                |
| Free tier            | Unlimited                        | Generous (10k MAU)                     |
| Sign-in UI           | DIY                              | Beautiful pre-built                    |
| Org / teams support  | Manual                           | First-class                            |
| MFA / passkeys       | Build it                         | Out of box                              |
| Sessions             | DB or JWT                        | Hosted                                  |
| Webhooks             | DIY                              | Built-in                                |
| Migration off        | Just JS — easy                   | Less easy                              |

## Auth.js (NextAuth) — App Router
```ts
// app/api/auth/[...nextauth]/route.ts
import NextAuth from 'next-auth';
import Google from 'next-auth/providers/google';
import Credentials from 'next-auth/providers/credentials';

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    Google({ clientId: ..., clientSecret: ... }),
    Credentials({
      async authorize(credentials) { return await verifyUser(credentials); },
    }),
  ],
  session: { strategy: 'jwt' },
});

export const { GET, POST } = handlers;
```
```tsx
// in a server component
import { auth } from '@/auth';
const session = await auth();
if (!session) redirect('/login');
```

## Clerk — Next.js
```tsx
// app/layout.tsx
import { ClerkProvider } from '@clerk/nextjs';
export default function Layout({ children }) {
  return <ClerkProvider><html><body>{children}</body></html></ClerkProvider>;
}

// any server component
import { auth } from '@clerk/nextjs/server';
const { userId } = await auth();

// middleware
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';
const isProtectedRoute = createRouteMatcher(['/dashboard(.*)']);
export default clerkMiddleware((auth, req) => {
  if (isProtectedRoute(req)) auth().protect();
});
```

## When to pick which
- **Auth.js** — full control, no vendor lock-in, willing to build features (orgs, MFA, audit, account management UI)
- **Clerk** — ship faster, beautiful UX out of the box, B2B with orgs, willing to pay
- **Auth0 / Cognito / Stytch / WorkOS** — alternatives in the same space
- **Roll your own** — only when neither fits compliance / weird-protocol needs (see [[Full-Stack Auth Flow]])

## Real World Usage
- Most Next.js SaaS picks Auth.js or Clerk
- Enterprise SSO → WorkOS / Auth0
- Mobile-first → Stytch / Firebase Auth
- High-touch compliance → in-house (rare)

## Common Mistakes
- Treating Auth.js as a complete IDP — it's a library; you still own session storage decisions
- Clerk's free tier underestimated → cost surprise at scale
- Not understanding session strategy (JWT cookie vs DB session) implications for revocation
- Mixing Clerk on frontend and your own JWT for API — two auth systems = bugs
- Forgetting RBAC inside the tenant (Clerk has Organizations + Roles)

## Prerequisites
- [[Full-Stack Auth Flow]] · [[Protected Routes End-to-End]] · [[OAuth Flow]]

## What To Learn Next
- [[Multi-Tenant Patterns]] · [[Webhooks]]

## Best Learning Resources

### Official Documentation
- [Auth.js docs](https://authjs.dev/)
- [Clerk docs](https://clerk.com/docs)
- [Lucia Auth (lighter alternative)](https://lucia-auth.com/)

### Best YouTube Resource
- [Theo — Auth.js vs Clerk](https://www.youtube.com/@t3dotgg)
- [Web Dev Cody — Clerk + Next.js](https://www.youtube.com/@WebDevCody)

### Best Free Course
- [Auth.js Getting Started](https://authjs.dev/getting-started/introduction)
- [Clerk Quickstart](https://clerk.com/docs/quickstarts/nextjs)

### Best Advanced Resource
- [The Copenhagen Book — auth design](https://thecopenhagenbook.com/)

### Best Practice Project
Build a SaaS dashboard with: signup → email verify → org creation → invite teammates → role-based gates → SSO. Try Auth.js first; then port to Clerk; compare LOC + features delivered.

### Recommended Order to Learn
1. OAuth flow basics ([[OAuth Flow]])
2. Auth.js Google + Credentials providers
3. Sessions: JWT vs DB
4. Middleware-gated routes
5. Clerk: provider + middleware + UI components
6. Orgs + roles in Clerk
7. Webhooks (Clerk events into your DB)

## Interview Questions
**Q. Why might you pick Clerk over Auth.js?**
A. Beautiful UX, MFA, passkeys, orgs, less code. Trade: vendor lock-in + cost.

**Q. JWT session strategy in Auth.js — pros / cons?**
A. Pro: stateless, no DB read per request. Con: hard to revoke instantly without a denylist.

**Q. When roll your own?**
A. Specific compliance, unusual protocols, no acceptable vendor. Otherwise the off-the-shelf paths win.

## Related
- [[Full-Stack Auth Flow]] · [[OAuth Flow]] · [[Multi-Tenant Patterns]] · [[Protected Routes End-to-End]]
