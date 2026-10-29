# 575. Distribute Candies

**Difficulty:** Easy

**Tags:** `array`, `hash-table`

---

## Description

Alice has `n` candies, where the `i^th` candy is of type `candyType[i]`. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat `n / 2` of the candies she has (`n` is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array `candyType` of length `n`, return _the **maximum** number of different types of candies she can eat if she only eats_ `n / 2` _of them_.

**Example 1:**

```
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
```

**Example 2:**

```
Input: candyType = [1,1,2,3]
Output: 2
Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
```

**Example 3:**

```
Input: candyType = [6,6,6,6]
Output: 1
Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
```

**Constraints:**

- `n == candyType.length`
- `2 <= n <= 10^4`
- `n` is even.
- `-10^5 <= candyType[i] <= 10^5`

---

## Hints

<details>
<summary>Hint 1</summary>

To maximize the number of kinds of candies, we should try to distribute candies such that Alice will gain all kinds.
</details>

<details>
<summary>Hint 2</summary>

What is the upper limit of the number of kinds of candies Alice will gain? Remember candies are to distributed equally.
</details>

<details>
<summary>Hint 3</summary>

Which data structure is the most suitable for finding the number of kinds of candies?
</details>

<details>
<summary>Hint 4</summary>

Will hashset solves the problem? Inserting all candies kind in the hashset and then checking its size with upper limit.
</details>
