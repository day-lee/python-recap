https://leetcode.com/problems/product-price-at-a-given-date/

> 핵심 키워드: 독립 집합 분리, NOT EXISTS(셔틀구조), LEFT JOIN + COALESCE

- 16일 이후는 가격 고정이라 그룹바이하고 해빙 절에서 최소 값(처음 나타난 값)이 기준일 보다 큰 경우만 찾아줌

### 방법 1: UNION ALL 방식 (독립적인 두 조건 합치기)
* [A 그룹] 16일 이전 기록 존재 => 16일 이하 중 그룹바이에서 '최대 날짜(최신값)' 찾기 (`WHERE (id, date) IN` 구조)
* [B 그룹] 16일 이전 기록 전무 => 가격 10원 고정 (`HAVING MIN` 또는 `NOT EXISTS` 사용)

#### 치트키: NOT EXISTS 문법의 본질 (Correlated 상관 쿼리)
* 파이썬의 `if not (False) == True` 방식과 동일!
* 셔틀 구조: 바깥 테이블(p1)이 안쪽(p2)한테 "내 아이디 줄 테니까 검사해봐" 하고 조건 전달.
* 빈손(못 찾아야) 통과: 안쪽 서브쿼리가 '빈손(False)'으로 돌아와야 최종 합격시켜서 10원 낙찰

1번 union all 방식 

-- 1. 지정일 이전 기록이 있는 제품들의 최신 가격 구하기
SELECT product_id, new_price AS price
FROM Products
WHERE (product_id, change_date) IN (
    SELECT product_id, MAX(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
UNION ALL
-- 2. 지정일 이전 기록이 아예 없는 제품들은 가격을 10으로 고정하기
SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';

-- 추가 2. NOT EXISTS를 사용해 "2019-08-16 이하의 기록이 '존재하지 않는' 제품"만 뽑기, if not (false): 기록없네 
-- correlated 상관 쿼리. 바깥과 안쪽 서브쿼리가 연결되어 있어서 
-- 바깥이 안쪽에게 "야, 내 아이디 줄 테니까 이거로 안에서 검사 좀 해봐"하는 셔틀구조. not exists는 빈손이어야 통과시켜줌. (못찾아야)
SELECT DISTINCT p1.product_id, 10 AS price
FROM Products p1
WHERE NOT EXISTS (
    SELECT 1 
    FROM Products p2 
    WHERE p1.product_id = p2.product_id 
      AND p2.change_date <= '2019-08-16'
);

---------------------------------------------------------------

2번. window function() 

### 방법 2: WINDOW FUNCTION 방식 (판 짜서 덧붙이기)
* 1 CTE 안에서 16일 이하 데이터만 `ROW_NUMBER() ... DESC`로 1등 뽑아두기.
* 2 원본 테이블에서 `DISTINCT product_id`로 모든 아이디 베이스 깔아두기.
* 3 `LEFT JOIN`으로 1등 데이터만 매칭하고, 기록이 없어 사라진 녀석들은 null처리하는 함수 사용 `COALESCE(price, 10)` 

WITH RankedPrices AS (
    SELECT product_id, new_price, change_date,
           ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
-- 모든 제품 목록을 가져오기 위해 원본에서 product_id만 DISTINCT로 추출 후 LEFT JOIN
SELECT DISTINCT p.product_id, 
       COALESCE(rp.new_price, 10) AS price
FROM Products p
LEFT JOIN RankedPrices rp 
       ON p.product_id = rp.product_id AND rp.rn = 1;






---------------------------------------------------------------
-- 어찌어찌 구하긴 했는데 성능 최적화가 필요함

with max_date as (select product_id, max(change_date) as change_date
from products where change_date <= '2019-08-16'
group by product_id),

new_products as (select p.product_id, p.change_date, p.new_price from max_date md join products p
on p.change_date = md.change_date and p.product_id = md.product_id) 

select distinct dp.product_id, coalesce(np.new_price, 10) as price from products dp
left join new_products np on np.product_id = dp.product_id
