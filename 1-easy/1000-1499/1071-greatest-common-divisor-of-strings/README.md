# 1071. Greatest Common Divisor of Strings

**Difficulty:** Easy

**Tags:** `math`, `string`

---

## Description

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return _the largest string_ `x` _such that_ `x` _divides both_ `str1` _and_ `str2`.

**Example 1:**

**Input:** str1 = "ABCABC", str2 = "ABC"

**Output:** "ABC"

**Example 2:**

**Input:** str1 = "ABABAB", str2 = "ABAB"

**Output:** "AB"

**Example 3:**

**Input:** str1 = "LEET", str2 = "CODE"

**Output:** ""

**Example 4:**

**Input:** str1 = "AAAAAB", str2 = "AAA"

**Output:** ""

**Constraints:**

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of English uppercase letters.

---

## Hints

<details>
<summary>Hint 1</summary>

The greatest common divisor must be a prefix of each string, so we can try all prefixes.
</details>
