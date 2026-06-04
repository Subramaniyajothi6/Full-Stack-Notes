---
tags: [nextjs, advanced, performance]
---

# Streaming and Suspense

> Flush HTML chunks progressively so the user sees something *now*; slow data resolves into placeholder UI later.

## Loading file convention
```
app/dashboard/
  page.tsx
  loading.tsx     # automatic Suspense fallback for this segment
```
Next wraps `page.tsx` in a `<Suspense fallback={<Loading />}>` boundary.

## Manual Suspense boundaries
```tsx
import { Suspense } from 'react';

export default function Dashboard() {
  return (
    <>
      <Header />
      <Suspense fallback={<Skeleton kind="chart" />}>
        <Chart />            // async, fetches data
      </Suspense>
      <Suspense fallback={<Skeleton kind="list" />}>
        <RecentList />
      </Suspense>
    </>
  );
}

async function Chart() {
  const data = await db.metric.findMany();   // server component awaits
  return <BarChart data={data} />;
}
```
Each boundary streams independently.

## error.tsx
```
app/dashboard/error.tsx     # caught by the framework, shows fallback
```
Co-locates error boundary per segment.

## not-found.tsx
```
app/dashboard/not-found.tsx
```
For `notFound()` calls from server components.

## When NOT to wrap
Wrapping the entire page in one Suspense = single late flush. Defeat: split into independent boundaries so headers / nav render instantly while slower sections stream.

## Real World Usage
- Dashboards with multiple widgets
- Marketing pages with above-the-fold static + below-the-fold dynamic
- Search results page (form instant, results stream)
- Skeleton loaders that match final layout (no CLS)

## Common Mistakes
- One giant Suspense at the page root → no streaming win
- Loading components that change layout drastically (CLS)
- Awaiting all data sequentially in one server component (parallelize with `Promise.all`)
- Suspense fallback that hits the network (cascade)
- Missing `error.tsx` → unhandled errors crash whole route

## Prerequisites
- [[Next.js App Router]] · [[React Server Components]] · [[Lazy Loading and Suspense]]

## What To Learn Next
- [[Caching and Revalidation]] · [[Edge Runtime]]

## Best Learning Resources

### Official Documentation
- [Next.js — Loading UI and Streaming](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming)
- [React — Suspense](https://react.dev/reference/react/Suspense)

### Best YouTube Resource
- [Lee Robinson — Streaming + Suspense](https://www.youtube.com/@leerob)
- [Jack Herrington — RSC + streaming](https://www.youtube.com/@jherr)

### Best Free Course
- [Next.js Learn — Loading UI chapter](https://nextjs.org/learn)

### Best Advanced Resource
- [React conf — streaming RSC talks](https://www.youtube.com/results?search_query=react+server+components+streaming)

### Best Practice Project
Build a 3-widget dashboard. Wrap each in its own Suspense. Add an artificial 1-second latency to one — verify the others render at TTFB while it streams in.

### Recommended Order to Learn
1. `loading.tsx` segment convention
2. Manual `<Suspense>` boundaries
3. Parallel data fetching with `Promise.all`
4. `error.tsx` + `not-found.tsx`
5. Skeleton design (no CLS)
6. Streaming Server Actions (return progressive results)

## Interview Questions
**Q. How does streaming improve perceived perf?**
A. Header + above-the-fold ship to the browser at TTFB; slow parts arrive later — total LCP and INP improve.

**Q. Suspense fallback rules?**
A. Must render synchronously; can't suspend itself. Should match the final layout to avoid CLS.

## Related
- [[Next.js App Router]] · [[React Server Components]] · [[Lazy Loading and Suspense]] · [[Caching and Revalidation]]
