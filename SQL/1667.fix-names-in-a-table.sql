https://leetcode.com/problems/fix-names-in-a-table

- sql 인덱스는 1부터 시작한다!!!
- LENGTH() 는 문자열 길이 돌려준다. 
- LEFT(col, 1): 문자 왼쪽에서부터 1개만 
- RIGHT(col, 1): 문자 오른쪽에서부터 1개만. 여기선 동적으로 숫자가 필요하니까 전체 length 길이 구해두고 -1 해서 대응함  
- UPPER() 대문자
- LOWER() 소문자
- 문자열 합치기 concat(a, b)

select 
user_id, 
CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, LENGTH(name) -1 ))) as name
from users
order by user_id