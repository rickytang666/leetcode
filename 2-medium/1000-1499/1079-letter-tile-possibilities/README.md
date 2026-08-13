# 1079. Letter Tile Possibilities

**Difficulty:** Medium

**Tags:** `hash-table`, `string`, `backtracking`, `counting`

---

## Description

You have `n` `tiles`, where each tile has one letter `tiles[i]` printed on it.

Return _the number of possible non-empty sequences of letters_ you can make using the letters printed on those `tiles`.

**Example 1:**

```
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
```

**Example 2:**

```
Input: tiles = "AAABBC"
Output: 188
```

**Example 3:**

```
Input: tiles = "V"
Output: 1
```

**Constraints:**

- `1 <= tiles.length <= 7`
- `tiles` consists of uppercase English letters.

---

## Hints

<details>
<summary>Hint 1</summary>

Try to build the string with a backtracking DFS by considering what you can put in every position.
</details>
