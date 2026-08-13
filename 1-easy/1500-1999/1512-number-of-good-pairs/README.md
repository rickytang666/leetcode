# 1512. Number of Good Pairs

**Difficulty:** Easy

**Tags:** `array`, `hash-table`, `math`, `counting`

---

## Description

Given an array of integers `nums`, return _the number of **good pairs**_.

A pair `(i, j)` is called _good_ if `nums[i] == nums[j]` and `i` < `j`.

**Example 1:**

```
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
```

**Example 2:**

```
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: 0
```

**Constraints:**

* `1 <= nums.length <= 100`
* `1 <= nums[i] <= 100`

---

## Hints

<details>
<summary>Hint 1</summary>

Count how many times each number appears. If a number appears n times, then n \* (n – 1) // 2 good pairs can be made with this number.
</details>
