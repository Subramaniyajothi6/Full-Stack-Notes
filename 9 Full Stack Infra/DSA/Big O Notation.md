---
tags: [dsa, beginner, foundation]
---

# Big O Notation

> Asymptotic upper bound on how an algorithm's time or space grows as input size grows.

## Why it matters
The shared vocabulary for talking about efficiency. Lets you reason about which algorithm scales without running it.

## Common classes (slow → fast growth)
| Big O      | Example                         |
| ---------- | ------------------------------- |
| O(1)       | hash map lookup, array index    |
| O(log n)   | binary search                   |
| O(n)       | single loop, linear scan        |
| O(n log n) | mergesort, heapsort             |
| O(n²)      | nested loops                    |
| O(2ⁿ)      | recursive fib, subset enumeration|
| O(n!)      | permutations, traveling salesman|

## Cousins
- **Big Ω** — best case (lower bound)
- **Big Θ** — tight bound (when O and Ω match)
- **Amortized** — average per op over a sequence (e.g., dynamic array push is O(1) amortized)

## How to read code
- One independent loop over n → O(n)
- Two nested independent loops → O(n²)
- Halving each step → O(log n)
- Doubling work each step → O(2ⁿ)
- Drop constants and lower-order terms — O(3n + 5) is O(n)

## Real World Usage
- Choosing data structure (hash map vs sorted array)
- Predicting whether a brute force is fast enough
- Reasoning about cache friendliness, not just operations
- Benchmark sanity-checking

## Common Mistakes
- Confusing time with space — analyze both
- Treating "n²" as "always slow" — for small n, it can win on constants
- Ignoring hidden costs (string concatenation, list slicing)
- Using O() to compare two O(n) algorithms — constants and locality matter

## Prerequisites
- Basic loops and recursion

## What To Learn Next
- [[Two Pointers]] · [[Binary Search]] · [[Hash Maps]]

## Best Learning Resources

### Official Documentation
- [Big-O cheatsheet (community)](https://www.bigocheatsheet.com/) — handy reference for every common DS/algo

### Best YouTube Resource
- [HackerRank — Big O Notation](https://www.youtube.com/c/HackerrankOfficial) — clear visual intro
- [Abdul Bari — Algorithm complexity](https://www.youtube.com/c/AbdulBariYT) — algorithm course classic

### Best Free Course
- [Khan Academy — Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms) — broad foundation
- [MIT 6.006 (free OCW)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — university-level

### Best Advanced Resource
- ["Introduction to Algorithms" (CLRS)](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/) — definitive textbook
- [Algorithms by Sedgewick (Princeton free Coursera)](https://www.coursera.org/learn/algorithms-part1)

### Best Practice Project
Take 5 LeetCode problems you've already solved. For each: re-state the time and space complexity in Big O, identify the bottleneck, and propose one specific change that would improve it (or argue why it's already optimal).

### Recommended Order to Learn
1. Read code, count loops/recursive calls
2. Memorize common classes
3. Practice deriving for snippets you didn't write
4. Master/recurrence trees for divide-and-conquer
5. Amortized analysis (dynamic arrays, hash maps)

## Interview Questions
**Q. Time complexity of `arr.includes(x)` vs `set.has(x)`?**
A. Array O(n), Set O(1) average.

**Q. Why is mergesort O(n log n)?**
A. log n levels of recursion, each level does O(n) work merging.

**Q. Hash map worst case is O(n) — when?**
A. Adversarial input causing all keys to collide into one bucket. Modern languages mitigate with random hash seeds.

**Q. What's amortized analysis?**
A. Average cost per operation over a sequence. Dynamic array push is O(n) when it resizes, but O(1) amortized.

## Related
- [[Hash Maps]] · [[Binary Search]] · [[Dynamic Programming]]
