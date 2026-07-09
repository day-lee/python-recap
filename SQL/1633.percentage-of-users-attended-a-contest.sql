https://leetcode.com/problems/percentage-of-users-attended-a-contest


- aggregation 조합을 한번에 쓰면 괄호 하나씩 빠트리기 쉽다. 
- 일단 한개씩 구하고 조립을 하자. 
- 혹시 avg()로 한번에 구할 수도 있는지 고려는 해보자.

- ORDER BY는 SELECT보다 늦게 실행되는 유일한 절이다. 
따라서 SELECT 절에서 새로 창조한 **계산식의 별명(Alias)**을 마음껏 가져다 쓸 수 있다!


select contest_id, 
round(((count(user_id) / (select count(distinct user_id) from users) ) * 100), 2) as percentage
from register 
group by contest_id
order by percentage desc, contest_id asc