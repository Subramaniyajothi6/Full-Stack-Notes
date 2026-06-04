---
tags: [dsa, data-structure, intermediate]
---

# Trees and BSTs

> Hierarchical data structure. Binary Search Trees (BSTs) maintain sorted order for O(log n) lookup on balanced trees.

## Tree basics
- **Root, parent, child, leaf, height, depth**
- **Binary tree** — at most 2 children per node
- **BST** — left subtree < node < right subtree
- **Balanced** — heights of two subtrees differ by at most 1 (AVL, Red-Black)

## Traversals
| Order      | Visit         | Use                          |
| ---------- | ------------- | ---------------------------- |
| Pre-order  | root → L → R  | clone, prefix expressions    |
| In-order   | L → root → R  | sorted output of BST         |
| Post-order | L → R → root  | delete, postfix expressions  |
| Level-order| BFS           | level statistics             |

## DFS template
```js
function inorder(node, out) {
  if (!node) return;
  inorder(node.left, out);
  out.push(node.val);
  inorder(node.right, out);
}
```

## BFS / level-order
See [[BFS]].

## BST operations
| Op       | Balanced  | Worst (skewed) |
| -------- | --------- | -------------- |
| Search   | O(log n)  | O(n)           |
| Insert   | O(log n)  | O(n)           |
| Delete   | O(log n)  | O(n)           |

## Real World Usage
- Filesystems (directories)
- DB indexes (B-trees, Red-Black trees)
- DOM (browser rendering tree)
- Auto-completion ([[Tries]] are tree-shaped)
- Expression parsing (AST)
- Linux kernel scheduler (rbtree)

## Common Mistakes
- Stack overflow on deeply unbalanced trees — use iterative or increase stack
- Forgetting BST property direction (left < root < right, not the other way)
- BST delete edge cases (two children — replace with in-order successor)
- Mutating shared subtrees thinking you copied

## Prerequisites
- Recursion · [[DFS]] · [[BFS]] · [[Stacks]] · [[Queues]]

## What To Learn Next
- [[Heaps]] · [[Tries]] · [[Graphs]]

## Best Learning Resources

### Official Documentation
- [LeetCode — Tree tag](https://leetcode.com/tag/tree/)
- [neetcode.io — Trees track](https://neetcode.io/roadmap)

### Best YouTube Resource
- [NeetCode — Tree problems](https://www.youtube.com/c/NeetCode)
- [William Fiset — Tree algorithms](https://www.youtube.com/c/WilliamFiset-videos)

### Best Free Course
- [USACO Guide — Trees](https://usaco.guide/silver/intro-tree)
- [neetcode.io free trees track](https://neetcode.io/)

### Best Advanced Resource
- ["Algorithms" — Sedgewick (BST/Red-Black tree chapters)](https://algs4.cs.princeton.edu/) — visualizations
- [Red-Black tree tutorial — cp-algorithms](https://cp-algorithms.com/data_structures/treap.html)

### Best Practice Project
Invert Binary Tree, Maximum Depth, Same Tree, Subtree of Another Tree, Lowest Common Ancestor of BST, Binary Tree Level Order Traversal, Validate BST, Kth Smallest Element in BST, Construct Binary Tree from Preorder + Inorder, Serialize and Deserialize Binary Tree.

### Recommended Order to Learn
1. Recursive traversals (pre/in/post)
2. Level-order (BFS)
3. BST property + validate
4. Tree construction from traversals
5. LCA (BST and general binary tree)
6. Serialize / deserialize
7. Balanced trees (AVL, Red-Black) — concept-level

## Interview Questions
**Q. Why is BST in-order traversal sorted?**
A. By definition: left subtree < root < right subtree, so in-order visits in non-decreasing order.

**Q. Worst-case insert?**
A. O(n) on skewed (sorted-input) BST. Self-balancing trees (AVL, Red-Black) keep O(log n) guaranteed.

**Q. How would you find the LCA of two nodes in a BST?**
A. Walk from root. If both targets less than node → go left. If both greater → go right. Else current node is LCA.

**Q. Convert sorted array to balanced BST?**
A. Recursively pick middle as root; recurse on halves.

## Related
- [[Heaps]] · [[Tries]] · [[DFS]] · [[BFS]] · [[Graphs]]
