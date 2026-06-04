---
tags: [infra, language, intermediate]
---

# TypeScript

> JavaScript with a static type system. Compiles to plain JS. The de-facto language of modern frontend and most new Node backends.

## Why it matters
Catches a class of bugs at edit time. Refactoring at scale becomes safe. Editor tooling (autocomplete, "go to definition") becomes reliable. Most major libraries (React, Next.js, Vite, Vue, Svelte) are TS-first.

## Core ideas
- **Structural typing** — `{ name: string }` matches anything with that shape, regardless of class
- **Inference** — most types are auto-inferred; annotate boundaries (params, returns, exports)
- **Unions / intersections** — `A | B` (either), `A & B` (both)
- **Generics** — type parameters: `function id<T>(x: T): T`
- **Literal & template literal types** — `'red' | 'blue'`, `` `on${Capitalize<T>}` ``
- **Discriminated unions** — pattern of using a `type` field to narrow
- **`unknown` vs `any`** — `unknown` forces narrowing; `any` opts out (avoid)
- **Utility types** — `Partial<T>`, `Pick<T, K>`, `Omit<T, K>`, `Record<K, V>`, `ReturnType<F>`

## Example
```ts
type User = { id: string; email: string; role: 'user' | 'admin' };

function greet(u: User): string {
  return `Hello, ${u.email}`;
}

// Discriminated union
type Result<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

function unwrap<T>(r: Result<T>): T {
  if (r.ok) return r.data;
  throw new Error(r.error);
}

// Generic constraint
function pluck<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

## Real World Usage
- React + Vite / Next.js apps (TS by default in most templates)
- Node/Express APIs with shared types between client and server
- Library authoring (publishers ship `.d.ts` declarations)
- Schema-driven APIs with [Zod](https://zod.dev/), tRPC, or Prisma generating TS types from schema

## Common Mistakes
- `any` everywhere → forfeits all benefits
- Casting (`as`) instead of narrowing → lies to the compiler
- Implementing types that the inferer would have given you → noise
- Treating `==` warnings as TS issues — TS doesn't fix runtime null-safety
- Ignoring `strict: true` in `tsconfig` (turn it on)
- `noUncheckedIndexedAccess` left off → `arr[i]` is `T` but really `T | undefined`

## Edge cases worth knowing
- `Object.keys(o)` returns `string[]`, not `(keyof T)[]`
- Promises auto-flatten — `Promise<Promise<X>>` is `Promise<X>` to TS
- Function parameter bivariance — `(x: A) => void` accepts wider param types historically; `strictFunctionTypes` fixes it
- `never` as exhaustiveness guard in `switch` exhausts unions

## Prerequisites
- [[JavaScript MOC|JavaScript fundamentals]]
- [[Object Reference Behavior|Object Reference Behavior]]
- [[Promises|Promises]]

## What To Learn Next
- [[React MOC|React]] (TS-first)
- [[Next.js App Router]] (TS-first)
- [[Zustand]] · [[TanStack Query]] (TS-first APIs)
- Zod (runtime + types in one)

## Best Learning Resources

### Official Documentation
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) — canonical, well-written
- [TypeScript Playground](https://www.typescriptlang.org/play) — try anything live
- [tsconfig reference](https://www.typescriptlang.org/tsconfig) — every flag explained

### Best YouTube Resource
- [Matt Pocock](https://www.youtube.com/@mattpocockuk) — best TypeScript educator on the internet right now
- [Theo (t3.gg)](https://www.youtube.com/@t3dotgg) — practical full-stack TS
- [Jack Herrington](https://www.youtube.com/@jherr) — TS in React patterns

### Best Free Course
- [Total TypeScript Beginner's Tutorial (Matt Pocock)](https://www.totaltypescript.com/tutorials) — free interactive
- [Type-Level TypeScript](https://type-level-typescript.com/) — free course on advanced types
- [TypeScript Deep Dive (Basarat)](https://basarat.gitbook.io/typescript) — free book

### Best Advanced Resource
- [Total TypeScript (Matt Pocock, paid)](https://www.totaltypescript.com/) — definitive course
- [type-challenges (GitHub)](https://github.com/type-challenges/type-challenges) — gym for advanced types
- [TypeScript repo on GitHub](https://github.com/microsoft/TypeScript) — read PRs to see how the team thinks

### Best Practice Project
Take an existing JS project (one of yours from `7 Projects`) and migrate it to TS strict mode. Track every `// @ts-expect-error` and resolve it. Publish a small library with proper `.d.ts` exports and dual ESM/CJS builds.

### Recommended Order to Learn
1. Basic types + inference + tsconfig strict
2. Functions, generics, union/intersection
3. Narrowing (`typeof`, `in`, discriminated unions, custom guards)
4. Utility types (`Partial`, `Pick`, `Omit`, `Record`, `ReturnType`)
5. Conditional types + `infer`
6. Mapped + template literal types
7. Module declarations + `.d.ts`
8. Performance + `tsc --build` for monorepos

## Interview Questions
**Q. `unknown` vs `any` vs `never`?**
A. `unknown` accepts anything but forces narrowing before use (safe top type). `any` opts out of checking entirely. `never` is the bottom type — values that cannot exist (e.g., function that always throws).

**Q. What is structural typing?**
A. Type compatibility based on shape, not declared name. Two unrelated types with the same shape are interchangeable.

**Q. Difference between `interface` and `type`?**
A. Mostly interchangeable. `interface` declarations merge across files (declaration merging); `type` doesn't. Use `interface` for public shapes that may be extended, `type` for unions/computed types.

**Q. How does TypeScript narrow?**
A. Through control-flow analysis: `typeof`, `instanceof`, `in`, equality checks, custom user-defined type guards (`(x): x is T`), and discriminated unions.

**Q. What's a discriminated union?**
A. A union where each member has a unique literal field (`type: 'a'` vs `type: 'b'`); the compiler narrows the whole object based on that field.

**Q. `extends` in conditional types?**
A. `T extends U ? X : Y` — at the type level, asks "is T assignable to U?" Used with `infer` to extract types: `type ReturnType<F> = F extends (...a: any) => infer R ? R : never`.

**Q. Why prefer `as const` over plain literals?**
A. Without `as const`, arrays and object fields widen (`'red'` becomes `string`). `as const` keeps the narrow literal types — essential for `keyof` patterns.

## Related
- [[Rust]] · [[Go]] · [[JavaScript MOC|JavaScript MOC]] · [[Next.js App Router]]
