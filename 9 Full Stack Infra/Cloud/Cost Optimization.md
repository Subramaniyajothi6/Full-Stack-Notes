---
tags: [cloud, intermediate, ops]
---

# Cost Optimization

> Cloud bills sneak up. The lever is rarely "one big change" — it's many small awareness wins.

## The hierarchy of cost waste
1. **Idle resources** — running things no one uses
2. **Oversized resources** — instances bigger than the workload
3. **Wrong pricing model** — on-demand when reserved/spot would be 70% cheaper
4. **Egress** — data leaving the cloud (especially cross-AZ, cross-region)
5. **Storage tier** — Standard when Glacier/IA fits
6. **Excess observability** — logs/metrics never queried but ingested

## Tooling
- **Cost Explorer** (AWS) / **Cloud Billing** (GCP) / **Cost Management** (Azure)
- **AWS Budgets + alerts**
- **Trusted Advisor / Compute Optimizer**
- **CloudHealth / Cloudability / Vantage / Infracost** — third-party
- **Spot.io / Karpenter** — automated rightsizing

## Big-win patterns
- **Spot instances** — 70–90% off, interruptable; great for stateless workers
- **Savings Plans / Reserved Instances** — 30–60% off for committed usage
- **Lifecycle policies on S3** — auto-tier old objects
- **TTL on CloudWatch logs** — cap retention
- **VPC endpoints** — kill NAT egress for S3/DynamoDB
- **Use Cloud Run / Lambda** for bursty low-volume workloads
- **Stop dev environments overnight** — 70% off automatically

## Egress economics
- Cross-AZ: ~$0.01/GB
- Cross-region: ~$0.02/GB
- Internet egress: $0.05–0.09/GB
- Cloudflare R2 / Backblaze B2 = $0 egress (alt to S3 for read-heavy workloads)

## Real World Usage
- Monthly cost-review with stakeholders
- Per-team / per-tenant cost attribution via tags
- Idle-resource killer cron
- Rightsizing recommendations turned into Terraform PRs
- Migration off NAT Gateway to VPC endpoints

## Common Mistakes
- No tagging → can't attribute cost
- "Just leave it running" dev environments
- CloudWatch log retention default = forever
- Always-on RDS multi-AZ for dev
- Default S3 storage class (no lifecycle)
- Single region with cross-region traffic for users that don't need it
- Surprise bill from cross-account data transfer

## Prerequisites
- [[AWS]] · [[VPC and Networking]]

## What To Learn Next
- [[Containers in the Cloud]] · [[Lambda and Serverless]]

## Best Learning Resources

### Official Documentation
- [AWS Well-Architected — Cost pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/)
- [AWS Pricing Calculator](https://calculator.aws/)
- [Google Cloud — Cost optimization](https://cloud.google.com/cost-management)

### Best YouTube Resource
- [Last Week in AWS — Corey Quinn](https://www.youtube.com/c/LastWeekinAWS)
- [TechWorld with Nana — cloud cost](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [AWS Skill Builder — Cost optimization](https://explore.skillbuilder.aws/)
- [FinOps Foundation](https://www.finops.org/)

### Best Advanced Resource
- ["Cloud FinOps" (O'Reilly)](https://www.oreilly.com/library/view/cloud-finops-2nd/9781492054610/)
- [Cloudability / Vantage blogs](https://www.vantage.sh/blog)

### Best Practice Project
Open your AWS account. Tag every resource by `team`, `env`, `app`. Enable Cost Explorer's groups. Identify top-5 cost lines. Cut one in half (instance type, retention, tier). Document the saving.

### Recommended Order to Learn
1. Tagging strategy
2. Budgets + anomaly alerts
3. Reserved Instances / Savings Plans
4. Spot for stateless work
5. Storage lifecycle policies
6. Egress audit + VPC endpoints
7. Rightsizing automation

## Interview Questions
**Q. Why is egress the silent killer?**
A. It's the line item teams discover too late. Cross-AZ, cross-region, and internet traffic all add up — and Cloudflare R2 / Backblaze cut it to zero for some workloads.

**Q. Spot vs Reserved?**
A. Spot is steep discount for interruptable, stateless workloads. Reserved is a commitment for steady-state baseline. Use both: Reserved for floor, Spot for peaks.

**Q. Why tag everything?**
A. Without tags you can't attribute cost to product / team / feature. Cost reviews stall instantly.

## Related
- [[AWS]] · [[VPC and Networking]] · [[Containers in the Cloud]] · [[Lambda and Serverless]]
