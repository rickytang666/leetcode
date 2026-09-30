# 3890. Integers With Multiple Sum of Two Cubes

**Difficulty:** Medium

**Tags:** `hash-table`, `sorting`, `counting`, `enumeration`

---

## Description

You are given an integer `n`.

An integer `x` is considered **good** if there exist **at least** two **distinct** pairs `(a, b)` such that:

- `a` and `b` are positive integers.
- `a <= b`
- `x = a^3 + b^3`

Return an array containing all good integers **less than or equal to** `n`, sorted in ascending order.

**Example 1:**

**Input:** n = 4104

**Output:** [1729,4104]

**Explanation:**

Among integers less than or equal to 4104, the good integers are:

- 1729: `1^3 + 12^3 = 1729` and `9^3 + 10^3 = 1729`.
- 4104: `2^3 + 16^3 = 4104` and `9^3 + 15^3 = 4104`.

Thus, the answer is `[1729, 4104]`.

**Example 2:**

**Input:** n = 578

**Output:** []

**Explanation:**

There are no good integers less than or equal to 578, so the answer is an empty array.

**Constraints:**

- `1 <= n <= 10^9`

---

## Hints

<details>
<summary>Hint 1</summary>

Iterate over all pairs `(a, b)` with `a <= b` and `a^3 + b^3 <= n`
</details>

<details>
<summary>Hint 2</summary>

Use a map to count how many times each value of `a^3 + b^3` appears
</details>

<details>
<summary>Hint 3</summary>

A value is good if it can be formed by at least two distinct pairs
</details>

<details>
<summary>Hint 4</summary>

Collect all such values and return them in sorted order
</details>
