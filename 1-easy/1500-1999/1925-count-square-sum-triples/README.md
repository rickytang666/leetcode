# 1925. Count Square Sum Triples

**Difficulty:** Easy

**Tags:** `math`, `enumeration`

---

## Description

A **square triple** `(a,b,c)` is a triple where `a`, `b`, and `c` are **integers** and `a^2 + b^2 = c^2`.

Given an integer `n`, return _the number of **square triples** such that_ `1 <= a, b, c <= n`.

**Example 1:**

```
Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
```

**Example 2:**

```
Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
```

**Constraints:**

* `1 <= n <= 250`

---

## Hints

<details>
<summary>Hint 1</summary>

Iterate over all possible pairs (a,b) and check that the square root of a \* a + b \* b is an integers less than or equal n
</details>

<details>
<summary>Hint 2</summary>

You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt
</details>
