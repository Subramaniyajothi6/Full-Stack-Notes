---
tags: [ai, advanced, quality]
---

# Evals

> Tests for LLM outputs. The only way to know whether a prompt or model change made things better or worse.

## What an eval is
A held-out set of `(input, expected_output)` pairs plus a scoring function. Run model → score → aggregate.

## Scoring methods
- **Exact match** / regex — for structured outputs
- **String similarity** (BLEU, ROUGE) — translation/summary
- **Embedding similarity** — semantic
- **LLM-as-judge** — another model scores; cheap + scalable
- **Human ratings** — gold standard for subjective tasks
- **Trajectory eval** (for agents) — was the right tool called?

## RAGAS-style metrics
- **Faithfulness** — answer grounded in retrieved context
- **Answer relevance**
- **Context precision / recall**

## Tools
- **Braintrust** — managed eval platform
- **Langfuse / Helicone / LangSmith** — tracing + evals
- **promptfoo** — open-source, CLI-driven
- **Evidently** — model monitoring
- Custom: just Python/TS scripts running through your harness

## Real World Usage
- Regression gating in CI — prompt change can't ship unless evals pass
- A/B testing models (Claude vs GPT) on your tasks
- Continuous monitoring of production quality
- Selecting between RAG configurations

## Common Mistakes
- Eval set too small → noise > signal
- Eval set drawn from training-set distribution → over-optimistic
- LLM-as-judge using the same model that generated the answer (collusion)
- No baseline → "improvements" without comparison
- Confusing unit tests with evals (deterministic vs probabilistic)
- Evaluating only happy path

## Prerequisites
- [[Prompt Engineering]] · [[AI Providers]]

## What To Learn Next
- [[Tracing and Observability]] · [[Fine-tuning vs RAG]]

## Best Learning Resources

### Official Documentation
- [Anthropic Evals Cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/misc)
- [OpenAI Evals repo](https://github.com/openai/evals)
- [Braintrust docs](https://www.braintrust.dev/docs)

### Best YouTube Resource
- [Hamel Husain — Evals talks](https://www.youtube.com/results?search_query=hamel+husain+evals)
- [Latent Space podcast — eval episodes](https://www.youtube.com/c/LatentSpace)

### Best Free Course
- [Hamel Husain — A Field Guide to AI Engineering Evals](https://hamel.dev/blog/posts/evals/) — gold-tier writeup
- [DeepLearning.AI — Building Evaluations of LLM Apps](https://www.deeplearning.ai/short-courses/)

### Best Advanced Resource
- [RAGAS docs + paper](https://docs.ragas.io/)
- [Eugene Yan — eval patterns](https://eugeneyan.com/writing/)

### Best Practice Project
Build a 50-question eval set for a RAG app. Compare two retrieval strategies (BM25 vs hybrid). Score with recall@k + LLM-judged faithfulness. Document which wins and why.

### Recommended Order to Learn
1. Hand-crafted eval set + exact-match scoring
2. LLM-as-judge with calibration
3. RAGAS metrics for retrieval
4. Continuous eval in CI
5. Production monitoring + drift detection
6. Trajectory evals for agents

## Interview Questions
**Q. Why are LLM outputs hard to test?**
A. Non-deterministic, free-form text, judgment-based correctness. Hence eval ≠ unit test.

**Q. LLM-as-judge — what are its risks?**
A. Bias toward verbose outputs, agreement bias when judge == generator, length bias. Calibrate against humans periodically.

**Q. How do you avoid eval drift?**
A. Version eval sets, hold out a "gold" set you never optimize against.

## Related
- [[Prompt Engineering]] · [[Tracing and Observability]] · [[RAG]] · [[Fine-tuning vs RAG]]
