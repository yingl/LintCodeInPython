-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --

select
(
    if(
        (select count(*) from (select distinct height from players) p) >= 2,
        (select distinct height from players order by height desc limit 1 offset 1),
        NULL
    )
) second_height

-- https://www.lintcode.com/problem/the-height-of-the-second-tallest-player/
