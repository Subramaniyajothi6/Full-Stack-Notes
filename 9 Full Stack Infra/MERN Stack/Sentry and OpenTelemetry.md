---
tags: [mern, observability, intermediate]
---

# Sentry and OpenTelemetry

> Errors + traces + performance across client, server, and workers. Sentry is the easiest on-ramp; OpenTelemetry is the open standard.

## Sentry essentials
- Errors: stack traces, breadcrumbs, source maps, user context
- Performance: web vitals + transactions across services
- Session Replay: video-like reproduction of user sessions
- Releases: tie errors to deploy / commit
- Integrations for React, Node, Next.js, React Native, etc.

### React + Sentry
```ts
// sentry.client.config.ts
import * as Sentry from '@sentry/nextjs';
Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  tracesSampleRate: 0.1,
  replaysSessionSampleRate: 0.01,
  replaysOnErrorSampleRate: 1.0,
});
```

### Node + Sentry
```ts
import * as Sentry from '@sentry/node';
Sentry.init({ dsn: process.env.SENTRY_DSN, tracesSampleRate: 0.1 });

// Express
app.use(Sentry.Handlers.requestHandler());
// ...routes
app.use(Sentry.Handlers.errorHandler());
```

## OpenTelemetry essentials
- Vendor-neutral standard for traces + metrics + logs
- SDK + auto-instrumentations
- Exports to: Tempo, Jaeger, Honeycomb, Datadog, New Relic, Grafana Cloud
- Semantic conventions standardize attribute names

### Node OTEL bootstrap
```ts
// otel.ts (imported before everything else)
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';

new NodeSDK({
  traceExporter: new OTLPTraceExporter({ url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT }),
  instrumentations: [getNodeAutoInstrumentations()],
}).start();
```

## Sentry + OpenTelemetry — pick one or both
- **Sentry alone** — fastest path to value, especially for errors + replays
- **OpenTelemetry alone** — own your data, swap backends, full stack
- **Both** — Sentry for errors / replays + OTEL for distributed traces

## Real World Usage
- Catch unhandled errors in React + Node + workers
- p95 latency dashboards across services
- Tracing a single user request from React click → DB query
- Release-gated alerting (regression detection)
- AI app cost + latency observability with OTEL GenAI conventions

## Common Mistakes
- 100% trace sampling in prod (cost explosion)
- Forgetting source maps → minified stack traces
- Letting PII leak into trace attributes
- Initializing OTEL after app imports (loses auto-instrumentation)
- No alerting on error rate / latency SLOs (data without action)
- Mixing Sentry + Datadog + New Relic for the same thing (duplicate cost)

## Prerequisites
- [[Logging Across Services]] · [[Error Handling in Node]] · [[Background Jobs]]

## What To Learn Next
- [[Realtime with Socket.IO]] · [[Tracing and Observability]]

## Best Learning Resources

### Official Documentation
- [Sentry docs](https://docs.sentry.io/)
- [OpenTelemetry docs](https://opentelemetry.io/docs/)
- [OpenTelemetry JS](https://opentelemetry.io/docs/instrumentation/js/)

### Best YouTube Resource
- [Sentry YouTube](https://www.youtube.com/c/SentryIO)
- [Hussein Nasser — observability](https://www.youtube.com/@hnasr)
- [Honeycomb — observability talks](https://www.youtube.com/c/honeycombio)

### Best Free Course
- [Sentry tutorials](https://docs.sentry.io/tutorial/)
- [Honeycomb — Observability Engineering (free book)](https://www.honeycomb.io/observability-engineering-oreilly-book-2022)

### Best Advanced Resource
- [Charity Majors talks (Honeycomb)](https://www.youtube.com/results?search_query=charity+majors)
- [Distributed Tracing in Practice (O'Reilly)](https://www.oreilly.com/library/view/distributed-tracing-in/9781492056621/)

### Best Practice Project
Add Sentry to React + Node. Wire OpenTelemetry on the Node side exporting to a free Grafana Cloud / Honeycomb endpoint. Reproduce a 500; walk the full trace from React click to failed DB query.

### Recommended Order to Learn
1. Sentry browser + Node SDK
2. Source maps + releases
3. Performance traces in Sentry
4. OTEL Node SDK + auto-instrumentations
5. Span context propagation across services
6. SLOs + alerts
7. Cost-aware sampling

## Interview Questions
**Q. Sentry vs OpenTelemetry?**
A. Sentry is a product focused on errors + session replays. OTEL is a standard for traces/metrics/logs across backends. They're complementary.

**Q. Why sample?**
A. 100% tracing is cost-prohibitive. Sample by rate (10%) or "always for errors, sometimes for success."

**Q. Why initialize OTEL before everything else?**
A. Auto-instrumentation hooks must wrap modules before they're imported by your app.

## Related
- [[Logging Across Services]] · [[Error Handling in Node]] · [[Tracing and Observability]]
