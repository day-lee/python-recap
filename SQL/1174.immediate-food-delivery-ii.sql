1174. Immediate Food Delivery II
https://leetcode.com/problems/immediate-food-delivery-ii

- WHERE IN 패턴: where (col1, col2) in (subquery, 리스트)  
- 체크리스트에 이름이 있는지 검사하는 필터링 기계 
- 그룹별 최대값, 최소값 데이터 1건을 남긴다. e.g. WHERE (고객, 주문일) IN (고객별 첫 주문일 목록)
- 존재 여부 체크: e.g. WHERE 회원ID IN (2026년 구매 회원ID 목록)
- not in 은 리스트에 없는 것만 골라라. e.g. 아직 오더 안한 오더리스트에 없는 회원만 조회하기

- 첫 주문일만 뽑아내는 서브 쿼리를 만든다. 
- 더 덧붙일 테이블이 없으므로 필터링을 위해 where in 서브쿼리 구조를 사용한다. 
- 조인은 새롭게 덧붙일 필드가 있지 않은 이상 지양해야함. - 너무 복잡해짐.

- cte는 common table expression: 물리적으로 디스크에 테이블 저장하지 않고, 쿼리 가공 껍데기에 불과하다. 쿼리 실행시에만 존재했다 사라진다. 
- temporary table은 진짜 물리테이블. 데이터가 너무 많으면 중간 계산 결과를 밀어넣고 인덱스 걸어 사용함. 

- ranked cte 
-- 가장 현대적임. 전통RDB 환경보다 대용량 분산 환경(AWS Redshift, Snowflake, Google BigQuery, Spark)에서는 윈도우 함수 방식을 선호. 
--> 대용량 분산 DB(distributed env, system)는 정렬과 분산 처리에 특화되어 있다. 
-- 조인 연산 없이 한번 정렬하고 필터링으로 행 압축할 수 있음. avg(조건식)으로 연산량이 적음 
-- RDB 환경이라면 대용량 데이터에서 정렬할 때 메모리 부하가 생길 수 있음 
-- 비즈니스 요구사항 병화에 유연하게 대처가능, 두번째주 배송비율 알고 싶다면 rn = 2로 바꾸면 된다. 

-- 여기서 rank()말고 row_number()를 써야하는 이유는 공동 순위 이슈가 있을 수 있어서임. 중복 제거한 유일성을 보장해야하는 결과는 row_number()를 써야함.  
WITH ranked_delivery AS (
    SELECT *,
           ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM delivery
)
SELECT ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM ranked_delivery
WHERE rn = 1;
-- 조건식의 결과는 숫자다. type casting이 되어 참이면 1 아니면 0 
-- AVG() 는 (당일배송 성공한 주문 수) / (전체 첫 주문 수) 이것과 같아진다. 
-- 테이블을 딱 한번만 훑으면서 조건맞는 개수와 전체 합계를 구하므로 성능상 유리하다. 

- where in 패턴 
-- 전통적 RDB환경에 적합
-- 테이블 2번 스캔 
-- 대용량 데이터에는 복합 인덱스가 걸려있을 시 where in 패턴이 인덱스를 탈 수 있어 유리함 
-- 빅데이터 환경에서는 다중 열 in 문법을 지원하지 않을 수 있음 
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



나의 버려야 할 나쁜 습관 쿼리들 (성능 고려안하고 그냥 답만 나오는 쿼리들)
- cte, inner join 
-- 가상의 임시 테이블을 생성함. 
-- 테이블 3번 스캔으로 성능 낭비가 심함  
with f_date as (select customer_id, min(order_date) as f_date
from delivery 
group by customer_id) 
select round((count(*) / (select count(*) from f_date)) * 100, 2) as immediate_percentage
from delivery d join f_date f on d.customer_id = f.customer_id and
d.customer_pref_delivery_date = f.f_date and d.order_date = f.f_date
--

- cte, inner join 
-- 가상 임시 테이블 2개 생성
-- 카운트 서브쿼리가 두번 발생해서 데이터가 커질 때 연산때문에 타임아웃 될 수 있음 
with first_orders as (
    select customer_id, min(order_date) first_order
    from delivery
    group by customer_id
),
immediate_orders as (
    select fo.customer_id, d.order_date, d.customer_pref_delivery_date
    from first_orders fo join delivery d 
    on fo.customer_id = d.customer_id 
    and fo.first_order = d.order_date
)
-- 분자/분모 스칼라 서브쿼리를 나누는 방식은 데이터 커질 때 바로 터질 수 있음. 사용 금지!! 
select round((select count(*) from immediate_orders) /(select count(*) from first_orders) * 100, 2) as immediate_percentage;
--