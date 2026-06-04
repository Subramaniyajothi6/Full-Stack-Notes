---
tags: [cloud, advanced, scale]
---

# Multi-Region

> Running across multiple cloud regions for latency, compliance, or HA. The complexity multiplier of cloud architecture.

## Why
- **Latency** — users in EU shouldn't traverse Atlantic per request
- **Compliance / data residency** — GDPR, region-pinned data
- **HA** — survive entire region outage
- **Burst capacity** — failover during regional spike

## Topologies
- **Active-passive** — primary serves traffic, standby ready
- **Active-active** — both regions serve traffic
- **Read-local, write-global** — reads near user, writes to one primary
- **Sharded by tenant** — each tenant pinned to a region

## DNS-level
- **Route 53** / **Cloud DNS** with geolocation or latency-based routing
- Health checks for failover
- TTL trade-offs (low = fast failover, high = better caching)

## Data layer
- **Aurora Global Database** — Postgres with cross-region replicas, ~1s lag
- **DynamoDB Global Tables** — multi-region, multi-master (with conflict resolution)
- **MongoDB Atlas Global Clusters**
- **Object storage replication** — S3 Cross-Region Replication
- **CockroachDB / Spanner** — globally distributed SQL natively

## Edge layer
- [[CDN]] + [[Edge Computing]] make read-mostly content near-instant globally
- Origin shielding to reduce cross-region origin hits

## Real World Usage
- Global SaaS dashboards
- Content platforms (CDN-heavy)
- Financial systems with strict data-residency
- Multi-region disaster-recovery plans
- Gaming with regional matchmaking

## Common Mistakes
- "Active-active" with a single Postgres in one region (writes still cross-Atlantic)
- No conflict-resolution strategy for multi-master writes
- DNS TTLs too high → failover takes minutes
- Forgetting cross-region egress costs ([[Cost Optimization]])
- Inconsistent secrets / configs across regions
- No regional smoke tests after deploy

## Prerequisites
- [[AWS]] · [[VPC and Networking]] · [[CDN]] · [[Backups and Restore]]

## What To Learn Next
- [[Cost Optimization]] · [[Edge Computing]]

## Best Learning Resources

### Official Documentation
- [AWS Multi-Region Reference Architectures](https://aws.amazon.com/architecture/global-architectures/)
- [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)
- [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)

### Best YouTube Resource
- [AWS re:Invent — multi-region talks](https://www.youtube.com/c/AmazonWebServices)
- [Hussein Nasser — multi-region patterns](https://www.youtube.com/@hnasr)

### Best Free Course
- [AWS Well-Architected — Reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/)

### Best Advanced Resource
- [Designing Data-Intensive Applications — replication chapters](https://dataintensive.net/)
- [Werner Vogels — All Things Distributed](https://www.allthingsdistributed.com/)

### Best Practice Project
Take a single-region app and add: (1) CloudFront global CDN, (2) read replica in a second region, (3) Route 53 geo routing for static assets, (4) regional health checks. Measure latency from 3 continents before/after.

### Recommended Order to Learn
1. CDN globally (cheap latency win)
2. Edge compute near users
3. Cross-region read replicas
4. Geo-routed DNS
5. Active-passive failover
6. Active-active + conflict resolution
7. Compliance + data residency patterns

## Interview Questions
**Q. Why is "active-active" hard for writes?**
A. Two regions accepting writes → conflicts. Need either single-leader, CRDTs, or app-level resolution.

**Q. CDN vs multi-region origin?**
A. CDN caches static + cache-friendly responses near users (cheap). Multi-region origin replicates dynamic data closer (expensive, complex).

**Q. RPO / RTO in multi-region?**
A. Active-passive failover ≈ minutes RTO + seconds RPO (async replication). Active-active ≈ near-zero, with consistency tradeoffs.

## Related
- [[CDN]] · [[Edge Computing]] · [[Backups and Restore]] · [[Cost Optimization]]
