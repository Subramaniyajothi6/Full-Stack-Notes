---
tags: [typescript, intermediate, concept]
---

# Generic Constraints

> `<T extends X>` says "T can be any type, but it must at least be X-shaped." Lets you safely access properties on a generic.

## Basics
```ts
function pickProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const u = { id: 1, name: 'a' };
pickProp(u, 'id');      // number
pickProp(u, 'name');    // string
pickProp(u, 'missing'); // compile error
```

## Constrained shape
```ts
function loudest<T extends { volume: number }>(items: T[]): T {
  return items.reduce((a, b) => a.volume > b.volume ? a : b);
}
```

## Constrained vs default
```ts
type Box<T extends string = 'hi'> = { v: T };
type A = Box;            // 'hi'
type B = Box<'world'>;
```

## Bounded by union
```ts
type Status = 'open' | 'closed';
function setStatus<S extends Status>(s: S) { /* ... */ }
```

## Real World Usage
- `keyof` constraints for object access
- API client where `path` constrains response type
- Forms where field name constrains value type
- Tree / graph operations

## Common Mistakes
- Forgetting the constraint, then `T['x']` errors mysteriously
- Constraint too narrow → callers can't pass valid data
- Confusing `extends` in a generic constraint with `extends` in conditional types — different syntax positions

## Prerequisites
- [[Generics]] · [[Union and Intersection Types]] · [[keyof and Index Access]]

## What To Learn Next
- [[Conditional Types]] · [[Mapped Types]] · [[Utility Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Constraints](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)

### Best YouTube Resource
- [Matt Pocock — `extends` patterns](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Type-Level TypeScript](https://type-level-typescript.com/)

### Best Advanced Resource
- [type-challenges](https://github.com/type-challenges/type-challenges) — gym for constraint-driven types

### Best Practice Project
Write a fully typed `pick(obj, keys[])` that preserves both the picked key set *and* their value types. Ensure passing an unknown key is a compile error.

### Recommended Order to Learn
1. `T extends Shape`
2. `K extends keyof T`
3. `extends` with literal unions
4. Default type parameters
5. Constraint + conditional combo

## Interview Questions
**Q. Why use `K extends keyof T` instead of `K: string`?**
A. `keyof T` ensures only valid keys of `T` pass; `string` would let any string through and `T[K]` would fail.

**Q. Constraint with default — when?**
A. When most callers want one concrete type but power-users may override.

## Related
- [[Generics]] · [[Conditional Types]] · [[keyof and Index Access]]
