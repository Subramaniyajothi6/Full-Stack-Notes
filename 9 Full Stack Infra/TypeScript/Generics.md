---
tags: [typescript, intermediate, concept]
---

# Generics

> Type parameters that let a function or type work over many shapes while preserving the relationship between input and output.

## Basics
```ts
function id<T>(x: T): T { return x; }

const a = id(1);       // a: number
const b = id('hi');    // b: string
```

## Generic interfaces
```ts
interface Box<T> { value: T }
const x: Box<number> = { value: 1 };
```

## Generic constraints — see [[Generic Constraints]]
```ts
function lengthy<T extends { length: number }>(x: T) { return x.length; }
```

## Default type parameters
```ts
type Action<T = void> = { type: string; payload: T };
type Boot = Action;            // payload: void
type Click = Action<{x: number; y: number}>;
```

## Inference vs explicit
```ts
id(42);          // T inferred as number
id<string>('x'); // T explicitly string
```
Annotate when inference picks something wider than you want.

## Real World Usage
- Containers (`Array<T>`, `Promise<T>`, `Map<K,V>`)
- API helpers (`function get<T>(url): Promise<T>`)
- Form / hook libraries (`useState<T>`, `useForm<T>`)
- Utility types ([[Utility Types]])

## Common Mistakes
- Adding a type parameter that's used only once (it's just `unknown`/`any` in disguise — you don't need a generic)
- Forgetting the `extends` constraint when you need a property
- Inference forced into the wrong shape — use defaults or explicit args
- Naming convention: `T` for one, `T,U,V` for many, `TKey/TValue` for clarity

## Prerequisites
- [[Type Inference]] · [[Union and Intersection Types]]

## What To Learn Next
- [[Generic Constraints]] · [[Utility Types]] · [[Mapped Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)

### Best YouTube Resource
- [Matt Pocock — Generics deep dive](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript — Generics workshops](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [Type-Level TypeScript — generics module](https://type-level-typescript.com/)

### Best Practice Project
Write a `useFetch<T>(url): { data: T; loading; error }` hook. Use it in three components with different `T`s; verify zero `any` ends up in the consumer code.

### Recommended Order to Learn
1. Generic functions
2. Generic interfaces / types
3. Constraints (`extends`)
4. Default type params
5. Inference vs explicit
6. Higher-order generics (returning generic functions)

## Interview Questions
**Q. When do you need a generic vs `any`?**
A. Use generics when input and output relate (return type depends on input). Use `any` (or better, `unknown`) only at hard untyped boundaries.

**Q. Single-use generic — code smell?**
A. Yes, often. If `T` only appears once it's not relating anything.

## Related
- [[Generic Constraints]] · [[Utility Types]] · [[Conditional Types]]
