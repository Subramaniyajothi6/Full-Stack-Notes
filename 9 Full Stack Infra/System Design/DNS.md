---
tags: [infra, internet, beginner]
---

# DNS

> The internet's phone book — translates domain names (`api.example.com`) into IP addresses.

## Why it matters
Every request starts with DNS resolution. Slow or misconfigured DNS = slow page loads or outages. Engineers must understand DNS for deployments, CDNs, email, and security.

## Core ideas
- **Resolver** — your OS asks a recursive resolver (8.8.8.8, 1.1.1.1) for the answer
- **Zones & records** — `A` (IPv4), `AAAA` (IPv6), `CNAME` (alias), `MX` (mail), `TXT` (verification, SPF), `NS` (nameservers), `SRV` (services)
- **TTL** — how long a record may be cached
- **Authoritative vs recursive** — authoritative servers own a zone; recursive servers fetch and cache for clients
- **Anycast** — same IP advertised from many edges; client hits nearest

## Example
```
dig +short example.com           # quick A record
dig example.com NS               # nameservers
dig example.com TXT              # SPF / domain verification
```

## Real World Usage
- Pointing a domain at Vercel/Netlify (CNAME or ALIAS)
- Email setup: MX + SPF + DKIM + DMARC
- Multi-region failover via health-checked DNS (Route 53)
- DNS-based service discovery in microservices

## Common Mistakes
- Setting CNAME on the apex (`example.com`) — not allowed by spec; use ALIAS/ANAME
- Forgetting low TTL before a migration (cache lags)
- Mixing apex A records and CDN — breaks email/SSL
- Wildcard `*` records that swallow typos

## Prerequisites
- [[Client-Server Model|Client/Server Model]]
- [[HTTP and HTTPS|HTTP & HTTPS]]

## What To Learn Next
- [[CDN|CDN]] · [[Edge Computing]] · [[AWS]]

## Best Learning Resources

### Official Documentation
- [Cloudflare Learning Center — DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) — clearest engineering primer
- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) — the spec, dense but canonical

### Best YouTube Resource
- [ByteByteGo — How DNS Works](https://www.youtube.com/c/ByteByteGo) — visual, system-design framing
- [Hussein Nasser — DNS series](https://www.youtube.com/@hnasr) — packet-level depth

### Best Free Course
- [Cloudflare Learning Path: Networking](https://www.cloudflare.com/learning/) — broad fundamentals, free

### Best Advanced Resource
- [Julia Evans — Implement DNS in a weekend](https://implement-dns.wizardzines.com/) — write the resolver, learn the protocol

### Best Practice Project
Buy a cheap domain, host a static site on Vercel, configure email with SPF/DKIM/DMARC, then add a subdomain pointing to a Cloudflare worker. End with `dig` walkthroughs.

### Recommended Order to Learn
1. Resolver flow + record types
2. TTL, caching, propagation
3. Apex vs subdomain limitations
4. Email: MX/SPF/DKIM/DMARC
5. Anycast + GeoDNS for performance

## Interview Questions
**Q. What happens when I type `example.com` in my browser?**
A. Browser checks cache → OS cache → recursive resolver → root → TLD → authoritative server → returns A record → TCP/TLS handshake → HTTP request.

**Q. Why can't a CNAME live at the apex?**
A. RFC forbids CNAME alongside other records; apex needs `SOA`/`NS`. Solutions: ALIAS/ANAME (Route 53/Cloudflare flatten internally).

**Q. Difference between A and AAAA?**
A. A = IPv4 (32-bit), AAAA = IPv6 (128-bit).

**Q. How does DNS-based load balancing work?**
A. Resolver returns one of several IPs (round-robin) or the IP of the nearest edge (GeoDNS/anycast).

## Related
- [[CDN|CDN]] · [[HTTP and HTTPS|HTTP & HTTPS]]
