# 5. Longest Palindromic Substring

**Difficulty:** Medium

**Tags:** `two-pointers`, `string`, `dynamic-programming`, `manacher`

---

## Description

Given a string `s`, return _the longest_ _palindromic_ _substring_ in `s`.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consist of only digits and English letters.

---

## Hints

<details>
<summary>Hint 1</summary>

How can we reuse a previously computed palindrome to compute a larger palindrome?
</details>

<details>
<summary>Hint 2</summary>

If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
</details>

<details>
<summary>Hint 3</summary>

Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.
</details>
