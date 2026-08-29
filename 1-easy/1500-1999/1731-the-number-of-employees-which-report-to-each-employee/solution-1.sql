-- Schema
Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int);
Truncate table Employees;
insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', NULL, '43');
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41');
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36');
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', NULL, '37');

-- Write your PostgreSQL query statement below
SELECT
    e1.employee_id,
    e1.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
JOIN Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
ORDER BY e1.employee_id;