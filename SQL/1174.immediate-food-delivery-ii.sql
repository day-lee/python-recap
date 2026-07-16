1174. Immediate Food Delivery II
https://leetcode.com/problems/immediate-food-delivery-ii

- WHERE IN 패턴: where (col1, col2) in (subquery, 리스트)  
- 체크리스트에 이름이 있는지 검사하는 필터링 기계 
- 그룹별 최대값, 최소값 데이터 1건을 남긴다. e.g. WHERE (고객, 주문일) IN (고객별 최소 주문일 목록)
- 존재 여부 체크: e.g. WHERE 회원ID IN (2026년 구매 회원ID 목록)
- not in 은 리스트에 없는 것만 골라라. e.g. 아직 오더 안한 오더리스트에 없는 회원만 조회하기

- 첫 주문만 뽑아내는 서브 쿼리를 만든다. 
- 더 덧붙일 테이블이 없으므로 필터링을 위해 where in 서브쿼리 구조를 사용한다. 
- 조인은 새롭게 덧붙일 필드가 있지 않은 이상 지양해야함. - 너무 복잡해짐.


Select 
-- 조건부 집계로 바로 avg()를 구함
    round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
-- where in 패턴으로 고객별 최소 주문일만 남긴다.
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);
