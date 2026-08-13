# 1871. Jump Game VII

**Difficulty:** Medium

**Tags:** `string`, `dynamic-programming`, `sliding-window`, `prefix-sum`

---

## Description

You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

- `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and
- `s[j] == '0'`.

Return `true` _if you can reach index_ `s.length - 1` _in_ `s`_, or_ `false` _otherwise._

**Example 1:**

```
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3.
In the second step, move from index 3 to index 5.
```

**Example 2:**

```
Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
```

**Constraints:**

- `2 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `s[0] == '0'`
- `1 <= minJump <= maxJump < s.length`

---

## Hints

<details>
<summary>Hint 1</summary>

Consider for each reachable index i the interval [i + a, i + b].
</details>

<details>
<summary>Hint 2</summary>

Use partial sums to mark the intervals as reachable.
</details>
