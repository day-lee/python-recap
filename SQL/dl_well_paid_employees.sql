-- https://datalemur.com/questions/sql-well-paid-employees
-- leetcode 181 동일

-- 이너 조인이 바른 접근인걸 알면서도 성능상 early filtering 한 뒤에 조인해야지 라고 생각함
-- 문제는 대부분 조직은 매니저-매니저의 매니저-.. 이런식으로 다단계 구조임 따라서 manager_id is null로 필터링을하면 상위 포식자 매니저들만 남게됨. 
-- 따라서 그냥 모두 이너 조인한 뒤에 조건주는게 나음 

-- Early Filtering 이 유용한 경우 
-- 대규모 데이터셋에서 회원별 총 주문 금액 구하는 경우 그룹바이로 집계 후 조인이 필요함 
-- 조건이 복잡할 때, LIKE'%단어%', DATE_FORMAT(date, '%Y') = '2026' 함수 등 
-- JSON, LONGTEXT가 포함되어있다면
-- 실시간 로그, Time-series 대용량 테이블일 떄, 최근 1시간만 뽑아서 메칭. 
-- WITH base as (select ... where created_at > NOW() - INTERVAL 1 HOUR)


select emp.employee_id as employee_id, emp.name as employee_name
from employee mgr inner join employee as emp on mgr.employee_id = emp.manager_id 
where emp.salary > mgr.salary