---
tags: [react, advanced, modern]
---

# Server Components

> Components that render on the server, ship zero JS for themselves to the client.

## Why
- Smaller bundles
- Data fetching closer to source
- Composable with Client Components

## Constraints
- No `useState`, `useEffect`, no event handlers
- Can `await` data directly
- Mark Client Components with `'use client'`

## Frameworks
- Next.js App Router
- Remix (similar via loaders)

## Common mistakes
- Importing client-only libs into server components
- Passing non-serializable props across the boundary

## Related
- [[Concurrent Rendering]] · [[Lazy Loading and Suspense]]

<!-- upgrade-notes.py auto-appended -->

## Prerequisites
- TODO: link prerequisite notes

## What To Learn Next
- TODO: link follow-up notes

## Real World Usage
- TODO: where this concept appears in production

## Best Learning Resources

### Official Documentation
- https://react.dev/ — TODO: pick the most relevant page and say why

### Best YouTube Resource
- TODO: e.g. Jack Herrington, Theo, Web Dev Simplified

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
