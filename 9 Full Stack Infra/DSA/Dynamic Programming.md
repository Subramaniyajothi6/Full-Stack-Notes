---
tags: [dsa, pattern, advanced]
---

# Dynamic Programming

> Solve problems by combining solutions to overlapping subproblems. Memoize or tabulate.

## When to reach for it
- Optimal substructure (problem solvable from sub-solutions)
- Overlapping subproblems (same subproblem solved many times)
- "Number of ways", "min/max cost", "longest", "shortest" with sequence/grid input

## Two flavors

### Top-down (memoization) — usually clearer to write
```js
function fib(n, memo = new Map()) {
  if (n < 2) return n;
  if (memo.has(n)) return memo.get(n);
  const r = fib(n - 1, memo) + fib(n - 2, memo);
  memo.set(n, r);
  return r;
}
```

### Bottom-up (tabulation) — usually faster, no recursion
```js
function fib(n) {
  if (n < 2) return n;
  const dp = new Array(n + 1);
  dp[0] = 0; dp[1] = 1;
  for (let i = 2; i <= n; i++) dp[i] = dp[i-1] + dp[i-2];
  return dp[n];
}
```

## Common archetypes
| Pattern             | Example                              |
| ------------------- | ------------------------------------ |
| 1D                  | House Robber, Climbing Stairs         |
| 2D grid             | Unique Paths, Min Path Sum            |
| Knapsack            | 0/1 Knapsack, Coin Change             |
| Longest subseq.     | LIS, LCS                              |
| Edit distance       | Levenshtein                           |
| Interval DP         | Burst Balloons                        |
| State machine       | Best Time to Buy/Sell Stock variants  |

## Recipe (top-down)
1. Define the recursive subproblem (`f(i)` or `f(i, j, ...)`)
2. Write the recurrence (base case + transitions)
3. Memoize on the parameters
4. Convert to bottom-up if needed for perf

## Real World Usage
- Edit distance for fuzzy search (`fzf`, `git diff`)
- Cell-phone keyboard predictions
- Bioinformatics alignment (BLAST)
- Compilation register allocation
- Resource optimization

## Common Mistakes
- Treating any recursion problem as DP — DP needs *overlapping* subproblems
- Wrong memoization key (missing a parameter)
- Off-by-one in base cases
- Mutating shared state inside the recurrence
- Top-down stack overflow on huge inputs (switch to bottom-up)

## Prerequisites
- Recursion · [[Big O Notation]] · [[DFS]]

## What To Learn Next
- [[Greedy]] · [[Backtracking]]

## Best Learning Resources

### Official Documentation
- [LeetCode — DP tag](https://leetcode.com/tag/dynamic-programming/)
- [neetcode.io — DP track](https://neetcode.io/roadmap)

### Best YouTube Resource
- [Aditya Verma — DP playlist](https://www.youtube.com/c/AdityaVermaTheProgrammingLord) — best DP teacher on YouTube
- [NeetCode — DP](https://www.youtube.com/c/NeetCode)
- [Errichto — DP for competitive programming](https://www.youtube.com/c/Errichto)

### Best Free Course
- [USACO Guide — DP](https://usaco.guide/gold/intro-dp)
- [MIT 6.006 (free)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — DP lectures

### Best Advanced Resource
- [Competitive Programmer's Handbook — DP](https://cses.fi/book/book.pdf)
- [Atcoder Educational DP Contest](https://atcoder.jp/contests/dp/tasks) — 26 progressive DP problems

### Best Practice Project
Climbing Stairs → House Robber → Coin Change → Longest Increasing Subsequence → Longest Common Subsequence → Edit Distance → Word Break → Best Time to Buy/Sell Stock IV → Burst Balloons → Regular Expression Matching. Re-solve each top-down then bottom-up.

### Recommended Order to Learn
1. 1D DP (Climbing Stairs, House Robber)
2. Decision DP (Coin Change variants)
3. 2D grid DP (Unique Paths, Min Path Sum)
4. Subsequence DP (LIS, LCS, Edit Distance)
5. Knapsack 0/1 + unbounded
6. State-machine DP (stock buy/sell)
7. Interval DP

## Interview Questions
**Q. Memoization vs tabulation?**
A. Memo is top-down recursion + cache; only computes needed states. Tabulation is bottom-up loop; faster constants, no stack risk.

**Q. How to find DP states?**
A. Identify what changes between recursive calls. Each varying value is a state dimension.

**Q. Space optimization?**
A. Often only the last 1–2 rows of the table are needed → reduce O(n²) to O(n).

**Q. DP vs Greedy?**
A. Greedy commits to a choice based on local optimum; DP considers all choices and remembers them.

## Related
- [[Greedy]] · [[Backtracking]] · [[DFS]]
