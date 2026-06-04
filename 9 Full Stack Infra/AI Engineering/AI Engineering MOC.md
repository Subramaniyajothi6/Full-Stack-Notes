---
tags: [moc, ai-engineering]
---

# AI Engineering MOC

> Building products on top of LLMs: SDKs, agents, retrieval, embeddings, providers, evals, observability.

## SDKs + agents
- [[AI SDK by Vercel]] — TS-first toolkit for streaming, tool calling, structured outputs
- [[AI Agents]] — loop, tools, memory, planning, evals

## Retrieval + RAG
- [[RAG]] — retrieve + augment + generate
- [[Embeddings]] — vector representations of meaning
- [[Vector Search]] — ANN algorithms, hybrid search, reranking
- [[Vector Databases]] — Pinecone, Weaviate, Qdrant, pgvector landscape
- [[Turbopuffer]] — object-storage-native vector DB

## Providers + landscape
- [[AI Providers]] — Anthropic, OpenAI, Google, Meta, xAI, etc.

## Prompting + quality
- [[Prompt Engineering]] — structuring inputs for reliable outputs
- [[Evals]] — measuring LLM quality
- [[Tracing and Observability]] — debugging + cost tracking
- [[Fine-tuning vs RAG]] — when to do each
- [[Guardrails]] — safety + prompt-injection defense

## Modern patterns
- [[Generative UI]] — model returns React components
- [[Multimodal LLMs]] — image / audio / video inputs and outputs

## Suggested order
1. [[AI Providers]] (mental map)
2. [[AI SDK by Vercel]] → first chat UI
3. [[Prompt Engineering]] → [[Evals]]
4. [[Embeddings]] → [[Vector Search]] → [[Vector Databases]] → [[RAG]]
5. [[AI Agents]] → [[Guardrails]] → [[Tracing and Observability]]
6. [[Generative UI]] → [[Multimodal LLMs]]
7. [[Fine-tuning vs RAG]] (when prompting + RAG isn't enough)

## Roadmap to fill in
- [ ] Streaming UIs deep dive
- [ ] Token + cost budgeting
- [ ] Persistent memory + summarization
- [ ] Reranking strategies (Cohere, Voyage, cross-encoders)
- [ ] Voice agents (Realtime APIs)
- [ ] Image generation (DALL-E, Imagen, Flux)
- [ ] Agent orchestration frameworks (LangGraph, Inngest agents)

## Related stacks
- [[NextJS MOC]] — RSC + AI SDK
- [[PostgreSQL MOC]] — pgvector for retrieval
- [[DevOps MOC]] — Sandboxing for agent code execution
- [[System Design MOC]] — caching, rate limits, queues

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
