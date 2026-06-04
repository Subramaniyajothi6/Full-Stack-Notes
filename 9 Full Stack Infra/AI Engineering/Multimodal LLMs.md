---
tags: [ai, advanced, concept]
---

# Multimodal LLMs

> Models that accept and/or emit images, audio, video alongside text.

## Capability matrix (May 2025)
| Provider          | Text | Image in | Image out | Audio in | Audio out | Video in |
|-------------------|------|----------|-----------|----------|-----------|----------|
| Anthropic Claude  | ✅   | ✅       | ❌        | ❌       | ❌        | ❌       |
| OpenAI GPT-4o     | ✅   | ✅       | ✅        | ✅       | ✅        | partial  |
| Google Gemini     | ✅   | ✅       | ✅        | ✅       | ✅        | ✅       |
| OSS (Llama 3 Vision) | ✅ | ✅      | ❌        | ❌       | ❌        | ❌       |

(Capabilities move fast — always check provider docs.)

## Image input
```ts
import { generateText } from 'ai';
const { text } = await generateText({
  model: anthropic('claude-3-5-sonnet'),
  messages: [{
    role: 'user',
    content: [
      { type: 'text', text: 'Extract every line item from this receipt as JSON.' },
      { type: 'image', image: receiptBytes },
    ],
  }],
});
```

## Use cases
- OCR + structured extraction (receipts, invoices, IDs)
- Visual QA / "describe this chart"
- Accessibility (alt text generation)
- Voice assistants (audio in → text → audio out)
- Video summarization
- UI from screenshots ("rebuild this design in React")

## Embeddings — multimodal
CLIP-style models embed images and text into the same space → "search images by text query."

## Real World Usage
- Receipt / document processing
- Product photo → metadata
- Voice-enabled customer support
- Accessibility tooling
- Video understanding / moderation
- Sketch-to-code

## Common Mistakes
- Sending huge unresized images (cost + latency)
- Trusting OCR without confidence checks / human review for high-stakes
- Mixing multimodal embeddings with text-only ones (incompatible spaces)
- Ignoring audio sample-rate requirements per provider
- Re-encoding losing quality before sending

## Prerequisites
- [[AI Providers]] · [[AI SDK by Vercel]] · [[Embeddings]]

## What To Learn Next
- [[Generative UI]] · [[Fine-tuning vs RAG]]

## Best Learning Resources

### Official Documentation
- [Anthropic — Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)
- [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime)
- [Google Gemini multimodal](https://ai.google.dev/gemini-api/docs/vision)

### Best YouTube Resource
- [Theo — multimodal demos](https://www.youtube.com/@t3dotgg)
- [Greg Kamradt — image AI tutorials](https://www.youtube.com/c/GregKamradt)

### Best Free Course
- [Vercel AI SDK examples — multimodal](https://github.com/vercel/ai)
- [Anthropic cookbook — vision examples](https://github.com/anthropics/anthropic-cookbook)

### Best Advanced Resource
- [CLIP paper (OpenAI)](https://arxiv.org/abs/2103.00020)
- [Hugging Face multimodal collections](https://huggingface.co/models?pipeline_tag=image-text-to-text)

### Best Practice Project
Build a "receipt → spreadsheet" pipeline: upload image → Claude/GPT extracts line items as JSON → write to Google Sheets. Add a confidence check + human review queue for items the model is unsure about.

### Recommended Order to Learn
1. Image input + extraction
2. Multimodal embeddings (CLIP)
3. Voice in/out (Realtime APIs)
4. Video understanding
5. Image generation (DALL-E, Imagen, Flux)
6. Combining modalities in agents

## Interview Questions
**Q. Are multimodal embeddings interchangeable with text embeddings?**
A. Only if from the same multimodal model (CLIP). Mixing CLIP image vectors with OpenAI text embeddings is meaningless.

**Q. Why resize images before sending?**
A. Cost is per-tile/token; high-res images can balloon spend and latency without quality gain.

## Related
- [[AI Providers]] · [[AI SDK by Vercel]] · [[Embeddings]] · [[Generative UI]]
