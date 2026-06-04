---
tags: [typescript, beginner, tooling]
---

# tsconfig and Strict Mode

> The compiler's settings. Enable strict mode and you get the real value of TypeScript.

## Minimum modern config
```jsonc
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",      // or "Node16" for Node ESM
    "strict": true,                     // enables every strict flag (read below)
    "noUncheckedIndexedAccess": true,   // arr[i] is T | undefined
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "isolatedModules": true,            // safe for SWC / esbuild
    "skipLibCheck": true,
    "verbatimModuleSyntax": true,       // explicit `import type`
    "resolveJsonModule": true,
    "esModuleInterop": true
  }
}
```

## What `strict: true` enables
- `noImplicitAny` — variables without inferable type can't fall back to `any`
- `strictNullChecks` — `null` and `undefined` aren't sneakily assignable everywhere
- `strictFunctionTypes` — parameter bivariance fixed
- `strictBindCallApply` — `bind`/`call`/`apply` are type-checked
- `strictPropertyInitialization` — class fields must be initialized
- `noImplicitThis` — `this` of unknown type is an error
- `useUnknownInCatchVariables` — `catch (e)` is `unknown`, not `any`
- `alwaysStrict` — emits `"use strict"`

## Strongly recommended beyond `strict`
- `noUncheckedIndexedAccess` — guards against array OOB
- `exactOptionalPropertyTypes` — `{a?: string}` doesn't accept `{a: undefined}`
- `verbatimModuleSyntax` — explicit type-only imports

## Project structure
- One `tsconfig.base.json` with shared options
- Per-app/package `tsconfig.json` extending it
- `tsc --build` for monorepos with project references

## Real World Usage
- New projects: enable everything from day one
- Migrating JS → TS: gradually tighten flags (start with `noImplicitAny` off, then `strictNullChecks`, etc.)
- Library authors ship a stricter config than they require of consumers

## Common Mistakes
- `strict: false` "to make errors go away" — defeats the purpose
- Missing `noUncheckedIndexedAccess` — array access masks runtime crashes
- Setting `target: ES5` for modern Node (you're losing native features)
- Forgetting `isolatedModules` for tools like esbuild / SWC
- `paths` aliases without runtime resolver match

## Prerequisites
- [[TypeScript]] · [[Modules]]

## What To Learn Next
- [[Declaration Files]] · [[Type Inference]]

## Best Learning Resources

### Official Documentation
- [tsconfig reference (every flag)](https://www.typescriptlang.org/tsconfig)
- [TS Handbook — Project Configuration](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)

### Best YouTube Resource
- [Matt Pocock — tsconfig walkthrough](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Matt Pocock — tsconfig.json template](https://www.totaltypescript.com/tsconfig-cheat-sheet)

### Best Advanced Resource
- [Effective TypeScript — Item 2 (Know Which Options You're Using)](https://effectivetypescript.com/)

### Best Practice Project
Enable every strict flag in an existing project. Fix errors one file at a time. Document each flag's value-add.

### Recommended Order to Learn
1. `strict: true`
2. `noUncheckedIndexedAccess`
3. `exactOptionalPropertyTypes`
4. `module` + `moduleResolution`
5. `target` for the runtime
6. `paths` aliases
7. Project references for monorepos

## Interview Questions
**Q. What does `strict: true` do?**
A. Turns on a bundle of strict-checking flags (null checks, implicit any, etc.) — the recommended baseline.

**Q. Why `noUncheckedIndexedAccess`?**
A. Array/index access becomes `T | undefined`, exposing real possibilities of out-of-bounds reads.

## Related
- [[TypeScript]] · [[Declaration Files]] · [[Modules]]
