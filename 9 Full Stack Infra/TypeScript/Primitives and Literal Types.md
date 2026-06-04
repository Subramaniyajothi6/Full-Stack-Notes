---
tags: [typescript, beginner, concept]
---

# Primitives and Literal Types

> Core types (`string`, `number`, `boolean`) and their narrower siblings — string/number/boolean *literals*.

## Primitives
```ts
let s: string = 'hi';
let n: number = 1;
let b: boolean = true;
let big: bigint = 10n;
let sym: symbol = Symbol('s');
```

## Literal types
A specific value as its own type:
```ts
type Theme = 'light' | 'dark' | 'system';
let mode: Theme = 'light';   // only those three strings allowed

type Dice = 1 | 2 | 3 | 4 | 5 | 6;
type Truthy = true;
```

## as const — keep literals from widening
```ts
const colors = ['red', 'green', 'blue'];        // string[]
const colors = ['red', 'green', 'blue'] as const; // readonly ['red','green','blue']

type Color = typeof colors[number];              // 'red' | 'green' | 'blue'
```

## Real World Usage
- Discriminator fields in [[Discriminated Unions|discriminated unions]]
- Enum-replacements (`'asc' | 'desc'`)
- Component variant props (`'primary' | 'secondary'`)
- Event names (`'click' | 'hover'`)

## Common Mistakes
- Using `string` when `'asc' | 'desc'` is meant
- Forgetting `as const` so literal types widen at object/array boundaries
- Using TypeScript `enum` when union literals would be safer + tree-shakeable

## Prerequisites
- [[TypeScript]] · [[Type Inference]]

## What To Learn Next
- [[Union and Intersection Types]] · [[Type Narrowing]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

### Best YouTube Resource
- [Matt Pocock — Literal types & `as const`](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript Beginner's Tutorial](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [Type-Level TypeScript — Literal types module](https://type-level-typescript.com/)

### Best Practice Project
Replace every TS `enum` in a project with a literal union + `as const` array; observe smaller bundle and clearer IDE hints.

### Recommended Order to Learn
1. Primitives
2. Literal types
3. `as const`
4. Union of literals
5. `typeof arr[number]` pattern

## Interview Questions
**Q. Why prefer literal unions over `enum`?**
A. Literal unions are erased at runtime (zero JS), tree-shakeable, and idiomatic in modern TS. Enums emit JS objects.

**Q. What does `as const` do?**
A. Tells TS "treat this as the narrowest possible literal type, deeply readonly."

## Related
- [[Type Inference]] · [[Union and Intersection Types]] · [[Discriminated Unions]]
