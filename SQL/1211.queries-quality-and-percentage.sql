https://leetcode.com/problems/queries-quality-and-percentage

그룹바이 
- sum(조건식)은 0 or 1 값으로 치환된다. 
- sum() / count() 는 결국 avg() 로 바꿀 수 있다. 
- CASE WHEN THEN ELSE END 가 표준 SQL이다. postgresql에서는 ::int로 타입을 지정해줘야한다. 


SELECT 
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100, 2) AS poor_query_percentage
FROM 
    queries
GROUP BY 
    query_name;


--
select 
query_name,
round((sum(rating / position) / count(*)), 2) as quality,
round((sum(rating < 3) / count(*) * 100), 2) as  
poor_query_percentage
-- ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
from queries 
group by query_name 