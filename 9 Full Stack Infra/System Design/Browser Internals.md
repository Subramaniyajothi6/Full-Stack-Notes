---
tags: [infra, internet, intermediate]
---

# Browser Internals

> How a modern browser turns a URL into pixels: networking → parsing → render → composite.

## Why it matters
Performance, accessibility, and bug debugging all live in the browser pipeline. Knowing it lets you reason about jank, paint timings, and security boundaries.

## Core ideas
- **Process model** — browser process, renderer per site (site isolation), GPU process, network process
- **Critical rendering path** — HTML → DOM, CSS → CSSOM → render tree → layout → paint → composite
- **Event loop** — tasks, microtasks, requestAnimationFrame, idle callbacks
- **Storage** — cookies, localStorage, IndexedDB, Cache API, OPFS
- **Security** — same-origin policy, CORS, CSP, sandboxing

## Render path (mental model)
```
HTML  ─► DOM ─┐
              ├─► render tree ─► layout ─► paint ─► composite
CSS   ─► CSSOM ┘
JS    ─► mutates DOM/CSSOM (can block parser)
```

## Real World Usage
- Optimizing LCP/FID/CLS (Core Web Vitals)
- Avoiding layout thrash (read-then-write batching)
- Using `requestAnimationFrame` for smooth animations
- Debugging memory leaks via Performance + Memory panels

## Common Mistakes
- Synchronous `<script>` blocking parser — use `defer` or `async`
- Heavy work on the main thread (move to Web Workers)
- Forgetting that JS reading layout (`offsetHeight`) forces synchronous reflow
- Storing tokens in localStorage (XSS reads it)

## Prerequisites
- [[Event Loop]] · [[HTTP and HTTPS|HTTP & HTTPS]]

## What To Learn Next
- [[Browser DevTools]] · [[CDN|CDN]] · [[WASM]]

## Best Learning Resources

### Official Documentation
- [web.dev — How browsers work](https://web.dev/articles/howbrowserswork) — Google's canonical write-up
- [MDN — Critical rendering path](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path) — actionable, accurate

### Best YouTube Resource
- [Fireship — Browser Engines](https://www.youtube.com/c/Fireship) — quick mental model
- [Jake Archibald — In the loop](https://www.youtube.com/watch?v=cCOL7MC4Pl0) — definitive event loop talk

### Best Free Course
- [Frontend Masters — Browser Internals (free chapters)](https://frontendmasters.com/) — clear, paid extension if you want depth

### Best Advanced Resource
- [Inside look at modern web browser (Chrome team)](https://developer.chrome.com/blog/inside-browser-part1/) — 4-part series with diagrams

### Best Practice Project
Build a "performance audit" page that intentionally triggers layout thrash, long tasks, and large images. Profile with DevTools, then fix and document each metric improvement.

### Recommended Order to Learn
1. Process model (browser, renderer, GPU)
2. Critical rendering path
3. Event loop + microtasks vs tasks
4. Performance APIs (PerformanceObserver, Web Vitals)
5. Security model (origin, CSP)

## Interview Questions
**Q. What happens between `Enter` in URL bar and pixels on screen?**
A. DNS → TCP/TLS → HTTP → HTML parse → DOM + CSSOM → render tree → layout → paint → composite.

**Q. Why is `defer` better than `async` for non-critical scripts?**
A. `defer` preserves order and runs after parsing. `async` runs as soon as fetched, may execute out of order.

**Q. Why does reading `element.offsetHeight` after a write cause jank?**
A. Forces synchronous layout (reflow) because the browser must compute up-to-date geometry.

**Q. What is the difference between paint and composite?**
A. Paint fills pixels into layers; composite assembles layers on the GPU. `transform`/`opacity` skip paint = cheap.

## Related
- [[Browser DevTools]] · [[Performance Optimization|Performance Optimization]]
