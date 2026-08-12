# 570. Managers with at Least 5 Direct Reports

**Difficulty:** Medium

**Acceptance Rate:** 49.4%

**Tags:** `Database`

---

## Description

Table: `Employee`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
```

Write a solution to find managers with at least **five direct reports**.

Return the result table in **any order**.

The result format is in the following example.

**Example 1:**

```
Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
```

---

## Hints

<details>
<summary>Hint 1</summary>

Try to get all the mangerIDs that have count bigger than 5
</details>

<details>
<summary>Hint 2</summary>

Use the last hint's result as a table and do join with origin table at id equals to managerId
</details>

<details>
<summary>Hint 3</summary>

This is a very good example to show the performance of SQL code. Try to work out other solutions and you may be surprised by running time difference.
</details>

<details>
<summary>Hint 4</summary>

If your solution uses 'IN' function and runs more than 5 seconds, try to optimize it by using 'JOIN' instead.
</details>

