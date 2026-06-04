---
tags: [nodejs, beginner, syntax]
---

# Global Objects in Node

> Available without `require/import`.

## Common globals
- `process` — see [[Process and Environment]]
- `global` — equivalent of `window` (but rarely use)
- `console` — logging (writes to stderr/stdout)
- `__dirname`, `__filename` — current file path (CommonJS only)
- `Buffer` — see [[Buffers]]
- `setImmediate`, `setTimeout`, `setInterval`, `queueMicrotask`

## ESM caveat
`__dirname`/`__filename` not available in ES modules — use:
```js
import { fileURLToPath } from 'url';
const __filename = fileURLToPath(import.meta.url);
```

## Related
- [[CommonJS vs ES Modules]] · [[Process and Environment]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Common Mistakes
- TODO: pitfalls and edge cases

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
