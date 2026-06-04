---
tags: [mern, integration, intermediate]
---

# API Contract

> The agreement between frontend and backend on URLs, methods, request/response shapes, and error formats.

## Why it matters
Without a clear contract you get drift: client expects field `userName`, server returns `username`. Multiply across 50 endpoints and feature velocity collapses.

## Three common styles
| Style | Strengths | Weaknesses |
|---|---|---|
| **REST** | Simple, cacheable, broad tooling | Over/under fetch, multiple round trips |
| **GraphQL** | Client picks shape, single endpoint, strong types | Caching is custom, N+1 risk, server complexity |
| **tRPC** | TS types flow client↔server with zero codegen | Locks both sides to TypeScript |

## REST contract checklist
- Plural resource URLs (`/users`, `/users/:id/posts`)
- Status codes used correctly (201 Created, 204 No Content, 409 Conflict)
- Consistent error shape: `{ error: { code, message, details? } }`
- Pagination convention (cursor vs offset) documented once
- Versioning strategy (`/v1`, header, or evolution-only)
- OpenAPI / Swagger spec checked into the repo

## GraphQL contract checklist
- Schema-first or code-first decided
- Naming conventions for queries, mutations, subscriptions
- Pagination: Relay-style cursor connections
- Error handling: typed errors in payload vs throws
- Persisted queries for production

## tRPC contract
- Routers grouped by domain (`userRouter`, `postRouter`)
- Input validated with Zod (becomes the contract)
- Procedures: `query` for reads, `mutation` for writes
- Shared `inferRouterInputs` / `inferRouterOutputs` types

## Real World Usage
- Public APIs ship REST + OpenAPI for tooling
- Internal SaaS dashboards often pick tRPC for velocity
- Mobile apps with bandwidth constraints favor GraphQL
- BFF (Backend for Frontend) layer compose multiple contracts

## Common Mistakes
- Returning different shapes for the same logical entity in different endpoints
- Mixing snake_case and camelCase across routes
- Versioning by adding fields silently (breaking implicit contracts)
- No examples in the spec → consumers guess
- Letting validation diverge: schema in client, different schema in server

## Prerequisites
- [[REST API Design]] · [[REST vs GraphQL]] · [[Validation]]

## What To Learn Next
- [[Type Sharing]] · [[Form Lifecycle]] · [[Cross-Domain Cookies]]

## Best Learning Resources

### Official Documentation
- [OpenAPI Specification](https://swagger.io/specification/) — the REST contract standard
- [GraphQL docs](https://graphql.org/learn/)
- [tRPC docs](https://trpc.io/docs)

### Best YouTube Resource
- [Theo — REST vs GraphQL vs tRPC](https://www.youtube.com/@t3dotgg)
- [Hussein Nasser — API design](https://www.youtube.com/@hnasr)

### Best Free Course
- [Stoplight — OpenAPI tutorial](https://stoplight.io/api-types/openapi)
- [tRPC quickstart](https://trpc.io/docs/quickstart)

### Best Advanced Resource
- [GraphQL best practices — Apollo](https://www.apollographql.com/docs/technotes/)
- [API Design Patterns (book) — JJ Geewax](https://www.manning.com/books/api-design-patterns)

### Best Practice Project
Spec a `/posts` API in OpenAPI, generate types for both Node server and React client. Then port the same to tRPC. Note the file/code overhead in each approach.

### Recommended Order to Learn
1. REST principles + OpenAPI
2. Error shapes + status codes
3. GraphQL schema + queries
4. tRPC for internal apps
5. Pagination + filtering conventions
6. Versioning strategies

## Interview Questions
**Q. When pick GraphQL over REST?**
A. Many client variants needing different shapes; deeply nested relations; rapid client-driven iteration.

**Q. tRPC vs GraphQL?**
A. tRPC: zero schema, TS-only, fastest DX. GraphQL: language-agnostic, federated services, public APIs.

**Q. How do you version a REST API?**
A. URL prefix (`/v1`), header (`Accept: application/vnd.api.v2+json`), or additive evolution. Most teams pick URL.

## Related
- [[REST API Design]] · [[REST vs GraphQL]] · [[Type Sharing]] · [[Validation]]
