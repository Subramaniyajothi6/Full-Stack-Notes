---
tags: [infra, aws, intermediate]
---

# AWS S3

> Amazon's flagship object storage service. Defines the de-facto API for object storage.

## Why it matters
Touches almost every AWS workload. Storage backbone for backups, static sites, data lakes, ML, and serverless.

## Core ideas
- **Bucket** — globally unique name, region-bound
- **Storage classes** — Standard, IA, Glacier (Instant/Flexible/Deep) — see lifecycle
- **Versioning** + **MFA delete**
- **Replication** — same-region (SRR) or cross-region (CRR)
- **Encryption** — SSE-S3 (default), SSE-KMS, SSE-C, client-side
- **Access logging + EventBridge / SQS / Lambda** triggers
- **VPC endpoints** — keep traffic off the public internet

## Patterns
```ts
// presigned upload
const url = await getSignedUrl(s3, new PutObjectCommand({...}), { expiresIn: 60 });

// multipart for large files (>100MB)
import { Upload } from '@aws-sdk/lib-storage';
await new Upload({ client: s3, params: { Bucket, Key, Body } }).done();
```

## Real World Usage
- Static website hosting (S3 + CloudFront)
- Database / disk backups
- Data lake (S3 + Athena)
- Lambda triggers on object created
- Build / container image artifacts

## Common Mistakes
- Bucket policy `Principal: *` with `s3:*` permissions — full public bucket
- Disabling Block Public Access settings carelessly
- Forgetting CORS for browser uploads
- Putting millions of objects under one prefix → list+sort latency
- Manual multipart cleanup (orphaned uploads cost real money)
- Cross-region traffic in hot path → egress costs

## Prerequisites
- [[Object Storage]] · [[AWS]]

## What To Learn Next
- [[CDN|CDN]] · [[Terraform]] · [[CI CD]]

## Best Learning Resources

### Official Documentation
- [S3 User Guide](https://docs.aws.amazon.com/s3/) — canonical
- [S3 best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html)

### Best YouTube Resource
- [TechWorld with Nana — AWS S3](https://www.youtube.com/c/TechWorldwithNana)
- [Stephane Maarek — AWS courses](https://www.youtube.com/c/StephaneMaarek) — exam-grade walk-throughs

### Best Free Course
- [AWS Skill Builder — S3 Storage Foundations](https://explore.skillbuilder.aws/) — free official

### Best Advanced Resource
- [AWS re:Invent — S3 deep dives](https://www.youtube.com/results?search_query=aws+reinvent+s3) — annual architecture talks
- [Werner Vogels' blog](https://www.allthingsdistributed.com/) — design history

### Best Practice Project
Set up a serverless image pipeline: client uploads via presigned URL → S3 → Lambda resizes (sharp) → writes to a `thumbs/` prefix → CloudFront serves both originals and thumbs with appropriate cache rules. Add lifecycle to tier originals > 90 days.

### Recommended Order to Learn
1. Buckets + objects + IAM
2. Presigned URLs + CORS
3. Lifecycle + versioning + replication
4. Encryption + KMS
5. Events → Lambda/SQS
6. CloudFront integration + signed CDN URLs

## Interview Questions
**Q. How do you serve private files via CDN?**
A. Origin: S3 (private). CloudFront with origin access identity (OAI/OAC). App generates signed CDN URLs.

**Q. What's the durability of S3 Standard?**
A. 99.999999999% (11 nines).

**Q. How would you handle a 5GB upload from browser?**
A. Multipart upload with presigned URLs per part; client manages parts and completes.

**Q. SSE-S3 vs SSE-KMS?**
A. SSE-S3: AWS-managed key, simple. SSE-KMS: customer KMS key, audit trail, fine-grained access — costs extra per request.

## Related
- [[Object Storage]] · [[AWS]] · [[CDN|CDN]] · [[Terraform]]
