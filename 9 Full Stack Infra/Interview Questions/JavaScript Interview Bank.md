---
tags: [interview, javascript]
---

# JavaScript Interview Bank

## Core
**Q. `var` vs `let` vs `const`?**
A. `var` function-scoped + hoisted with `undefined`. `let`/`const` block-scoped, in TDZ until declared. `const` cannot rebind (object is still mutable). See [[let vs var vs const]].

**Q. Hoisting?**
A. Declarations move to top of scope. `var` initialised `undefined`; `let`/`const` exist but are uninitialised (TDZ); function declarations fully hoisted. See [[Hoisting]].

**Q. `==` vs `===`?**
A. `==` coerces; `===` strict equality. Always prefer `===`. See [[Equality Comparison]].

**Q. What is a closure?**
A. A function that captures variables from its lexical scope. Survives after outer function returns. Used for privacy, currying, hooks.

**Q. Explain the event loop.**
A. Stack runs sync code; tasks (timers, I/O) queue in macrotask queue; microtasks (promises) run between tasks. See [[Event Loop]].

**Q. `null` vs `undefined`?**
A. `undefined` — no value assigned. `null` — explicit "no value". `typeof null === 'object'` (legacy bug). See [[null vs undefined]].

## Async
**Q. Promise vs callback?**
A. Promise represents future value, chainable, error propagation. Avoids callback hell.

**Q. What does `async` return?**
A. Always a Promise. `await` only inside async functions (or top-level in modules).

**Q. `Promise.all` vs `Promise.allSettled`?**
A. `all` rejects on first failure; `allSettled` waits for all and returns statuses.

## Functions
**Q. Arrow vs regular function?**
A. Arrows: lexical `this`, no `arguments`, can't be `new`'d, no `prototype`. See [[Arrow functions]].

**Q. `call` vs `apply` vs `bind`?**
A. `call(ctx, ...args)` invokes; `apply(ctx, [args])` invokes with array; `bind(ctx)` returns new function. See [[Call Apply Bind]].

## OOP
**Q. Prototype chain?**
A. Each object has an internal Prototype slot (`__proto__`) linking to another. Lookups walk chain until found or `null`. See [[Prototypes]].

**Q. `class` vs prototype?**
A. `class` is syntactic sugar over prototypes. Same mechanism underneath. See [[Prototypes]].

## Tricky
**Q. What logs?**
```js
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i), 0);
// 3 3 3 — var is function-scoped
// Use let → 0 1 2
```

**Q. `[1,2,3] === [1,2,3]`?**
A. `false`. Reference equality.

**Q. NaN comparisons?**
A. `NaN === NaN` is false. Use `Number.isNaN`. See [[NaN]].

## See also
- [[JavaScript Interview Notes]]
