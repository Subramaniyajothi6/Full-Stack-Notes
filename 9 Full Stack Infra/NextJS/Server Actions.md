---
tags: [nextjs, intermediate, pattern]
---

# Server Actions

> Async functions tagged `'use server'`. The framework exposes them as RPC endpoints that you call from client or server components — typed end-to-end.

## Inline action
```tsx
// app/posts/page.tsx (server component)
import { db } from '@/lib/db';

async function createPost(formData: FormData) {
  'use server';
  const title = formData.get('title') as string;
  await db.post.create({ data: { title } });
}

export default function Page() {
  return (
    <form action={createPost}>
      <input name="title" />
      <button>Create</button>
    </form>
  );
}
```

## Imported from a separate file
```ts
// app/actions/posts.ts
'use server';
import { db } from '@/lib/db';
import { z } from 'zod';

const Schema = z.object({ title: z.string().min(1).max(120) });

export async function createPost(input: unknown) {
  const data = Schema.parse(input);
  return db.post.create({ data });
}
```
```tsx
// Client component
'use client';
import { createPost } from '@/app/actions/posts';
async function onSubmit(fd: FormData) {
  await createPost({ title: fd.get('title') });
}
```

## Pending UI
```tsx
'use client';
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? '…' : 'Create'}</button>;
}
```

## Revalidate after mutation
```ts
import { revalidatePath, revalidateTag } from 'next/cache';

export async function deletePost(id: string) {
  'use server';
  await db.post.delete({ where: { id } });
  revalidatePath('/posts');         // refresh that route's cache
  revalidateTag('posts');           // refresh by tag
}
```

## Real World Usage
- Form submissions without writing a `POST` handler
- Optimistic UI mutations with `useTransition` / `useOptimistic`
- Server-side typed RPC
- Replacing tRPC for Next-only apps

## Common Mistakes
- Returning non-serializable values (Date, Map, classes that don't serialize)
- Forgetting to validate input — Server Actions are *public* endpoints
- Missing `revalidatePath` / `revalidateTag` after mutation → stale UI
- Skipping CSRF concerns when also exposing classic POST handlers
- Calling an action inside a `useEffect` (it'll fire on render)

## Prerequisites
- [[Next.js App Router]] · [[React Server Components]] · [[Form Lifecycle]]

## What To Learn Next
- [[Caching and Revalidation]] · [[Route Handlers]] · [[Type Sharing]]

## Best Learning Resources

### Official Documentation
- [Next.js — Server Actions and Mutations](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)
- [React — `useFormStatus`, `useFormState`, `useOptimistic`](https://react.dev/reference/react-dom/hooks/useFormStatus)

### Best YouTube Resource
- [Theo — Server Actions deep dive](https://www.youtube.com/@t3dotgg)
- [Lee Robinson — Server Actions](https://www.youtube.com/@leerob)
- [Jack Herrington — Server Actions patterns](https://www.youtube.com/@jherr)

### Best Free Course
- [Next.js Learn — Server Actions chapter](https://nextjs.org/learn)

### Best Advanced Resource
- [Sam Selikoff — Optimistic UI with Server Actions](https://www.youtube.com/@SamSelikoff)

### Best Practice Project
Build a todo app: list (server component) + form (server action `addTodo`) + optimistic update via `useOptimistic` + `revalidateTag('todos')`. Validate input with Zod.

### Recommended Order to Learn
1. Inline action in server component
2. Imported action with Zod validation
3. `useFormStatus` for pending state
4. `useFormState` for server-returned errors
5. `useOptimistic` for instant UI
6. Revalidation (path + tag)
7. Calling actions from client components / `startTransition`

## Interview Questions
**Q. How does a Server Action reach the server?**
A. The framework wires it to a hidden POST endpoint; the client sends a fetch with the action id + serialized args.

**Q. Why validate Server Action input?**
A. They're exposed endpoints. Anyone can call them with any payload.

**Q. Why revalidatePath after a mutation?**
A. The cached server render of that path is stale; the next request must re-render with fresh data.

## Related
- [[Next.js App Router]] · [[React Server Components]] · [[Caching and Revalidation]] · [[Form Lifecycle]]
