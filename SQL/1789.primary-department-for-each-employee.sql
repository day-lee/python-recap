https://leetcode.com/problems/primary-department-for-each-employee/

- 아이디어는 맞았는데 조합을 잘못했다. 80점

1. 서브쿼리 
- Y는 그대로 출력하고 그룹바이 해서 카운트1 인 애들에 속하면 IN 출력 
- 실무에서는 성능저하 우려. OR + IN 조합이 인덱스를 타지 못하고 full table scan을 할 확률이 높다. 

select employee_id, department_id
from employee
where primary_flag = 'Y' or 
employee_id in (select employee_id from employee group by employee_id having count(employee_id) = 1)

---
2. 유니온
- N 이면서 카운트1만 걸러서 + Y만 걸러서, 교집합 없으니 union all 괜찮음  
- 실무에서 안정적, 스캔은 두번하게됨 

select employee_id, department_id
from employee
group by employee_id 
having count(department_id) = 1

union all
select employee_id, department_id
from employee
where primary_flag = 'Y'

---
3. 윈도우 펑션 
- row_number 지정 후 Y의 경우 1을 부여함. N은 한개밖에 없으니 1, rn 1만 필터링 
- 가장 추천하는 방식 테이블 한번 스캔

with total_cnt as (
select employee_id, department_id, primary_flag,
-- 안전장치 해당 직원의 전체 부서 개수를 같이 구해둠
COUNT(*) OVER(PARTITION BY employee_id) as dept_cnt
from employee)

select employee_id, department_id from total_cnt where dept_cnt = 1 or primary_flag = 'Y';