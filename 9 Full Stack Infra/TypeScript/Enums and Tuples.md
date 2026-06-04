---
tags: [typescript, intermediate, syntax]
---

# Enums and Tuples

> Two specialized type forms: `enum` (named constants, runtime cost) and tuples (fixed-length typed arrays).

## Enums
```ts
enum Direction { Up, Down, Left, Right }    // numeric, 0..3
enum Status { Open = 'open', Closed = 'closed' }   // string

let s: Status = Status.Open;
```

### Trade-offs
- ✅ Familiar from C-family languages
- ❌ Numeric enums are bidirectional (`Direction[0]` returns `'Up'`) — surprising
- ❌ Emit JS code (not erased) — bundle cost
- ❌ Not tree-shakeable in older bundlers
- ❌ `const enum` IS erased but breaks `isolatedModules`

### Modern alternative — literal union + `as const`
```ts
const STATUS = ['open', 'closed', 'pending'] as const;
type Status = typeof STATUS[number];
```
Smaller bundle, type-erased, just as type-safe.

## Tuples
```ts
type Point = [number, number];
type RGB = [r: number, g: number, b: number];   // labeled tuples
type Maybe<T> = [ok: true, value: T] | [ok: false, error: string];

const p: Point = [3, 4];
```

### Variadic tuples
```ts
type Concat<A extends any[], B extends any[]> = [...A, ...B];
type X = Concat<[1, 2], ['a']>;   // [1, 2, 'a']
```

### React-style hook returns
```ts
function useToggle(): [boolean, () => void] {
  const [v, set] = useState(false);
  return [v, () => set(p => !p)];
}
```

## Real World Usage
- Tuples: hook returns, function args spreading, fixed coordinate pairs
- Enums: legacy code, interop with C-style APIs
- Literal unions: state machines, variants, theme keys (preferred over enums)

## Common Mistakes
- Using `enum` when literal union would do — bundle bloat
- Tuple where an object would be more readable (`[number, number, number]` vs `{x, y, z}`)
- Treating tuple `as const` then expecting mutation — readonly enforced
- Forgetting variadic-tuple syntax requires TS 4.0+

## Prerequisites
- [[Primitives and Literal Types]] · [[Type Inference]]

## What To Learn Next
- [[Generics]] · [[Conditional Types]]

## Best Learning Resources

### Official Documentation
- [TS Handbook — Enums](https://www.typescriptlang.org/docs/handbook/enums.html)
- [TS Handbook — Tuples](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)

### Best YouTube Resource
- [Theo — Don't use enums](https://www.youtube.com/@t3dotgg)
- [Matt Pocock — Tuples in TS](https://www.youtube.com/@mattpocockuk)

### Best Free Course
- [Total TypeScript — Tuples](https://www.totaltypescript.com/tutorials)

### Best Advanced Resource
- [type-challenges — variadic tuple problems](https://github.com/type-challenges/type-challenges)

### Best Practice Project
Replace enums in a small project with `as const` literal unions. Compare bundle size before/after. Then write a `zip<A,B>` using variadic tuples.

### Recommended Order to Learn
1. `enum` vs literal union (and why prefer the latter)
2. String enums when you must
3. Tuple basics
4. Labeled tuples
5. Variadic tuples + spread

## Interview Questions
**Q. Why prefer literal unions over enums?**
A. Erased at runtime, smaller bundle, idiomatic in modern TS, tree-shakeable.

**Q. What's a labeled tuple?**
A. Tuple with element names for IDE hints: `type RGB = [r: number, g: number, b: number]`. Names are documentation only — no runtime effect.

## Related
- [[Primitives and Literal Types]] · [[Generics]] · [[Conditional Types]]
