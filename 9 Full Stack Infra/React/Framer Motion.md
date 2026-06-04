---
tags: [infra, frontend, intermediate]
---

# Framer Motion

> Production-grade animation library for React. Declarative, gesture-aware, layout animations.

## Why it matters
Smooth animations boost perceived quality. Framer Motion handles springs, gestures, presence, and layout animations without manual `requestAnimationFrame`.

## Core ideas
- `motion.div` — drop-in animatable element
- `animate` / `initial` / `exit` — declarative states
- `<AnimatePresence>` — handle exit animations on unmount
- **Layout animations** — `layoutId` shares state across components for seamless morphs
- **Gestures** — `whileHover`, `whileTap`, `drag`
- **Variants** — orchestrate parent-child sequences

## Example
```tsx
import { motion, AnimatePresence } from 'framer-motion';

<AnimatePresence>
  {open && (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -10 }}
      transition={{ type: 'spring', stiffness: 300 }}
    />
  )}
</AnimatePresence>
```

## Real World Usage
- Modal/drawer enter-exit
- Drag-to-reorder lists
- Page transitions in Next.js
- Hero shared-element morphs (`layoutId`)

## Common Mistakes
- Animating `width`/`height` per frame (layout-thrash) — use `transform` and `scale`
- Forgetting `AnimatePresence` → exit animations skip
- Heavy variants on every list item → jank
- Importing into a Server Component (it's client-only)

## Prerequisites
- [[Components|Components]] · [[Browser Internals]]

## What To Learn Next
- [[shadcn UI]] · [[Radix UI]]

## Best Learning Resources

### Official Documentation
- [Framer Motion docs](https://www.framer.com/motion/) — examples + API
- [Motion.dev (rebranded)](https://motion.dev/)

### Best YouTube Resource
- [Sam Selikoff](https://www.youtube.com/c/SamSelikoff) — best Framer Motion teacher
- [Tim Krieger — Framer playlists](https://www.youtube.com/results?search_query=framer+motion+tutorial)

### Best Free Course
- [Build UI — Framer Motion Recipes](https://buildui.com/recipes) — Sam Selikoff's recipe pack

### Best Advanced Resource
- [Framer source on GitHub](https://github.com/framer/motion) — internals
- [Josh Comeau — Animation principles](https://www.joshwcomeau.com/) — broader animation theory

### Best Practice Project
Build an interactive product gallery with drag, swipe-to-dismiss, layout-morphing card to fullscreen, and orchestrated entry animations on scroll. Profile and keep it 60 fps.

### Recommended Order to Learn
1. `motion.X` + `animate`/`initial`
2. Variants + orchestration
3. `AnimatePresence`
4. Layout animations (`layoutId`)
5. Gestures (drag, hover, tap)
6. Performance — layout vs transform; use `useMotionValue` for raw

## Interview Questions
**Q. Why is animating `transform` cheaper than `top`/`width`?**
A. Transform skips layout/paint and runs on the GPU compositor.

**Q. What problem does `layoutId` solve?**
A. Animates between two unrelated elements that share an id, creating shared-element transitions.

**Q. Why doesn't my exit animation fire?**
A. Component is not wrapped in `AnimatePresence`, or `key` is unstable causing remounts.

## Related
- [[shadcn UI]] · [[Radix UI]]
