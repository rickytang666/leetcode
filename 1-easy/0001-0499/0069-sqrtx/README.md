# 69. Sqrt(x)

**Difficulty:** Easy

**Tags:** `math`, `binary-search`

---

## Description

Given a non-negative integer `x`, return _the square root of_ `x` _rounded down to the nearest integer_. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

**Example 1:**

```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

**Example 2:**

```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

**Constraints:**

- `0 <= x <= 2^31 - 1`

---

## Hints

<details>
<summary>Hint 1</summary>

Try exploring all integers. (Credits: @annujoshi)
</details>

<details>
<summary>Hint 2</summary>

Use the sorted property of integers to reduced the search space. (Credits: @annujoshi)
</details>
