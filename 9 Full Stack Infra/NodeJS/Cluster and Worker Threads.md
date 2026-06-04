---
tags: [nodejs, advanced, concurrency]
---

# Cluster and Worker Threads

> Two ways to use multiple cores.

## Cluster
Forks **N processes** sharing a port. OS load-balances connections.
```js
import cluster from 'cluster';
import os from 'os';
if (cluster.isPrimary) {
  os.cpus().forEach(() => cluster.fork());
} else {
  startServer();
}
```

## Worker Threads
**Threads in same process**, share `ArrayBuffer` via SharedArrayBuffer or messages.
```js
import { Worker } from 'worker_threads';
const w = new Worker('./heavy.js');
w.postMessage({ data });
w.on('message', result => ...);
```

## When to use which
- Cluster — scaling stateless HTTP servers
- Worker threads — CPU-bound work inside one process (image processing, parsing)

## Production
Use a process manager (PM2, systemd) instead of writing cluster code yourself.

## Related
- [[Child Process]] · [[Performance and Profiling]]

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
