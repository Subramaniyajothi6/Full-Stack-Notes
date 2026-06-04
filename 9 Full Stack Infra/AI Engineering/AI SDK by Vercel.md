---
tags: [infra, ai, intermediate]
---

# AI SDK by Vercel

> TypeScript-first toolkit for building AI apps. Provider abstraction (OpenAI, Anthropic, Google, etc.), streaming, structured outputs, tool calling, RSC integration.

## Why it matters
Standardizes the LLM wiring for React/Next apps. Avoid provider lock-in; swap models with a one-line change. Battle-tested streaming + tool-calling integrations.

## Core ideas
- **`ai` package** — core: `generateText`, `streamText`, `generateObject`, `streamObject`, `tool`
- **Providers** — `@ai-sdk/openai`, `@ai-sdk/anthropic`, `@ai-sdk/google`, etc.
- **`useChat` / `useCompletion`** — React hooks for streaming UIs
- **Structured outputs** — Zod schemas → typed JSON
- **Tools** — model can call functions, you implement them
- **AI SDK UI / RSC** — generative UI from server components

## Example
```ts
import { openai } from '@ai-sdk/openai';
import { generateText, streamText, tool } from 'ai';
import { z } from 'zod';

const { text } = await generateText({
  model: openai('gpt-5'),
  prompt: 'Summarize:\n' + doc,
});

// streaming
const { textStream } = streamText({ model: openai('gpt-5'), prompt });
for await (const chunk of textStream) process.stdout.write(chunk);

// tool calling
await generateText({
  model: openai('gpt-5'),
  tools: {
    weather: tool({
      description: 'Get weather',
      parameters: z.object({ city: z.string() }),
      execute: async ({ city }) => fetch(`...`).then(r => r.json()),
    }),
  },
  prompt: 'Weather in NYC?',
});
```

## Real World Usage
- ChatGPT clones with custom data
- AI assistants with tool access (search, DB, file ops)
- Generative UI (LLM picks which React component to render)
- Background AI workflows (agents)

## Common Mistakes
- Forgetting to stream → poor UX on long responses
- No `maxTokens` / rate limit → blown bills
- Embedding secrets client-side
- Validating tool args with hand-written checks instead of Zod
- Ignoring abort signals — costs $ on canceled requests

## Prerequisites
- [[Promises|Promises]] · [[Next.js App Router]] · [[useEffect|useEffect]]

## What To Learn Next
- [[AI Agents]] · [[RAG]] · [[Embeddings]]

## Best Learning Resources

### Official Documentation
- [Vercel AI SDK Docs](https://sdk.vercel.ai/docs) — best-in-class
- [AI SDK examples on GitHub](https://github.com/vercel/ai/tree/main/examples)

### Best YouTube Resource
- [Theo (t3.gg) — AI SDK videos](https://www.youtube.com/@t3dotgg)
- [Lee Robinson — Vercel + AI](https://www.youtube.com/@leerob)
- [Jack Herrington — AI SDK builds](https://www.youtube.com/@jherr)

### Best Free Course
- [Build a generative UI app — Vercel tutorial](https://sdk.vercel.ai/docs/getting-started/nextjs-app-router)

### Best Advanced Resource
- [Vercel AI SDK source on GitHub](https://github.com/vercel/ai)
- [Vercel Engineering blog — AI posts](https://vercel.com/blog)

### Best Practice Project
Build a "chat with PDF" app: upload PDF → chunk + embed (`@ai-sdk/openai`) → store in pgvector → `useChat` UI streaming with tool calling for "search-document" + "list-pages." Add abort controls + token budgeting per user.

### Recommended Order to Learn
1. `generateText` / `streamText` basics
2. `useChat` + streaming UI
3. Structured outputs with Zod
4. Tool calling
5. RAG integration
6. Generative UI (RSC + AI)
7. Agent patterns

## Interview Questions
**Q. Why use the AI SDK over calling OpenAI directly?**
A. Provider abstraction, streaming primitives, type-safe structured outputs, framework-friendly hooks, tool-calling helpers.

**Q. How does it handle streaming?**
A. Returns an async iterator and a server response stream; `useChat` plumbs it into React state with `useSyncExternalStore`-style updates.

**Q. What is structured output?**
A. Forcing the model to produce JSON conforming to a schema (Zod). The SDK retries / repairs on parse failures.

**Q. Provider routing — switching models?**
A. Replace the provider import; same call shape across providers (with provider-specific options when needed).

## Related
- [[AI Agents]] · [[RAG]] · [[Next.js App Router]] · [[Embeddings]]
