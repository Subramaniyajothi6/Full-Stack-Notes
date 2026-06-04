---
tags: [nodejs, advanced, concept]
---

# V8 Engine

> Google's open-source JavaScript engine that powers Chrome and Node.

## What it does
- Parses JS into AST
- Compiles to bytecode (Ignition) → optimizes hot code (TurboFan / Maglev / Sparkplug)
- Manages memory + garbage collection (generational, mark-sweep)

## Optimizations to know
- **Hidden classes** — V8 assigns shapes; consistent property order matters
- **Inline caches** — speeds up property access on similar shapes
- **Deopt** — when assumptions break (changing types), V8 falls back

## Memory areas
- Stack — function frames
- Heap — objects (split into young/old generations)

## Related
- [[Node Architecture]] · [[Performance and Profiling]]

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
