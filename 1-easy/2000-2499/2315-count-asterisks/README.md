# 2315. Count Asterisks

**Difficulty:** Easy

**Tags:** `string`

---

## Description

You are given a string `s`, where every **two** consecutive vertical bars `'|'` are grouped into a **pair**. In other words, the 1^st and 2^nd `'|'` make a pair, the 3^rd and 4^th `'|'` make a pair, and so forth.

Return _the number of_ `'*'` _in_ `s`_, **excluding** the_ `'*'` _between each pair of_ `'|'`.

**Note** that each `'|'` will belong to **exactly** one pair.

**Example 1:**

```
Input: s = "l|*e*et|c**o|*de|"
Output: 2
Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
The characters between the first and second '|' are excluded from the answer.
Also, the characters between the third and fourth '|' are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.
```

**Example 2:**

```
Input: s = "iamprogrammer"
Output: 0
Explanation: In this example, there are no asterisks in s. Therefore, we return 0.
```

**Example 3:**

```
Input: s = "yo|uar|e**|b|e***au|tifu|l"
Output: 5
Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". There are 5 asterisks considered. Therefore, we return 5.
```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters, vertical bars `'|'`, and asterisks `'*'`.
- `s` contains an **even** number of vertical bars `'|'`.

---

## Hints

<details>
<summary>Hint 1</summary>

Iterate through each character, while maintaining whether we are currently between a pair of ‘|’ or not.
</details>

<details>
<summary>Hint 2</summary>

If we are not in between a pair of ‘|’ and there is a ‘\*’, increment the answer by 1.
</details>
