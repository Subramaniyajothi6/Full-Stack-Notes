---
tags: [infra, devops, intermediate]
---

# Terraform

> Infrastructure as Code (IaC). Declare cloud resources in HCL; Terraform plans + applies the diff.

## Why it matters
Reproducible, reviewable, version-controlled infrastructure. The dominant multi-cloud IaC tool.

## Core ideas
- **Provider** — plugin for AWS, GCP, Azure, Cloudflare, etc.
- **Resource** — a managed thing (`aws_s3_bucket`, `aws_iam_role`)
- **State** — JSON file mapping config to real resources; store remotely (S3 + DynamoDB lock)
- **Plan** — preview the diff before applying
- **Modules** — reusable groups of resources
- **Workspaces** — multiple state files per config (env separation)

## Example
```hcl
terraform {
  required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } }
  backend "s3" {
    bucket         = "my-tf-state"
    key            = "prod/app.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-lock"
  }
}

provider "aws" { region = "us-east-1" }

resource "aws_s3_bucket" "uploads" {
  bucket = "myapp-uploads"
}

resource "aws_s3_bucket_public_access_block" "uploads" {
  bucket                  = aws_s3_bucket.uploads.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

## Real World Usage
- Provision entire cloud env from a repo
- PR-reviewed infra changes (`terraform plan` in CI)
- Multi-cloud abstraction
- Modules shared across teams

## Common Mistakes
- Storing state locally → no team collaboration; lose state = chaos
- Editing resources outside Terraform — drift
- Hardcoding secrets in `.tf` files (use vars + remote backends)
- Overly broad modules — hard to use, hard to test
- No `terraform plan` in PR review

## Prerequisites
- [[AWS]] (or GCP/Azure) · [[CI CD]]

## What To Learn Next
- [[Pulumi]] · [[CI CD]] · [[Docker]]

## Best Learning Resources

### Official Documentation
- [Terraform Docs](https://developer.hashicorp.com/terraform) — clear + complete
- [AWS provider reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Registry](https://registry.terraform.io/) — modules

### Best YouTube Resource
- [TechWorld with Nana — Terraform](https://www.youtube.com/c/TechWorldwithNana)
- [Anton Putra — Terraform with cloud](https://www.youtube.com/c/AntonPutra)

### Best Free Course
- [HashiCorp Learn — Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) — official, free
- [Gruntwork — Terraform: Up & Running (book has free chapters)](https://www.terraformupandrunning.com/)

### Best Advanced Resource
- ["Terraform: Up & Running" — Yevgeniy Brikman](https://www.terraformupandrunning.com/) — definitive book
- [Cloud Posse modules](https://github.com/cloudposse) — production-grade examples

### Best Practice Project
Codify a small AWS env: VPC + subnets + RDS + ECS + ALB + S3 + CloudFront. Split into modules: `network`, `database`, `app`. Store state in S3+Dynamo. Wire `terraform plan` in PR CI.

### Recommended Order to Learn
1. Providers + resources
2. Variables + outputs
3. State + remote backends + locking
4. Modules
5. Workspaces vs separate root configs (prefer separate)
6. Drift detection + import

## Interview Questions
**Q. Why store state remotely?**
A. Team collaboration, locking to prevent concurrent applies, encryption at rest, audit.

**Q. What is drift?**
A. Real infra differs from `.tf` config (someone clicked in console). `terraform plan` shows it; `apply` reconciles.

**Q. Modules — when to extract?**
A. When the same set of resources is needed in multiple places, or to encode org standards (e.g., "our Postgres setup").

**Q. Terraform vs CloudFormation?**
A. Terraform = multi-cloud, HCL, third-party. CFN = AWS only, JSON/YAML, native, deeper AWS integration.

## Related
- [[Pulumi]] · [[AWS]] · [[CI CD]]
