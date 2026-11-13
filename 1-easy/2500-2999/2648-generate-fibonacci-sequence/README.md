# 2648. Generate Fibonacci Sequence

**Difficulty:** Easy

---

## Description

Write a generator function that returns a generator object which yields the **fibonacci sequence**.

The **fibonacci sequence** is defined by the relation `X_n = X_n-1 + X_n-2`.

The first few numbers of the series are `0, 1, 1, 2, 3, 5, 8, 13`.

**Example 1:**

```
Input: callCount = 5
Output: [0,1,1,2,3]
Explanation:
const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3
```

**Example 2:**

```
Input: callCount = 0
Output: []
Explanation: gen.next() is never called so nothing is outputted
```

**Constraints:**

- `0 <= callCount <= 50`

---

## Hints

<details>
<summary>Hint 1</summary>

Javascript has the concept of generators. They are critical to this problem.
</details>

<details>
<summary>Hint 2</summary>

First yield 0 and 1.
</details>

<details>
<summary>Hint 3</summary>

Create an infinite "while(true)" loop.
</details>

<details>
<summary>Hint 4</summary>

In that loop, continuously yield the next value which is the sum of the previous two.
</details>
