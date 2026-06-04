---
tags: [dsa, pattern, intermediate]
---

# Fast and Slow Pointers

> Two pointers moving at different speeds. Standard for cycle detection in linked lists or sequences.

## When to reach for it
- Linked list cycle detection (Floyd's algorithm)
- Find middle of linked list
- Find cycle's start
- Happy number / sequence cycle detection
- Palindromic linked list

## Template — cycle detection
```js
let slow = head, fast = head;
while (fast && fast.next) {
  slow = slow.next;
  fast = fast.next.next;
  if (slow === fast) return true;     // cycle exists
}
return false;
```

## Find cycle entry (Floyd)
```js
// after slow === fast inside cycle:
slow = head;
while (slow !== fast) { slow = slow.next; fast = fast.next; }
return slow;   // entry point
```

## Find middle of linked list
```js
let slow = head, fast = head;
while (fast && fast.next) { slow = slow.next; fast = fast.next.next; }
return slow;
```

## Real World Usage
- Detecting cycles in iterators / sequences (no extra memory)
- Cycle detection in graph adjacency lists (lightweight check)
- Sliding window's cousin for ordered linked structures

## Common Mistakes
- Not checking `fast && fast.next` → null dereference
- Returning the meeting point as cycle entry (it's not — see Floyd's second pass)
- Using a hash set for cycle detection — works but uses O(n) extra memory
- Off-by-one when finding the "middle" (which middle for even length?)

## Prerequisites
- [[Linked Lists]] · [[Two Pointers]]

## What To Learn Next
- [[Binary Search]] · [[Hash Maps]]

## Best Learning Resources

### Official Documentation
- [LeetCode — Linked List tag](https://leetcode.com/tag/linked-list/)
- [neetcode.io — Linked List track](https://neetcode.io/roadmap)

### Best YouTube Resource
- [NeetCode — Linked List Cycle](https://www.youtube.com/c/NeetCode) — clean Floyd explanation
- [Back To Back SWE — Floyd's algorithm derivation](https://www.youtube.com/c/BackToBackSWE)

### Best Free Course
- [neetcode.io](https://neetcode.io/) — free track covers this end-to-end

### Best Advanced Resource
- [Floyd's tortoise and hare paper / proof](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare) — math
- [Brent's algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Brent's_algorithm) — alternative variant

### Best Practice Project
Solve, in this order: Linked List Cycle, Linked List Cycle II (entry point), Middle of Linked List, Happy Number, Palindrome Linked List, Reorder List. For Cycle II, derive Floyd's "head + meeting" proof on paper.

### Recommended Order to Learn
1. Cycle detection (does cycle exist?)
2. Cycle entry point (Floyd's)
3. Middle of linked list
4. Happy Number (sequence cycle)
5. Palindromic linked list (reverse second half)
6. Reorder list

## Interview Questions
**Q. Why does fast pointer move 2× and not 3×?**
A. 2× is the smallest speed difference that still guarantees meeting in any cycle. Higher multiples work but no benefit.

**Q. Why use Floyd's over a Hash Set?**
A. O(1) extra space vs O(n).

**Q. Why does the entry-point trick work?**
A. Math: distance from head to entry equals distance from meeting point back to entry (modular arithmetic on cycle length).

## Related
- [[Linked Lists]] · [[Two Pointers]] · [[Sliding Window]]
