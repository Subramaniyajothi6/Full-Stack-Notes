---
tags: [mern, observability, intermediate]
---

# Logging Across Services

> Structured, correlated, searchable logs across the React app, the Express API, and the workers — so a user complaint becomes a 30-second investigation, not a day.

## The pillars (logs / metrics / traces)
| Pillar | Tool                                | Question answered                  |
|--------|-------------------------------------|------------------------------------|
| Logs   | Pino, Winston + Loki / Datadog      | What happened, in what order?      |
| Metrics| Prometheus / Grafana / Datadog      | How often, how fast, how many?     |
| Traces | OpenTelemetry → Jaeger / Tempo      | Where did this single request go?  |

## Structured logging (Pino)
```ts
import pino from 'pino';
const log = pino({
  level: process.env.LOG_LEVEL ?? 'info',
  redact: ['req.headers.authorization', 'req.headers.cookie', 'password'],
  formatters: { level: (label) => ({ level: label }) },
});
log.info({ userId, route: '/api/orders' }, 'created order');
```

JSON output gets ingested by Loki / Datadog / CloudWatch — query by field.

## Request correlation (request-id)
```ts
import { randomUUID } from 'crypto';

app.use((req, res, next) => {
  req.id = req.headers['x-request-id'] || randomUUID();
  res.setHeader('x-request-id', req.id);
  req.log = log.child({ reqId: req.id });
  next();
});

app.get('/api/orders', (req, res) => {
  req.log.info({ userId: req.user.sub }, 'list orders');
  // every downstream call passes req.id along
});
```

The frontend includes `x-request-id` in fetch; the API echoes it; workers log it. One id traces a user action through every system.

## Frontend errors → backend
```ts
// React error boundary or window.onerror
window.addEventListener('error', (e) => {
  fetch('/api/log', {
    method: 'POST',
    body: JSON.stringify({ msg: e.message, stack: e.error?.stack }),
  });
});
```
Or use Sentry / LogRocket / Highlight (handles errors + breadcrumbs + replay).

## Distributed tracing (OpenTelemetry)
Single SDK exports spans across:
- HTTP requests (incoming + outgoing)
- DB queries (Mongoose, Prisma)
- Queue jobs (BullMQ instrumentations)

Traces show "request X took 1.2s — 80ms in Express, 1100ms in Mongo, 20ms in cache". Without traces, you guess.

## Real World Usage
- Customer reports "my order is missing" → search by their userId or request id → see the failure
- p95 latency alert → trace shows DB query as the bottleneck
- Error rate spike → group by error message → find new deploy regression
- Cron job that runs in 30 seconds today vs 2 minutes yesterday → trace explains

## Common Mistakes
- `console.log` in production (no structure, no level filtering)
- Logging secrets (Authorization headers, cookies, passwords) — use redactors
- No request id correlation — debugging across services is impossible
- Log levels misused (everything `info`)
- Frontend errors never reach the backend
- Logging entire request bodies (PII leak, storage cost)
- Sampling 100% of traces in prod — costly; sample by path or error

## Prerequisites
- [[Logging in Node]] · [[Logging with Morgan]] · [[Error Handling in Node]]

## What To Learn Next
- [[Realtime with Socket.IO]] · [[Background Jobs]]

## Best Learning Resources

### Official Documentation
- [Pino docs](https://getpino.io/)
- [OpenTelemetry — JS](https://opentelemetry.io/docs/instrumentation/js/)
- [Sentry SDK docs](https://docs.sentry.io/)
- [Datadog Logs / APM](https://docs.datadoghq.com/)

### Best YouTube Resource
- [Hussein Nasser — observability](https://www.youtube.com/@hnasr)
- [TechWorld with Nana — Prometheus + Grafana](https://www.youtube.com/c/TechWorldwithNana)

### Best Free Course
- [Honeycomb — Observability Engineering (free book)](https://www.honeycomb.io/observability-engineering-oreilly-book-2022)
- [Grafana Labs blog + free courses](https://grafana.com/training/)

### Best Advanced Resource
- [Distributed Tracing in Practice (book) — O'Reilly](https://www.oreilly.com/library/view/distributed-tracing-in/9781492056621/)
- [Google SRE Book — Monitoring chapters](https://sre.google/sre-book/monitoring-distributed-systems/)

### Best Practice Project
Add structured logging + request-id correlation + Sentry to a MERN app. Wire OpenTelemetry to a free Honeycomb / Tempo backend. Reproduce a 500 in dev and walk the trace from React click to DB query.

### Recommended Order to Learn
1. Structured logger (Pino) with levels
2. Request-id correlation
3. Frontend error capture (Sentry)
4. Metrics + dashboards (Prometheus + Grafana)
5. Distributed tracing (OpenTelemetry)
6. Alerting (PagerDuty / Slack rules)
7. SLOs + error budgets

## Interview Questions
**Q. Why structured logs over plain text?**
A. Queryable by field (`level`, `userId`, `route`); aggregation tools index them; secrets are easier to redact.

**Q. What's a request id and why does it matter?**
A. A unique value carried across services in headers; lets you reconstruct one user's journey across N components.

**Q. Logs vs metrics vs traces — when which?**
A. Logs: events/details. Metrics: numbers/aggregates. Traces: paths through systems. Mature observability uses all three.

## Related
- [[Logging in Node]] · [[Logging with Morgan]] · [[Error Handling in Node]] · [[Background Jobs]] · [[Realtime with Socket.IO]]
