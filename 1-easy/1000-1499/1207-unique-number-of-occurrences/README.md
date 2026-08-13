# 1207. Unique Number of Occurrences

**Difficulty:** Easy

**Tags:** `array`, `hash-table`

---

## Description

Given an array of integers `arr`, return `true` _if the number of occurrences of each value in the array is **unique** or_ `false` _otherwise_.

**Example 1:**

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

**Example 2:**

```
Input: arr = [1,2]
Output: false
```

**Example 3:**

```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

**Constraints:**

* `1 <= arr.length <= 1000`
* `-1000 <= arr[i] <= 1000`

---

## Hints

<details>
<summary>Hint 1</summary>

Find the number of occurrences of each element in the array using a hash map.
</details>

<details>
<summary>Hint 2</summary>

Iterate through the hash map and check if there is a repeated value.
</details>
