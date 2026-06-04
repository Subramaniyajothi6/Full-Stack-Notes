---
tags: [typescript, advanced, syntax]
---

# Conditional Types

> `T extends U ? X : Y` — ask at the type level "is T assignable to U?" and pick X or Y.

## Basics
```ts
type IsString<T> = T extends string ? true : false;
type A = IsString<'hi'>;   // true
type B = IsString<42>;     // false
```

## The `infer` keyword
Capture a sub-type from a wider type:
```ts
type ReturnType<F> = F extends (...args: any[]) => infer R ? R : never;
type ElementType<A> = A extends Array<infer E> ? E : never;
type Promised<P> = P extends Promise<infer V> ? V : P;
```

## Distributive over unions
When the checked type is a "naked" type parameter, a union distributes:
```ts
type ToArray<T> = T extends any ? T[] : never;
type X = ToArray<string | number>;   // string[] | number[]
```
Wrap in `[T]` to **disable** distribution:
```ts
type ToArrayNonDist<T> = [T] extends [any] ? T[] : never;
type Y = ToArrayNonDist<string | number>; // (string | number)[]
```

## Real World Usage
- Library types (`ReturnType`, `Awaited`, `Parameters`)
- Routing — derive params from a path string
- API clients — input → output type relationships
- Branded types

## Common Mistakes
- Hitting recursion limits on deeply nested conditionals
- Forgetting union distribution → unexpected single-branch result
- Using `extends` for inheritance vs at the type level — different positions
- `infer` placement matters; only valid in the `extends` clause

## Prerequisites
- [[Generics]] · [[Generic Constraints]] · [[Mapped Types]]

## What To Learn Next
- [[Template Literal Types]] · [[keyof and Index Access]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)

### Best YouTube Resource
- [Matt Pocock — Conditional types & infer](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Type-Level TypeScript — Conditional types module](https://type-level-typescript.com/)

### Best Advanced Resource
- [type-challenges (medium/hard)](https://github.com/type-challenges/type-challenges)

### Best Practice Project
Implement `ParseRoute<'/users/:id/posts/:postId'>` that yields `{ id: string; postId: string }` using template literal types + `infer`.

### Recommended Order to Learn
1. `extends ? :` basics
2. `infer` to capture sub-types
3. Distribution over unions
4. Disabling distribution with `[T]`
5. Recursion + tail-recursive patterns

## Interview Questions
**Q. What does `infer` do?**
A. Captures a sub-type within a conditional `extends` clause for use in the true-branch.

**Q. Why does `T extends any ? T[] : never` distribute over unions?**
A. Because the checked type is a "naked" type parameter; TS applies the conditional to each member separately.

## Related
- [[Mapped Types]] · [[Generics]] · [[Template Literal Types]]
