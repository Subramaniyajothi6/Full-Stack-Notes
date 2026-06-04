---
tags: [typescript, intermediate, pattern]
---

# Type Guards

> Functions that narrow types beyond what built-in checks can express, by returning a special return type.

## User-defined type guard (`is`)
```ts
function isString(x: unknown): x is string {
  return typeof x === 'string';
}

function f(x: unknown) {
  if (isString(x)) x.toUpperCase();   // x: string
}
```

## Custom shape guard
```ts
type User = { id: string; email: string };
function isUser(x: unknown): x is User {
  return typeof x === 'object' && x !== null
    && 'id' in x && typeof (x as any).id === 'string'
    && 'email' in x && typeof (x as any).email === 'string';
}
```

## Assertion functions (`asserts`)
Throw if not the type, narrow the rest of the function:
```ts
function assertString(x: unknown): asserts x is string {
  if (typeof x !== 'string') throw new Error('not a string');
}

function g(x: unknown) {
  assertString(x);
  x.toUpperCase();   // x: string after the assert
}
```

## Better: use a validator (Zod)
Hand-rolled guards drift. Schema libraries give you guards + parsing free:
```ts
import { z } from 'zod';
const User = z.object({ id: z.string(), email: z.string().email() });
type User = z.infer<typeof User>;

const result = User.safeParse(input);
if (result.success) result.data.email;   // typed
```

## Real World Usage
- Validating untrusted input (request bodies, JSON.parse output)
- Discriminating among interfaces without a discriminator field
- Working with `unknown` from APIs
- Library code that exposes "is X" helpers

## Common Mistakes
- Lying in the body of a guard (`return true` regardless) — silently breaks downstream narrowing
- Assertion functions that don't actually throw on failure
- Repeating guard logic when a schema lib would centralize it
- Guards that depend on async work (guards must be sync)

## Prerequisites
- [[Type Narrowing]] · [[unknown vs any vs never]]

## What To Learn Next
- [[Generics]] · [[Conditional Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Type predicates](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)
- [Zod docs](https://zod.dev/)

### Best YouTube Resource
- [Matt Pocock — Type predicates & assertion functions](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript — Type predicates module](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [Effective TypeScript — Item 22 (Use type predicates)](https://effectivetypescript.com/)

### Best Practice Project
Write a `parseEnv(raw: NodeJS.ProcessEnv): AppConfig` using Zod; replace any `process.env.X` reads in the codebase with the validated config object.

### Recommended Order to Learn
1. typeof / in / instanceof narrowing
2. User-defined `is` guards
3. Assertion functions (`asserts`)
4. Schema-based guards (Zod / Valibot)
5. Generic guards

## Interview Questions
**Q. Difference between `x is string` and `asserts x is string`?**
A. `x is string` returns a boolean for `if` branches. `asserts` throws and narrows for the rest of the function.

**Q. Why prefer Zod over hand-written guards?**
A. Single source of truth, parses + validates, errors are structured, schema can drive types.

## Related
- [[Type Narrowing]] · [[unknown vs any vs never]] · [[Discriminated Unions]]
