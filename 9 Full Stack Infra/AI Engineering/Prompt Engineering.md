---
tags: [ai, intermediate, pattern]
---

# Prompt Engineering

> Structuring inputs to LLMs to get reliable, targeted outputs. The cheap lever you pull before fine-tuning.

## Building blocks
- **System prompt** — role, behavior, constraints
- **User message** — the task
- **Few-shot examples** — show desired input/output pairs
- **Output format** — request JSON, XML tags, markdown
- **Chain-of-thought** — "think step by step" or scratchpad
- **Self-critique** — "list potential errors, then revise"

## Patterns
- **XML tagging** — `<context>...</context><question>...</question>` — Claude-style
- **Schema-first** — give JSON schema, ask to fill it
- **Reasoning + answer split** — `<thinking>…</thinking><answer>…</answer>`
- **Role priming** — "You are a senior engineer reviewing…"
- **Constraint enumeration** — "Output must: (1) ... (2) ..."
- **Negative examples** — "Do not include…"

## Real World Usage
- Code generation with style constraints
- Classification with confidence
- Summarization with target audience
- Search query expansion
- Tool routing (decide which function to call)

## Common Mistakes
- Vague tasks → hallucinated outputs
- No output format → free-form mess to parse
- Few-shot examples bleeding distribution into output
- Over-engineering prompts when a smaller model + RAG would do
- Treating prompt as code (no eval) → silent regressions

## Prerequisites
- [[AI Providers]] · [[AI SDK by Vercel]]

## What To Learn Next
- [[Evals]] · [[AI Agents]] · [[RAG]]

## Best Learning Resources

### Official Documentation
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

### Best YouTube Resource
- [Greg Kamradt — prompt engineering](https://www.youtube.com/c/GregKamradt)
- [Anthropic's Prompt Engineering Interactive Course (YouTube + repo)](https://github.com/anthropics/prompt-eng-interactive-tutorial)

### Best Free Course
- [Anthropic Interactive Tutorial (free, hands-on)](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/)

### Best Advanced Resource
- [Lilian Weng — Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
- [PromptingGuide.ai](https://www.promptingguide.ai/)

### Best Practice Project
Build a JSON-extractor that parses unstructured emails into `{ sender, intent, deadline }`. Iterate via evals on 30 labeled examples until ≥95% accuracy without fine-tuning.

### Recommended Order to Learn
1. Clear task + format
2. Few-shot examples
3. Chain-of-thought
4. Schema-first with Zod / JSON schema
5. Self-critique loops
6. Evals to measure improvements
7. Prompt management (version, test, deploy)

## Interview Questions
**Q. Why few-shot examples?**
A. They steer the model toward your distribution + format without retraining.

**Q. When does prompt engineering hit its ceiling?**
A. When even good prompts produce inconsistent results on a held-out eval; consider fine-tuning, better retrieval, or a stronger model.

## Related
- [[Evals]] · [[AI Agents]] · [[RAG]] · [[AI SDK by Vercel]]
