https://leetcode.com/problems/sales-person/

- 한 번도 ~를 하지 않은 조건 
- ~를 한번이라도 한 사람을 먼저 구하고, 그 사람들을 전체 명단에서 제외 
- 전체 집합에서 - 부분 집합(red와 거래한 사원) = 여집합 (전체에서 나를 제외한 나머지 전부 - Complement)

-- not in 
- 이름말고 sales_id로 구분해야함. 

SELECT name 
FROM salesperson 
WHERE sales_id NOT IN (
    -- 굳이 salesperson을 조인하지 않고, 거래 기록에서 바로 RED의 sales_id를 추출 (성능 최적화)
    -- 한 번 이라도 RED와 거래한 sales_id를 추출
    SELECT o.sales_id
    FROM orders o 
    JOIN company c ON o.com_id = c.com_id -- using(com_id)
    WHERE c.name = 'RED'
);


-- not exists 
- 상관 서브쿼리: 서브쿼리 내부에서 메인 쿼리 테이블 salesperson s를 참조함 
- 조건 만족하는 데이터 찾는 즉시 스캔 early exit 중단을 하므로 성능 좋다. 
select s.name
from salesperson s 
where not exists(
select 1 
from orders o
join company c using(com_id)
where o.sales_id = s.sales_id and c.name = 'RED')
-- sales_id가 같고 회사 이름이 red인 집합에 존재하지 않아야 참이되면서 결과값에 포함됨 
-- 데이터가 존재한다면 1을 반환하여 false 가 되고, 아무 기록이 없으면 아무것도 반환하지 않아 조건이 true가 되어 최종 출력됨. 



-- group by, having sum(case when )으로 조건에 맞는 개수 세서 0인 사람만 필터링  
select sp.name
from salesperson sp left join orders o on sp.sales_id = o.sales_id 
left join company c on o.com_id = c.com_id
group by sp.sales_id, sp.name
having sum(case when c.name = 'RED' then 1 else 0 end)  = 0