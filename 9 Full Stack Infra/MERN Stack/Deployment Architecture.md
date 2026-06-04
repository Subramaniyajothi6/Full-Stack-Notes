---
tags: [mern, deployment, intermediate]
---

# Deployment Architecture

> The shape of your production environment. Pick the simplest option that meets your reliability + cost + scale needs.

## Three common shapes

### A. Managed PaaS (simplest)
```
Vercel (Next.js / React) ── HTTPS ──▶ Render (Express) ── connection ──▶ MongoDB Atlas
                                              │
                                              └────▶ Cloudinary / S3 (uploads)
```
- Zero ops
- Global edge for frontend
- Costs scale with traffic
- Vendor lock-in is real

### B. Single-VPS Dockerized (cheapest)
```
$10 VPS:
  nginx (TLS, reverse proxy)
    ├── docker container: web (built React static)
    ├── docker container: api (Node + Express)
    └── docker container: mongo
  certbot (Let's Encrypt)
```
- One bill, full control
- Manual scaling
- You own SRE
- Great for side projects, prototypes

### C. AWS production (most flexible)
```
Route 53 (DNS)
   └── CloudFront (CDN)
         ├── S3 (React static build)
         └── ALB
               └── ECS Fargate (Express containers, multi-AZ)
                     ├── RDS Postgres / DocumentDB / Atlas (data)
                     ├── ElastiCache Redis (cache, sessions, queues)
                     └── S3 (user uploads, signed URLs)
   └── ACM (TLS certs)
   └── CloudWatch + X-Ray (observability)
   └── EventBridge / SQS (async)
```
- Production-grade reliability
- Pay-per-use, scales horizontally
- Real ops cost (Terraform, IAM, monitoring)

## How to choose
| Question | Answer → recommend |
|---|---|
| Side project / portfolio? | A or B |
| 1–10 paying users? | A |
| 100+ paying users, B2B? | A or C |
| Compliance / data residency? | C |
| Cost-sensitive, willing to operate? | B |
| Need global low latency? | A (Vercel) or C (CloudFront) |

## Real World Usage
- Indie hackers / MVPs → A
- Bootstrapped SaaS → A or B until scaling forces C
- Startups with funding → A early, C as they grow
- Enterprise → C from day one (or Azure/GCP equivalents)

## Common Mistakes
- Deploying to `us-east-1` only when users are global
- No environment parity (dev runs in Docker, prod runs on Vercel — different kinds of bugs in each)
- Storing uploads on the API container's local disk (lost on redeploy)
- Hard-coding secrets in repo or in build-time env
- Forgetting healthchecks → bad instances stay in load balancer
- Single Mongo instance (no replica set) — first failure is data loss
- DNS caching during a switch — preview environments help

## Prerequisites
- [[Docker]] · [[CI CD]] · [[Cloud MOC]] · [[Environment Management]]

## What To Learn Next
- [[Dockerized MERN]] · [[Full-Stack CI CD]] · [[AWS]]

## Best Learning Resources

### Official Documentation
- [Vercel docs — Frameworks](https://vercel.com/docs/frameworks)
- [Render docs — Web Services](https://render.com/docs/web-services)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

### Best YouTube Resource
- [Theo — deployment options](https://www.youtube.com/@t3dotgg)
- [TechWorld with Nana — Cloud architectures](https://www.youtube.com/c/TechWorldwithNana)
- [Be A Better Dev — AWS architectures](https://www.youtube.com/c/BeABetterDev)

### Best Free Course
- [AWS Free Tier hands-on](https://aws.amazon.com/free/)
- [Fly.io Speedrun](https://fly.io/speedrun/) — deploy in 5 minutes

### Best Advanced Resource
- [Designing Data-Intensive Applications (book) — Kleppmann](https://dataintensive.net/) — long-term reference
- [The Twelve-Factor App](https://12factor.net/) — checklist for cloud-native apps

### Best Practice Project
Take a MERN app and deploy it three ways: (A) Vercel + Render + Atlas, (B) single VPS with `docker compose`, (C) AWS with ECS + RDS + S3 + CloudFront via Terraform. Compare cost, latency, deploy time, and downtime during deploys.

### Recommended Order to Learn
1. Single PaaS deploy (Vercel + Render)
2. Single VPS with Docker
3. Reverse proxy + TLS + Certbot
4. Object storage for uploads + CDN
5. AWS ECS + RDS pattern
6. Multi-AZ, auto-scaling, blue-green deploys

## Interview Questions
**Q. When pick a single VPS over a PaaS?**
A. Cost (10× cheaper at low scale), full control, learning. Drawbacks: you operate it.

**Q. Why static frontend on CDN/S3 + API container?**
A. Static = infinitely scalable, near-zero cost. API does the dynamic work, scales independently.

**Q. What's blue-green deployment?**
A. Run new version (green) alongside old (blue), shift traffic, keep blue ready for rollback.

## Related
- [[Docker]] · [[Dockerized MERN]] · [[CI CD]] · [[Full-Stack CI CD]] · [[AWS]] · [[Environment Management]]
