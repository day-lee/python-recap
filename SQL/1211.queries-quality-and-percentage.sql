https://leetcode.com/problems/queries-quality-and-percentage

그룹바이 
- sum(조건식)은 0 or 1 값으로 치환된다. 
- sum() / count() 는 결국 avg() 로 바꿀 수 있다. 

select 
query_name,
round((sum(rating / position) / count(*)), 2) as quality,
round((sum(rating < 3) / count(*) * 100), 2) as  
poor_query_percentage
-- ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
from queries 
group by query_name 