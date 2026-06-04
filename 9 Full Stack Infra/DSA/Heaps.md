---
tags: [dsa, data-structure, intermediate]
---

# Heaps

> Tree-based data structure where each node satisfies a heap property (min-heap: parent ≤ children). Backbone of priority queues.

## Operations
| Op            | Time      |
| ------------- | --------- |
| `peek` (top)  | O(1)      |
| `push`        | O(log n)  |
| `pop`         | O(log n)  |
| Build from n  | O(n)      |
| Heapsort      | O(n log n)|

## When to reach for it
- "Top K" problems
- Schedulers, task queues with priority
- Dijkstra's shortest path
- Median maintenance (two-heap trick)
- Merge K sorted lists

## JS — there's no built-in
Use a small implementation or a library (`@datastructures-js/priority-queue`).

```js
class MinHeap {
  constructor(cmp = (a, b) => a - b) { this.a = []; this.cmp = cmp; }
  size() { return this.a.length; }
  peek() { return this.a[0]; }
  push(v) {
    this.a.push(v);
    this._up(this.a.length - 1);
  }
  pop() {
    const top = this.a[0], last = this.a.pop();
    if (this.a.length) { this.a[0] = last; this._down(0); }
    return top;
  }
  _up(i) {
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.cmp(this.a[i], this.a[p]) < 0) { [this.a[i], this.a[p]] = [this.a[p], this.a[i]]; i = p; }
      else break;
    }
  }
  _down(i) {
    const n = this.a.length;
    while (true) {
      let l = 2*i + 1, r = l + 1, best = i;
      if (l < n && this.cmp(this.a[l], this.a[best]) < 0) best = l;
      if (r < n && this.cmp(this.a[r], this.a[best]) < 0) best = r;
      if (best === i) break;
      [this.a[i], this.a[best]] = [this.a[best], this.a[i]];
      i = best;
    }
  }
}
```

## Two-heap median pattern
Maintain `low` (max-heap) for the lower half and `high` (min-heap) for the upper. After each insert, rebalance so sizes differ by at most 1. Median = top of bigger heap or average of tops.

## Real World Usage
- OS process scheduler (priority queue)
- Network packet queueing (QoS)
- Event simulators
- A* / Dijkstra search
- Streaming top-K (analytics)

## Common Mistakes
- Using a sorted array — push is O(n)
- Forgetting to handle the empty-heap pop
- Wrong comparator direction (`cmp` returning >0 vs <0)
- Treating Top-K as "sort entire array" — use a size-K heap for O(n log k)

## Prerequisites
- [[Big O Notation]] · [[Trees and BSTs]]

## What To Learn Next
- [[BFS]] (Dijkstra) · [[Topological Sort]] · [[Greedy]]

## Best Learning Resources

### Official Documentation
- [LeetCode — Heap (Priority Queue) tag](https://leetcode.com/tag/heap-priority-queue/)
- [neetcode.io — Heap track](https://neetcode.io/roadmap)

### Best YouTube Resource
- [Abdul Bari — Heaps and Heapsort](https://www.youtube.com/c/AbdulBariYT)
- [NeetCode — Heap problems](https://www.youtube.com/c/NeetCode)

### Best Free Course
- [USACO Guide — Heaps](https://usaco.guide/gold/PURS#heaps)
- [neetcode.io free track](https://neetcode.io/)

### Best Advanced Resource
- [Fibonacci heap (CLRS)](https://en.wikipedia.org/wiki/Fibonacci_heap) — better amortized for Dijkstra
- [Pairing heap, leftist heap (Wikipedia)](https://en.wikipedia.org/wiki/Pairing_heap)

### Best Practice Project
Kth Largest Element in Array, Top K Frequent Elements, Last Stone Weight, K Closest Points to Origin, Find Median from Data Stream, Merge K Sorted Lists, Task Scheduler, Reorganize String.

### Recommended Order to Learn
1. Conceptual heap (parent/child indices)
2. Implement push/pop on array
3. Top-K with size-K heap
4. Two-heap median trick
5. Heap in Dijkstra

## Interview Questions
**Q. Why O(n) to build a heap, not O(n log n)?**
A. Tighter analysis: most nodes are near leaves where sift-down work is bounded — sum is geometric, totals O(n).

**Q. Top K — heap of size K vs sort whole array?**
A. Heap O(n log k); full sort O(n log n). For small k, heap wins.

**Q. Why two heaps for streaming median?**
A. Constant-time top access + O(log n) insert keeps median always at the heap roots.

## Related
- [[Trees and BSTs]] · [[Greedy]] · [[BFS]]
