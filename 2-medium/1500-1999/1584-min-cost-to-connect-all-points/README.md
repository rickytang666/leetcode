# 1584. Min Cost to Connect All Points

**Difficulty:** Medium

**Acceptance Rate:** 70.5%

**Tags:** `Array`, `Union-Find`, `Graph Theory`, `Minimum Spanning Tree`

---

## Description

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
![](https://assets.leetcode.com/uploads/2020/08/26/c.png)
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Constraints:**

* `1 <= points.length <= 1000`
* `-106 <= xi, yi <= 106`
* All pairs `(xi, yi)` are distinct.

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

