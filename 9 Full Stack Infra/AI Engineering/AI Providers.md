---
tags: [infra, ai, intermediate]
---

# AI Providers

> The companies/APIs that host LLMs you call. Knowing strengths, prices, and quirks lets you pick the right model per job.

## Major providers (May 2025 landscape)
| Provider     | Flagship models                | Strengths                                |
| ------------ | ------------------------------ | ---------------------------------------- |
| Anthropic    | Claude (Opus/Sonnet/Haiku)     | Reasoning, code, long context, agents    |
| OpenAI       | GPT-4o / GPT-5 / o-series       | Tooling ecosystem, image gen, voice      |
| Google       | Gemini Pro / Flash / 2.x        | Long context, native multimodal, price   |
| Meta         | Llama (open weights)           | Self-host friendly                       |
| Mistral      | Mistral, Codestral             | Open weights, EU                         |
| xAI          | Grok                           | Frontier scale, X integration            |
| DeepSeek     | DeepSeek                       | Cost-effective frontier-ish              |
| Cohere       | Command, Embed, Rerank         | RAG + reranking specialists              |

## Hosting / aggregators
- **OpenRouter** — single API, route across providers
- **Vercel AI Gateway / AI SDK** — abstraction layer, see [[AI SDK by Vercel]]
- **Bedrock (AWS)**, **Azure OpenAI**, **Vertex AI (GCP)** — enterprise hosting
- **Together / Fireworks / Groq / Replicate** — inference for OSS models
- **Anthropic Claude Platform**, **OpenAI Platform** — direct

## Choosing a model
- **Frontier reasoning / code** — Claude Opus, GPT-5, Gemini Pro
- **Cheap general** — Claude Haiku, GPT-4o-mini, Gemini Flash
- **Open weights / self-host** — Llama, Mistral, DeepSeek
- **Embeddings** — OpenAI `text-embedding-3-*`, Voyage, Cohere
- **Reranking** — Cohere Rerank, Voyage Rerank

## Real World Usage
- Multi-provider strategy (failover + cost optimization)
- Different models per task (cheap classify, expensive synthesize)
- On-prem / VPC hosting via Bedrock/Azure for compliance

## Common Mistakes
- Locking into one provider's SDK — use [[AI SDK by Vercel]]
- Ignoring rate limits, getting 429s in prod
- Same model for all tasks — overspending
- Sending PII to consumer APIs without DPA / compliance review

## Prerequisites
- [[AI SDK by Vercel]]

## What To Learn Next
- [[AI Agents]] · [[Embeddings]] · [[RAG]]

## Best Learning Resources

### Official Documentation
- [Anthropic API docs](https://docs.anthropic.com/)
- [OpenAI API docs](https://platform.openai.com/docs)
- [Google AI / Gemini docs](https://ai.google.dev/)
- [Vercel AI SDK provider list](https://sdk.vercel.ai/providers/ai-sdk-providers)

### Best YouTube Resource
- [Theo — provider comparisons](https://www.youtube.com/@t3dotgg)
- [Simon Willison — talks](https://www.youtube.com/results?search_query=simon+willison+llm)
- [Latent Space podcast](https://www.youtube.com/c/LatentSpace) — deeper provider analysis

### Best Free Course
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) — patterns
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

### Best Advanced Resource
- [Artificial Analysis](https://artificialanalysis.ai/) — independent model benchmarks + price
- [LMSYS Chatbot Arena](https://arena.lmsys.org/) — community ELO leaderboard
- [Simon Willison's blog](https://simonwillison.net/) — frequent model reviews

### Best Practice Project
Build a multi-provider chat with the AI SDK. Add a model picker (Claude Sonnet, GPT-5, Gemini Flash, Llama-3 via Together). Log latency, cost, and quality (LLM-as-judge eval) per model on the same prompts.

### Recommended Order to Learn
1. Pick one provider (Anthropic or OpenAI), get fluent
2. Embedding + reranking providers
3. Self-host via Together/Fireworks
4. Aggregators (OpenRouter, Bedrock)
5. Evals to drive routing

## Interview Questions
**Q. How do you avoid vendor lock-in?**
A. Abstract via SDK ([[AI SDK by Vercel]]), keep prompts portable, evaluate with provider-agnostic harness.

**Q. Open vs closed weights — when to use which?**
A. Closed = best frontier, easy ops. Open = self-host (privacy, cost at scale, fine-tuning).

**Q. What's a context window and why does it matter?**
A. Max tokens per request. Bigger window = more retrieved context but cost grows; recall sometimes drops past a model's effective window.

## Related
- [[AI SDK by Vercel]] · [[AI Agents]] · [[RAG]] · [[Embeddings]]
