---
tags: [interview, nodejs]
---

# NodeJS Interview Bank

**Q. What is Node?**
A. JS runtime built on V8 + libuv. See [[What is NodeJS]].

**Q. Single-threaded but handles thousands of connections — how?**
A. Non-blocking I/O via libuv. JS runs on one thread; OS/thread pool handles I/O.

**Q. Walk through event loop phases.**
A. Timers → Pending → Idle → Poll → Check (setImmediate) → Close. Microtasks + nextTick between phases. See [[Event Loop in Node]].

**Q. `setImmediate` vs `setTimeout(0)` vs `process.nextTick`?**
A. `nextTick` first (highest), then microtasks, then timers (>= 1ms), then `setImmediate` (next iteration). Order between `setTimeout(0)` and `setImmediate` depends on context.

**Q. Streams — what for?**
A. Process data in chunks. Memory-efficient. Four kinds: Readable, Writable, Duplex, Transform. See [[Streams]].

**Q. Buffer?**
A. Fixed-size raw bytes. Used for binary data. See [[Buffers]].

**Q. CommonJS vs ES Modules?**
A. CJS sync, dynamic, `require/module.exports`. ESM async, static, `import/export`, top-level await. See [[CommonJS vs ES Modules]].

**Q. How do you scale Node across cores?**
A. Cluster (forks N processes), Worker Threads (in-process threads), or process manager (PM2). See [[Cluster and Worker Threads]].

**Q. Error handling best practices?**
A. async/await with try/catch, propagate via `next(err)` in Express, listen to `uncaughtException`/`unhandledRejection`, distinguish operational vs programmer errors. See [[Error Handling in Node]].

**Q. Memory leak debugging?**
A. Heap snapshots (Chrome DevTools), compare across time, look for retained closures, listeners, caches.

**Q. Why prefer async fs APIs?**
A. Sync APIs block the event loop, which blocks all requests.

**Q. What's libuv?**
A. C library providing event loop + async I/O + thread pool that Node uses. See [[libuv]].
