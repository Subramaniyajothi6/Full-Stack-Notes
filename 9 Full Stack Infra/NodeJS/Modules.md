---
tags: [nodejs, beginner, concept]
---

# Modules

> Files are modules. Each has its own scope.

## Two systems
- **CommonJS** (CJS) — `require`, `module.exports`. Default for `.js` unless `"type": "module"`.
- **ES Modules** (ESM) — `import`/`export`. Default with `"type": "module"` or `.mjs`.

## CJS
```js
// math.js
module.exports = { add: (a,b) => a+b };
// app.js
const { add } = require('./math');
```

## ESM
```js
// math.js
export const add = (a,b) => a+b;
// app.js
import { add } from './math.js';
```

## Common mistakes
- Mixing `require` of an ESM module — needs dynamic `import()`
- Forgetting `.js` extensions in ESM
- Circular dependencies — both modules see partially loaded exports

## Related
- [[CommonJS vs ES Modules]] · [[npm and package.json]]

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
