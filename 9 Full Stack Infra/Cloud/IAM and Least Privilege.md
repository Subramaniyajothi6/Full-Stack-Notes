---
tags: [cloud, intermediate, security]
---

# IAM and Least Privilege

> Identity and Access Management — who can do what, to which resources, under which conditions. The first thing to misconfigure that ruins your week.

## AWS IAM building blocks
- **User** — long-lived identity (avoid for app code)
- **Role** — short-lived credentials assumable by services / federations
- **Group** — bundle of users (rarely needed for service accounts)
- **Policy** — JSON document with `Effect, Action, Resource, Condition`
- **Identity policies** — attached to user/role
- **Resource policies** — attached to resources (S3 bucket, KMS key)
- **Service-linked roles** — AWS creates for its services
- **STS** — Security Token Service (assume role, federate)

## Policy anatomy
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": ["arn:aws:s3:::myapp-uploads/${aws:userid}/*"]
  }]
}
```

## Least-privilege patterns
- One role per service, not one mega-role
- Use IAM Access Analyzer to find unused permissions
- Use `aws:SourceIp`, `aws:RequestedRegion`, `aws:MultiFactorAuthPresent` conditions
- Federate humans via SSO; never hand out long-lived keys
- Apps use IRSA (EKS), instance profiles (EC2), task roles (ECS), or OIDC (GitHub Actions)

## Cross-account access
```
prod account: role "deploy" trusts → ci account
ci account user assumes deploy via STS
```
Eliminates static keys in CI.

## Real World Usage
- App code never knows AWS keys — uses metadata-service-supplied credentials
- GitHub Actions → AWS via OIDC, no secrets in CI
- Per-tenant scoped S3 prefixes
- Break-glass admin role behind MFA + audit

## Common Mistakes
- `*` actions or resources on production policies
- Long-lived `AKIA...` keys in env vars or repos
- Forgetting service-linked roles (`AWSServiceRoleFor*`) when troubleshooting
- Trust policies that don't restrict `sts:AssumeRole` source
- IAM changes done by hand, untracked by Terraform / CloudFormation
- Wide `s3:*` instead of `s3:GetObject` / `PutObject` on specific prefixes

## Prerequisites
- [[AWS]] · [[VPC and Networking]]

## What To Learn Next
- [[Secrets Management]] · [[Cost Optimization]] · [[Lambda and Serverless]]

## Best Learning Resources

### Official Documentation
- [IAM User Guide](https://docs.aws.amazon.com/IAM/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)

### Best YouTube Resource
- [Stephane Maarek — IAM](https://www.youtube.com/c/StephaneMaarek)
- [Be A Better Dev — IAM deep dive](https://www.youtube.com/c/BeABetterDev)

### Best Free Course
- [AWS Skill Builder — IAM Foundations](https://explore.skillbuilder.aws/)
- [policy-sentry (CLI tool for least-privilege policies)](https://github.com/salesforce/policy_sentry)

### Best Advanced Resource
- [AWS IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
- [Last Week in AWS — IAM essays](https://www.lastweekinaws.com/)

### Best Practice Project
Audit an existing AWS account: find IAM users with console-and-key, replace with SSO + roles. Move CI from access key to OIDC. Run Access Analyzer; tighten any over-broad policy.

### Recommended Order to Learn
1. Users vs roles vs groups
2. Policy JSON anatomy
3. Trust policies + STS assume role
4. Per-service roles (ECS task, Lambda exec)
5. OIDC federation (GitHub Actions, EKS IRSA)
6. Access Analyzer + least-privilege workflow
7. Cross-account patterns

## Interview Questions
**Q. Why prefer roles over IAM users for app code?**
A. Roles deliver short-lived rotating credentials via the metadata service. Users mean long-lived keys that leak.

**Q. What's IRSA?**
A. IAM Roles for Service Accounts (EKS) — Kubernetes pods assume IAM roles via OIDC, no shared cluster credentials.

**Q. Identity vs resource policy?**
A. Identity policies say "this principal can do X." Resource policies say "this resource allows X by these principals." S3 buckets and KMS keys often need both.

## Related
- [[AWS]] · [[Secrets Management]] · [[VPC and Networking]]
