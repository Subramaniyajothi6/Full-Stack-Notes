---
tags: [typescript, intermediate, pattern]
---

# Discriminated Unions

> A union of object types with one shared literal field (the *discriminator*) so the compiler can narrow based on its value.

## The pattern
```ts
type Shape =
  | { kind: 'circle'; radius: number }
  | { kind: 'square'; size: number }
  | { kind: 'rect'; w: number; h: number };

function area(s: Shape) {
  switch (s.kind) {
    case 'circle': return Math.PI * s.radius ** 2;
    case 'square': return s.size ** 2;
    case 'rect':   return s.w * s.h;
  }
}
```
Inside each `case`, `s` is narrowed to the matching member.

## Exhaustive check
```ts
function area(s: Shape): number {
  switch (s.kind) {
    case 'circle': return ...;
    case 'square': return ...;
    case 'rect':   return ...;
    default: {
      const _: never = s;       // compile error if a new shape is added
      throw new Error('unhandled shape');
    }
  }
}
```

## Real World Usage
- Result types (`{ok: true; data} | {ok: false; error}`)
- State machines (`{status:'idle'} | {status:'loading'} | {status:'success'; data}`)
- Redux/Zustand action shapes
- API response variants
- Tree node types (AST)

## Common Mistakes
- Discriminator field must be literal type — `kind: string` won't narrow
- Forgetting `default: never` exhaustiveness — new variants silently fall through
- Sharing field names that conflict (e.g., one variant has `data: string`, another `data: number`)
- Discriminator can be any literal type (string, number, boolean) but consistency helps readability

## Prerequisites
- [[Union and Intersection Types]] · [[Type Narrowing]] · [[Primitives and Literal Types]]

## What To Learn Next
- [[Type Guards]] · [[Mapped Types]] · [[Conditional Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Discriminated Unions](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)

### Best YouTube Resource
- [Matt Pocock — Discriminated unions in real apps](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Type-Level TypeScript](https://type-level-typescript.com/)

### Best Advanced Resource
- [State Machines in TypeScript — XState docs](https://stately.ai/docs)

### Best Practice Project
Replace ad-hoc `if (data.error) ...` patterns in your code with a `Result<T,E>` discriminated union. Then add an exhaustive `match` helper.

### Recommended Order to Learn
1. Two-variant union (`Result`)
2. Switch + narrowing
3. Exhaustive `never` check
4. State machines
5. Generic discriminated unions (`State<T>`)

## Interview Questions
**Q. Why does narrowing rely on a literal field?**
A. The compiler matches each member by the unique literal value at that field; non-literal types don't differentiate.

**Q. What does `const _: never = x` accomplish?**
A. Forces a compile error when a new variant is added but not handled — exhaustiveness check.

## Related
- [[Type Narrowing]] · [[Type Guards]] · [[Union and Intersection Types]]
