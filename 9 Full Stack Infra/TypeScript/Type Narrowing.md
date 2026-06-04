---
tags: [typescript, intermediate, concept]
---

# Type Narrowing

> Refining a wider type to a narrower one based on runtime checks. The compiler tracks branches.

## Built-in narrowing
```ts
function f(x: string | number) {
  if (typeof x === 'string') {
    x.toUpperCase();   // x: string here
  } else {
    x.toFixed(2);      // x: number here
  }
}
```

## Tools the compiler uses
- `typeof` — primitives
- `instanceof` — class instances
- `in` — property check on object types
- Equality (`===`, `!==`) with literals
- Truthy/falsy checks
- Custom **type guard** functions (see [[Type Guards]])
- Discriminated unions (see [[Discriminated Unions]])

## `in` for shape detection
```ts
type Cat = { meow: () => void };
type Dog = { bark: () => void };
function speak(a: Cat | Dog) {
  if ('meow' in a) a.meow();
  else a.bark();
}
```

## Truthy narrowing
```ts
function len(s?: string) {
  if (s) s.length;      // s: string here
  // s: string | undefined here
}
```

## Real World Usage
- Distinguishing API success vs error payloads
- Form state machines (`'idle' | 'loading' | 'success' | 'error'`)
- Optional chaining alternatives
- Working with DOM events

## Common Mistakes
- `typeof null === 'object'` — null sneaks through `typeof === 'object'` checks
- `Array.isArray()` is the only safe array check (not `typeof === 'object'`)
- Narrowing inside async/await may be lost across `await` boundaries
- Mutating a narrowed variable inside a callback widens it back

## Prerequisites
- [[Union and Intersection Types]] · [[Primitives and Literal Types]]

## What To Learn Next
- [[Type Guards]] · [[Discriminated Unions]] · [[unknown vs any vs never]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)

### Best YouTube Resource
- [Matt Pocock — Narrowing & control flow analysis](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript — Narrowing chapters](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [Effective TypeScript — Items 28-30](https://effectivetypescript.com/) — narrowing patterns

### Best Practice Project
Write a `parseConfig(raw: unknown): Config | null` function that narrows from `unknown` step by step using `in`, `typeof`, and `Array.isArray`.

### Recommended Order to Learn
1. typeof + instanceof + `in`
2. Truthy + equality narrowing
3. Discriminated unions
4. Custom type guards
5. Assertion functions (`asserts`)
6. `never` for exhaustiveness

## Interview Questions
**Q. Why is `Array.isArray` safer than `typeof x === 'object'`?**
A. Arrays are typeof `'object'`, but so are null, plain objects, and Maps. `Array.isArray` is the only correct check.

**Q. What's control-flow analysis?**
A. The compiler tracks which type a variable has on each branch based on the checks executed before that branch.

## Related
- [[Type Guards]] · [[Discriminated Unions]] · [[Union and Intersection Types]]
