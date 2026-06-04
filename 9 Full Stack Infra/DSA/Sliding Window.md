---
tags: [dsa, pattern, beginner]
---

# Sliding Window

> Two pointers `l` and `r` defining a window over a contiguous range. Expand `r`, shrink `l` based on a condition.

## When to reach for it
- "Longest / shortest substring with property X"
- "Sum / count of subarrays with property X"
- Fixed-size window problems (max sum of window of size k)
- String matching with constraints

## Two flavors

### Fixed window (size k)
```js
let sum = 0;
for (let i = 0; i < k; i++) sum += arr[i];
let best = sum;
for (let r = k; r < arr.length; r++) {
  sum += arr[r] - arr[r - k];
  best = Math.max(best, sum);
}
```

### Variable window
```js
let l = 0, best = 0;
const seen = new Map();
for (let r = 0; r < s.length; r++) {
  seen.set(s[r], (seen.get(s[r]) ?? 0) + 1);
  while (windowInvalid()) {
    seen.set(s[l], seen.get(s[l]) - 1);
    if (seen.get(s[l]) === 0) seen.delete(s[l]);
    l++;
  }
  best = Math.max(best, r - l + 1);
}
```

## Example — Longest substring without repeating characters
```js
function lengthOfLongestSubstring(s) {
  const seen = new Map();
  let l = 0, best = 0;
  for (let r = 0; r < s.length; r++) {
    if (seen.has(s[r]) && seen.get(s[r]) >= l) l = seen.get(s[r]) + 1;
    seen.set(s[r], r);
    best = Math.max(best, r - l + 1);
  }
  return best;
}
```

## Real World Usage
- Rate limiting (sliding-window counters)
- Time-series anomaly detection
- Streaming aggregations
- Token bucket / leaky bucket variants

## Common Mistakes
- Forgetting to remove the leftmost element from your window state when shrinking
- `Math.max` with `r - l` (off by one — use `r - l + 1`)
- Confusing "longest" (maximize while valid) vs "shortest" (minimize while valid)
- Resetting state instead of incrementally updating

## Prerequisites
- [[Two Pointers]] · [[Hash Maps]]

## What To Learn Next
- [[Fast and Slow Pointers]] · [[Binary Search]]

## Best Learning Resources

### Official Documentation
- [LeetCode — Sliding Window tag](https://leetcode.com/tag/sliding-window/)
- [neetcode.io roadmap — Sliding Window](https://neetcode.io/roadmap)

### Best YouTube Resource
- [NeetCode — Sliding Window playlist](https://www.youtube.com/c/NeetCode)
- [Aditya Verma — Sliding Window playlist](https://www.youtube.com/c/AdityaVermaTheProgrammingLord) — best dedicated coverage

### Best Free Course
- [Tech Interview Handbook — Sliding Window](https://www.techinterviewhandbook.org/algorithms/sliding-window/)
- [neetcode.io free track](https://neetcode.io/)

### Best Advanced Resource
- [Sean Prashad's LeetCode patterns](https://seanprashad.com/leetcode-patterns/)
- ["Competitive Programmer's Handbook" (Antti Laaksonen, free)](https://cses.fi/book/book.pdf)

### Best Practice Project
Solve in order: Maximum Sum Subarray of Size K, Longest Substring Without Repeating Characters, Longest Substring with K Distinct Characters, Minimum Window Substring, Permutation in String, Sliding Window Maximum. After each, articulate the invariant in one sentence.

### Recommended Order to Learn
1. Fixed-size window
2. Variable window with simple counter
3. Variable window with Hash Map state
4. Minimum-window pattern (shrink to find shortest)
5. Sliding Window Maximum (deque optimization)

## Interview Questions
**Q. Time complexity?**
A. O(n) — each element enters and leaves the window at most once.

**Q. When does sliding window NOT work?**
A. When the underlying problem requires non-contiguous selection or sorted-only input — pick another pattern.

**Q. Why is Sliding Window Maximum O(n) with a deque?**
A. Each element is pushed and popped at most once across the whole iteration, despite the inner `while`.

## Related
- [[Two Pointers]] · [[Hash Maps]] · [[Fast and Slow Pointers]]
