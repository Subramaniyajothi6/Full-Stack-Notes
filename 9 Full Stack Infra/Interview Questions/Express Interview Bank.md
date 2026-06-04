---
tags: [interview, express]
---

# Express Interview Bank

**Q. What is middleware?**
A. Function `(req, res, next)` running in order. Can pass through, end response, or signal error. See [[Middleware]].

**Q. How does error middleware differ?**
A. 4-arg signature `(err, req, res, next)`. Express auto-routes errors here.

**Q. Order of middleware matters?**
A. Yes — body parser before routes that read `req.body`; auth before protected; error handler last.

**Q. JWT vs session cookies?**
A. See [[Sessions vs JWT]]. JWT stateless but harder to revoke; sessions need shared store.

**Q. Where do you put JWT in browser?**
A. httpOnly cookie (XSS-safer). Localstorage exposes to any script.

**Q. CORS — what is it?**
A. Browser policy blocking cross-origin requests. Server opt-in via headers. See [[CORS]].

**Q. What does Helmet do?**
A. Sets security headers (CSP, HSTS, no-sniff, frame options). See [[Helmet and Security]].

**Q. How to handle async errors in Express?**
A. Wrap handler in try/catch and `next(err)`, or use `express-async-errors`, or wrap with `asyncHandler` util.

**Q. REST design principles?**
A. Resources in URLs, HTTP verbs for actions, proper status codes, idempotent PUT/DELETE, JSON bodies, consistent shapes. See [[REST API Design]].

**Q. Rate limiting in distributed setup?**
A. Redis-backed counters; algorithm choice (token bucket, sliding window). See [[Rate Limiting]].

**Q. Validate user input — why and how?**
A. All input is untrusted. Validate type/shape with Zod/Joi; reject with 400. See [[Validation]].

**Q. Graceful shutdown?**
A. Listen to SIGTERM, stop accepting new connections, finish in-flight, close DB pool, exit.
