---
tags: [ai, advanced, frontend]
---

# Generative UI

> The model doesn't just return text — it returns *which React component to render* and with what props. Combines streaming + tool calling + RSC.

## The idea
```
User: "Show me weekly sales"
LLM: → emits a tool call → server runs query → returns <BarChart data={...} />
```
The chat surface renders a real, interactive component instead of a markdown table.

## Stack (Vercel AI SDK pattern)
```tsx
// app/api/chat/route.ts
import { streamUI } from 'ai/rsc';
import { openai } from '@ai-sdk/openai';
import { z } from 'zod';

const result = await streamUI({
  model: openai('gpt-5'),
  prompt,
  tools: {
    weeklySales: {
      description: 'Show a weekly sales chart',
      parameters: z.object({ weeks: z.number().min(1).max(12) }),
      generate: async ({ weeks }) => {
        const data = await getSales(weeks);
        return <SalesChart data={data} />;
      },
    },
  },
});
```

## Patterns
- **Tool → component map** — each tool returns a JSX node
- **Streaming text + components** — `streamUI` interleaves
- **Server-rendered tool output** — keeps client bundle tiny
- **Conversation history** — store tool calls + results, not raw JSX

## Real World Usage
- AI copilots inside SaaS dashboards (Linear, Vercel)
- Conversational search where results are rich cards
- AI commerce assistants returning product cards
- Education assistants returning interactive widgets

## Common Mistakes
- Returning JSX with closures that don't serialize across the RSC boundary
- Re-running expensive tools on every render (memoize / cache)
- Letting the model choose between 50 tools without descriptions → poor routing
- No fallback when tool fails → blank component
- Mixing client-only components into the RSC return tree without `'use client'` boundaries

## Prerequisites
- [[AI SDK by Vercel]] · [[React Server Components]] · [[Next.js App Router]]

## What To Learn Next
- [[AI Agents]] · [[Streaming and Suspense]]

## Best Learning Resources

### Official Documentation
- [Vercel AI SDK — Generative UI](https://sdk.vercel.ai/docs/ai-sdk-rsc)
- [Next.js — Server Components + AI](https://nextjs.org/docs)

### Best YouTube Resource
- [Theo — Generative UI demos](https://www.youtube.com/@t3dotgg)
- [Lee Robinson — RSC + AI](https://www.youtube.com/@leerob)

### Best Free Course
- [Vercel AI SDK getting started](https://sdk.vercel.ai/docs/getting-started/nextjs-app-router)

### Best Advanced Resource
- [Vercel AI templates repo](https://github.com/vercel/ai-chatbot)

### Best Practice Project
Build a "data assistant" — accepts natural language, decides between `<Table>` / `<BarChart>` / `<KPI>` / `<List>` via tools, streams the right one back. Add an `error.tsx` fallback per route segment.

### Recommended Order to Learn
1. Streaming text responses
2. Tool calling basics
3. `streamUI` returning JSX from a tool
4. Multiple tools + routing
5. Component caching across messages
6. Combining with [[Streaming and Suspense]]

## Interview Questions
**Q. Why ship rendered components instead of JSON + client render?**
A. Smaller client bundle, server has access to data + auth, simpler client glue.

**Q. How does the tool output reach the client?**
A. Through the AI SDK's RSC payload — same mechanism as any RSC tree.

## Related
- [[AI SDK by Vercel]] · [[React Server Components]] · [[AI Agents]] · [[Streaming and Suspense]]
