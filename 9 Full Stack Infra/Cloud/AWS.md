---
tags: [infra, cloud, intermediate]
---

# AWS

> Amazon Web Services — the largest public cloud. ~200 services across compute, storage, database, AI, networking.

## Why it matters
Most production workloads either run on AWS or compete with companies that do. Knowing core AWS lets you ship and reason about cloud architecture broadly.

## Core building blocks
- **Compute** — EC2 (VMs), ECS/Fargate (containers), Lambda (serverless), Beanstalk (PaaS)
- **Storage** — S3 (objects), EBS (block, attached to EC2), EFS (NFS)
- **Database** — RDS (Postgres/MySQL), Aurora (managed Postgres+, scale-out), DynamoDB (NoSQL), ElastiCache (Redis/Memcached)
- **Networking** — VPC, subnets, route tables, NAT, ALB/NLB, CloudFront (CDN), Route 53 (DNS), API Gateway
- **Identity** — IAM (users, roles, policies), Cognito (end-user auth)
- **Messaging** — SQS, SNS, EventBridge, MSK (Kafka)
- **Observability** — CloudWatch, X-Ray
- **AI** — Bedrock, SageMaker

## Mental model
1. Pick a region (`us-east-1` cheapest)
2. Create a VPC with public + private subnets
3. Run app on ECS/Fargate (or EKS/EC2)
4. Store data in RDS/DynamoDB
5. Static assets in S3 + CloudFront
6. Auth via Cognito or app-level
7. Observability via CloudWatch + X-Ray

## Real World Usage
- Almost every "production" workload reachable from this list
- Combine with Terraform for IaC

## Common Mistakes
- Running everything in `us-east-1` for global users
- Not setting Budgets + cost alarms — surprise bills
- Public S3 buckets
- Hardcoding access keys → leak. Use IAM Roles.
- Lambda functions doing 30-second cold starts because of huge dependencies
- Skipping VPC endpoints → S3/DynamoDB traffic goes through NAT (egress costs)

## Prerequisites
- [[Linux Basics]] · [[Client-Server Model|Client/Server]]

## What To Learn Next
- [[Terraform]] · [[Pulumi]] · [[CI CD]] · [[GCP]] · [[Azure]]

## Best Learning Resources

### Official Documentation
- [AWS Documentation](https://docs.aws.amazon.com/) — service-by-service
- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

### Best YouTube Resource
- [Stephane Maarek — AWS Certified Developer/Architect](https://www.youtube.com/c/StephaneMaarek) — exam-grade clarity
- [TechWorld with Nana — AWS](https://www.youtube.com/c/TechWorldwithNana)
- [Be A Better Dev — AWS architectures](https://www.youtube.com/c/BeABetterDev)

### Best Free Course
- [AWS Skill Builder](https://explore.skillbuilder.aws/) — official, many free courses
- [AWS Cloud Practitioner Essentials](https://aws.amazon.com/training/learn-about/cloud-practitioner/) — free intro

### Best Advanced Resource
- [Werner Vogels — All Things Distributed](https://www.allthingsdistributed.com/) — CTO essays
- [AWS re:Invent talks on YouTube](https://www.youtube.com/c/AmazonWebServices) — annual deep dives
- [Cloud Posse / Last Week in AWS](https://www.lastweekinaws.com/) — Corey Quinn newsletter, sharp

### Best Practice Project
Deploy a MERN app on AWS: ECR for images, ECS Fargate for the API, RDS Postgres in private subnet, S3 + CloudFront for the React build, Cognito for auth, ALB in front of ECS, all defined in Terraform. Add CloudWatch dashboards + alarms.

### Recommended Order to Learn
1. IAM + S3 + EC2 basics
2. VPC networking
3. RDS + ElastiCache
4. ECS/Fargate + ALB
5. Lambda + API Gateway + EventBridge
6. CI/CD via CodeBuild/CodeDeploy or GitHub Actions
7. Observability + cost optimization

## Interview Questions
**Q. ECS vs EKS vs Fargate?**
A. ECS = AWS container orchestrator. EKS = managed Kubernetes. Fargate = serverless compute backend usable with both, no nodes to manage.

**Q. Why use a VPC?**
A. Network isolation, control over routing/firewall (security groups, NACLs), private subnets for DBs.

**Q. RDS vs DynamoDB?**
A. RDS = managed relational. DynamoDB = NoSQL key-value, single-digit ms latency, serverless.

**Q. How do you reduce Lambda cold starts?**
A. Smaller artifact, provisioned concurrency, avoid heavy init, prefer Node/Go over JVM.

## Related
- [[GCP]] · [[Azure]] · [[Terraform]] · [[AWS S3]]
