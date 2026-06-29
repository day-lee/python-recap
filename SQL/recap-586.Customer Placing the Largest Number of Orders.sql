최대 주문 횟수를 가지는 고객을 찾는 쿼리 

--1 
-- 간단하지만 동률이 있을 경우 값의 정확성이 보장되지 않음. 
-- order by에 두번째 기준을 세워줘야함. 
select customer_number
from orders 
group by customer_number 
order by count(customer_number) desc limit 1

-- 2
-- 서브쿼리가 중첩되면서 가독성이 떨어짐 
-- 동률의 결과를 모두 출력하면서 정확성은 보장됨 
-- 카운트로 집계한 결과를 가지고, 다시 max를 구하려면 중첩될 수 밖에 없다. -> 극복하려고 윈도우 함수가 나왔다. 
select customer_number
from orders 
group by customer_number
having count(customer_number) = 
(select max(sub.c) from ( select count(customer_number) as c from orders group by customer_number ) as sub)

-- 3 
-- 윈도우 함수로 정확성과 가독성을 챙길 수 있음 
-- 윈도우 함수를 사용한 대안 (동률 처리 가능, 서브쿼리 1번)
select customer_number
from (
    select customer_number,
           dense_rank() over (order by count(customer_number) desc) as rnk
    from orders
    group by customer_number
) sub
where rnk = 1