---
tags: [typescript, intermediate, concept]
---

# unknown vs any vs never

> Three "special" types covering: unknown safe top, any escape hatch, and impossible bottom.

## any — opt out
```ts
let x: any = 5;
x.foo.bar();      // no error, no safety, no autocomplete
```
- Disables type checking on the value
- Spreads silently (`any` returned from a fn pollutes consumers)
- Use only at hard untyped boundaries; prefer `unknown`

## unknown — safe top type
```ts
let x: unknown = JSON.parse(input);
x.foo;                 // ❌ must narrow first
if (typeof x === 'object' && x !== null && 'foo' in x) {
  x.foo;               // ✅ narrowed
}
```
- Accepts anything (top type)
- Forces narrowing before use
- Right choice for parsed JSON, error catches, generic event payloads

## never — bottom type
```ts
function fail(msg: string): never { throw new Error(msg); }

function exhaustive(s: Shape) {
  switch (s.kind) { ... default: const _: never = s; }
}
```
- No value can have type `never`
- Used for: functions that always throw / loop, exhaustive switch checks, filtering in conditional types

## Quick rule
| Need | Use |
|---|---|
| "anything, but I'll check" | `unknown` |
| "anything, ignore types" | `any` (last resort) |
| "this case can't happen" | `never` |

## Real World Usage
- `catch (e: unknown)` — TS 4.4+ default
- API responses before validation (`unknown` → Zod)
- `function fail(): never` — assertion helpers
- Conditional-type filters (`extends ... ? ... : never`)

## Common Mistakes
- Using `any` everywhere — defeats TypeScript
- Comparing `unknown` against `===` then assuming type — that's a type guard, not a value check
- Returning `never` from non-throwing functions — they unify away
- Forgetting `never` in exhaustive `switch` → silent gaps when union grows

## Prerequisites
- [[TypeScript]] · [[Type Narrowing]] · [[Type Guards]]

## What To Learn Next
- [[Discriminated Unions]] · [[Type Assertions]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — `unknown`](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#unknown)
- [TS Handbook — `never`](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-never-type)

### Best YouTube Resource
- [Matt Pocock — unknown vs any](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript Beginner's Tutorial](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [Effective TypeScript — Item 39 (avoid `any`)](https://effectivetypescript.com/)

### Best Practice Project
Search your repo for `: any` and `as any`. Replace with `unknown` + narrowing or proper types. Watch how many bugs the migration uncovers.

### Recommended Order to Learn
1. `any` (avoid)
2. `unknown` + narrowing
3. `never` for impossible
4. `never` for exhaustiveness
5. Filtering via `never` in conditional types

## Interview Questions
**Q. unknown vs any — practical difference?**
A. `unknown` requires narrowing before use; `any` allows everything silently. `unknown` keeps safety; `any` gives it up.

**Q. When does TypeScript infer `never`?**
A. Functions that always throw, exhausted unions, intersections of incompatible primitives, conditional-type filters.

## Related
- [[Type Narrowing]] · [[Type Guards]] · [[Discriminated Unions]]
