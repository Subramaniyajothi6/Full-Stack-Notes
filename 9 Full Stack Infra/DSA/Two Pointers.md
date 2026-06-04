---
tags: [dsa, pattern, beginner]
---

# Two Pointers

> Use two indices walking through a sequence (often from both ends, or at different speeds).

## When to reach for it
- Sorted array problems
- Pair / triplet sums
- Palindromes
- In-place mutations (e.g., remove duplicates)
- Merging two sorted arrays

## Templates

### Opposite ends
```js
let l = 0, r = arr.length - 1;
while (l < r) {
  if (cond) l++;
  else r--;
}
```

### Same direction (read + write)
```js
let write = 0;
for (let read = 0; read < arr.length; read++) {
  if (keep(arr[read])) arr[write++] = arr[read];
}
```

## Example — Two Sum (sorted)
```js
function twoSum(nums, target) {
  let l = 0, r = nums.length - 1;
  while (l < r) {
    const s = nums[l] + nums[r];
    if (s === target) return [l, r];
    if (s < target) l++;
    else r--;
  }
  return [];
}
```

## Real World Usage
- In-place dedup (remove duplicates from sorted array)
- Reverse string / array in place
- Sliding-window cousins
- Merging streams

## Common Mistakes
- Forgetting the array must be sorted for opposite-ends pattern
- Off-by-one when `l <= r` vs `l < r`
- Mutating during iteration without using a write pointer
- Skipping pointer increments after a match (infinite loop)

## Prerequisites
- [[Big O Notation]]

## What To Learn Next
- [[Sliding Window]] · [[Fast and Slow Pointers]] · [[Binary Search]]

## Best Learning Resources

### Official Documentation
- [LeetCode — Two Pointers tag](https://leetcode.com/tag/two-pointers/) — practice set
- [NeetCode roadmap](https://neetcode.io/roadmap) — curated path

### Best YouTube Resource
- [NeetCode — Two Pointers explained](https://www.youtube.com/c/NeetCode) — best LeetCode-pattern channel
- [Back To Back SWE](https://www.youtube.com/c/BackToBackSWE) — methodical walk-throughs

### Best Free Course
- [neetcode.io — Free Two Pointers track](https://neetcode.io/) — curated problem progression
- [Tech Interview Handbook](https://www.techinterviewhandbook.org/algorithms/two-pointers/) — open-source patterns

### Best Advanced Resource
- [Sean Prashad's LeetCode patterns](https://seanprashad.com/leetcode-patterns/) — problem-by-pattern map
- [Educative — Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview) — paid, classic

### Best Practice Project
Solve 8 LeetCode two-pointer problems back-to-back: Valid Palindrome, Two Sum II, 3Sum, Container With Most Water, Trapping Rain Water, Remove Duplicates from Sorted Array, Move Zeroes, Sort Colors. For each, write the time + space complexity from scratch.

### Recommended Order to Learn
1. Opposite-ends template + Two Sum II
2. Same-direction (read/write) + Remove Duplicates
3. 3Sum (master loop + two pointers inside)
4. Container With Most Water + Trapping Rain Water
5. Variants on linked lists ([[Fast and Slow Pointers]])

## Interview Questions
**Q. Why does opposite-ends require sorted input?**
A. Without order, a "too small" decision can't tell which side to advance.

**Q. Time and space?**
A. Typically O(n) time, O(1) space — that's the whole point.

**Q. How does this differ from sliding window?**
A. Two pointers describe a position pair; sliding window adds the constraint that the pair encloses a continuous range that grows/shrinks based on a condition.

## Related
- [[Sliding Window]] · [[Fast and Slow Pointers]] · [[Binary Search]]
