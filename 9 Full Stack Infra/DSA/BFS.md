---
tags: [dsa, pattern, intermediate, graph]
---

# BFS

> Breadth-First Search. Explore by levels using a queue. Finds shortest path in unweighted graphs.

## When to reach for it
- Shortest path in unweighted graph or grid
- Level-order traversal of a tree
- Word ladder / shortest transformation
- Multi-source spread (rotting oranges, bushfire)
- Bipartite check

## Template — graph
```js
function bfs(start, adj) {
  const visited = new Set([start]);
  const q = [start];
  while (q.length) {
    const node = q.shift();             // O(n) per shift; use deque for big inputs
    for (const next of adj.get(node) ?? []) {
      if (!visited.has(next)) {
        visited.add(next);
        q.push(next);
      }
    }
  }
}
```

## Level-by-level
```js
let level = 0;
while (q.length) {
  const size = q.length;
  for (let i = 0; i < size; i++) {
    const node = q.shift();
    // process node at this level
    for (const next of neighbors(node)) {
      if (!visited.has(next)) {
        visited.add(next);
        q.push(next);
      }
    }
  }
  level++;
}
```

## Multi-source BFS
```js
const q = [];
for (const src of sources) { q.push(src); visited.add(src); }
// then run normal BFS
```

## Real World Usage
- Web crawl with bounded depth
- Social network "people you may know" (n-hops)
- Network flooding
- Build-system topological dep level
- Routing in unweighted networks

## Common Mistakes
- `array.shift()` is O(n) — use a deque (`Deno.collections` / `denque` / index-based) for big inputs
- Adding to `visited` on dequeue instead of enqueue → re-visiting
- Forgetting bounds in grid problems
- Mixing BFS with weighted graphs (use Dijkstra instead)

## Prerequisites
- [[Queues]] · [[Graphs]] · [[Hash Maps]]

## What To Learn Next
- [[DFS]] · [[Topological Sort]] · [[Heaps]] (Dijkstra)

## Best Learning Resources

### Official Documentation
- [LeetCode — BFS tag](https://leetcode.com/tag/breadth-first-search/)
- [neetcode.io — Graph track](https://neetcode.io/roadmap)

### Best YouTube Resource
- [NeetCode — BFS playlist](https://www.youtube.com/c/NeetCode)
- [William Fiset — Graph theory series](https://www.youtube.com/c/WilliamFiset-videos) — best graph educator

### Best Free Course
- [USACO Guide — BFS](https://usaco.guide/silver/graph-traversal)
- [neetcode.io free graph track](https://neetcode.io/)

### Best Advanced Resource
- [Competitive Programmer's Handbook — Graph traversal](https://cses.fi/book/book.pdf)
- [0-1 BFS (deque trick) — cp-algorithms](https://cp-algorithms.com/graph/01_bfs.html)

### Best Practice Project
Solve in order: Number of Islands, Rotting Oranges, Walls and Gates, Pacific Atlantic Water Flow, Word Ladder, Shortest Path in Binary Matrix, 01 Matrix, Open the Lock, Bus Routes.

### Recommended Order to Learn
1. Tree level-order traversal
2. Grid BFS (Number of Islands)
3. Multi-source (Rotting Oranges)
4. Implicit-graph BFS (Word Ladder)
5. 0-1 BFS (deque trick)
6. Bidirectional BFS

## Interview Questions
**Q. BFS vs DFS — when?**
A. BFS for shortest unweighted path / level-order. DFS for "any path" / connectivity / backtracking.

**Q. Why is BFS correct for shortest unweighted path?**
A. It explores all length-1 paths before length-2, etc. — first time you reach a node is via the shortest path.

**Q. Time and space?**
A. O(V + E) time, O(V) space.

## Related
- [[DFS]] · [[Graphs]] · [[Topological Sort]] · [[Queues]]
