# Missing Topics

A reference of important topics not yet covered in this vault, organized by priority.

---

## Priority 1 — Essential

### GraphQL
- Implementation guide (REST vs GraphQL is covered in theory only)
- Schema design, resolvers, mutations
- Apollo Server / Apollo Client integration with MERN

### Observability & Monitoring
- OpenTelemetry instrumentation
- Prometheus + Grafana setup
- Structured logging with correlation IDs
- Distributed tracing
- Sentry / Datadog / New Relic integration

### Security
- OWASP Top 10
- XSS, CSRF, SQL Injection prevention
- Security headers deep dive (beyond Helmet)
- Input validation strategies
- Secrets rotation

### Search Integration
- Elasticsearch basics and integration
- Meilisearch / Typesense as alternatives
- Full-text search patterns in MERN

### API Documentation
- OpenAPI / Swagger guide
- API versioning strategies
- Deprecation policies

### Error Handling Patterns
- Structured error codes across the stack
- Error recovery strategies
- Class-based custom errors in Express

### Database Migrations (In Depth)
- Prisma migration patterns
- Knex migration patterns
- Schema evolution strategies

---

## Priority 2 — Advanced but Practical

### DSA (No Dedicated Files Yet)
- Linked lists, stacks, queues
- Tries, graphs, union-find
- Topological sort, greedy algorithms
- Sorting algorithms (mergesort, quicksort, heapsort)
- Bit manipulation
- Dijkstra, Bellman-Ford, Floyd-Warshall
- Segment tree, Fenwick tree
- String algorithms (KMP, Rabin-Karp)

### TypeScript (Advanced)
- Function overloads
- Decorators (TypeScript 5)
- Branded / nominal types
- Abstract classes and class types
- React-specific TypeScript patterns
- Advanced utility type patterns (DeepPartial, etc.)
- JS to TS migration strategies

### Next.js (Missing)
- Metadata API (comprehensive guide)
- i18n and multi-locale routing
- Auth.js / Clerk detailed integration
- Self-hosting Next.js (Node vs container)
- ISR fine-tuning
- Web Vitals monitoring
- Draft/preview mode

### Redis (Advanced)
- HyperLogLog (approximate cardinality)
- Redis JSON module
- Redis Search (FT.*)
- Performance tuning (maxmemory, eviction policies)
- Redis Sentinel operations
- Slowlog and latency monitoring

### PostgreSQL (Advanced)
- Triggers and stored procedures
- Table partitioning
- Materialized views
- LISTEN / NOTIFY for pub/sub
- Backup and recovery (pg_dump, WAL archiving)
- Point-in-time recovery
- Custom data types and domains

### DevOps (Missing)
- Kubernetes and Helm in depth
- Argo CD / GitOps
- Blue-green and canary deployments
- Observability: Prometheus, Grafana, OpenTelemetry
- Secrets management: Vault, SOPS
- Pod security policies
- Container scanning and security

### Webhooks
- Retry logic
- Signature verification (HMAC)
- Idempotency keys
- Delivery guarantees

### MongoDB (Advanced)
- Change streams
- TTL indexes
- Geospatial queries
- GridFS for large files
- Full-text search indexing
- Schema migration strategies

---

## Priority 3 — Worth Adding Eventually

### tRPC
- No notes at all — popular in Next.js / MERN ecosystem
- tRPC vs REST vs GraphQL comparison

### Rate Limiting Algorithms
- Token bucket
- Leaky bucket
- Sliding window
- Redis-based implementation

### Event Sourcing / CQRS
- Event-driven architecture patterns
- Audit trail implementation
- SAGA and compensation patterns

### Git (Advanced)
- Git internals (objects, refs, packfiles)
- Conventional commits and semantic-release
- Monorepo tools (Turborepo, Nx)
- Git LFS for binaries
- Git bisect for debugging

### Testing (Gaps)
- Property-based testing (fast-check)
- Accessibility testing (a11y)
- Storybook and Chromatic
- Test data factories
- Performance testing (k6, Lighthouse)

### AI Engineering (Gaps)
- Streaming UIs deep dive
- Token and cost budgeting
- Voice agents (Realtime APIs)
- Hybrid search (keyword + semantic)
- Agent orchestration frameworks (LangGraph)
- Reranking strategies (Cohere, cross-encoders)

### Cloud (Gaps)
- RDS and managed databases on AWS
- DynamoDB deep dive
- CloudWatch and alerting setup
- Auto-scaling policies
- VPC peering and transit gateways
- CloudFront caching strategies

### System Design (Advanced)
- Consensus algorithms (Raft, Paxos)
- Distributed transactions and SAGA
- Consistent hashing
- Circuit breaker and bulkhead patterns
- Idempotency and exactly-once semantics
- Backpressure handling

---

## Quick Summary

| Section | Key Gap |
|---|---|
| GraphQL | No implementation notes at all |
| Observability | Missing across every section |
| Security | No OWASP or prevention guide |
| DSA | ~8 topics have no dedicated files |
| TypeScript | Missing advanced patterns |
| Next.js | Auth, i18n, self-hosting missing |
| DevOps | Kubernetes/Helm barely covered |
| tRPC | Zero coverage |
| Search | Elasticsearch/Meilisearch missing |
| AI Engineering | Streaming, voice, hybrid search missing |
