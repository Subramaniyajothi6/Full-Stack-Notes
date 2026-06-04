---
tags: [typescript, advanced, syntax]
---

# Template Literal Types

> Compose string types from other string types using template-literal syntax at the type level.

## Basics
```ts
type Hello = 'hello';
type Greeting = `${Hello} world`;            // 'hello world'

type Lang = 'en' | 'es';
type Greet<L extends Lang> = `${L}_greeting`; // 'en_greeting' | 'es_greeting'
```

## Distributive over unions
```ts
type Side = 'top' | 'bottom';
type Edge = 'left' | 'right';
type CornerKey = `${Side}-${Edge}`;
// 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right'
```

## Built-in helpers
- `Uppercase<S>` · `Lowercase<S>`
- `Capitalize<S>` · `Uncapitalize<S>`

## Practical: route param parsing
```ts
type Params<S extends string> =
  S extends `${string}/:${infer P}/${infer R}` ? P | Params<`/${R}`> :
  S extends `${string}/:${infer P}` ? P :
  never;

type X = Params<'/users/:id/posts/:postId'>;  // 'id' | 'postId'
```

## Real World Usage
- Route param extraction (Next.js / TanStack Router)
- CSS-in-TS color/spacing token names
- Event names (`onClick`, `onSubmit` — `on${Capitalize<E>}`)
- API path types in tRPC / OpenAPI codegen
- Branded keys in GraphQL codegen

## Common Mistakes
- Recursive template types hitting TS's depth limit
- Forgetting `infer` captures within template-literal extends
- Building runtime values from these types at runtime — they're erased
- Distributing where you didn't want to (use `[T]` to bracket)

## Prerequisites
- [[Conditional Types]] · [[Mapped Types]] · [[Primitives and Literal Types]]

## What To Learn Next
- [[Utility Types]] · [[Type Assertions]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Template Literal Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html)

### Best YouTube Resource
- [Matt Pocock — Template literal magic](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Type-Level TypeScript](https://type-level-typescript.com/)

### Best Advanced Resource
- [type-challenges (template literal problems)](https://github.com/type-challenges/type-challenges)

### Best Practice Project
Build a typed event-emitter where `emit('user:created', payload)` is type-checked against a registry mapped from event-name strings to payload types.

### Recommended Order to Learn
1. Concatenation
2. Distribution across unions
3. Built-in `Uppercase`/`Capitalize` etc.
4. `infer` inside template patterns
5. Recursive parsing patterns
6. Library uses (TanStack Router, tRPC)

## Interview Questions
**Q. Why are template literal types powerful?**
A. They turn arbitrary string structure into compile-time information — routes, events, paths all become typed.

**Q. What does `\`on\${Capitalize<E>}\`` produce for `E = 'click' | 'hover'`?**
A. `'onClick' | 'onHover'`.

## Related
- [[Conditional Types]] · [[Mapped Types]] · [[Primitives and Literal Types]]
