---
tags: [mern, architecture, advanced]
---

# Multi-Tenant Patterns

> Serving multiple customers (orgs / workspaces) from one application without their data ever crossing.

## The three isolation strategies
| Strategy             | Isolation | Cost  | Ops complexity |
| -------------------- | --------- | ----- | -------------- |
| Shared DB, shared schema (tenantId column) | low | low | low |
| Shared DB, schema-per-tenant               | medium | medium | medium |
| DB-per-tenant                              | high | high | high |

Most B2B SaaS starts with strategy 1; some upgrade to 2/3 for enterprise customers with compliance needs.

## Shared schema with `tenantId` (most common)
```ts
// every model has tenantId
const PostSchema = new mongoose.Schema({
  tenantId: { type: ObjectId, required: true, index: true },
  authorId: { type: ObjectId, required: true },
  title: String,
  body: String,
});

// always include tenantId in queries
const posts = await Post.find({ tenantId: req.tenant.id, authorId: req.user.sub });
```

## Per-request tenant context
```ts
// middleware extracts tenant from the URL or token
app.use(async (req, res, next) => {
  const slug = req.params.tenantSlug ?? req.user.tenantSlug;
  req.tenant = await Tenant.findOne({ slug });
  if (!req.tenant) return res.sendStatus(404);
  next();
});

// every query, log, and event tags tenantId
req.log = log.child({ tenantId: req.tenant.id });
```

## Tenant resolution patterns
- **Subdomain** — `acme.app.com` → `slug=acme`
- **Path prefix** — `app.com/acme/...`
- **Token claim** — JWT contains `tenantId`
- **Single-tenant token + tenant switcher** — for users in multiple orgs

## Compound indexes for tenant-scoped queries
```js
db.posts.createIndex({ tenantId: 1, createdAt: -1 });
db.posts.createIndex({ tenantId: 1, authorId: 1 });
```
Tenant-id should be the first key of practically every index.

## Member roles within a tenant
```ts
const Membership = {
  tenantId, userId, role: 'owner' | 'admin' | 'member' | 'viewer',
  invitedBy, joinedAt
};
```
Auth checks combine: AuthN (who is the user), tenant scope (is the user a member of this tenant), AuthZ (does their role allow this action).

## Real World Usage
- B2B dashboards (Slack workspaces, Notion teams, Linear teams)
- Multi-store e-commerce platforms
- Agencies with multiple client workspaces
- White-label SaaS

## Common Mistakes
- Forgetting `tenantId` in a single query → cross-tenant data leak (catastrophic)
- Hard-coding role strings everywhere — define an enum/const
- Not indexing on `tenantId` first → slow queries on the largest tenants
- One bad tenant DoSing the cluster (no per-tenant quotas)
- Audit logs without tenant scope — useless for incident triage
- "Noisy neighbor" — one giant tenant degrades others; needs per-tenant resource limits or sharding by tenant
- Trusting client to pass tenant id — derive server-side from membership

## Prerequisites
- [[Protected Routes End-to-End]] · [[Full-Stack Auth Flow]] · [[MongoDB]]

## What To Learn Next
- [[Feature Flags]] · [[Webhooks]]

## Best Learning Resources

### Official Documentation
- [PostgreSQL Row-Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) — DB-enforced tenant isolation
- [MongoDB Multi-Tenant Patterns](https://www.mongodb.com/blog/post/building-multi-tenant-saas-applications)

### Best YouTube Resource
- [ByteByteGo — Multi-tenant architecture](https://www.youtube.com/c/ByteByteGo)
- [Theo — SaaS multi-tenancy](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [AWS Multi-Tenant SaaS whitepapers](https://aws.amazon.com/architecture/) — solid free reading
- [Microsoft Multi-Tenant SaaS architecture](https://learn.microsoft.com/azure/architecture/guide/multitenant/overview)

### Best Advanced Resource
- [Tailscale engineering blog](https://tailscale.com/blog/) — deep multi-tenant network design
- [Stripe / Slack / Notion engineering blogs](https://stripe.com/blog/engineering)

### Best Practice Project
Add multi-tenancy to an existing single-tenant app: tenant slug in subdomain, membership table, all queries scoped, role checks on writes. Audit every controller; try to cross tenants via direct id access.

### Recommended Order to Learn
1. Tenant model + membership
2. Tenant resolution + middleware
3. Tenant-scoped queries + indexes
4. RBAC inside a tenant
5. Audit logs with tenant id
6. Per-tenant quotas + rate limits
7. Sharding / dedicated DBs for enterprise

## Interview Questions
**Q. Why is `tenantId` in every query mandatory?**
A. Forgetting it once leaks data across tenants — the worst kind of bug. Some teams enforce via Postgres RLS or a Mongoose plugin.

**Q. Subdomain vs path-prefix tenant routing?**
A. Subdomains feel more separate (good for white-labeling, cookies stay scoped). Paths are simpler infra-wise.

**Q. Strategy 1 vs strategy 3?**
A. Shared schema = cheap, easy. DB-per-tenant = max isolation, easier compliance, much more ops. Most start with shared schema.

## Related
- [[Protected Routes End-to-End]] · [[Full-Stack Auth Flow]] · [[Feature Flags]] · [[Logging Across Services]]
