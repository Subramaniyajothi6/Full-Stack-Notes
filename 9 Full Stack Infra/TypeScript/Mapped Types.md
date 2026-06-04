---
tags: [typescript, advanced, syntax]
---

# Mapped Types

> Generate a new type by transforming each key of an existing type.

## The shape
```ts
type Readonly<T> = { readonly [K in keyof T]: T[K] };
type Partial<T>  = { [K in keyof T]?: T[K] };
type Nullable<T> = { [K in keyof T]: T[K] | null };
```

## Modifiers
- `readonly` / `-readonly` — add or remove
- `?` / `-?` — make optional or required

```ts
type RequireAll<T> = { [K in keyof T]-?: T[K] };
type Mutable<T>    = { -readonly [K in keyof T]: T[K] };
```

## Key remapping (`as`)
```ts
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type U = { name: string; age: number };
type UG = Getters<U>;
// { getName: () => string; getAge: () => number }
```

## Filtering keys
```ts
type StringKeys<T> = {
  [K in keyof T as T[K] extends string ? K : never]: T[K];
};
```

## Real World Usage
- API response transformers (e.g., Snake → camel)
- Form `errors` object derived from `values` object
- ORM-like getters / setters
- Reactive store APIs (`useStore` derived selectors)
- Test mock builders

## Common Mistakes
- Forgetting `keyof T` in the `in` clause
- Mapping over `T` when you needed to map over `keyof T`
- Using `as` remapping without [[Template Literal Types]] — limits power
- Recursive mapped types blowing up compile time

## Prerequisites
- [[Generics]] · [[keyof and Index Access]] · [[Conditional Types]]

## What To Learn Next
- [[Conditional Types]] · [[Template Literal Types]] · [[Utility Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)

### Best YouTube Resource
- [Matt Pocock — Mapped types](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Type-Level TypeScript — Mapped types](https://type-level-typescript.com/)

### Best Advanced Resource
- [type-challenges — mapped type problems](https://github.com/type-challenges/type-challenges)

### Best Practice Project
Build a `DeepPartial<T>` and `DeepReadonly<T>`. Then write `Camelize<T>` that recursively renames snake_case keys to camelCase using key remapping + template literals.

### Recommended Order to Learn
1. Basic `[K in keyof T]: T[K]`
2. `readonly` and `?` modifiers
3. Removing modifiers (`-readonly`, `-?`)
4. Key remapping `as`
5. Filtering with `as ... never`
6. Recursive mapped types

## Interview Questions
**Q. What's `[K in keyof T]`?**
A. Iterate over each key of T; the value of the new type at that key is whatever expression follows the colon.

**Q. Why remove `readonly` with `-readonly`?**
A. To produce a mutable copy of an immutable type — common when building update DTOs.

## Related
- [[Conditional Types]] · [[Template Literal Types]] · [[Utility Types]]
