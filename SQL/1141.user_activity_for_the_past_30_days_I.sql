https://leetcode.com/problems/user-activity-for-the-past-30-days-i 
- where date_field between '2019-07-27' and '2019-07-30' 

--  postgresql 버젼 날짜 포매팅 
-- date between a and b 

select 
activity_date as day,
count(distinct user_id) as active_users
from activity 
where activity_date > '2019-07-27'::date - interval '30 days' and activity_date <= '2019-07-27'::date
group by activity_date
--
select 
activity_date as day, count(distinct user_id) as active_users
from activity 
where activity_date between (date '2019-07-27' - interval '29 days') and date '2019-07-27' 
group by activity_date

-- mysql 
-- datediff(date1, date2) < 30 
SELECT
activity_date as day,
COUNT(DISTINCT user_id) as active_users  
FROM Activity
where 
datediff('2019-07-27', activity_date) < 30
and
activity_date <= '2019-07-27'
GROUP BY activity_date