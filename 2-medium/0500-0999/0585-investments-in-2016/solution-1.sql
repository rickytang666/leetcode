-- Schema
Create Table If Not Exists Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float);
Truncate table Insurance;
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('1', '10', '5', '10', '10');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('2', '20', '20', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('3', '10', '30', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('4', '10', '40', '40', '40');

-- Write your PostgreSQL query statement below
SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016
FROM (
    SELECT
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv_peers,
        COUNT(*) OVER (PARTITION BY lat, lon) AS city_peers
    FROM Insurance
) t
WHERE tiv_peers >= 2 AND city_peers = 1;