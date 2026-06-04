---
tags: [infra, ai, intermediate]
---

# RAG

> Retrieval-Augmented Generation — retrieve relevant context from your data and feed it to an LLM at query time.

## Why it matters
LLMs don't know your private docs and have stale knowledge. RAG injects fresh, relevant context per query — avoiding fine-tuning and giving citations.

## Core flow
1. **Ingest** — load + chunk + embed your data, store in vector DB
2. **Retrieve** — embed query, search top-k from vector DB (+ keyword)
3. **Rerank** (optional) — cross-encoder ranks top-100 → top-10
4. **Augment** — add retrieved chunks to the LLM prompt
5. **Generate** — LLM answers, cites sources

## Better-than-naive techniques
- **Hybrid search** — vector + BM25
- **Query rewriting** — LLM rewrites the query for retrieval
- **Multi-query** — generate variants, fuse results (RRF)
- **Reranking** — Cohere Rerank, Voyage rerank, BGE
- **Chunking** — sentence-aware, recursive, semantic chunks (not fixed-size)
- **Metadata filters** — user_id, doc_type
- **Citations** — return chunk ids alongside answer

## Real World Usage
- Chat with docs / wiki / codebase
- Customer support over knowledge base
- Legal / medical / research assistants
- Personal knowledge agents

## Common Mistakes
- Tiny chunks (<200 tokens) — lose context
- Huge chunks (>2k tokens) — recall drops
- Vector-only — keyword precision lost; use hybrid
- No reranking — top-k of pure ANN is noisy
- No eval set — improvements are guesses
- Stuffing all retrieved text — exceeds context window or distracts model

## Prerequisites
- [[Embeddings]] · [[Vector Databases]] · [[AI SDK by Vercel]]

## What To Learn Next
- [[AI Agents]] · [[Vector Search]] · [[pgvector]] · [[Turbopuffer]]

## Best Learning Resources

### Official Documentation
- [Pinecone — RAG guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- [LlamaIndex docs](https://docs.llamaindex.ai/) — RAG framework
- [LangChain RAG cookbook](https://python.langchain.com/docs/use_cases/question_answering/)

### Best YouTube Resource
- [Greg Kamradt — RAG playlists](https://www.youtube.com/c/GregKamradt) — best practical channel
- [James Briggs](https://www.youtube.com/@jamesbriggs) — Pinecone-led RAG videos
- [LangChain channel](https://www.youtube.com/@LangChain)

### Best Free Course
- [DeepLearning.AI — Building Applications with Vector Databases](https://www.deeplearning.ai/short-courses/) — free
- [Pinecone Learn — Hierarchy of RAG](https://www.pinecone.io/learn/) — articles

### Best Advanced Resource
- [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — chunk enrichment
- [Cohere — Rerank docs + papers](https://docs.cohere.com/docs/rerank-overview)
- [LlamaIndex — Advanced RAG patterns](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)

### Best Practice Project
"Chat with my notes": ingest a folder of markdown, smart-chunk + embed, store in [[pgvector]], implement hybrid search + Cohere rerank, build a Next.js chat with citations. Add an eval harness with 30 Q/A pairs and track recall@k.

### Recommended Order to Learn
1. Naive RAG (load → chunk → embed → search → answer)
2. Better chunking + metadata filters
3. Hybrid search
4. Reranking
5. Query rewriting + multi-query
6. Evals (RAGAS, custom)

## Interview Questions
**Q. Why RAG over fine-tuning?**
A. Faster, cheaper, fresh data, citations, no retraining when data changes.

**Q. Why does pure vector search fail?**
A. Misses keyword precision (rare names, codes). Hybrid + rerank fixes this.

**Q. How do you measure RAG quality?**
A. Recall@k for retrieval; faithfulness, answer relevance, context relevance for generation. RAGAS or custom evals.

**Q. Chunk size — how to choose?**
A. Trade-off: small chunks = precise retrieval, may lose context; large chunks = more context, recall suffers. Start ~500 tokens with overlap.

## Related
- [[Embeddings]] · [[Vector Databases]] · [[AI Agents]] · [[AI SDK by Vercel]]
