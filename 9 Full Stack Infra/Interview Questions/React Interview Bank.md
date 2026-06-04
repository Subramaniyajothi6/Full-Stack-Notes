---
tags: [interview, react]
---

# React Interview Bank

## Core
**Q. What is the Virtual DOM?**
A. In-memory tree React diffs against; only changed nodes hit real DOM. See [[Virtual DOM]].

**Q. Why keys in lists?**
A. Stable identity for reconciliation; wrong keys break state and animations. Index is fine only for static lists. See [[Lists and Keys]].

**Q. Controlled vs uncontrolled?**
A. Controlled — React owns value via state. Uncontrolled — DOM owns, read via ref. See [[Controlled vs Uncontrolled Components]].

## Hooks
**Q. Rules of hooks?**
A. Top-level only; only from React functions or custom hooks. See [[Rules of Hooks]].

**Q. useEffect vs useLayoutEffect?**
A. `useEffect` runs after paint (async). `useLayoutEffect` runs synchronously after DOM mutation, before paint — for measuring layout.

**Q. What's a stale closure?**
A. Effect/handler captures old state due to missing dep. Fix with deps or refs. See [[useEffect]].

**Q. useMemo vs useCallback?**
A. `useMemo` memoizes a value. `useCallback` memoizes a function. Equivalent: `useCallback(fn, deps) === useMemo(() => fn, deps)`.

## Performance
**Q. When does React.memo help?**
A. When parent passes stable props and child is expensive. Useless if parent always passes new object/fn props.

**Q. How to debug re-renders?**
A. React DevTools Profiler, "Highlight updates" toggle, why-did-you-render lib.

## State management
**Q. Context vs Redux?**
A. Context for low-frequency global values (theme, locale). Redux for complex/global state with strong devtools. See [[Context API]] · [[Redux Toolkit]].

**Q. Lifting state — when too far?**
A. When unrelated components re-render. Pull state down or move to context/store.

## Routing
**Q. Difference between `Link` and `<a>`?**
A. `<a>` triggers full navigation. `Link` does client-side routing without reload.

## Modern
**Q. What changes with Server Components?**
A. Render on server, ship 0 JS. No state/effects/event handlers. See [[Server Components]].

**Q. Concurrent rendering — what's `useTransition`?**
A. Marks a state update as non-urgent so React can keep current UI responsive. See [[Concurrent Rendering]].

## Tricky
**Q. Why component must be capitalized?**
A. Lowercase = HTML element to React.

**Q. What does Fragment solve?**
A. Returning multiple siblings without wrapping div.
