---
tags: [testing, advanced, performance]
---

# Load Testing

> Send synthetic traffic at growing rates to find where your system breaks. Before users do.

## Categories
- **Smoke** — small load to verify it runs (every deploy)
- **Load** — expected traffic; validate normal behavior
- **Stress** — beyond expected; find the breaking point
- **Soak** — long-duration to find memory leaks
- **Spike** — sudden burst; test elasticity

## Tools
- **k6** — JS-scripted, modern, CLI + cloud
- **Artillery** — YAML/JS, Node-friendly
- **Locust** — Python, distributed
- **JMeter** — Java, GUI heritage
- **Gatling** — Scala, high-throughput
- **wrk / hey / vegeta** — simple CLI for HTTP

## k6 example
```js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 50 },
    { duration: '3m', target: 50 },
    { duration: '1m', target: 200 },
    { duration: '3m', target: 200 },
    { duration: '1m', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed:   ['rate<0.01'],
  },
};

export default function () {
  const r = http.get('https://api.example.com/health');
  check(r, { 'status 200': (r) => r.status === 200 });
  sleep(1);
}
```

## What to measure
- **Throughput** (rps)
- **Latency** (p50, p95, p99) — tail matters
- **Error rate**
- **CPU / mem / IO / DB connections** on the server
- **Saturation** (queue depths, dropped requests)

## Real World Usage
- Pre-launch capacity planning
- Performance regression detection in CI
- Validating an auto-scaling policy
- Stress-testing rate limiters
- Hunting tail-latency contributors

## Common Mistakes
- Testing from same network as the server → unrealistic latencies
- No warm-up → cold caches skew first runs
- Single-VU scenarios miss concurrency bugs
- Open-loop vs closed-loop confusion — read the model
- Not monitoring the server during the test (you only see client side)
- Hammering production without coordination

## Prerequisites
- [[E2E Testing]] · [[CI CD]] · [[Deployment Architecture]]

## What To Learn Next
- [[Mutation Testing]] · [[Logging Across Services]]

## Best Learning Resources

### Official Documentation
- [k6 docs](https://k6.io/docs/)
- [Artillery docs](https://www.artillery.io/docs)
- [Locust docs](https://docs.locust.io/)

### Best YouTube Resource
- [k6 YouTube](https://www.youtube.com/c/k6Load-testing)
- [Hussein Nasser — load testing](https://www.youtube.com/@hnasr)

### Best Free Course
- [k6 Learn (free)](https://k6.io/docs/examples/)
- [Grafana k6 cloud free tier](https://grafana.com/products/cloud/k6/)

### Best Advanced Resource
- [Brendan Gregg — performance methodology](https://www.brendangregg.com/methodology.html)
- [SRE book — Capacity planning chapters](https://sre.google/books/)

### Best Practice Project
Take a JSON API. Define a baseline (1× expected traffic) k6 script. Add a smoke + stress profile. Run, find the breaking point, instrument the server with [[Logging Across Services]], find the bottleneck (CPU / DB / GC), document.

### Recommended Order to Learn
1. Single-VU script
2. Scenarios with stages
3. Thresholds + checks
4. Distributed runs (cloud or `k6 run --execution-segment`)
5. Soak + spike tests
6. Tying to CI gates

## Interview Questions
**Q. Why is p99 latency more useful than mean?**
A. Mean hides tail problems. p99 captures the slowest 1% — what real users experience during a bad moment.

**Q. Open-loop vs closed-loop?**
A. Closed-loop = each VU waits for its previous response. Open-loop = constant request rate regardless of latency. Open-loop simulates real-world bursts better.

## Related
- [[Logging Across Services]] · [[Deployment Architecture]] · [[CI CD]] · [[Caching Layers]]
