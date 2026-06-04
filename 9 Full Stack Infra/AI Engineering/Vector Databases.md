---
tags: [infra, database, ai, advanced]
---

# Vector Databases

> Databases optimized for similarity search over high-dimensional vectors (embeddings).

## Why it matters
Embeddings power semantic search, RAG, recommendation, and image/audio search. Vector DBs make k-NN search fast at scale.

## Core ideas
- **Embedding** — fixed-length vector representing text/image/audio meaning
- **Distance** — cosine, Euclidean, dot product
- **ANN** — Approximate Nearest Neighbors (HNSW, IVF, ScaNN) trade tiny accuracy for huge speed
- **Hybrid search** — combine vector + keyword (BM25) for best results
- **Filters** — pre-filter or post-filter by metadata (e.g., user_id)

## Options
| Tool         | Hosted | Open source | Notes                                       |
| ------------ | ------ | ----------- | ------------------------------------------- |
| Pinecone     | Yes    | No          | Managed, easy                               |
| Weaviate     | Both   | Yes         | Schema, hybrid                              |
| Qdrant       | Both   | Yes         | Rust, fast, filter-friendly                 |
| Milvus       | Both   | Yes         | Large-scale                                 |
| pgvector     | —      | Yes         | Postgres extension — see [[pgvector]]       |
| Turbopuffer  | Yes    | No          | Object-storage-backed — see [[Turbopuffer]] |
| Chroma       | Both   | Yes         | DX-focused, good for prototypes             |

## Real World Usage
- RAG over docs (chat-with-docs)
- Semantic product search
- Image similarity / dedup
- Recommendation systems
- Anomaly detection

## Common Mistakes
- Choosing distance metric inconsistent with your model (most OpenAI/Cohere = cosine)
- Pre-filtering aggressively destroys ANN graphs — read your DB's filter strategy
- Forgetting normalization when using dot-product as cosine
- Reindexing every change — use incremental
- Treating vector DB as the source of truth (it isn't; keep canonical store)

## Prerequisites
- [[Embeddings]] · [[Database Indexing|Database Indexing]]

## What To Learn Next
- [[pgvector]] · [[Vector Search]] · [[RAG]] · [[Turbopuffer]]

## Best Learning Resources

### Official Documentation
- [Pinecone Learning Center](https://www.pinecone.io/learn/) — best pedagogy for vector concepts
- [Weaviate docs](https://weaviate.io/developers/weaviate)
- [Qdrant docs](https://qdrant.tech/documentation/)

### Best YouTube Resource
- [James Briggs — Pinecone YouTube](https://www.youtube.com/@jamesbriggs) — practical RAG + vector DB
- [Greg Kamradt — RAG/Vector channels](https://www.youtube.com/c/GregKamradt)

### Best Free Course
- [Pinecone — Embeddings and Vector Databases (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/) — free
- [Weaviate Academy](https://weaviate.io/developers/academy) — interactive

### Best Advanced Resource
- [HNSW paper](https://arxiv.org/abs/1603.09320) — original ANN graph algorithm
- [FAISS docs](https://faiss.ai/) — Meta's vector search library

### Best Practice Project
Build a "chat with my notes" app: load Markdown, chunk + embed (OpenAI/Cohere), store in pgvector or Qdrant, then a Next.js chat UI that retrieves top-k chunks and feeds them to an LLM with citations.

### Recommended Order to Learn
1. Embeddings concept + distance metrics
2. ANN algorithms (HNSW, IVF)
3. Choose tool (pgvector for relational, dedicated DB for scale)
4. Hybrid search
5. Production: filtering, sharding, reindexing

## Interview Questions
**Q. Why approximate, not exact, nearest neighbor?**
A. Exact k-NN at billions of vectors is intractable. ANN trades <1% accuracy for orders-of-magnitude speed.

**Q. When pgvector vs dedicated vector DB?**
A. pgvector when data fits in Postgres and you want one DB. Dedicated when scale, query latency, or features (hybrid, multi-tenant) matter.

**Q. Why hybrid search?**
A. Pure vector misses keyword precision (rare names, identifiers). BM25 + vector + reranker beats either alone.

**Q. What is reranking?**
A. Run a cheap retriever to get 100 candidates, then a stronger cross-encoder to score top-10. Big quality boost.

## Related
- [[Embeddings]] · [[Vector Search]] · [[pgvector]] · [[RAG]]
