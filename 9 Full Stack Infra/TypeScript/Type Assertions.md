---
tags: [typescript, intermediate, syntax]
---

# Type Assertions

> Tell the compiler "trust me, this value is type X." Lies that survive compile time and explode at runtime.

## Syntax
```ts
const el = document.querySelector('#x') as HTMLInputElement;
const n  = (input as unknown) as number;     // double assertion
```

## When (rarely) okay
- DOM queries that the IDE can't infer
- `JSON.parse` after you've schema-validated separately
- Library types that are too narrow

## When NOT okay
- "Just to make TS shut up" — every `as` is a comment that says "I'm overriding the compiler"
- Coercing one value to another's type — the value is unchanged; only the *belief* is

## Better alternatives
- **Narrow** with checks ([[Type Narrowing]])
- **Type guards** ([[Type Guards]])
- **Validators** (Zod / Valibot)
- **Generic constraints** ([[Generic Constraints]])

## `satisfies` — assert without narrowing away
```ts
type Theme = Record<string, string>;
const colors = {
  primary: '#3b82f6',
  danger:  '#ef4444',
} satisfies Theme;
// type is exact { primary: '#3b82f6'; danger: '#ef4444' } — narrow keys preserved
// while still validating against Theme
```

## Const assertion
```ts
const palette = ['red', 'green', 'blue'] as const;
// readonly tuple of literal strings
```

## Real World Usage
- DOM `querySelector` to a specific element
- `as const` for literal locking
- `satisfies` for typed config objects
- After Zod parsing (rarely needed; `parse` returns typed already)

## Common Mistakes
- `x as Y` to silence errors that indicate real bugs
- Casting through `unknown` (`x as unknown as Y`) as a TS escape hatch
- Forgetting `as const` makes a value deeply readonly
- Choosing `as Theme` over `satisfies Theme` and losing literal types

## Prerequisites
- [[TypeScript]] · [[Type Narrowing]]

## What To Learn Next
- [[Type Guards]] · [[Primitives and Literal Types]] · [[unknown vs any vs never]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)
- [TS 4.9 — `satisfies`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html)

### Best YouTube Resource
- [Matt Pocock — `satisfies` vs `as`](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript — Asserting types module](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [Effective TypeScript — Item 9 (Prefer Type Annotations to Assertions)](https://effectivetypescript.com/)

### Best Practice Project
Audit `as` usage in your codebase: classify each as "necessary" or "lazy"; replace lazy ones with proper narrowing or schema validation.

### Recommended Order to Learn
1. Why assertions are dangerous
2. `as Type` syntax
3. `as const`
4. `satisfies` (TS 4.9+)
5. Double assertion (`as unknown as Y`) — last resort

## Interview Questions
**Q. `as const` vs `as Type`?**
A. `as const` narrows to the deepest literal/readonly form. `as Type` *casts* to a wider/different type.

**Q. Why does `as` not change runtime behavior?**
A. TypeScript erases types; only the compiler's view shifts.

**Q. `satisfies` vs `as`?**
A. `satisfies` validates without widening; `as` overrides the inferred type entirely.

## Related
- [[Type Guards]] · [[Type Narrowing]] · [[Primitives and Literal Types]]
