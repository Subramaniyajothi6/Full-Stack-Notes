---
tags: [moc, typescript, language]
---

# TypeScript MOC

> Static type system for JavaScript. Modern frontend + Node default.

## Overview
- [[TypeScript]] — full intro: why, core ideas, best practices

## Foundations
- [[Type Inference]]
- [[Primitives and Literal Types]]
- [[Union and Intersection Types]]
- [[Type vs Interface]]
- [[Enums and Tuples]]

## Narrowing
- [[Type Narrowing]]
- [[Type Guards]]
- [[Discriminated Unions]]
- [[unknown vs any vs never]]
- [[Type Assertions]]

## Generics + advanced types
- [[Generics]]
- [[Generic Constraints]]
- [[Utility Types]]
- [[keyof and Index Access]]
- [[Mapped Types]]
- [[Conditional Types]]
- [[Template Literal Types]]

## Tooling + ecosystem
- [[tsconfig and Strict Mode]]
- [[Modules]]
- [[Declaration Files]]

## Suggested order
1. [[TypeScript]] (skim) → [[tsconfig and Strict Mode]]
2. [[Type Inference]] → [[Primitives and Literal Types]] → [[Union and Intersection Types]]
3. [[Type Narrowing]] → [[Discriminated Unions]] → [[Type Guards]] → [[unknown vs any vs never]]
4. [[Type vs Interface]] → [[Enums and Tuples]] → [[Type Assertions]]
5. [[Generics]] → [[Generic Constraints]] → [[Utility Types]]
6. [[keyof and Index Access]] → [[Mapped Types]] → [[Conditional Types]] → [[Template Literal Types]]
7. [[Modules]] → [[Declaration Files]]

## Roadmap to fill in
- [ ] Function overloads
- [ ] Index signatures + Record patterns
- [ ] Branded / nominal types
- [ ] Class types + abstract classes
- [ ] Decorators (TS 5)
- [ ] Symbol-keyed types
- [ ] React-specific TS patterns
- [ ] TS perf (`tsc --extendedDiagnostics`, `--generateTrace`)
- [ ] Migrating a JS codebase to TS

## Related stacks
- [[JavaScript MOC]] — language foundation
- [[React MOC]] — TS-first
- [[NextJS MOC]] — TS-first

## Related
- [[Full Stack Infra MOC]] · [[MERN MOC]]
