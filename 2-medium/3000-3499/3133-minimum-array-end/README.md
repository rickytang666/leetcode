# 3133. Minimum Array End

**Difficulty:** Medium

**Acceptance Rate:** 55.4%

**Tags:** `Bit Manipulation`

---

## Description

You are given two integers `n` and `x`. You have to construct an array of **positive** integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1]` is **greater than** `nums[i]`, and the result of the bitwise `AND` operation between all elements of `nums` is `x`.

Return the **minimum** possible value of `nums[n - 1]`.

**Example 1:**

**Input:** n = 3, x = 4

**Output:** 6

**Explanation:**

`nums` can be `[4,5,6]` and its last element is 6.

**Example 2:**

**Input:** n = 2, x = 7

**Output:** 15

**Explanation:**

`nums` can be `[7,15]` and its last element is 15.

**Constraints:**

* `1 <= n, x <= 108`

---

## Hints

<details>
<summary>Hint 1</summary>

Each element of the array should be obtained by “merging” <code>x</code> and <code>v</code> where <code>v = 0, 1, 2, …(n - 1)</code>.
</details>

<details>
<summary>Hint 2</summary>

To merge <code>x</code> with another number <code>v</code>, keep the set bits of <code>x</code> untouched, for all the other bits, fill the set bits of <code>v</code> from right to left in order one by one.
</details>

<details>
<summary>Hint 3</summary>

So the final answer is the “merge” of <code>x</code> and <code>n - 1</code>.
</details>

