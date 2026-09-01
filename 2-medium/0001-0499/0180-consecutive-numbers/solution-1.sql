-- Schema
Create table If Not Exists Logs (id int, num int);
Truncate table Logs;
insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('2', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');

-- Write your PostgreSQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num) OVER (ORDER BY id) AS prev_num,
        LEAD(num) OVER (ORDER BY id) AS next_num
    FROM Logs
) t
WHERE num = prev_num AND num = next_num;