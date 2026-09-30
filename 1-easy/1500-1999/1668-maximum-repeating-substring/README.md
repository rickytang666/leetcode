# 1668. Maximum Repeating Substring

**Difficulty:** Easy

**Tags:** `string`, `dynamic-programming`, `string-matching`

---

## Description

For a string `sequence`, a string `word` is **`k`\-repeating** if `word` concatenated `k` times is a substring of `sequence`. The `word`'s **maximum `k`\-repeating value** is the highest value `k` where `word` is `k`\-repeating in `sequence`. If `word` is not a substring of `sequence`, `word`'s maximum `k`\-repeating value is `0`.

Given strings `sequence` and `word`, return _the **maximum `k`\-repeating value** of `word` in `sequence`_.

**Example 1:**

```
Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
```

**Example 2:**

```
Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
```

**Example 3:**

```
Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".
```

**Constraints:**

- `1 <= sequence.length <= 100`
- `1 <= word.length <= 100`
- `sequence` and `word` contains only lowercase English letters.

---

## Hints

<details>
<summary>Hint 1</summary>

The constraints are low enough for a brute force approach.
</details>

<details>
<summary>Hint 2</summary>

Try every k value from 0 upwards until word is no longer k-repeating.
</details>
