---
tags: [infra, frontend, intermediate]
---

# Immer

> Write mutating-looking code; Immer produces immutable updates via a Proxy draft.

## Why it matters
Immutable updates with deep nesting are painful (`{ ...state, a: { ...state.a, b: { ...state.a.b, c: 1 } } }`). Immer eliminates the spread soup. Used inside Redux Toolkit and Zustand-immer middleware.

## Core ideas
- `produce(state, draft => { draft.x = 1 })` returns a new immutable state
- Draft is a Proxy; mutations are recorded then applied structurally-shared
- Patches and inverse patches enable undo/redo and CRDT-like flows

## Example
```ts
import { produce } from 'immer';

const next = produce(state, draft => {
  draft.users[0].friends.push('alice');
});
// state is unchanged
```

## Real World Usage
- Redux Toolkit reducers (Immer is built-in)
- Zustand `immer` middleware for nested stores
- Form state with deep nesting
- Optimistic UI updates

## Common Mistakes
- Mutating original outside `produce` thinking it's tracked
- Returning a value AND mutating draft (Immer warns)
- Putting non-plain objects (Date, Map) in draft without enabling `enableMapSet`/`enablePatches`
- Performance assumption — Proxies have overhead; not for hot paths

## Prerequisites
- [[Object Reference Behavior|Object reference behavior]]
- [[State in React|React State]]

## What To Learn Next
- [[Redux Toolkit|Redux Toolkit]] · [[Zustand]]

## Best Learning Resources

### Official Documentation
- [Immer docs](https://immerjs.github.io/immer/) — clear, example-rich

### Best YouTube Resource
- [Michel Weststrate (Immer author)](https://www.youtube.com/results?search_query=michel+weststrate+immer)
- [Jack Herrington — Immer in React](https://www.youtube.com/@jherr)

### Best Free Course
- [Egghead — Immutable React State with Immer](https://egghead.io/) — short, dense

### Best Advanced Resource
- [Immer patches & undo/redo](https://immerjs.github.io/immer/patches/) — building blocks for collaborative editors

### Best Practice Project
Implement a tree editor (folders/files) with Immer + patches. Add undo/redo using inverse patches; add a JSON export to verify structure.

### Recommended Order to Learn
1. `produce` basics
2. Patches + inverse patches
3. Map/Set support
4. Performance: when to use raw spreads instead

## Interview Questions
**Q. How does Immer make immutable updates feel mutable?**
A. Wraps the input in a Proxy; records the mutations; produces a new object that shares unchanged subtrees.

**Q. When NOT to use Immer?**
A. Hot inner loops where Proxy overhead matters; very large arrays where structural sharing is unimportant.

**Q. Patches use case?**
A. Time-travel debugging, CRDT-like collaborative state, undo/redo stacks.

## Related
- [[Redux Toolkit|Redux Toolkit]] · [[Zustand]]
