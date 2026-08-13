# 678. Valid Parenthesis String

**Difficulty:** Medium

**Tags:** `string`, `dynamic-programming`, `stack`, `greedy`

---

## Description

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` _if_ `s` _is **valid**_.

The following rules define a **valid** string:

* Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
* Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
* Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
* `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "(*)"
Output: true
```

**Example 3:**

```
Input: s = "(*))"
Output: true
```

**Constraints:**

* `1 <= s.length <= 100`
* `s[i]` is `'('`, `')'` or `'*'`.

---

## Hints

<details>
<summary>Hint 1</summary>

Use backtracking to explore all possible combinations of treating '\*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
</details>

<details>
<summary>Hint 2</summary>

DP[i][j] represents whether the substring s[i:j] is valid.
</details>

<details>
<summary>Hint 3</summary>

Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
</details>

<details>
<summary>Hint 4</summary>

How about using 2 stacks instead of 1? Think about it.
</details>
