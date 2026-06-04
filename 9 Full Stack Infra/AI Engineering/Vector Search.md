---
tags: [infra, ai, intermediate]
---

# Vector Search

> Finding nearest vectors in a high-dimensional space. The retrieval step of RAG and semantic search.

## Why it matters
Naive `O(n)` distance over millions of vectors is too slow. ANN algorithms (HNSW, IVF) make it `O(log n)` with tiny accuracy loss.

## Algorithm cheat sheet
- **Flat (brute force)** — exact, slow at scale, simple to implement
- **IVF (Inverted File)** — partition vectors into Voronoi cells; search nearest cells
- **HNSW** — hierarchical small-world graph; navigation in log time
- **PQ (Product Quantization)** — compress vectors; trade accuracy for memory
- **ScaNN** — Google's approach, anisotropic quantization

## Knobs to tune
| Algorithm | Knobs                          | Notes                              |
| --------- | ------------------------------ | ---------------------------------- |
| HNSW      | `m`, `ef_construction`, `ef`   | Higher = better recall + slower    |
| IVF       | `nlist`, `nprobe`              | Train on representative sample     |
| Flat      | none                           | Best baseline for accuracy         |

## Hybrid search
Combine vector ANN with BM25 (lexical). Fuse via Reciprocal Rank Fusion (RRF) or weighted score. Massive recall improvement for technical/proper-noun queries.

## Reranking
Top-k=100 from ANN → cross-encoder reranker → top-10. Big quality win.

## Real World Usage
- RAG retrieval
- Product / image / audio recommendation
- Semantic-aware search bars
- Plagiarism / dedup

## Common Mistakes
- Choosing HNSW with default knobs and never tuning
- Pre-filter that dwarfs the index (e.g., narrow tenant) → poor recall
- Reranking 1000 candidates (latency explodes); 100 is standard
- Not benchmarking on your own data — public leaderboards mislead

## Prerequisites
- [[Embeddings]] · [[Vector Databases]]

## What To Learn Next
- [[RAG]] · [[pgvector]] · [[Turbopuffer]]

## Best Learning Resources

### Official Documentation
- [Pinecone Learn — ANN algorithms](https://www.pinecone.io/learn/series/faiss/)
- [Weaviate docs — vector index](https://weaviate.io/developers/weaviate/concepts/vector-index)
- [FAISS wiki](https://github.com/facebookresearch/faiss/wiki)

### Best YouTube Resource
- [James Briggs — ANN walkthroughs](https://www.youtube.com/@jamesbriggs)
- [Hussein Nasser — vector indexes](https://www.youtube.com/@hnasr)

### Best Free Course
- [Pinecone — Faiss series](https://www.pinecone.io/learn/series/faiss/) — free articles + videos

### Best Advanced Resource
- [HNSW paper (Malkov & Yashunin)](https://arxiv.org/abs/1603.09320)
- [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — accuracy-boosting tricks
- [BEIR benchmark](https://github.com/beir-cellar/beir) — evaluate retrievers

### Best Practice Project
On 100k chunks, benchmark recall@10 + latency for: pgvector HNSW, pgvector IVFFlat, brute-force, and Qdrant HNSW. Add hybrid (BM25 + vector) and a Cohere rerank step. Plot accuracy/latency Pareto curves.

### Recommended Order to Learn
1. Brute-force k-NN baseline
2. IVF vs HNSW tradeoffs
3. Knob tuning (ef, nlist, nprobe)
4. Hybrid search (BM25 + vector)
5. Reranking
6. Evaluation (recall, MRR)

## Interview Questions
**Q. Why ANN instead of exact?**
A. Exact = O(n × dim). ANN trades <1% recall for orders-of-magnitude speedup.

**Q. Why does recall drop under heavy filtering?**
A. ANN graphs assume vectors are dense; filtering removes nodes mid-traversal. Implementations use post-filter or pre-filter strategies with tradeoffs.

**Q. How does Reciprocal Rank Fusion work?**
A. Score = Σ 1/(k + rank_in_each_list). No score-normalization headache; works across heterogeneous rankers.

## Related
- [[Embeddings]] · [[Vector Databases]] · [[RAG]] · [[pgvector]] · [[Turbopuffer]]
