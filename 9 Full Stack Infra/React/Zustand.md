---
tags: [infra, frontend, intermediate]
---

# Zustand

> Tiny, hooks-first state manager for React. No provider, no boilerplate.

## Why it matters
The pragmatic alternative to Redux for app-level state. ~1KB, TypeScript-first, works great with selectors.

## Core ideas
- A `create(set => ({...}))` returns a hook
- Components subscribe via selector functions
- Immutable update (or use Immer middleware)
- Middleware: `persist`, `devtools`, `immer`, `subscribeWithSelector`
- Vanilla store available for non-React contexts

## Example
```ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

const useStore = create(
  persist(
    (set, get) => ({
      count: 0,
      inc: () => set(s => ({ count: s.count + 1 })),
      reset: () => set({ count: 0 }),
    }),
    { name: 'counter' }
  )
);

// usage
const count = useStore(s => s.count);
const inc = useStore(s => s.inc);
```

## Real World Usage
- Cart, modal, toast managers
- Theme/locale switches
- Auth user object (with persist middleware)
- Multi-step form wizards

## Common Mistakes
- Selecting whole state (no selector) → re-renders on every change
- Returning new object from selector (`s => ({ a: s.a })`) → always re-renders; use `useShallow`
- Mutating without `set` → no re-render
- Stuffing server state into Zustand instead of [[TanStack Query]]

## Prerequisites
- [[State in React|React State]] · [[useReducer|useReducer]]

## What To Learn Next
- [[Immer]] · [[TanStack Query]] · [[Redux Toolkit|Redux Toolkit]]

## Best Learning Resources

### Official Documentation
- [Zustand Docs](https://zustand.docs.pmnd.rs/) — concise, example-driven
- [GitHub README](https://github.com/pmndrs/zustand)

### Best YouTube Resource
- [Jack Herrington — Zustand vs Redux](https://www.youtube.com/@jherr)
- [Theo — Why Zustand](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [TkDodo's blog — Working with Zustand](https://tkdodo.eu/blog) — same author as TanStack Query writeups, deep React patterns

### Best Advanced Resource
- [Daishi Kato (Zustand author) — talks & blog posts](https://github.com/dai-shi)

### Best Practice Project
Build a Trello-style kanban with Zustand for local board state, persist middleware, and `useShallow` selectors. Add undo/redo via temporal middleware.

### Recommended Order to Learn
1. Basic store + hook
2. Selectors + `useShallow`
3. Middleware (persist, devtools)
4. Immer middleware
5. Vanilla stores + cross-tab sync

## Interview Questions
**Q. Zustand vs Redux?**
A. Zustand is smaller, no provider, no actions/reducers — pick for app state. Redux Toolkit shines for time-travel devtools and large opinionated codebases.

**Q. How does Zustand avoid prop drilling without a Provider?**
A. The hook reads from a module-level vanilla store. React subscriptions are wired via `useSyncExternalStore`.

**Q. Why does my component re-render on every state change?**
A. You're not using a selector or returning a new object from one. Use `useShallow` for object selections.

## Related
- [[Immer]] · [[TanStack Query]] · [[Zustand and Alternatives|Zustand & Alternatives]]
