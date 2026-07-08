https://leetcode.com/problems/primary-department-for-each-employee/

집합적 사고(Set-oriented Thinking)
"부서 수가 1개인 직원 집합"과 "부서 수가 여러 개이면서 대표 부서인 직원 집합"의 합집합 구하기 

- 아이디어는 맞았는데 조합을 잘못했다. 80점
- 윈도우 함수로 해당 직원 부서 개수를 구해두고, count(department_id) over(partition by employee_id) 이 CTE에서 카운트가 1이거나 flag가 y인 직원만 골라서 필터링해준다. 
- union 로 카운트가 1인 직원 + flag가 Y인 직원을 묶어줄 수도 있다. union 을 쓰면 중복을 줄일 수 있다. 
- 두 그룹은 독립적인 조건을 가지고 있어서 union 으로 집합을 결합  

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
- UNION 기본값이 UNION DISTINCT임 UNION ALL과 비교했을 때 중복 검사를 하느라 성능이 조금 느릴 수 있음 
- 두개가 완전한 독립 집합이므로 distinct를 건너 뛰면 성능 최적화 가능 
- 대신 primary_flag = 'N'을 확실하게 표시해서 안정화. 여기서 MAX(primary_flag) = 'N'를 쓴 이유는 having 절이기 때문.
대표 값이 필요하므로 어그리게이션 써야함. (알파벳 순서로 보면 'N'이 'Y'보다 앞섬(N < Y).)

select employee_id, department_id
from employee
group by employee_id 
HAVING COUNT(department_id) = 1 AND MAX(primary_flag) = 'N'

UNION ALL

union 
select employee_id, department_id
from employee
WHERE primary_flag = 'Y';
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