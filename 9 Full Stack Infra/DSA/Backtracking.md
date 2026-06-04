---
tags: [dsa, pattern, advanced]
---

# Backtracking

> DFS that tries options, undoes them on dead ends, and explores alternatives. Standard for combinatorial search.

## When to reach for it
- Permutations, combinations, subsets
- N-Queens, Sudoku
- Word Search in grid
- Generate Parentheses
- Constraint-satisfaction problems

## Template
```js
function backtrack(state) {
  if (isComplete(state)) {
    record(state);
    return;
  }
  for (const choice of choices(state)) {
    if (!isValid(state, choice)) continue;
    apply(state, choice);
    backtrack(state);
    undo(state, choice);
  }
}
```

## Subsets template
```js
function subsets(nums) {
  const out = [];
  function dfs(i, path) {
    if (i === nums.length) { out.push([...path]); return; }
    dfs(i + 1, path);                  // skip
    path.push(nums[i]);
    dfs(i + 1, path);                  // take
    path.pop();
  }
  dfs(0, []);
  return out;
}
```

## Permutations template
```js
function permute(nums) {
  const out = [], used = new Array(nums.length).fill(false);
  function dfs(path) {
    if (path.length === nums.length) { out.push([...path]); return; }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true; path.push(nums[i]);
      dfs(path);
      path.pop(); used[i] = false;
    }
  }
  dfs([]);
  return out;
}
```

## Real World Usage
- Constraint solvers (SAT, scheduling)
- Game-playing AI (chess move search before MCTS)
- Crossword / Sudoku solvers
- Theorem provers
- Parsers with ambiguous grammars

## Common Mistakes
- Forgetting to undo state → corruption
- Pushing references to mutable state into result (`out.push(path)` instead of `[...path]`)
- Missing pruning → TLE on problems where the search space is enormous
- Treating "subsets" and "permutations" with the same template

## Prerequisites
- Recursion · [[DFS]]

## What To Learn Next
- [[Dynamic Programming]] · [[Trees and BSTs]] · [[Tries]]

## Best Learning Resources

### Official Documentation
- [LeetCode — Backtracking tag](https://leetcode.com/tag/backtracking/)
- [neetcode.io — Backtracking](https://neetcode.io/roadmap)

### Best YouTube Resource
- [NeetCode — Backtracking playlist](https://www.youtube.com/c/NeetCode)
- [Errichto — Recursion and backtracking](https://www.youtube.com/c/Errichto)

### Best Free Course
- [Tech Interview Handbook — Backtracking](https://www.techinterviewhandbook.org/algorithms/backtracking/)
- [neetcode.io free backtracking track](https://neetcode.io/)

### Best Advanced Resource
- [Knuth — "Dancing Links" paper](https://arxiv.org/abs/cs/0011047) — backtracking on steroids for exact cover

### Best Practice Project
Solve in order: Subsets, Subsets II (dedup), Permutations, Permutations II, Combinations, Combination Sum, Combination Sum II, Word Search, Letter Combinations of a Phone Number, Generate Parentheses, N-Queens, Sudoku Solver.

### Recommended Order to Learn
1. Subsets (binary include/exclude)
2. Permutations
3. Combinations
4. With duplicates (sort + skip)
5. Grid + Word Search (DFS in grid)
6. Constraint problems (N-Queens, Sudoku)

## Interview Questions
**Q. Time complexity bounds?**
A. Often O(n × 2ⁿ) for subsets, O(n × n!) for permutations. Pruning improves the constant but not asymptotic class.

**Q. How to handle duplicates?**
A. Sort input; skip when `i > start && nums[i] === nums[i-1]` to dedupe at each level.

**Q. Backtracking vs DP — when which?**
A. Backtracking explores all configurations. DP exploits overlapping subproblems. If subproblems repeat, prefer DP/memoization.

## Related
- [[DFS]] · [[Dynamic Programming]] · [[Tries]]
