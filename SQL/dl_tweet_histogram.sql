https://datalemur.com/questions/sql-histogram-tweets

- 날짜 추출시 
- LEFT(col, 4), RIGHT(col, 4)
- YEAR(col), MONTH(col), DAY(col)
 

with base as (
SELECT  
user_id, count(user_id) as cnt, left(tweet_date, 4) as year
from tweets
where left(tweet_date, 4) = '2022'
group by user_id)

-- select * from base

select
count(cnt) as tweet_bucket,
cnt as users_num 
from base
group by cnt 
order by tweet_bucket asc