---
tags: [typescript, intermediate, syntax]
---

# keyof and Index Access

> `keyof T` — union of T's keys. `T[K]` — the value type at key K.

## keyof
```ts
type User = { id: string; email: string; age: number };
type UserKeys = keyof User;       // 'id' | 'email' | 'age'
```

## Index access
```ts
type IdType = User['id'];                  // string
type EmailOrAge = User['email' | 'age'];   // string | number
type AnyValue = User[keyof User];          // string | number
```

## With arrays
```ts
const palette = ['red', 'green', 'blue'] as const;
type Color = typeof palette[number];        // 'red' | 'green' | 'blue'
```

## With nested objects
```ts
type Config = { db: { url: string; pool: number } };
type DbUrl = Config['db']['url'];           // string
```

## In generics
```ts
function get<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

## Real World Usage
- Picking known keys at runtime with type safety
- Deriving union types from object/array constants
- Building type-safe form helpers
- ORM-like field-aware utilities
- Theme tokens (`keyof Theme`)

## Common Mistakes
- `keyof Object` on `{}` returns `never` (or symbol-only) — don't expect string keys
- Index access on a nullable property returns `T | undefined` only with strict optional checks
- `keyof T` on classes includes inherited methods
- Index signatures (`[k: string]: T`) make `keyof X` = `string | number`

## Prerequisites
- [[Generics]] · [[Generic Constraints]] · [[Primitives and Literal Types]]

## What To Learn Next
- [[Mapped Types]] · [[Conditional Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — keyof](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html)
- [TS Handbook — Indexed Access](https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html)

### Best YouTube Resource
- [Matt Pocock — keyof patterns](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Type-Level TypeScript — Object types](https://type-level-typescript.com/)

### Best Advanced Resource
- [Effective TypeScript — Item 14 (`keyof` carefully)](https://effectivetypescript.com/)

### Best Practice Project
Define a theme `as const` then derive type-safe `Color`, `Spacing`, `Font` types from it. Use them in component props with autocomplete.

### Recommended Order to Learn
1. `keyof T` on object types
2. `T[K]` indexed access
3. Combination: `T[keyof T]`
4. `typeof arr[number]` array-to-union
5. Generic `T, K extends keyof T`

## Interview Questions
**Q. What is `T[keyof T]`?**
A. A union of all value types in T.

**Q. Why does `keyof Array<T>` include `'length'`, `'push'`, etc.?**
A. `Array` is an interface with those members. Use `number` for index access.

## Related
- [[Generics]] · [[Mapped Types]] · [[Generic Constraints]]
