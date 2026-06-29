-- 이름이 'M' 으로 시작하지 않음은 not like 연산자와 문자열 뒤 'M%'을 사용해서 %와일드 카드 검색을 사용한다. 

select employee_id, 
(case when employee_id % 2 != 0 and name not like 'M%' then salary else 0 end)
 as bonus
from employees 
order by employee_id