---
tags: [mern, scale, intermediate]
---

# Background Jobs

> Work that doesn't fit in the request/response cycle: emails, image processing, AI calls, scheduled tasks, retries.

## Why move it out of the request
- User shouldn't wait on a 5-second email send
- Retries with backoff need a queue
- Throttling external APIs (rate limit) needs a worker pool
- Scheduled tasks (cron) need durability across restarts

## Stack of choice (Node)
- **BullMQ** (Redis-backed queues) — most popular
- **Inngest / Trigger.dev** — durable workflows + cron, hosted
- **Temporal** — heavyweight, advanced workflows
- **Native cron** (`node-cron`) — simplest, single-node only

## BullMQ example
```ts
// queues/email.ts
import { Queue, Worker } from 'bullmq';

const connection = { host: 'localhost', port: 6379 };

export const emailQueue = new Queue('email', { connection });

new Worker('email', async (job) => {
  if (job.name === 'send') {
    await sendgrid.send(job.data);
  }
}, {
  connection,
  concurrency: 10,
  limiter: { max: 100, duration: 60_000 },     // 100/min throttle
});

// Producer (e.g., in an Express handler)
await emailQueue.add('send', { to, subject, body }, {
  attempts: 5,
  backoff: { type: 'exponential', delay: 5_000 },
  removeOnComplete: 1_000,
});
```

## Patterns
- **Idempotent jobs** — running twice has the same effect (use unique `jobId`)
- **Dead-letter queue** — jobs that fail after N retries land here for inspection
- **Cron jobs** — `repeat: { pattern: '0 * * * *' }`
- **Fan-out** — one event → producers add many child jobs
- **Pipelines** — output of job A feeds job B (use `flow producer` in BullMQ)

## Real World Usage
- Welcome emails, password resets
- Image resizing, thumbnail generation
- AI inference jobs (long-running)
- Webhook delivery with retries
- Daily digests, weekly reports
- Search indexing jobs (Algolia, Meilisearch sync)
- Stripe / payment processing
- ETL pipelines

## Common Mistakes
- Doing the work synchronously in the request handler ("just one extra second" → tail latency disaster)
- Not making jobs idempotent → double charges, double emails
- No DLQ → silent failures
- Holding DB transactions across queue calls (release first, then enqueue)
- No metrics → no idea your queue is backed up
- Running workers in the same process as the API → CPU spikes hurt request latency
- No backoff → retry storms hammer downstream services

## Prerequisites
- [[Redis]] · [[NodeJS MOC]] · [[Error Handling in Node]]

## What To Learn Next
- [[Logging Across Services]] · [[Realtime with Socket.IO]]

## Best Learning Resources

### Official Documentation
- [BullMQ docs](https://docs.bullmq.io/)
- [Inngest docs](https://www.inngest.com/docs)
- [Trigger.dev docs](https://trigger.dev/docs)
- [Temporal docs](https://docs.temporal.io/)

### Best YouTube Resource
- [Theo — Inngest / Trigger.dev](https://www.youtube.com/@t3dotgg)
- [Hussein Nasser — Queue patterns](https://www.youtube.com/@hnasr)

### Best Free Course
- [BullMQ patterns guide](https://docs.bullmq.io/patterns/introduction)
- [Inngest Quickstart](https://www.inngest.com/docs/getting-started)

### Best Advanced Resource
- [Designing Data-Intensive Applications — chapter on stream processing](https://dataintensive.net/)
- [Resque / Sidekiq design notes (Ruby roots, generic principles)](https://github.com/sidekiq/sidekiq/wiki)

### Best Practice Project
Add a job queue to your MERN app: send welcome email on signup via BullMQ; generate thumbnails on upload; run a nightly cleanup cron. Add a `/admin/queues` dashboard via `bull-board`. Force a job to fail and inspect retries + DLQ.

### Recommended Order to Learn
1. Queue basics (producer + worker)
2. Retries + backoff
3. Concurrency + rate limiting
4. Cron + repeating jobs
5. Pipelines / flows
6. Observability (metrics, dashboards)
7. Durable workflow systems (Inngest, Temporal)

## Interview Questions
**Q. Why use a queue instead of `setTimeout` or async?**
A. Queues are durable (survive restarts), distributed (worker pool scales), and observable (metrics, retries, DLQ).

**Q. Idempotency — why does it matter for jobs?**
A. Workers can crash mid-job, leading to retries. Idempotent jobs make double-execution safe.

**Q. BullMQ vs Inngest?**
A. BullMQ is self-hosted, Redis-based, full control. Inngest is hosted, durable, opinionated workflow model.

## Related
- [[Redis]] · [[Realtime with Socket.IO]] · [[Logging Across Services]] · [[NodeJS MOC]]
