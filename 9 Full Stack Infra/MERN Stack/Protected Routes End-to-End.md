---
tags: [mern, auth, intermediate]
---

# Protected Routes End-to-End

> A protected feature needs gates at three levels: route guard (frontend), API middleware (backend), data scope (DB). Skip any one and a determined user gets through.

## The three gates

### 1. Frontend route guard (UX, not security)
```tsx
function RequireAuth({ children }: { children: React.ReactNode }) {
  const { user, loading } = useAuth();
  if (loading) return <Spinner />;
  if (!user) return <Navigate to="/login" replace />;
  return <>{children}</>;
}

<Route path="/dashboard" element={<RequireAuth><Dashboard /></RequireAuth>} />
```
Purpose: don't show users a page they can't load. **Not** a security boundary.

### 2. Backend middleware (real security)
```ts
function requireAuth(req, res, next) { /* verify JWT cookie */ }
function requireRole(role) {
  return (req, res, next) => {
    if (!req.user || !req.user.roles.includes(role)) return res.sendStatus(403);
    next();
  };
}

app.use('/api/admin', requireAuth, requireRole('admin'), adminRouter);
```
Purpose: every request that reaches a handler is authenticated and authorized.

### 3. Data scope (resource ownership)
```ts
// Bad — IDOR vulnerability
app.get('/api/orders/:id', requireAuth, async (req, res) => {
  res.json(await Order.findById(req.params.id));
});

// Good — scoped to owner
app.get('/api/orders/:id', requireAuth, async (req, res) => {
  const order = await Order.findOne({ _id: req.params.id, userId: req.user.sub });
  if (!order) return res.sendStatus(404);
  res.json(order);
});
```
Purpose: even authenticated users can only access *their* data.

## Patterns by route type
| Route                    | Guards                                                          |
|--------------------------|-----------------------------------------------------------------|
| `/login`, `/signup`      | none (anti-rate-limit only)                                     |
| `/dashboard`             | requireAuth                                                     |
| `/admin/*`               | requireAuth + requireRole('admin')                              |
| `/orders/:id`            | requireAuth + ownership scope in query                          |
| `/teams/:teamId/*`       | requireAuth + team membership lookup                            |

## Real World Usage
- SaaS multi-tenant: every query includes `tenantId`
- E-commerce: order belongs to user; admin sees all
- Social: post visibility (public/friends/private) becomes a query filter
- Healthcare: HIPAA-style strict scope checks

## Common Mistakes
- Frontend-only checks ("just hide the button") — bypassed via curl
- IDOR — `/orders/:id` without ownership check leaks anyone's order
- Role string literals scattered across the codebase ("admin", "Admin", "ADMIN")
- Mixing AuthN (who) and AuthZ (what) — they need separate middleware
- Skipping audit logging on privileged routes
- Trusting `req.body.userId` instead of `req.user.sub`

## Prerequisites
- [[Full-Stack Auth Flow]] · [[Authentication vs Authorization]] · [[Protected Routes]]

## What To Learn Next
- [[OAuth Flow]] · [[Cross-Domain Cookies]]

## Best Learning Resources

### Official Documentation
- [OWASP — IDOR / Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
- [Auth.js callbacks](https://authjs.dev/concepts/session-strategies)

### Best YouTube Resource
- [Theo — RBAC patterns](https://www.youtube.com/@t3dotgg)
- [Hussein Nasser — auth bypasses](https://www.youtube.com/@hnasr)

### Best Free Course
- [OWASP Top 10 explainers](https://owasp.org/www-project-top-ten/)
- [Frontend Masters — auth patterns (some free chapters)](https://frontendmasters.com/)

### Best Advanced Resource
- [Cedar policy language (AWS)](https://www.cedarpolicy.com/) — modern fine-grained authz
- [Open Policy Agent (OPA)](https://www.openpolicyagent.org/)

### Best Practice Project
Add a multi-tenant feature to your app: org → projects → tasks. Implement frontend route guards, backend middleware (requireAuth + requireOrg + requireRole), and ownership scope. Try to break it via curl/Postman — every attempt should fail with 401/403/404 (never 200).

### Recommended Order to Learn
1. Frontend `<RequireAuth>`
2. Backend `requireAuth` middleware
3. Role-based access (RBAC)
4. Resource ownership / scope
5. Attribute-based access (ABAC) for complex policies
6. Audit logging

## Interview Questions
**Q. Why is the frontend guard not security?**
A. Anyone can call your API directly with curl. Only the server-side checks protect data.

**Q. What's IDOR?**
A. Insecure Direct Object Reference: `/orders/:id` allows any authenticated user to fetch any order. Fix: scope by ownership in the DB query.

**Q. AuthN vs AuthZ?**
A. AuthN = who you are. AuthZ = what you may do.

**Q. RBAC vs ABAC?**
A. RBAC: roles → permissions. ABAC: rules over attributes (resource owner == user, time-based, etc.). RBAC is simpler; ABAC is more flexible.

## Related
- [[Full-Stack Auth Flow]] · [[Protected Routes]] · [[Authentication vs Authorization]] · [[Sessions vs JWT]]
