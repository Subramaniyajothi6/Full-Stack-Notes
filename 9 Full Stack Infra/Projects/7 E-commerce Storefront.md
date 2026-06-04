---
tags: [project, advanced, mern]
---

# 7. E-commerce Storefront

## Concepts practiced
- Cart state (Zustand or Redux)
- Inventory + transactions ([[Transactions|Mongo transactions]])
- Stripe (test mode) checkout
- Order lifecycle (pending → paid → shipped)
- Webhooks

## Milestones
1. Catalog (products, variants, search)
2. Cart (guest + signed-in merge on login)
3. Checkout → Stripe → webhook → order
4. Inventory decrement (transaction)
5. Order history, status emails
6. Admin: product CRUD, orders, refunds

## Common mistakes
- Trusting prices from client (always re-price on server)
- Decrementing inventory before payment success
- No idempotency on webhook handlers

## Next
- [[8 SaaS Dashboard]]

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
