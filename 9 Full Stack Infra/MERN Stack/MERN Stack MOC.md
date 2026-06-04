---
tags: [moc, mern, integration]
---

# MERN Stack MOC

> Orchestration layer — how the pieces fit together in production. Not a replacement for [[React MOC]] / [[NodeJS MOC]] / [[Express MOC]] / [[MongoDB MOC]] (those stay dedicated). This stack is about gluing them.

## Visual flow
- [[MERN Roadmap.canvas]] — master roadmap
- [[Projects Path.canvas]] — beginner → advanced project arc

## Frontend ↔ Backend Integration
- [[API Contract]] — REST vs GraphQL vs tRPC, error shapes, versioning
- [[Type Sharing]] — Zod / tRPC / OpenAPI for one source of truth
- [[Form Lifecycle]] — client → server → DB validation chain
- [[Cross-Domain Cookies]] — CORS, SameSite, the source of every "works in dev, breaks in prod" bug

## Authentication + Authorization
- [[Full-Stack Auth Flow]] — signup → JWT → cookie → refresh → logout
- [[Protected Routes End-to-End]] — frontend gate + backend middleware + data scope

## Deployment Architecture
- [[Deployment Architecture]] — PaaS vs single-VPS vs AWS production
- [[Dockerized MERN]] — `docker compose` stack with nginx + TLS
- [[Environment Management]] — `.env`, secrets, per-stage configs
- [[Full-Stack CI CD]] — pipeline: lint → test → build → deploy preview → prod

## Production Concerns
- [[Logging Across Services]] — structured logs, request-id correlation, traces
- [[Caching Layers]] — browser → CDN → reverse proxy → app → Redis → DB
- [[DB Migrations]] — versioned, forward-only schema changes
- [[Backups and Restore]] — RPO / RTO, restore drills

## Realtime + Async Work
- [[Realtime with Socket.IO]] — bidirectional realtime with Redis adapter
- [[Background Jobs]] — BullMQ, Inngest, durable async work
- [[Webhooks]] — incoming + outgoing event-driven integrations

## Architecture Patterns
- [[Multi-Tenant Patterns]] — tenant scoping, RBAC inside a tenant
- [[Feature Flags]] — decouple deploy from release

## Integrations
- [[File Upload Pipeline]] — presigned URLs → S3 → process → CDN
- [[Email Infrastructure]] — Resend / Postmark, deliverability, queueing
- [[Stripe Integration]] — payments, subscriptions, webhooks

## Suggested order
1. **Integration foundations** — [[API Contract]] → [[Type Sharing]] → [[Form Lifecycle]]
2. **Auth** — [[Full-Stack Auth Flow]] → [[Protected Routes End-to-End]] → [[Cross-Domain Cookies]]
3. **Deployment** — [[Deployment Architecture]] → [[Dockerized MERN]] → [[Environment Management]] → [[Full-Stack CI CD]]
4. **Reliability** — [[Logging Across Services]] → [[Caching Layers]] → [[DB Migrations]] → [[Backups and Restore]]
5. **Async** — [[Realtime with Socket.IO]] → [[Background Jobs]] → [[Webhooks]]
6. **Patterns** — [[Multi-Tenant Patterns]] → [[Feature Flags]]
7. **Integrations** — [[File Upload Pipeline]] → [[Email Infrastructure]] → [[Stripe Integration]]

## Roadmap to fill in
- [ ] Outbox pattern (transactional event publishing)
- [ ] Saga / compensation patterns
- [ ] Disaster-recovery runbook template
- [ ] On-call + incident response basics
- [ ] Cost monitoring + budgeting

## Related stacks
Foundation:
- [[JavaScript MOC]] · [[TypeScript MOC]] · [[System Design MOC]]

Components:
- [[React MOC]] · [[NodeJS MOC]] · [[Express MOC]] · [[MongoDB MOC]]

Layers:
- [[NextJS MOC]] · [[Cloud MOC]] · [[DevOps MOC]] · [[Testing MOC]]

Build + prep:
- [[Projects MOC]] · [[Interview MOC]]

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]] · [[MERN Roadmap.canvas]]
