---
tags: [system-design, beginner, concept]
---

# HTTP and HTTPS

## HTTP
Text-based request/response over TCP.
- Methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
- Status: 1xx info · 2xx success · 3xx redirect · 4xx client · 5xx server

## HTTPS
HTTP over TLS. Encrypts in transit, authenticates server (and optionally client).

## Versions
- HTTP/1.1 — text, head-of-line blocking per connection
- HTTP/2 — binary, multiplexed streams
- HTTP/3 — over QUIC (UDP), better mobile/lossy networks

## Related
- [[REST API Design|REST API Design]] · [[Helmet and Security|Helmet and Security]]

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
- https://aws.amazon.com/architecture/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. ByteByteGo, Hussein Nasser

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
