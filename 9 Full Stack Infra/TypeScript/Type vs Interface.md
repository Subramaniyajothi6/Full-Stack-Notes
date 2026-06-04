---
tags: [typescript, beginner, concept]
---

# Type vs Interface

> Both describe object shapes. Mostly interchangeable; pick by capability + convention.

## Capabilities table
| Feature                          | `type` | `interface` |
| -------------------------------- | ------ | ----------- |
| Object shape                     | ✅     | ✅          |
| Union types                      | ✅     | ❌          |
| Intersection                     | ✅     | ❌ (use `extends`) |
| Tuples                           | ✅     | ❌          |
| Primitives / literals / utility  | ✅     | ❌          |
| Declaration merging              | ❌     | ✅          |
| `extends` another                | ✅ (via `&`) | ✅       |
| Recursive                        | ✅     | ✅          |
| Better error messages            | ✅ (sometimes) | usually |

## Declaration merging — interface only
```ts
interface Window { myFlag: boolean }
// somewhere else
interface Window { anotherFlag: number }
// merged: { myFlag: boolean; anotherFlag: number }
```
Useful for augmenting `Window`, Express's `Request`, etc.

## Practical guidance
- **Public component props / library types** → `interface` (mergeable, common convention)
- **Unions, intersections, mapped, conditional** → `type`
- **Internal app types** → either; pick one and stick with it

## Real World Usage
- React component prop types — both work; team convention decides
- Library API surface — interface for extensibility
- Express middleware — `declare global { namespace Express { interface Request { user?: User } } }`
- DTOs derived via mapped/conditional types — `type`

## Common Mistakes
- Trying to define a union with `interface` (impossible)
- Unintended declaration merging on imported interfaces (cross-module shadowing)
- Inconsistent style across a codebase
- Choosing one without realizing union/utility needs force `type`

## Prerequisites
- [[TypeScript]] · [[Union and Intersection Types]]

## What To Learn Next
- [[Generics]] · [[Utility Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Differences Between Types and Interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

### Best YouTube Resource
- [Matt Pocock — Type vs interface](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript Beginner's Tutorial](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [Effective TypeScript — Item 13](https://effectivetypescript.com/)

### Best Practice Project
Pick one style for your repo (`type` everywhere by default, `interface` only when needed) and codify in your ESLint config (`@typescript-eslint/consistent-type-definitions`).

### Recommended Order to Learn
1. Object shape with both
2. When `type` is required (unions, utility)
3. Declaration merging with `interface`
4. Module augmentation patterns
5. ESLint enforcement

## Interview Questions
**Q. Can you define a union with `interface`?**
A. No. `interface` only describes object shapes. Use `type` for unions.

**Q. What's declaration merging good for?**
A. Augmenting library types (e.g., adding `req.user` to Express's `Request`) without forking the lib.

## Related
- [[Generics]] · [[Utility Types]] · [[Union and Intersection Types]]
