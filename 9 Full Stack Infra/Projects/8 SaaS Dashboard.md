---
tags: [project, advanced, mern]
---

# 8. SaaS Dashboard

> Multi-tenant, role-permission matrix, analytics.

## Concepts practiced
- Tenants (org → users → projects)
- RBAC + scoped permissions
- Audit log
- Background jobs (BullMQ + Redis)
- Analytics (server-aggregated)
- Billing (Stripe subscriptions)

## Milestones
1. Tenant model — every query scoped to `tenantId`
2. Invite flow (email tokens)
3. Roles: owner, admin, member, viewer
4. Audit log (who did what, when)
5. Background queue for heavy jobs
6. Subscription tiers + feature gates
7. Dashboard widgets + charts

## Common mistakes
- Forgetting tenant scope in a query → cross-tenant data leak
- Hard-coding role strings throughout codebase
- No idempotency on Stripe webhooks

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
-  — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. 

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
