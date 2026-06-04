---
tags: [infra, ai, intermediate]
---

# Embeddings

> Fixed-length numerical vectors that capture semantic meaning of text/image/audio. Similar inputs → similar vectors.

## Why it matters
Foundation of semantic search, RAG, recommendations, dedup, classification.

## Core ideas
- **Dimension** — 384 (small) to 3072 (large)
- **Distance** — cosine (most common), Euclidean, dot
- **Models** — `text-embedding-3-small` / `-large`, Voyage, Cohere, Gemini, BGE, Jina
- **Tokenization** — input is tokenized (BPE) before embedding; long inputs are chunked
- **Normalization** — unit-length vectors → cosine == dot product

## Example
```ts
import { embed, embedMany } from 'ai';
import { openai } from '@ai-sdk/openai';

const { embedding } = await embed({
  model: openai.embedding('text-embedding-3-small'),
  value: 'How does pgvector work?',
});

const { embeddings } = await embedMany({
  model: openai.embedding('text-embedding-3-small'),
  values: ['doc 1', 'doc 2', 'doc 3'],
});
```

## Real World Usage
- Vector search (RAG, semantic search)
- Recommendation ("similar to this product")
- Clustering, dedup
- Classification (embed + nearest centroid)
- Multimodal search (CLIP-style)

## Common Mistakes
- Mixing different models in same index (incompatible spaces)
- Forgetting to chunk long inputs (truncation silent in some APIs)
- Comparing un-normalized vectors with cosine assumption
- Re-embedding on every query in a hot path (cache!)
- Ignoring matryoshka / dimension truncation (newer models support fewer dims)

## Prerequisites
- Basic linear algebra intuition

## What To Learn Next
- [[Vector Databases]] · [[Vector Search]] · [[RAG]] · [[pgvector]]

## Best Learning Resources

### Official Documentation
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings) — clearest intro
- [Cohere Embed docs](https://docs.cohere.com/docs/embeddings)
- [Voyage AI docs](https://docs.voyageai.com/)

### Best YouTube Resource
- [3Blue1Brown — vector embeddings](https://www.youtube.com/c/3blue1brown) — intuition
- [James Briggs — embedding tutorials](https://www.youtube.com/@jamesbriggs)

### Best Free Course
- [Hugging Face — Sentence Transformers tutorial](https://huggingface.co/learn) — free
- [DeepLearning.AI — Embeddings short course](https://www.deeplearning.ai/short-courses/)

### Best Advanced Resource
- [Sentence Transformers paper + docs](https://www.sbert.net/) — open-source family
- [MTEB leaderboard (Hugging Face)](https://huggingface.co/spaces/mteb/leaderboard) — pick the right model
- [Matryoshka embeddings paper + post](https://huggingface.co/blog/matryoshka)

### Best Practice Project
Build a duplicate-detector: embed thousands of news headlines, find near-duplicates with cosine threshold > 0.9. Compare different models from MTEB leaderboard for accuracy and cost.

### Recommended Order to Learn
1. Token → vector intuition
2. Distance metrics + normalization
3. Picking a model (MTEB leaderboard)
4. Storing in vector DB
5. Hybrid + reranking
6. Multimodal embeddings (CLIP)

## Interview Questions
**Q. What does an embedding represent?**
A. A point in high-dim space where similar inputs cluster together — encoding semantic meaning learned from a model's training.

**Q. Cosine vs Euclidean?**
A. Cosine measures angle (orientation); insensitive to magnitude. Euclidean measures distance. For normalized vectors they're equivalent (up to monotonic transform).

**Q. Why use the smallest embedding dimension that works?**
A. Storage + ANN speed scale with dimension; larger isn't always better.

**Q. Why must production indexes use ONE model?**
A. Vectors from different models live in incompatible spaces; distances are meaningless across them.

## Related
- [[Vector Databases]] · [[Vector Search]] · [[RAG]] · [[pgvector]]
