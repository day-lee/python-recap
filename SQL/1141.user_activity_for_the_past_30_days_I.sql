https://leetcode.com/problems/user-activity-for-the-past-30-days-i 

- WHERE date_col BETWEEN '2019-07-27' AND '2019-07-30' 
- mysql: DATE_SUB(date_col, INTERVAL N DAY) 
- postgresql: date_col BETWEEN (date '2019-07-27' - INTERVAL '29 day') and DATE '2019-07-27'

- INTERVAL = (N-1) DAY -> 오늘 포함 총 N일 기간 구하기 
    전체 7일: INTERVAL 6 DAY -> 과거 6일 + 오늘 1일 

    1일전이면 어제, 오늘 이니까, 2일 기간: 어제(-1) between 오늘 
.. 30일 기간: -29 btw 오늘 

-- postgresql
select 
activity_date as day,
count(distinct user_id) as active_users
from activity 
where activity_date > '2019-07-27'::date - interval '30 days' and activity_date <= '2019-07-27'::date
group by activity_date
-- mysql
select 
activity_date as day, count(distinct user_id) as active_users
from activity 
where activity_date between (date '2019-07-27' - interval '29 days') and date '2019-07-27' 
group by activity_date


-- ===========================================================================================
-- mysql 
-- datediff(date1, date2) < 30 
SELECT
activity_date as day,
COUNT(DISTINCT user_id) as active_users  
FROM Activity
where 
datediff('2019-07-27', activity_date) < 30 and activity_date <= '2019-07-27'
GROUP BY activity_date


-- ===========================================================================================
-- mysql 
-- date_sub(date_col, interval N day)
-- inclusive라서 interval 30 day 아니고 29 day 임 
-- 2일이면 1 day, 30일이면 29 day

select activity_date as day, count(distinct user_id) as active_users
from activity
where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
group by activity_date