---
tags: [typescript, beginner, concept]
---

# Union and Intersection Types

> Union (`A | B`) — value is A *or* B. Intersection (`A & B`) — value satisfies *both* A and B.

## Union — alternation
```ts
type Id = string | number;
function find(id: Id) {
  if (typeof id === 'string') return byName(id);
  return byIndex(id);
}
```
Only properties present on **all** members are accessible without narrowing.

## Intersection — combination
```ts
type WithId = { id: string };
type WithCreatedAt = { createdAt: Date };
type Entity = WithId & WithCreatedAt;     // { id: string; createdAt: Date }
```
You get all fields from both sides.

## Mental model
- Union widens the *set of values* a variable can hold
- Intersection widens the *set of fields* a value must have
- For object types, intersection ≈ extending an interface

## Discriminated unions (preview)
The most powerful pattern combines literal types + unions — see [[Discriminated Unions]].

## Real World Usage
- API responses with multiple variants
- Mixed role/permission objects (`Admin & User & WithBilling`)
- Function inputs that accept multiple shapes
- Component props with conditional fields

## Common Mistakes
- Trying to access a union member's exclusive property without narrowing
- Conflicting fields in intersections (`{ a: string } & { a: number }` → `never`)
- Confusing intersection with extension — they're nearly the same for objects, different for primitives
- Building a god-type intersection where a discriminated union would clarify

## Prerequisites
- [[Primitives and Literal Types]] · [[Type Inference]]

## What To Learn Next
- [[Type Narrowing]] · [[Discriminated Unions]] · [[Generics]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Unions and Intersections](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)

### Best YouTube Resource
- [Matt Pocock — Union & intersection patterns](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Type-Level TypeScript — Unions module](https://type-level-typescript.com/)

### Best Advanced Resource
- [Effective TypeScript — Item 13 (Difference between types and interfaces)](https://effectivetypescript.com/)

### Best Practice Project
Model a `Result<T, E>` type as `{ok: true; data: T} | {ok: false; error: E}` and write helpers that narrow on `ok`. Avoid `as` assertions.

### Recommended Order to Learn
1. Union of primitives
2. Intersection of objects
3. Narrowing on a union (typeof / in / instanceof)
4. Discriminated unions
5. `never` and exhaustive checks

## Interview Questions
**Q. Difference between `A | B` and `A & B`?**
A. Union: holds *either* A or B. Intersection: must be *both* simultaneously.

**Q. Why does `{a: string} & {a: number}` produce `never`?**
A. No value can be both `string` and `number`; the intersection on the field is empty.

## Related
- [[Type Narrowing]] · [[Discriminated Unions]] · [[Type vs Interface]]
