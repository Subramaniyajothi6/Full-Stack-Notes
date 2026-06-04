---
tags: [moc, nextjs, framework]
---

# NextJS MOC

> React framework with file-based routing, server components, server actions, and an opinionated full-stack story.

## Foundations
- [[Next.js App Router]] — modern routing, RSC, streaming, server actions
- [[Pages Router]] — legacy `pages/` + `getStaticProps`/`getServerSideProps`
- [[React Server Components]] — engine underneath the App Router
- [[Routing Conventions]] — file/folder rules, groups, dynamic, parallel, intercepting

## Server logic
- [[Middleware]] — edge gates, redirects, rewrites
- [[Route Handlers]] — HTTP endpoints under `app/.../route.ts`
- [[Server Actions]] — typed RPC for forms and mutations

## Data + performance
- [[Data Fetching Patterns]] — server await, parallel, dedup, client query
- [[Caching and Revalidation]] — four caches + tag/path invalidation
- [[Streaming and Suspense]] — progressive HTML flush
- [[Edge Runtime]] — V8 isolates near users

## Ecosystem
- [[Convex]] — reactive backend that pairs with Next.js

## Suggested order
1. [[Next.js App Router]] (skim) → [[Routing Conventions]]
2. [[React Server Components]] → [[Data Fetching Patterns]]
3. [[Server Actions]] → [[Route Handlers]]
4. [[Middleware]] → [[Caching and Revalidation]]
5. [[Streaming and Suspense]]
6. [[Edge Runtime]]
7. [[Pages Router]] (only if maintaining legacy)
8. [[Convex]] (optional realtime backend)

## Roadmap to fill in
- [ ] Image, Font, Metadata APIs
- [ ] i18n + multi-locale routing
- [ ] App-level auth (Auth.js / Clerk integration)
- [ ] Parallel routes deep examples
- [ ] Intercepting routes (modal patterns)
- [ ] Static export
- [ ] ISR fine-tuning + on-demand revalidation
- [ ] Self-hosting Next.js (Node vs container)

## Related stacks
- [[React MOC]] · [[TypeScript MOC]] · [[Cloud MOC]]
- [[AI Engineering MOC]] — RSC pairs with AI SDK
- [[MERN Stack MOC]] — [[Full-Stack Auth Flow]] · [[Cross-Domain Cookies]]

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
