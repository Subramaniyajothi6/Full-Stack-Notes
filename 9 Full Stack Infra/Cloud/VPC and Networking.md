---
tags: [cloud, intermediate, networking]
---

# VPC and Networking

> A logically isolated section of the cloud where your resources live. Subnets, route tables, security groups, NAT — the basics every cloud workload sits on.

## Building blocks
- **VPC** — isolated network with CIDR (e.g., `10.0.0.0/16`)
- **Subnets** — slices of the VPC, each in one AZ
  - **Public** — has route to Internet Gateway
  - **Private** — no direct internet; outbound via NAT
  - **Isolated** — no internet at all (DBs, caches)
- **Internet Gateway (IGW)** — public internet ingress/egress
- **NAT Gateway** — outbound-only from private subnets (expensive!)
- **Route tables** — what goes where
- **Security Groups** — stateful firewall at the resource level
- **NACLs** — stateless firewall at the subnet level
- **VPC Endpoints** — private path to AWS services (S3, DynamoDB)
- **Peering / Transit Gateway** — connect VPCs

## Reference architecture
```
VPC 10.0.0.0/16
├── public  10.0.1.0/24 (AZ-a)  ── ALB
├── public  10.0.2.0/24 (AZ-b)  ── ALB
├── private 10.0.11.0/24 (AZ-a) ── ECS, Lambda  → NAT GW (egress)
├── private 10.0.12.0/24 (AZ-b)
├── isolated 10.0.21.0/24       ── RDS
└── isolated 10.0.22.0/24       ── RDS
```

## Real World Usage
- Production three-tier (web/app/db)
- Restricting DB access to private subnets only
- VPC endpoints to skip NAT cost for S3 traffic
- Hub-and-spoke transit for multi-account orgs
- Bastion / SSM Session Manager for admin access

## Common Mistakes
- DB in a public subnet
- Security Group set to `0.0.0.0/0` for SSH / DB
- One NAT Gateway → outage when its AZ fails (use one per AZ)
- IGW + private subnet without route → mystery no-internet
- Overlapping CIDRs that block future VPC peering
- Egress over NAT for S3 traffic when VPC endpoint is free

## Prerequisites
- [[AWS]] · [[Client-Server Model]] · [[DNS]]

## What To Learn Next
- [[IAM and Least Privilege]] · [[Lambda and Serverless]]

## Best Learning Resources

### Official Documentation
- [VPC User Guide](https://docs.aws.amazon.com/vpc/)
- [VPC subnets + route tables](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)

### Best YouTube Resource
- [Stephane Maarek — VPC fundamentals](https://www.youtube.com/c/StephaneMaarek)
- [Be A Better Dev — VPC](https://www.youtube.com/c/BeABetterDev)

### Best Free Course
- [AWS Skill Builder — Networking Essentials](https://explore.skillbuilder.aws/)
- [AWS re:Invent VPC talks](https://www.youtube.com/c/AmazonWebServices)

### Best Advanced Resource
- [AWS Networking workshops (GitHub)](https://github.com/aws-samples)

### Best Practice Project
Build a 3-AZ VPC in Terraform with public ALB, private ECS, isolated RDS. Add a VPC endpoint for S3 and one NAT Gateway per AZ. Verify traffic paths with `tcpdump` / VPC flow logs.

### Recommended Order to Learn
1. CIDRs + subnets + AZs
2. IGW + NAT + route tables
3. Security Groups vs NACLs
4. VPC endpoints (gateway + interface)
5. Peering / Transit Gateway
6. Flow logs + observability

## Interview Questions
**Q. Security Group vs NACL?**
A. SG is stateful, attached to resources, allow-only. NACL is stateless, attached to subnets, allow + deny.

**Q. Why VPC endpoints for S3?**
A. Free + private — traffic never leaves AWS network; saves NAT egress cost.

**Q. Single NAT Gateway risk?**
A. AZ failure = no outbound for all private subnets. Run one per AZ for HA.

## Related
- [[AWS]] · [[Lambda and Serverless]] · [[IAM and Least Privilege]]
