---
tags: [infra, database, intermediate]
---

# Object Storage

> Storage of arbitrary blobs (objects) in flat keyspace, accessed via HTTP API. Cheap, durable, infinite-scale.

## Why it matters
Files don't belong in your database or your container's local disk. Object storage is the right place for images, videos, backups, ML datasets, and increasingly, vector indexes.

## Core ideas
- **Bucket** — a named container
- **Object** — bytes + metadata + key
- **Eventual consistency** — historically; S3 is now strong-read-after-write
- **Versioning** — store every version of an object
- **Lifecycle** — auto-tier (Standard → IA → Glacier) or expire
- **Durability** — typically 11 nines (99.999999999%)
- **Access** — IAM policies, presigned URLs, public read with signed CDN

## Implementations
- AWS S3, GCP Cloud Storage, Azure Blob — see [[AWS S3]]
- Cloudflare R2 — S3-compatible, no egress fees
- Backblaze B2 — cheap
- MinIO — self-host, S3 API

## Common operations
```ts
// Node v3 SDK example
import { S3Client, PutObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const s3 = new S3Client({ region: 'us-east-1' });

// presigned upload URL
const url = await getSignedUrl(s3, new PutObjectCommand({
  Bucket: 'uploads', Key: `u/${userId}/${file}`,
  ContentType: 'image/png'
}), { expiresIn: 60 });
```

## Real World Usage
- Media uploads (avatars, attachments) via presigned URLs
- Static site hosting
- Build artifacts + container layers
- Database backups
- Data lake storage (Parquet)
- Vector index storage ([[Turbopuffer]])

## Common Mistakes
- Public read on a bucket holding private data
- Server-side proxy uploads instead of presigned (wastes bandwidth + memory)
- No lifecycle policy → cost spirals
- Using object storage like a filesystem (listing folders is O(n))
- Forgetting CORS for browser uploads

## Prerequisites
- [[HTTP and HTTPS|HTTP & HTTPS]] · [[CDN|CDN]]

## What To Learn Next
- [[AWS S3]] · [[CDN]] · [[Turbopuffer]]

## Best Learning Resources

### Official Documentation
- [AWS S3 docs](https://docs.aws.amazon.com/s3/) — most thorough
- [Cloudflare R2 docs](https://developers.cloudflare.com/r2/)

### Best YouTube Resource
- [Hussein Nasser — S3 and object storage](https://www.youtube.com/@hnasr)
- [TechWorld with Nana — S3 essentials](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [AWS Skill Builder — S3 fundamentals](https://explore.skillbuilder.aws/) — free
- [Cloudflare Learning — Object storage](https://www.cloudflare.com/learning/cloud/what-is-object-storage/)

### Best Advanced Resource
- [Werner Vogels' All Things Distributed — S3 design posts](https://www.allthingsdistributed.com/) — CTO essays
- [MinIO blog](https://blog.min.io/) — implementation perspective

### Best Practice Project
Add file uploads to your app: presigned PUT URLs, image resizing via a Lambda triggered on `s3:ObjectCreated`, CDN in front of public reads, and a lifecycle rule that tiers old originals to cheaper storage after 30 days.

### Recommended Order to Learn
1. Bucket/object/key concepts
2. IAM policies + presigned URLs
3. Versioning + lifecycle
4. CDN integration
5. Multipart upload for large files
6. Eventing (object created/deleted)

## Interview Questions
**Q. Why upload via presigned URL instead of through your server?**
A. Server doesn't proxy bytes — saves CPU/memory/bandwidth. Client uploads directly to S3 with a time-limited credential.

**Q. Object storage vs filesystem?**
A. Object: flat keyspace, HTTP API, infinite scale, eventually-consistent listing. FS: hierarchical, low latency, finite, POSIX semantics.

**Q. Why is "list bucket" expensive?**
A. Implemented via a sorted index across distributed shards; no real folders. Avoid in hot paths.

**Q. How do CDNs and S3 work together?**
A. CDN caches at edge; origin is S3. Use signed CDN URLs for private content; configure cache headers in metadata.

## Related
- [[AWS S3]] · [[CDN|CDN]] · [[Turbopuffer]]
