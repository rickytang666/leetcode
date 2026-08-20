-- Schema
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');

-- Write your PostgreSQL query statement below
SELECT
    ROUND(COUNT(*) FILTER (WHERE has_next_day)::numeric / COUNT(*), 2) AS fraction
FROM (
    SELECT DISTINCT ON (player_id)
        player_id,
        EXISTS (
            SELECT 1
            FROM Activity a2
            WHERE a2.player_id = a1.player_id AND a2.event_date = a1.event_date + 1
        ) AS has_next_day
    FROM Activity a1
    ORDER BY player_id, event_date
)