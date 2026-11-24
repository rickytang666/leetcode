# 1315. Sum of Nodes with Even-Valued Grandparent

**Difficulty:** Medium

**Tags:** `tree`, `depth-first-search`, `breadth-first-search`, `binary-tree`

---

## Description

Given the `root` of a binary tree, return _the sum of values of nodes with an **even-valued grandparent**_. If there are no nodes with an **even-valued grandparent**, return `0`.

A **grandparent** of a node is the parent of its parent if it exists.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/10/even1-tree.jpg)

```
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/10/even2-tree.jpg)

```
Input: root = [1]
Output: 0
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `1 <= Node.val <= 100`

---

## Hints

<details>
<summary>Hint 1</summary>

Traverse the tree keeping the parent and the grandparent.
</details>

<details>
<summary>Hint 2</summary>

If the grandparent of the current node is even-valued, add the value of this node to the answer.
</details>
