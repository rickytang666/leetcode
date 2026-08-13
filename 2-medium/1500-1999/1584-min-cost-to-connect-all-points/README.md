# 1584. Min Cost to Connect All Points

**Difficulty:** Medium

**Tags:** `array`, `union-find`, `graph`, `minimum-spanning-tree`

---

## Description

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x_i, y_i]`.

The cost of connecting two points `[x_i, y_i]` and `[x_j, y_j]` is the **manhattan distance** between them: `|x_i - x_j| + |y_i - y_j|`, where `|val|` denotes the absolute value of `val`.

Return _the minimum cost to make all points connected._ All points are connected if there is **exactly one** simple path between any two points.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Constraints:**

- `1 <= points.length <= 1000`
- `-10^6 <= x_i, y_i <= 10^6`
- All pairs `(x_i, y_i)` are distinct.

---

## Hints

<details>
<summary>Hint 1</summary>

Connect each pair of points with a weighted edge, the weight being the manhattan distance between those points.
</details>

<details>
<summary>Hint 2</summary>

The problem is now the cost of minimum spanning tree in graph with above edges.
</details>
