---
tags: [infra, frontend, intermediate]
---

# Pages Router

> The original Next.js routing system: `pages/` directory + per-page data-fetching functions. Still widely used in production.

## Why it matters
Massive existing codebase. New projects default to App Router but understanding Pages helps maintain old apps and reason about Next's evolution.

## Core ideas
- **`pages/` directory** — file-based routes
- **Data-fetching APIs**:
  - `getStaticProps` — SSG at build time
  - `getStaticPaths` — dynamic SSG params
  - `getServerSideProps` — SSR per request
  - `getInitialProps` — legacy
- **`_app.tsx`** — root component; `_document.tsx` — HTML template
- **API routes** — `pages/api/*.ts` export default handler
- **ISR** — `revalidate: 60` re-generates on demand

## Example
```ts
// pages/posts/[id].tsx
export const getStaticPaths: GetStaticPaths = async () => ({
  paths: [], fallback: 'blocking'
});
export const getStaticProps: GetStaticProps = async ({ params }) => {
  const post = await fetchPost(params!.id as string);
  return { props: { post }, revalidate: 60 };
};
```

## Real World Usage
- Marketing sites: `getStaticProps` + ISR
- Dashboards: `getServerSideProps`
- API endpoints colocated with frontend

## Common Mistakes
- Returning non-serializable values (Dates, classes) from `getStaticProps`
- Doing client-side DB calls in `getServerSideProps` thinking it's the browser
- Putting auth checks only in `pages/api` (skipping middleware)
- Mixing App Router and Pages Router data calls without understanding precedence

## Prerequisites
- [[React MOC|React]]

## What To Learn Next
- [[Next.js App Router]] · [[Edge Computing]]

## Best Learning Resources

### Official Documentation
- [Next.js Pages Router docs](https://nextjs.org/docs/pages) — the source
- [Next.js — Migrating to App Router](https://nextjs.org/docs/app/building-your-application/upgrading/app-router-migration)

### Best YouTube Resource
- [Lee Robinson — Next.js basics](https://www.youtube.com/@leerob)
- [Web Dev Simplified — Next.js](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [Next.js Learn (legacy Pages tracks)](https://nextjs.org/learn) — earlier paths still teach pages
- [The Net Ninja — Next.js Pages Router](https://www.youtube.com/c/TheNetNinja)

### Best Advanced Resource
- [Vercel blog — Incremental Static Regeneration](https://vercel.com/blog/nextjs-server-side-rendering-vs-static-generation)

### Best Practice Project
Convert a small static site to Pages Router with ISR: marketing pages SSG-built, blog with ISR (revalidate 60s), `/api/contact` for form handling. Then port the same app to App Router as a comparison exercise.

### Recommended Order to Learn
1. Routing + dynamic routes
2. SSG (`getStaticProps`/`getStaticPaths`)
3. SSR (`getServerSideProps`)
4. ISR
5. API routes
6. Migration paths to App Router

## Interview Questions
**Q. Difference between SSG and SSR?**
A. SSG renders at build time, infinitely cacheable. SSR renders per request — fresh data, slower TTFB.

**Q. What's ISR?**
A. Static pages regenerated in the background after a TTL — best of both worlds.

**Q. Why isn't `getServerSideProps` available in App Router?**
A. App Router uses async server components which fetch directly during render, replacing the prop function pattern.

## Related
- [[Next.js App Router]] · [[React Server Components]]
