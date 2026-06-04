---
tags: [nodejs, intermediate, concept]
---

# File System

> The `fs` module — sync, callback, and promise APIs.

## Promise API (preferred)
```js
import { readFile, writeFile } from 'fs/promises';

const text = await readFile('input.txt', 'utf8');
await writeFile('output.txt', text.toUpperCase());
```

## Streaming for big files
```js
import { createReadStream, createWriteStream } from 'fs';
createReadStream('big.csv').pipe(createWriteStream('copy.csv'));
```

## Common mistakes
- Using sync APIs (`readFileSync`) on the request path — blocks event loop
- Forgetting `utf8` encoding → returns Buffer
- Path joining with `/` — use `path.join` for cross-platform

## Related
- [[Streams]] · [[Buffers]]

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
