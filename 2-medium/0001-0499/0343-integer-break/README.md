# 343. Integer Break

**Difficulty:** Medium

**Tags:** `math`, `dynamic-programming`

---

## Description

Given an integer `n`, break it into the sum of `k` **positive integers**, where `k >= 2`, and maximize the product of those integers.

Return _the maximum product you can get_.

**Example 1:**

```
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

**Example 2:**

```
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

**Constraints:**

- `2 <= n <= 58`

---

## Hints

<details>
<summary>Hint 1</summary>

There is a simple O(n) solution to this problem.
</details>

<details>
<summary>Hint 2</summary>

You may check the breaking results of _n_ ranging from 7 to 10 to discover the regularities.
</details>
