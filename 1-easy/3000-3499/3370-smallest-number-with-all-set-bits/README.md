# 3370. Smallest Number With All Set Bits

**Difficulty:** Easy

**Tags:** `math`, `bit-manipulation`

---

## Description

You are given a _positive_ number `n`.

Return the **smallest** number `x` **greater than** or **equal to** `n`, such that the binary representation of `x` contains only set bits

**Example 1:**

**Input:** n = 5

**Output:** 7

**Explanation:**

The binary representation of 7 is `"111"`.

**Example 2:**

**Input:** n = 10

**Output:** 15

**Explanation:**

The binary representation of 15 is `"1111"`.

**Example 3:**

**Input:** n = 3

**Output:** 3

**Explanation:**

The binary representation of 3 is `"11"`.

**Constraints:**

- `1 <= n <= 1000`

---

## Hints

<details>
<summary>Hint 1</summary>

Find the strictly greater power of 2, and subtract 1 from it.
</details>
