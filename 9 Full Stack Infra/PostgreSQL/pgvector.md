---
tags: [infra, database, ai, intermediate]
---

# pgvector

> Postgres extension that adds a `vector` type and ANN indexes (IVFFlat, HNSW). Vector search inside your relational DB.

## Why it matters
Lets you keep one database. Joins between embeddings and your normal tables. Mature, ACID, backups same as everything else.

## Core ideas
- New type: `vector(N)` — fixed dimension
- Distance ops: `<->` L2, `<#>` negative inner product, `<=>` cosine distance
- Indexes:
  - **IVFFlat** — partition vectors into lists, scan top lists; needs `lists` parameter, fast build, good recall
  - **HNSW** — graph-based, higher recall, slower build, more memory
- Combine with normal `WHERE` filters

## Setup + example
```sql
CREATE EXTENSION vector;

CREATE TABLE docs (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT NOT NULL,
  body TEXT,
  embedding vector(1536)
);

CREATE INDEX docs_embed_idx ON docs USING hnsw (embedding vector_cosine_ops);

-- top 5 nearest for a user
SELECT id, body
FROM docs
WHERE user_id = $1
ORDER BY embedding <=> $2
LIMIT 5;
```

## Real World Usage
- RAG over user docs (one Postgres DB to rule them all)
- Semantic search inside SaaS products
- Multi-tenant chat-with-docs
- Hybrid search: BM25 (`tsvector`) + vector

## Common Mistakes
- Wrong distance op vs your embedding model (most use cosine `<=>`)
- Indexing without `ANALYZE` → planner confused
- Pre-filter blowing past `lists`/`ef_search` knobs → poor recall
- Storing very high-dimensional vectors without thinking about row size

## Prerequisites
- [[PostgreSQL]] · [[Embeddings]] · [[Vector Databases]]

## What To Learn Next
- [[Vector Search]] · [[RAG]] · [[Turbopuffer]]

## Best Learning Resources

### Official Documentation
- [pgvector GitHub README](https://github.com/pgvector/pgvector) — concise + complete
- [Supabase pgvector guide](https://supabase.com/docs/guides/ai)

### Best YouTube Resource
- [Supabase team — pgvector videos](https://www.youtube.com/c/Supabase)
- [Theo — RAG with pgvector](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Supabase AI tutorials](https://supabase.com/docs/guides/ai) — end-to-end recipes

### Best Advanced Resource
- [Crunchy Data blog — pgvector tuning](https://www.crunchydata.com/blog) — index choice + EXPLAIN
- [Neon blog — vector benchmarks](https://neon.tech/blog) — perf comparisons

### Best Practice Project
Take any 1000 markdown files, embed them with `text-embedding-3-small`, store in Supabase + pgvector, and build a Next.js search box with hybrid (BM25 + vector) results. Tune HNSW `m`/`ef_construction` for recall vs speed.

### Recommended Order to Learn
1. Install + basic vector type
2. IVFFlat vs HNSW
3. Distance operators
4. Index parameters (lists, m, ef_construction, ef_search)
5. Hybrid search with `tsvector`
6. Multi-tenant performance + filtering

## Interview Questions
**Q. IVFFlat vs HNSW — when which?**
A. IVFFlat: faster build, less memory, good for batch updates. HNSW: better recall, more memory, slower build.

**Q. Why pgvector instead of Pinecone?**
A. One DB simplifies ops; transactional consistency with relational data; cheaper at small/mid scale.

**Q. How do you do multi-tenant pgvector at scale?**
A. Per-tenant partitioning, keep `user_id` early in the index, monitor recall under filters; consider partitioned tables.

## Related
- [[PostgreSQL]] · [[Vector Databases]] · [[Embeddings]] · [[RAG]]
