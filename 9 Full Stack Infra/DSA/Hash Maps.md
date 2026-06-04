---
tags: [dsa, data-structure, beginner]
---

# Hash Maps

> Key → value lookups in O(1) average time. The most-used data structure in interviews.

## When to reach for it
- "Have we seen X before?"
- Frequency counting
- Pairing complement (Two Sum)
- Grouping by key
- Memoization cache

## JS / TS
```ts
const m = new Map();
m.set('a', 1);
m.has('a');                // true
m.get('a');                // 1
m.delete('a');
m.size;
for (const [k, v] of m) ...;

// counting pattern
const freq = new Map();
for (const x of arr) freq.set(x, (freq.get(x) ?? 0) + 1);

// Set when you only need keys
const seen = new Set();
seen.add('x'); seen.has('x');
```

## Why O(1) average
Hash function distributes keys across buckets. Collisions resolved via chaining or open addressing. Worst case O(n) on adversarial input — modern languages mitigate with random seeds.

## Real World Usage
- DB indexes (hash indexes)
- Caches (LRU layer above)
- Routing tables
- Deduplication
- Joins on keys
- Memoization

## Common Mistakes
- Using object as key in `Map` — works (reference equality), but `obj.toString()` collisions break `Object`-as-map
- `obj['constructor']` and other inherited keys leaking — use `new Map()` for untrusted keys
- Mutating a key after insertion → key becomes unfindable
- Treating order as undefined — `Map` preserves insertion order

## Prerequisites
- [[Big O Notation]]

## What To Learn Next
- [[Two Pointers]] · [[Sliding Window]] · [[Trees and BSTs]]

## Best Learning Resources

### Official Documentation
- [MDN — Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [MDN — Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)

### Best YouTube Resource
- [NeetCode — Hash Map problems](https://www.youtube.com/c/NeetCode)
- [Web Dev Simplified — Map vs Object](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [neetcode.io — Arrays & Hashing track](https://neetcode.io/)
- [Tech Interview Handbook — Hash table](https://www.techinterviewhandbook.org/algorithms/hash-table/)

### Best Advanced Resource
- [How HashMap works internally — JEP / Hashtable papers](https://en.wikipedia.org/wiki/Hash_table)
- [Robin Hood hashing, Cuckoo hashing — Wikipedia](https://en.wikipedia.org/wiki/Hash_table#Collision_resolution)

### Best Practice Project
Two Sum, Group Anagrams, Top K Frequent Elements (with [[Heaps]]), Valid Anagram, Contains Duplicate, Longest Consecutive Sequence, Subarray Sum Equals K, Find All Anagrams in a String, LRU Cache.

### Recommended Order to Learn
1. Map vs Object (when to use which in JS)
2. Frequency counting + Two Sum
3. Group-by patterns (Group Anagrams)
4. Prefix-sum + map (Subarray Sum Equals K)
5. LRU cache (`Map` + ordering)

## Interview Questions
**Q. `Map` vs plain object in JS?**
A. `Map` allows any key type, preserves insertion order, has size, iterates without inherited junk. Use `Map` for dynamic dictionaries.

**Q. Worst-case time?**
A. O(n) on adversarial collisions. JS engines randomize seeds to mitigate.

**Q. How does LRU cache work?**
A. `Map` of key→value plus moving accessed keys to the end on every read; oldest key is `.keys().next()`. Cap size and evict on overflow.

**Q. Why does mutating a key break the map?**
A. Keys are placed by hash; mutating changes the hash but not the bucket location.

## Related
- [[Big O Notation]] · [[Two Pointers]] · [[Sliding Window]] · [[Heaps]]
