---
tags: [typescript, intermediate, syntax]
---

# Utility Types

> Built-in generic types for transforming other types — `Partial`, `Pick`, `Omit`, `Record`, `ReturnType`, etc.

## The essentials
| Type | Purpose | Example |
|---|---|---|
| `Partial<T>` | All fields optional | `Partial<User>` |
| `Required<T>` | All fields required | `Required<User>` |
| `Readonly<T>` | All fields readonly | `Readonly<User>` |
| `Pick<T, K>` | Subset by keys | `Pick<User, 'id'\|'email'>` |
| `Omit<T, K>` | Everything except keys | `Omit<User, 'password'>` |
| `Record<K, V>` | Map of K → V | `Record<'a'\|'b', number>` |
| `Exclude<T, U>` | Remove from union | `Exclude<'a'\|'b', 'a'>` → `'b'` |
| `Extract<T, U>` | Keep matching members | `Extract<'a'\|1, string>` → `'a'` |
| `NonNullable<T>` | Strip null + undefined | `NonNullable<string\|null>` |
| `ReturnType<F>` | Return type of function | `ReturnType<typeof fn>` |
| `Parameters<F>` | Tuple of param types | `Parameters<typeof fn>` |
| `Awaited<T>` | Unwrap Promise<T> | `Awaited<Promise<number>>` → number |
| `InstanceType<C>` | Instance of a class | `InstanceType<typeof MyClass>` |

## Common patterns
```ts
type User = { id: string; email: string; password: string };

type PublicUser = Omit<User, 'password'>;           // hide secrets
type CreateUser = Pick<User, 'email' | 'password'>; // input shape
type UserPatch = Partial<User>;                      // PATCH body

type StatusMap = Record<'idle' | 'loading' | 'ok', boolean>;
```

## Real World Usage
- API DTOs derived from DB models
- React component props subsets
- Form drafts (`Partial<Entity>`)
- State derived from a typed action union

## Common Mistakes
- `Partial<T>` recursing only one level — for deep, use `DeepPartial<T>` (custom)
- `Omit<T, 'x'>` silently succeeds even if `'x'` isn't a key (older TS) — newer TS warns; consider `Omit<T, keyof T & 'x'>` patterns
- Using `Record<string, T>` as a free-for-all — index signatures + better keys are usually clearer

## Prerequisites
- [[Generics]] · [[keyof and Index Access]] · [[Mapped Types]]

## What To Learn Next
- [[Mapped Types]] · [[Conditional Types]] · [[Template Literal Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)

### Best YouTube Resource
- [Matt Pocock — Utility types tour](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript — Utility types](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [type-fest (sindresorhus)](https://github.com/sindresorhus/type-fest) — extra utility types beyond built-ins

### Best Practice Project
Take a Mongoose schema; derive `CreateInput`, `UpdateInput`, `PublicView` types from one base entity using only built-in utility types.

### Recommended Order to Learn
1. Pick / Omit / Partial / Required
2. Record / Readonly
3. Exclude / Extract / NonNullable
4. ReturnType / Parameters / Awaited
5. Custom utility types (your own DeepPartial)

## Interview Questions
**Q. `Pick<T, K>` vs `Omit<T, K>`?**
A. Pick keeps listed keys. Omit removes them. Both produce a new object type.

**Q. Difference between `Exclude` and `Omit`?**
A. `Exclude<T, U>` removes from a union; `Omit<T, K>` removes from an object's keys.

## Related
- [[Mapped Types]] · [[Generics]] · [[Conditional Types]]
