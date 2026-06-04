---
tags: [infra, ai, advanced]
---

# AI Agents

> LLM-driven systems that take goals, plan multi-step actions, call tools, and iterate based on observations.

## Why it matters
Agents power code-writing assistants, research tools, automation workflows. Designing them well (loops, tools, evals, guardrails) is the new app-engineering frontier.

## Core ideas
- **Tool use** — LLM emits structured tool calls; runtime executes; result feeds back
- **Loop** — Observe → Reason → Act → Repeat (until terminal step)
- **Memory** — short-term (in-context) + long-term (vector store)
- **Planning** — LLM produces plan; executor runs it (chain-of-thought, ReAct, plan-and-execute)
- **Multi-agent** — orchestrator delegates to specialist agents
- **Guardrails** — sandboxes, rate limits, content filters, max steps

## Architectures
- Single-agent loop (most common: Claude Code, Cursor, AI SDK)
- Plan-and-execute (planner → workers)
- Multi-agent (manager + specialists)
- Self-reflective (critic loop)

## Example (AI SDK shape)
```ts
const result = await generateText({
  model: openai('gpt-5'),
  tools: { search, readFile, runShell },
  toolChoice: 'auto',
  maxSteps: 10,
  prompt: userGoal,
});
```

## Real World Usage
- AI coding assistants (Cursor, Cline, Claude Code, Devin)
- Research agents (Perplexity, You.com, Tavily-based)
- Customer support agents
- Browser-driving agents (Browserbase, Operator)

## Common Mistakes
- Unbounded loops → cost explosions; always cap `maxSteps` and budgets
- Tools without [[Sandboxing]] → arbitrary RCE
- Treating retries as a fix for ambiguous prompts (improve prompt)
- No evals → no idea if a refactor regressed quality
- Letting agent see/modify its own prompt without care

## Prerequisites
- [[AI SDK by Vercel]] · [[RAG]]

## What To Learn Next
- [[Sandboxing]] · [[Remote Code Execution]] · [[Firecracker]]

## Best Learning Resources

### Official Documentation
- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents) — best agent design overview
- [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents) — official patterns
- [Vercel AI SDK — agents](https://sdk.vercel.ai/docs/ai-sdk-core/tools-and-tool-calling)

### Best YouTube Resource
- [Theo — agent videos](https://www.youtube.com/@t3dotgg)
- [Greg Kamradt — agent walk-throughs](https://www.youtube.com/c/GregKamradt)
- [LangChain channel](https://www.youtube.com/@LangChain)

### Best Free Course
- [DeepLearning.AI — short courses on Agents](https://www.deeplearning.ai/short-courses/) — free
- [Anthropic cookbooks (agents)](https://github.com/anthropics/anthropic-cookbook)

### Best Advanced Resource
- [Anthropic engineering blog — building Claude](https://www.anthropic.com/research)
- [Lilian Weng — LLM Agents (blog)](https://lilianweng.github.io/) — academic depth
- [Sweep / Cursor / Cline GitHub repos](https://github.com/getcursor) — read production loops

### Best Practice Project
Build a research agent that takes a question, plans search queries, calls a web search tool, reads pages, and synthesizes a cited answer. Add: max-steps cap, per-question budget, eval suite of 20 questions with expected citations.

### Recommended Order to Learn
1. Tool calling
2. Single-loop agents
3. Memory + scratchpad
4. Sandboxing dangerous tools
5. Evals + tracing
6. Multi-agent orchestration

## Interview Questions
**Q. Why does an agent need a max-step limit?**
A. LLMs can loop indefinitely on hard tasks → unbounded cost. Hard cap protects users and your budget.

**Q. How do you handle tool failures?**
A. Return error to model in conversation; model can retry, change approach, or admit failure.

**Q. ReAct vs plan-and-execute?**
A. ReAct interleaves reasoning + acting per step. Plan-and-execute makes a full plan first, then runs it; often more controllable, less adaptive.

**Q. How do you eval an agent?**
A. Curated test set; run agent; check outcomes (final answer or trajectory). Use traces (Langfuse, Helicone) and LLM-as-judge for soft metrics.

## Related
- [[AI SDK by Vercel]] · [[RAG]] · [[Sandboxing]] · [[Firecracker]]
