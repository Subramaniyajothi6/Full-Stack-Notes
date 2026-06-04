---
tags: [ai, advanced, observability]
---

# Tracing and Observability (AI)

> Every LLM call, tool invocation, and retrieval step recorded — so you can debug, eval, and price.

## What to capture per request
- Input prompt + messages
- Model + parameters (temp, top_p, max_tokens)
- Output tokens + finish reason
- Latency + token usage + cost
- Tool calls + outputs (for agents)
- Retrieval candidates + chosen chunks (for RAG)
- Trace tree across nested calls

## Tools
- **Langfuse** — open-source, self-hostable
- **Helicone** — drop-in proxy
- **LangSmith** — LangChain ecosystem
- **Braintrust** — eval + tracing combined
- **Arize Phoenix** — open-source, focused on LLM evals
- **OpenTelemetry GenAI** — emerging standard

## AI SDK + Langfuse example
```ts
import { generateText } from 'ai';
import { openai } from '@ai-sdk/openai';
import { langfuseTraceTool } from 'langfuse-vercel';

await generateText({
  model: openai('gpt-5'),
  prompt,
  experimental_telemetry: { isEnabled: true, functionId: 'summarize' },
});
```

## What to alert on
- p95 latency creep
- Error rate spikes
- Cost per request rising
- Eval scores dropping
- Token-usage outliers (prompt explosion bugs)

## Real World Usage
- Debugging "why did it hallucinate?"
- Tracking cost per feature, per user, per tenant
- Eval pipelines that replay production traces
- Compliance (audit trail for AI decisions)
- A/B testing model versions

## Common Mistakes
- Logging full prompts containing PII without redaction
- No sampling → 100% trace cost in prod
- Forgetting tool-call I/O in traces (loses agent context)
- Treating traces as logs only (never doing eval replay)
- No alerts on cost — silent bill explosions

## Prerequisites
- [[AI SDK by Vercel]] · [[Evals]] · [[Logging Across Services]]

## What To Learn Next
- [[Fine-tuning vs RAG]] · [[AI Agents]]

## Best Learning Resources

### Official Documentation
- [Langfuse docs](https://langfuse.com/docs)
- [Helicone docs](https://docs.helicone.ai/)
- [Arize Phoenix docs](https://docs.arize.com/phoenix)
- [Vercel AI SDK Telemetry](https://sdk.vercel.ai/docs/ai-sdk-core/telemetry)

### Best YouTube Resource
- [Latent Space podcast — observability deep dives](https://www.youtube.com/c/LatentSpace)
- [Langfuse YouTube channel](https://www.youtube.com/@langfuse)

### Best Free Course
- [Langfuse cookbook on GitHub](https://github.com/langfuse/langfuse-docs)
- [Anthropic — Tracing in agents](https://docs.anthropic.com/)

### Best Advanced Resource
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

### Best Practice Project
Instrument an existing AI feature with Langfuse. Run for a week; identify top-5 cost contributors and top-3 latency offenders. Replay 10 failures into your eval suite.

### Recommended Order to Learn
1. Trace every LLM call
2. Capture tool I/O for agents
3. Token + cost tracking
4. Connect traces to evals
5. Alerts + dashboards
6. Replay production traces in dev

## Interview Questions
**Q. What's a trace for an agent?**
A. Tree of spans — top-level run, each tool call as a child span, each model call inside as a leaf. Lets you reconstruct the decision tree.

**Q. Why not just use plain logs?**
A. LLM debugging needs structured I/O, parent/child relationships, cost/latency in one view, and eval-friendly replay.

## Related
- [[Evals]] · [[AI SDK by Vercel]] · [[Logging Across Services]]
