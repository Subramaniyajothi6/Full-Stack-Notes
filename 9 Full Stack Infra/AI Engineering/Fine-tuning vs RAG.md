---
tags: [ai, advanced, concept]
---

# Fine-tuning vs RAG

> Two ways to make an LLM smarter about *your* domain. Pick by what kind of knowledge gap you have.

## Decision matrix
| Need                                  | Pick           |
|---------------------------------------|----------------|
| Fresh / changing facts                | RAG            |
| Style / format / persona consistency  | Fine-tuning    |
| Strict output schema                  | Fine-tuning (or schema-constrained decode) |
| Citations required                    | RAG            |
| Smaller / cheaper inference           | Fine-tuning    |
| Quick to iterate                      | RAG            |
| Don't want to retrain                 | RAG            |
| Need domain reasoning the base lacks  | Fine-tuning + RAG |

## Fine-tuning flavors
- **SFT** (supervised) — input → output pairs
- **DPO** (direct preference optimization) — preferred vs rejected pairs
- **LoRA / QLoRA** — efficient adapters, no full re-train
- **RLHF / RLAIF** — reward-model based (expensive, less common nowadays)

## RAG flavors
See [[RAG]] for the retrieval pipeline. Includes hybrid search, reranking, query rewriting.

## When to combine
Most production apps use RAG (for facts) + light fine-tuning (for tone, structure, refusals). You rarely choose one or the other in isolation.

## Cost model
- Fine-tuning: one-time training + slightly cheaper per-token inference (smaller model)
- RAG: more tokens per request (retrieved context) but no training cost; instant iteration

## Real World Usage
- Customer support — fine-tuned tone + RAG over knowledge base
- Code completion — fine-tuned on language, RAG over the repo
- Legal — RAG for citations, fine-tuned for terse style
- Medical — RAG for protocols, fine-tuned for safety refusals

## Common Mistakes
- Fine-tuning a base model on questions it could answer with prompt + retrieval
- Treating fine-tuning as "teach the model facts" — it learns patterns, not retrievable knowledge
- Fine-tuning before doing evals (you can't measure the gain)
- RAG over messy chunked data — pipeline > model
- Skipping the cheaper option ([[Prompt Engineering]]) first

## Prerequisites
- [[RAG]] · [[Prompt Engineering]] · [[Evals]] · [[AI Providers]]

## What To Learn Next
- [[Generative UI]] · [[Guardrails]]

## Best Learning Resources

### Official Documentation
- [OpenAI fine-tuning docs](https://platform.openai.com/docs/guides/fine-tuning)
- [Anthropic — when to use fine-tuning](https://docs.anthropic.com/)
- [Together AI fine-tuning](https://docs.together.ai/docs/fine-tuning-overview)

### Best YouTube Resource
- [Trelis Research — fine-tuning](https://www.youtube.com/@TrelisResearch)
- [Maxime Labonne — LLM fine-tuning](https://www.youtube.com/@maximelabonne)

### Best Free Course
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) — covers fine-tuning
- [Maxime Labonne LLM course (GitHub)](https://github.com/mlabonne/llm-course)

### Best Advanced Resource
- [Anyscale / Together engineering blogs](https://www.anyscale.com/blog) — production fine-tuning
- [Sebastian Raschka — Build a LLM from Scratch](https://sebastianraschka.com/) — deep ML background

### Best Practice Project
Take a customer-support dataset. (1) Try RAG only — measure on eval set. (2) Try LoRA fine-tuning Llama with the dataset — re-measure. (3) Combine and re-measure. Document cost + quality tradeoffs.

### Recommended Order to Learn
1. Prompt engineering first
2. Naive RAG
3. RAG + reranking
4. LoRA fine-tuning small model
5. DPO with preference data
6. Continuous evals across the matrix

## Interview Questions
**Q. Will fine-tuning teach the model my private data?**
A. Imperfectly — it learns patterns. RAG is better for retrievable facts. Combine for best results.

**Q. LoRA — what is it?**
A. Low-Rank Adapters; trains small adapter layers instead of all model weights. ~99% cheaper, often comparable results.

**Q. When fine-tune over RAG?**
A. Style / persona consistency, refusal patterns, schema adherence, latency-critical paths where the smaller fine-tuned model wins.

## Related
- [[RAG]] · [[Prompt Engineering]] · [[Evals]] · [[AI Providers]]
