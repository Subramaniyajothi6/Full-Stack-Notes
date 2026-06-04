---
tags: [moc, cloud]
---

# Cloud MOC

> Hyperscalers + edge platforms. The infrastructure your app runs on.

## Providers (general)
- [[AWS]] — broadest service catalog; default for production
- [[GCP]] — Cloud Run, BigQuery, Spanner, GKE
- [[Azure]] — enterprise + Microsoft 365 integration, Azure OpenAI

## AWS-specific
- [[AWS S3]] — object storage flagship
- [[Object Storage]] — provider-agnostic concepts

## Networking + identity
- [[VPC and Networking]] — subnets, route tables, security groups
- [[IAM and Least Privilege]] — roles, policies, OIDC federation

## Compute
- [[Lambda and Serverless]] — event-driven functions
- [[Containers in the Cloud]] — ECS / Fargate, Cloud Run, App Runner, Fly

## Operations
- [[Secrets Management]] — SSM, Secrets Manager, Vault, Doppler
- [[Cost Optimization]] — Reserved / Spot / tagging / egress
- [[Multi-Region]] — global latency, HA, compliance

## Edge / performance
- [[Edge Computing]] — Cloudflare Workers, Vercel Edge, Lambda@Edge

## Suggested order
1. [[Object Storage]] (provider-agnostic foundation)
2. [[AWS]] → [[AWS S3]]
3. [[VPC and Networking]] → [[IAM and Least Privilege]]
4. [[Lambda and Serverless]] or [[Containers in the Cloud]] (pick by workload)
5. [[Secrets Management]]
6. [[Cost Optimization]]
7. [[Multi-Region]] · [[Edge Computing]] (when you outgrow one region)

## Roadmap to fill in
- [ ] Disaster recovery runbooks
- [ ] Compliance frameworks (SOC 2, HIPAA, ISO 27001) baseline
- [ ] WAF + DDoS protection details
- [ ] Service mesh in cloud (App Mesh, Istio on EKS)
- [ ] Data warehouses (BigQuery / Redshift / Snowflake)
- [ ] FinOps practices

## Related stacks
- [[DevOps MOC]] — Terraform, Docker, CI/CD ship to here
- [[System Design MOC]] — scaling, replication, CDN
- [[MERN Stack MOC]] — [[Deployment Architecture]]

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
