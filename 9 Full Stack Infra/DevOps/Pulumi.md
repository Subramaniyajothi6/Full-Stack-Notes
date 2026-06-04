---
tags: [infra, devops, intermediate]
---

# Pulumi

> Infrastructure as Code in real programming languages — TypeScript, Python, Go, C#, Java. Same provider ecosystem as Terraform but with loops, conditionals, abstractions, and your IDE.

## Why it matters
Real code beats DSLs for complex infra. Type checking, autocomplete, refactoring, npm packages, unit tests. The choice when your team thinks in code, not HCL.

## Core ideas
- **Resource** — same model as Terraform
- **Stack** — environment (dev/stage/prod) with its own state + config
- **Inputs/Outputs** — `Output<T>` are async values resolved at apply
- **State** — Pulumi Cloud (free tier) or self-hosted backend
- **Components** — reusable abstractions (the equivalent of Terraform modules)

## Example (TypeScript)
```ts
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("uploads", {
  acl: "private",
  versioning: { enabled: true },
});

new aws.s3.BucketPublicAccessBlock("block", {
  bucket: bucket.id,
  blockPublicAcls: true,
  blockPublicPolicy: true,
  ignorePublicAcls: true,
  restrictPublicBuckets: true,
});

export const bucketName = bucket.id;
```

## Real World Usage
- Teams already strong in TS/Python who don't want a second language for infra
- Infra abstractions sharing logic with app code
- Dynamic infra (loop over a config map → N resources)

## Common Mistakes
- Treating it like normal code — calling `await` on `Output<T>` too early; use `.apply`/`pulumi.all`
- Mutating shared state outside Pulumi
- Skipping `pulumi preview` in PR
- Mixing app code and infra in same package

## Prerequisites
- [[Terraform]] (concept-wise) · [[AWS]] (or GCP/Azure)

## What To Learn Next
- [[CI CD]] · [[Docker]]

## Best Learning Resources

### Official Documentation
- [Pulumi Docs](https://www.pulumi.com/docs/) — clear, language-aware
- [Pulumi Examples](https://github.com/pulumi/examples)

### Best YouTube Resource
- [Pulumi (official channel)](https://www.youtube.com/c/PulumiTV)
- [Anton Putra — Pulumi tutorials](https://www.youtube.com/c/AntonPutra)

### Best Free Course
- [Pulumi Learn](https://www.pulumi.com/learn/) — official
- [Pulumi Workshops on GitHub](https://github.com/pulumi/workshops)

### Best Advanced Resource
- [Component Resources](https://www.pulumi.com/docs/concepts/resources/components/) — abstraction guide
- [Crosswalk for AWS](https://www.pulumi.com/docs/clouds/aws/guides/) — opinionated AWS abstractions

### Best Practice Project
Re-implement the Terraform project (VPC + RDS + ECS + ALB + S3) in Pulumi/TypeScript. Wrap reusable patterns into Components. Add unit tests with `@pulumi/policy` for compliance ("no public S3 buckets").

### Recommended Order to Learn
1. Stacks + state
2. Inputs/Outputs + `.apply`
3. Component resources
4. Policies (Pulumi CrossGuard)
5. Multi-stack workflows

## Interview Questions
**Q. Pulumi vs Terraform?**
A. Pulumi = real programming languages (loops, types, packages). Terraform = HCL DSL (simpler reading, less expressive). Same underlying providers.

**Q. What is `Output<T>`?**
A. A future value resolved at apply time. Compose with `.apply`/`pulumi.all` rather than `await`.

**Q. How do you keep secrets out of state?**
A. Pulumi encrypts secret config in state automatically when you use `--secret` flags or `pulumi.secret()`.

## Related
- [[Terraform]] · [[AWS]] · [[CI CD]]
