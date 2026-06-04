---
tags: [nodejs, intermediate, pattern]
---

# Async Patterns in Node

> Three styles: callbacks, promises, async/await.

## Callbacks (legacy)
```js
fs.readFile('a', (err, data) => {
  if (err) return cb(err);
  ...
});
```

## Promises
```js
import { readFile } from 'fs/promises';
readFile('a').then(data => ...).catch(err => ...);
```

## async/await
```js
const data = await readFile('a');
```

## Patterns
- **Parallel** — `await Promise.all([...])`
- **Sequence** — `for…of` with `await`
- **Race** — `Promise.race`
- **Throttling** — semaphores, p-limit

## Common mistakes
- `forEach` with async — fire-and-forget
- Unhandled rejections — set handler on `process`
- Mixing styles inconsistently

## Related
- [[Promises|Promises]] · [[Async Await|Async Await]] · [[Error Handling in Node]]

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
