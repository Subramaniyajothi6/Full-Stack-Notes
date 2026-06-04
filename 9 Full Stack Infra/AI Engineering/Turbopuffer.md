---
tags: [infra, database, ai, advanced]
---

# Turbopuffer

> Serverless vector + full-text search built directly on object storage (S3). Cheap, scalable, "pay for what you use."

## Why it matters
Traditional vector DBs require always-on compute and RAM proportional to dataset. Turbopuffer's "object-storage-native" architecture trades a bit of latency for dramatically lower cost — making vector search affordable at hobbyist scale and competitive at enterprise scale.

## Core ideas
- **Storage on S3 (or compatible)** — durable, cheap, infinitely scalable
- **Multi-tenant by default** — namespaces isolate workloads
- **Hybrid search** — vectors + BM25 in one query
- **Schema** — typed metadata + indexes
- **No always-on cluster** — stateless query nodes pull from object storage with smart caching

## Tradeoffs
- ✅ Cheap idle (no per-hour cluster)
- ✅ Scales to billions of vectors
- ✅ Simple ops
- ⚠️ Cold reads slower than RAM-resident DBs
- ⚠️ Hosted-only (no self-hosted release)

## Real World Usage
- AI products with bursty traffic (cheap idle)
- Multi-tenant SaaS with per-customer namespaces
- Use cases where dataset >>> RAM budget

## Common Mistakes
- Treating it like an always-hot cache — cold latency exists
- Over-tiny namespaces — they have overhead
- Skipping `attributes` schema — slower filters
- Using only vector when hybrid would help

## Prerequisites
- [[Vector Databases]] · [[Object Storage]] · [[AWS S3]]

## What To Learn Next
- [[RAG]] · [[Vector Search]]

## Best Learning Resources

### Official Documentation
- [turbopuffer.com docs](https://turbopuffer.com/docs) — concise, current
- [Architecture explainer on the company blog](https://turbopuffer.com/blog) — read first; explains why object-storage-native matters

### Best YouTube Resource
- Founder talks/podcast appearances — search "Simon Eskildsen turbopuffer" on YouTube

### Best Free Course
- The official docs are short enough to read end-to-end in an afternoon.

### Best Advanced Resource
- [Turbopuffer engineering blog](https://turbopuffer.com/blog) — postmortems, perf, multitenancy
- [Pinecone serverless launch posts (comparison context)](https://www.pinecone.io/blog/)

### Best Practice Project
Build the same RAG app twice: once with [[pgvector]], once with Turbopuffer. Measure cold/warm latency, monthly cost at 0/100/10k QPS, and ergonomics (schema migrations, tenant isolation).

### Recommended Order to Learn
1. Object-storage-as-primary architecture concept
2. Namespaces + tenancy
3. Schema + attribute indexes
4. Hybrid search
5. Cost modeling vs alternatives

## Interview Questions
**Q. Why use object storage instead of a hot RAM cluster?**
A. ~100x cheaper per GB; trades a bit of latency for huge cost savings, ideal for idle/bursty workloads.

**Q. Tradeoff vs pgvector?**
A. pgvector: one DB, transactional joins. Turbopuffer: better at very large datasets, multitenant, low idle cost.

**Q. How does it stay fast despite reading from S3?**
A. Aggressive caching of hot regions, smart prefetch, columnar layouts in object storage.

## Related
- [[Vector Databases]] · [[pgvector]] · [[Object Storage]] · [[AWS S3]]
