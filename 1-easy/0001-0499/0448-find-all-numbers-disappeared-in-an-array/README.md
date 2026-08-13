# 448. Find All Numbers Disappeared in an Array

**Difficulty:** Easy

**Tags:** `array`, `hash-table`

---

## Description

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return _an array of all the integers in the range_ `[1, n]` _that do not appear in_ `nums`.

**Example 1:**

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

**Example 2:**

```
Input: nums = [1,1]
Output: [2]
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 10^5`
* `1 <= nums[i] <= n`

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

---

## Hints

<details>
<summary>Hint 1</summary>

This is a really easy problem if you decide to use additional memory. For those trying to write an initial solution using additional memory, think **counters!**
</details>

<details>
<summary>Hint 2</summary>

However, the trick really is to not use any additional space than what is already available to use. Sometimes, multiple passes over the input array help find the solution. However, there's an interesting piece of information in this problem that makes it easy to re-use the input array itself for the solution.
</details>

<details>
<summary>Hint 3</summary>

The problem specifies that the numbers in the array will be in the range [1, n] where n is the number of elements in the array. Can we use this information and modify the array in-place somehow to find what we need?
</details>
