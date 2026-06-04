---
tags: [typescript, intermediate, tooling]
---

# Declaration Files

> `.d.ts` files describe the *types* of JavaScript modules without containing implementation. Lets TS understand JS-only libraries and your own shipped code.

## Where they come from
- **`@types/*` packages** (`@types/node`, `@types/express`)
- **Bundled with libraries** (most modern libs ship `.d.ts`)
- **Hand-written** for untyped JS deps
- **Auto-emitted** from your TS source via `tsc --declaration`

## A simple `.d.ts`
```ts
// some-untyped-lib.d.ts
declare module 'some-untyped-lib' {
  export function greet(name: string): string;
  export const version: string;
}
```

## Ambient (global) declarations
```ts
// global.d.ts
declare const __APP_VERSION__: string;
interface Window { myFlag?: boolean }
```

## Module augmentation
Add fields to a third-party type without forking:
```ts
// types/express.d.ts
import 'express';
declare module 'express-serve-static-core' {
  interface Request { user?: { id: string } }
}
```

## Shipping types from your library
```jsonc
// package.json
{
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" }
  }
}
```
Run `tsc --declaration --declarationMap` to emit them.

## Real World Usage
- Augmenting Express `Request` with `user`
- Vite env (`vite-env.d.ts` declares `import.meta.env`)
- Adding global flags injected at build time
- Typing CSS modules, image imports, GraphQL files
- Authoring a TS library

## Common Mistakes
- Editing `node_modules/.../*.d.ts` directly (gone on reinstall) — use module augmentation
- `.d.ts` files importing values rather than types (only types in declaration files)
- Forgetting `declare global { ... }` wrap for global augments
- Declaration files placed outside `include` paths in tsconfig (TS doesn't see them)

## Prerequisites
- [[TypeScript]] · [[Modules]] · [[tsconfig and Strict Mode]]

## What To Learn Next
- [[Type vs Interface]] · [[Generics]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Declaration Files](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)
- [DefinitelyTyped repo (`@types/*`)](https://github.com/DefinitelyTyped/DefinitelyTyped)

### Best YouTube Resource
- [Matt Pocock — Module augmentation](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [TS Handbook — Library Structures](https://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html)

### Best Advanced Resource
- [Publishing TypeScript libraries — Andrew Branch / TS team blog](https://devblogs.microsoft.com/typescript/)

### Best Practice Project
Take an untyped npm package you depend on; write hand-rolled `.d.ts` declarations for the parts you use. Submit them to DefinitelyTyped if appropriate.

### Recommended Order to Learn
1. `@types/*` consumption
2. Hand-written `.d.ts` for untyped libs
3. Ambient global declarations
4. Module augmentation (Express `Request`)
5. Emitting types from your TS lib
6. `package.json` `exports` + types

## Interview Questions
**Q. What's a `.d.ts` file?**
A. A type-only description of a JS module. Contains no runtime code.

**Q. Why use module augmentation instead of patching node_modules?**
A. Patches survive package upgrades; node_modules edits are lost on reinstall.

## Related
- [[Type vs Interface]] · [[Modules]] · [[tsconfig and Strict Mode]]
