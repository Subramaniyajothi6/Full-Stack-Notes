---
tags: [dsa, pattern, intermediate, graph]
---

# DFS

> Depth-First Search. Go as deep as possible, then backtrack. Implementation: recursion or explicit stack.

## When to reach for it
- Tree / graph traversal
- Connectivity / island counting
- Detect cycle (with state coloring)
- Path finding (any path, all paths)
- Backbone of [[Backtracking]]
- Topological sort (post-order)

## Template — graph (recursive)
```js
function dfs(node, visited, adj) {
  if (visited.has(node)) return;
  visited.add(node);
  for (const next of adj.get(node) ?? []) {
    dfs(next, visited, adj);
  }
}
```

## Template — iterative with stack
```js
const stack = [start];
while (stack.length) {
  const node = stack.pop();
  if (visited.has(node)) continue;
  visited.add(node);
  for (const next of adj.get(node) ?? []) stack.push(next);
}
```

## Three colors (cycle detection in directed graph)
```js
const WHITE = 0, GRAY = 1, BLACK = 2;
const color = new Map();
function hasCycle(node) {
  if (color.get(node) === GRAY) return true;       // back-edge
  if (color.get(node) === BLACK) return false;
  color.set(node, GRAY);
  for (const next of adj.get(node) ?? []) {
    if (hasCycle(next)) return true;
  }
  color.set(node, BLACK);
  return false;
}
```

## Real World Usage
- Filesystem walks
- Compiler dependency graphs (cycle detection, build order)
- Sudoku solvers (with [[Backtracking]])
- AST analysis
- Maze solvers
- Garbage-collection mark phase

## Common Mistakes
- Stack overflow on deep graphs — switch to iterative
- Forgetting to mark visited → infinite loop on cycles
- Marking visited at wrong time (before vs after recursion) for specific algorithms
- Confusing pre-order vs post-order needs

## Prerequisites
- Recursion · [[Stacks]] · [[Graphs]]

## What To Learn Next
- [[Backtracking]] · [[Topological Sort]] · [[Union Find]]

## Best Learning Resources

### Official Documentation
- [LeetCode — DFS tag](https://leetcode.com/tag/depth-first-search/)
- [neetcode.io — Graph track](https://neetcode.io/roadmap)

### Best YouTube Resource
- [William Fiset — Graph theory](https://www.youtube.com/c/WilliamFiset-videos)
- [NeetCode — DFS](https://www.youtube.com/c/NeetCode)

### Best Free Course
- [USACO Guide — Graph Traversal](https://usaco.guide/silver/graph-traversal)
- [Sedgewick's Algorithms (Coursera, free audit)](https://www.coursera.org/learn/algorithms-part2)

### Best Advanced Resource
- [cp-algorithms — DFS](https://cp-algorithms.com/graph/depth-first-search.html)
- [Tarjan's SCC algorithm](https://cp-algorithms.com/graph/strongly-connected-components.html) — applied DFS magic

### Best Practice Project
Number of Islands, Max Area of Island, Surrounded Regions, Pacific Atlantic Water Flow, Course Schedule (cycle detect + topo sort), Clone Graph, All Paths From Source to Target, Word Search, Number of Connected Components in an Undirected Graph.

### Recommended Order to Learn
1. Tree DFS (pre/in/post-order)
2. Grid DFS (Number of Islands)
3. Cycle detection (3-color)
4. DFS + memo → [[Dynamic Programming]] cousin
5. Topological sort via post-order
6. Tarjan's SCC

## Interview Questions
**Q. DFS recursive vs iterative — tradeoff?**
A. Recursive is concise but risks stack overflow on deep graphs. Iterative uses explicit stack and is safe but more code.

**Q. Why three colors for directed cycle detection?**
A. WHITE = unvisited, GRAY = in current DFS path (cycle if revisited), BLACK = fully processed (safe).

**Q. Time and space?**
A. O(V + E) time, O(V) space (recursion stack or visited set).

## Related
- [[BFS]] · [[Graphs]] · [[Backtracking]] · [[Topological Sort]]
