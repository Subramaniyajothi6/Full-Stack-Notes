---
tags: [infra, backend, advanced, security]
---

# DoS Protection

> Defending against Denial-of-Service attacks — keeping a system available under malicious or accidental load.

## Why it matters
A single misbehaving client can starve a server; a coordinated attack can take down infrastructure. Every public service needs layered protection.

## Attack categories
- **Volumetric** — flood bandwidth (UDP floods, amplification)
- **Protocol** — TCP SYN floods, slowloris (slow read)
- **Application layer** — expensive endpoints, regex DoS, JSON bomb
- **Resource exhaustion** — disk fill, file-descriptor exhaustion, fork bombs

## Defense layers
1. **CDN / scrubbing** — Cloudflare, Akamai absorb volumetric traffic
2. **WAF** — block known patterns
3. **Rate limiting** — per-IP, per-user, per-API key (token bucket / sliding window)
4. **Auth before expensive work** — never run heavy queries for unauth users
5. **Timeouts everywhere** — read, write, request, downstream
6. **Bulkheads** — pool isolation (don't let one tenant exhaust DB connections)
7. **Backpressure** — return 429 + `Retry-After` instead of queuing forever
8. **Resource limits** — body size, JSON depth, regex complexity (use safe regex), file size
9. **Concurrency caps** — max in-flight per user
10. **Monitoring + auto-scaling** — but scaling alone is not protection

## Real World Usage
- Login/signup endpoints with strict per-IP and per-account rate limits
- API tiers with key-based quotas
- Edge protection against bots (Turnstile, hCaptcha)

## Common Mistakes
- Rate limiting only by IP (NAT/CGNAT shares IPs)
- ReDoS — vulnerable regex on user input (catastrophic backtracking)
- No body-size limit → memory bomb
- Auth-checks behind expensive queries → unauth users can DoS DB
- Trusting client `User-Agent` for bot detection

## Prerequisites
- [[Rate Limiting|Rate Limiting (Express)]] · [[Rate Limiting in System Design|Rate Limiting (system)]]

## What To Learn Next
- [[Sandboxing]] · [[CDN|CDN]] · [[Edge Computing]]

## Best Learning Resources

### Official Documentation
- [Cloudflare DDoS protection](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) — clear primer
- [OWASP — Denial of Service](https://owasp.org/www-community/attacks/Denial_of_Service)

### Best YouTube Resource
- [ByteByteGo — DDoS architectures](https://www.youtube.com/c/ByteByteGo)
- [Hussein Nasser — TCP SYN flood, slowloris](https://www.youtube.com/@hnasr)

### Best Free Course
- [Cloudflare Learning — Application security](https://www.cloudflare.com/learning/) — broad free reading

### Best Advanced Resource
- [Cloudflare engineering blog](https://blog.cloudflare.com/) — real attack postmortems
- [Netflix tech blog — Resilience patterns](https://netflixtechblog.com/) — bulkheads, hedging

### Best Practice Project
Add to an existing API: `helmet` headers, body size limits, slow-loris timeout, Redis-backed token-bucket per-user + per-IP, structured logging of 429s, dashboards with attack signals (top IPs, top routes by 429 rate). Load-test with `k6`.

### Recommended Order to Learn
1. Threat model + attack categories
2. Rate limiting algorithms
3. Timeouts + backpressure
4. Resource limits + body size
5. ReDoS + JSON-bomb prevention
6. CDN/WAF + bot management

## Interview Questions
**Q. Difference between DoS and DDoS?**
A. DoS = single source. DDoS = distributed across many sources (botnet) — must be mitigated at the edge.

**Q. Token bucket vs sliding window?**
A. Token bucket allows bursts up to bucket size, then steady rate. Sliding window enforces strict average over a moving period.

**Q. Why is unauth heavy work dangerous?**
A. Lets unauthenticated users force expensive work (DB, search, ML) — easy to DoS.

**Q. What is ReDoS?**
A. Regex with catastrophic backtracking. Input like `aaaaa…!` against `(a+)+$` runs exponentially. Use linear-time regex engines (RE2) or audit patterns.

## Related
- [[Sandboxing]] · [[Remote Code Execution]] · [[Rate Limiting in System Design|Rate Limiting]]
