---
tags: [dsa, pattern, intermediate]
---

# Binary Search

> Halve the search space each step. O(log n) lookup on sorted data — and on monotonic answer spaces.

## When to reach for it
- Sorted array lookup
- "Find smallest x such that f(x) is true" (monotonic predicate)
- Search rotated sorted array
- Capacity / scheduling problems ("can we do this in K days?")

## Template — find target
```js
let l = 0, r = arr.length - 1;
while (l <= r) {
  const m = (l + r) >> 1;             // avoids overflow vs floor((l+r)/2) in some langs
  if (arr[m] === target) return m;
  if (arr[m] < target) l = m + 1;
  else r = m - 1;
}
return -1;
```

## Template — leftmost index where condition is true
```js
let l = 0, r = n;                      // r is exclusive
while (l < r) {
  const m = (l + r) >> 1;
  if (predicate(m)) r = m;
  else l = m + 1;
}
return l;                              // first index where predicate is true (n if none)
```

## Search-on-answer
When the answer space is monotonic in some test:
```js
function canDoIn(days, weights) { /* simulate */ }
let lo = max(weights), hi = sum(weights);
while (lo < hi) {
  const m = (lo + hi) >> 1;
  if (canDoIn(m, weights)) hi = m;
  else lo = m + 1;
}
return lo;
```

## Real World Usage
- Database B-tree lookup
- Find the right version where a bug appeared (`git bisect`)
- Capacity planning ("smallest cluster that handles X req/s")
- Allocation problems

## Common Mistakes
- `(l + r) / 2` overflows in C/Java; use `l + (r - l) / 2`
- Confusing inclusive vs exclusive `r` between templates
- Updating `l = m` (not `m + 1`) → infinite loop
- Forgetting that input must be sorted (or predicate monotonic)

## Prerequisites
- [[Big O Notation]] · [[Two Pointers]]

## What To Learn Next
- [[Heaps]] · [[Trees and BSTs]] · [[Dynamic Programming]]

## Best Learning Resources

### Official Documentation
- [LeetCode — Binary Search tag](https://leetcode.com/tag/binary-search/)
- [neetcode.io — Binary Search](https://neetcode.io/roadmap)

### Best YouTube Resource
- [NeetCode — Binary Search](https://www.youtube.com/c/NeetCode)
- [Errichto — Binary search advanced](https://www.youtube.com/c/Errichto) — competitive-programming depth

### Best Free Course
- [Tech Interview Handbook — Binary Search](https://www.techinterviewhandbook.org/algorithms/binary-search/)
- [USACO Guide — Binary Search](https://usaco.guide/silver/binary-search) — solid free progression

### Best Advanced Resource
- [Russian Doll envelopes & binary search on answer (LeetCode editorial)](https://leetcode.com/problems/russian-doll-envelopes/editorial/)
- [Competitive Programmer's Handbook — Binary search](https://cses.fi/book/book.pdf)

### Best Practice Project
Solve in order: Binary Search, Search Insert Position, First Bad Version, Search in Rotated Sorted Array, Find Minimum in Rotated Sorted Array, Find Peak Element, Capacity to Ship Packages within D Days, Koko Eating Bananas, Median of Two Sorted Arrays.

### Recommended Order to Learn
1. Vanilla "find target"
2. Find-first / find-last (predicate template)
3. Rotated sorted array
4. 2D matrix binary search
5. Search-on-answer
6. Median of two sorted arrays (advanced)

## Interview Questions
**Q. Why is `(l + r) >> 1` safer than `(l + r) / 2`?**
A. JS bitwise shift coerces to 32-bit int; safer with floats. In Java/C/C++, `(l + r) / 2` overflows for large `l, r`.

**Q. Two templates — when to use which?**
A. "Find target" template for exact match. "Leftmost-true" template for predicate-based / answer-space problems.

**Q. Search-on-answer key idea?**
A. If `feasible(x)` is monotonic (false → true at some point), binary-search the threshold.

## Related
- [[Two Pointers]] · [[Heaps]] · [[Trees and BSTs]]
