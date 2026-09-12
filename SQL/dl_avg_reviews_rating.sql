https://datalemur.com/questions/sql-avg-review-ratings
-- postgreSQL 14
-- 년월일 추출할 때 extract(year from submit_date) 처럼 쓴다. 

-- CTE
with base as (SELECT extract(month from submit_date) as mth, product_id, stars FROM reviews)
select mth, product_id, round(avg(stars), 2) as avg_stars from base group by mth, product_id order by mth, product_id


-- quick version
-- group by 에서 extract(month from submit_date)를 바로 썼음 
select extract(month from submit_date) as mth, product_id, round(avg(stars), 2) as avg_stars 
from reviews group by extract(month from submit_date), product_id order by mth, product_id
