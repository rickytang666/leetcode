# 767. Reorganize String

**Difficulty:** Medium

**Tags:** `hash-table`, `string`, `greedy`, `sorting`, `heap-priority-queue`, `counting`

---

## Description

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return _any possible rearrangement of_ `s` _or return_ `""` _if not possible_.

**Example 1:**

```
Input: s = "aab"
Output: "aba"
```

**Example 2:**

```
Input: s = "aaab"
Output: ""
```

**Constraints:**

* `1 <= s.length <= 500`
* `s` consists of lowercase English letters.

---

## Hints

<details>
<summary>Hint 1</summary>

Alternate placing the most common letters.
</details>
