---
tags: [typescript, beginner, concept]
---

# Modules

> ESM `import`/`export` is the modern default. CJS `require` interoperates but with caveats. TypeScript's module options control which world your code targets.

## ESM
```ts
// math.ts
export function add(a: number, b: number) { return a + b; }
export type Pair = [number, number];

// main.ts
import { add, type Pair } from './math.js';   // .js even when source is .ts
```

## Type-only imports
```ts
import type { Pair } from './math';                 // erased
import { add, type Pair } from './math';            // mixed
```
With `verbatimModuleSyntax`, the syntax controls emission exactly — no surprise type imports kept at runtime.

## Default vs named
```ts
export default class A {}
export const b = 1;
// import A, { b } from './x';
```

## Re-exports
```ts
export { foo, bar } from './a';
export * from './b';
export * as utils from './u';
```

## tsconfig knobs
- `module` — `ESNext` / `NodeNext` / `CommonJS`
- `moduleResolution` — `Bundler` (Vite/webpack) / `Node16` / `Node10`
- `verbatimModuleSyntax` — strict type-only imports
- `isolatedModules` — required for SWC/esbuild

## Real World Usage
- Modern frontend (Vite, Next, Astro) — ESM + Bundler resolution
- Modern Node (Node 20+) — ESM (`"type": "module"`) or NodeNext
- Mixed CJS + ESM monorepos
- Library publishing with conditional exports

## Common Mistakes
- Forgetting `.js` extension in ESM imports of TS files
- Mixing `import` and `require` in CJS projects
- Importing CJS-only modules without dynamic `import()` from ESM
- `default` export conventions clashing across packages
- Top-level await in CJS (not allowed)

## Prerequisites
- [[TypeScript]] · [[../JavaScript/JavaScript MOC]]

## What To Learn Next
- [[Declaration Files]] · [[tsconfig and Strict Mode]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Modules](https://www.typescriptlang.org/docs/handbook/2/modules.html)
- [Node.js — ECMAScript modules](https://nodejs.org/api/esm.html)

### Best YouTube Resource
- [Theo — TS modules in 2024](https://www.youtube.com/@t3dotgg)

### Best Free Course
- [Matt Pocock — modules cheatsheet](https://www.totaltypescript.com/)

### Best Advanced Resource
- [Andrew Branch — A type-aware Node ESM](https://andrewbranch.github.io/)
- [TS team blog — module resolution](https://devblogs.microsoft.com/typescript/)

### Best Practice Project
Convert a small CJS Node project to NodeNext ESM. Update tsconfig, add `.js` extensions, set `"type": "module"` in package.json. Document every error and fix.

### Recommended Order to Learn
1. ESM exports + imports
2. Type-only imports
3. Re-exports
4. tsconfig `module` + `moduleResolution`
5. Node ESM specifics (extensions, package.json)
6. CJS interop patterns

## Interview Questions
**Q. Why does ESM require file extensions in imports?**
A. Spec compliance — Node ESM doesn't auto-resolve extensions like CJS did. Use `.js` even when the source is `.ts`.

**Q. `import type` vs `import { type X }`?**
A. Both erase at runtime; mixed form lets you import value + type from one statement.

## Related
- [[Declaration Files]] · [[tsconfig and Strict Mode]] · [[../JavaScript/JavaScript MOC]]
