---
tags: [nodejs, advanced, performance]
---

# Performance and Profiling

## Tools
- `--prof` (v8 sampler) → `node --prof-process`
- `clinic.js` — flamegraphs, doctor, bubbleprof
- `0x` — flamegraph generator
- Built-in `perf_hooks`

## Common bottlenecks
- Sync code on the request path
- JSON.parse / stringify on huge payloads
- Inefficient regex
- N+1 DB queries

## Memory leaks
- Heap snapshots in DevTools (compare two)
- Detached event listeners, unbounded caches

## Related
- [[Event Loop in Node]] · [[Cluster and Worker Threads]]

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
