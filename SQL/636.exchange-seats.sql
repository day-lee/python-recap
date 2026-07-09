https://leetcode.com/problems/exchange-seats

- CASE 문을 이용해서 컬럼의 정보를 바꿔 줄 수 있다. 
- 여기서는 홀수이면서 마지막 index의 경우가 예외이므로 max() 서브쿼리로 핸들링해줬다. 

select
(case 
when id % 2 = 1 and id != (select max(id) from seat) then id + 1
-- when id % 2 = 1 and  id = (select max(id) from seat) then id 
when id % 2 = 1 then id  -- 마지막 숫자이면서 홀수인 경우는 위에서 다뤘으니 여기선 홀수인 것만 체크
else id - 1 
end) as id, student
from seat 
order by id




-- 
같은 유형의 다른 문제 
https://datalemur.com/questions/sql-swapped-food-delivery

- postgresql은 IFNULL()이 없다. mysql에만 있음 
- COALESCE()가 표준 함수 
- 대용량 데이터에서 left join은 성능에 치명적일 수 있다. 

- with + cross join 방식이 성능이 훨씬 좋음 
- a Cartesian join (or CROSS JOIN) between the orders table and the order_counts CTE.
- CTE에서 구한 15가 total_orders 칼럼으로 모든 로우에 추가됨 
- 보통 크로스 조인은 N * M으로 왼쪽 모든 행과 오른쪽 모든 행을 조합해서 기하급수적으로 늘어나게되지만
- 이 경우에는 CTE가 스칼라 단일 값이라 1 * N 으로 테이블 숫자가 늘어나지 않는다. 

-- 전체 개수를 계산함 
with order_counts as (
    select count(order_id) as total_orders
    from orders
)

-- case 문을 이용해서 모듈러로 홀짝수 파악하고, 마지막 id 여부 판단함 
select 
    case
        when order_id % 2 != 0 and order_id != total_orders then order_id + 1 -- 홀수이고 마지막id아님 
        when order_id % 2 != 0 and order_id = total_orders then order_id -- 홀수인데 마지막 id 
        else order_id - 1 -- 짝수 
    end as corrected_order_id, 
    item 
from orders
cross join order_counts
order by corrected_order_id asc