---
tags: [nodejs, intermediate, concept]
---

# CommonJS vs ES Modules

| Aspect            | CommonJS                         | ES Modules                       |
| ----------------- | -------------------------------- | -------------------------------- |
| Syntax            | `require` / `module.exports`     | `import` / `export`              |
| Loading           | Synchronous                      | Asynchronous, static             |
| Top-level await   | No                               | Yes                              |
| `__dirname`       | Built-in                         | Construct from `import.meta.url` |
| Tree-shakeable    | Limited                          | Yes                              |
| File extension    | optional in require              | Required (`.js`, `.mjs`)         |

## Choosing
- New backends: ESM
- Existing CJS codebase: stay or migrate gradually
- Libraries: ship both via `exports` field

## Interop
- ESM can import CJS — default export is `module.exports`
- CJS importing ESM → use dynamic `import()`

## Related
- [[Modules]] · [[npm and package.json]]

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
