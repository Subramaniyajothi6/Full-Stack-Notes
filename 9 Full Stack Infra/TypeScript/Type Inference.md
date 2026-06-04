---
tags: [typescript, beginner, concept]
---

# Type Inference

> TypeScript figures out types from your code so you don't have to annotate everything.

## Why it matters
Inferred types are the path of least resistance. Annotating only at boundaries (function params, returns, exports) keeps code clean while preserving safety.

## Where inference works
```ts
const n = 42;            // n: 42 (literal)
let m = 42;              // m: number (widened)
const arr = [1, 2, 3];   // number[]
const obj = { a: 1 };    // { a: number }
const f = (x: number) => x * 2;  // (x: number) => number — return inferred
```

## Best-practice rule
**Annotate inputs (params, exports). Infer outputs.**
```ts
export function getUser(id: string): User {        // explicit return for public APIs
  return userMap.get(id)!;
}
function helper(x: number) {                       // internal — let it infer
  return x.toFixed(2);
}
```

## Contextual typing
TS infers parameter types from context:
```ts
[1, 2, 3].map(n => n * 2);                          // n: number, no annotation
const handler: MouseEventHandler = (e) => e.clientX;// e: React.MouseEvent
```

## Real World Usage
- Inline callbacks (`map`, `filter`, `reduce`) — never annotate
- Library API surface — explicitly annotate
- Hooks return tuples — annotate to control narrowing

## Common Mistakes
- Over-annotating internal vars (visual clutter, no benefit)
- Letting `let` widen primitives that should stay literal — use `as const`
- Returning conditional types without explicit annotation (inference fails on edge cases)
- Missing return type on exports → consumer sees inferred shape that may shift on internal refactor

## Prerequisites
- [[TypeScript]] · [[../JavaScript/Data Types]]

## What To Learn Next
- [[Primitives and Literal Types]] · [[Type Narrowing]] · [[Generics]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Type Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html)

### Best YouTube Resource
- [Matt Pocock — TS inference tips](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript Beginner's Tutorial](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [TypeScript Deep Dive — Type Inference chapter](https://basarat.gitbook.io/typescript/)

### Best Practice Project
Take any of your JS files; remove all explicit types except function params/returns at module boundaries; verify the IDE still shows correct shapes everywhere.

### Recommended Order to Learn
1. Primitive vs literal inference
2. Object + array literal inference
3. Contextual typing in callbacks
4. Annotation rule (boundaries only)
5. `as const` to lock inference

## Interview Questions
**Q. Why does `let x = 42` give `number` but `const x = 42` give `42`?**
A. `let` widens to the type; `const` is immutable so the literal is preserved.

**Q. When should you explicitly annotate return types?**
A. Public/exported functions — to lock the contract; conditional/recursive types where inference is fragile.

## Related
- [[Primitives and Literal Types]] · [[Type Narrowing]] · [[Type vs Interface]]
