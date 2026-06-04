---
tags: [nodejs, advanced, concept]
---

# Streams

> Process data in chunks. Memory-efficient for large or continuous data.

## Four types
- **Readable** — `fs.createReadStream`, HTTP request
- **Writable** — `fs.createWriteStream`, HTTP response
- **Duplex** — both (TCP socket)
- **Transform** — modifies as it passes (`zlib.createGzip`)

## Pipe
```js
import { pipeline } from 'stream/promises';
import { createReadStream, createWriteStream } from 'fs';
import { createGzip } from 'zlib';

await pipeline(
  createReadStream('in'),
  createGzip(),
  createWriteStream('in.gz')
);
```

## Common mistakes
- Forgetting error handling — use `pipeline` (handles errors + cleanup)
- Not respecting backpressure — `write` returns false → wait for `drain`
- Reading entire file into memory when stream would suffice

## Related
- [[File System]] · [[Buffers]] · [[HTTP Module]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://nodejs.org/en/docs — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Hussein Nasser, TechWorld with Nana, Traversy Media

### Best Free Course
- TODO

### Best Advanced Resource
- TODO

### Best Practice Project
- TODO: 1-paragraph project idea

### Recommended Order to Learn
1. TODO
2. TODO
3. TODO

## Interview Questions
**Q. TODO** — A. ...

**Q. TODO** — A. ...
