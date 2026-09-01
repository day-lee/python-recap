https://leetcode.com/problems/product-price-at-a-given-date/

> 핵심 키워드: 독립 집합 분리 

- SQL 튜닝(성능 최적화)을 할 때 "서브쿼리 IN 구조는 가급적 JOIN이나 CTE로 바꿔라"가 대원칙
- 대용량 데이터에서 디스크에서 데이터를 읽어오는 I/O 비용이 가장 큼. 읽는 횟수 최소화한 2번이 빠름. 

1번 스캔, 인덱스 정렬 연산 
- [고급 스킬] 데이터를 과거/미래로 쪼개서 합칠 생각만 했는데, 윈도우 함수 내부 ORDER BY에 우선순위 조건(Boolean)을 주면 모든 데이터를 한 줄로 세워서 한 번에 해결할 수 있구나!
- 비즈니스 요구사항 적용: 사용자가 물건을 주문할 때 배송지를 보여줘야 해. 1순위는 사용자가 지정한 '기본 배송지'를 보여주고, 만약 기본 배송지를 지정 안 한 회원이면 '가장 최근에 추가한 배송지'를 1등으로 뽑아줘.


with ranked_price as (
       select product_id, new_price, change_date, 
       row_number() over(partition by product_id
       order by (change_date <= '2019-08-16') desc,  -- 1순위 기준일 이전 
       change_date desc ) -- 2순위 그 안에서 최신 날짜 위로 
 as rn from products
) 

select product_id, if(change_date <= '2019-08-16', new_price, 10) as price
from ranked_price 
where rn = 1; 


================================================================================

2번. window function() 
- 테이블 스캔 2번으로 끝냄 가장 빠름
- left join + coalesce 처리시 distinct로 중복을 제거해야함. distinct는 중복제거 비용이 큼.
 실무에서는 마스터 테이블(기본정보)를 이용해야 성능이 안떨어짐. 
- left join은 개수가 뻥튀기가 되므로 어떻게 해야 개수를 늘리지 않을 수 있을지 고민하다가 distinct가 나옴 

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
-- 모든 제품 목록을 가져오기 위해 Product 원본 테이블에서 product_id만 DISTINCT로 추출 후 LEFT JOIN
-- 원본 테이블에는 16일 이후에만 나타나는 제품도 있지만, cte에서 없으니 left join 시 null 값으로 붙게됨. coalesce()로 null 핸들링  
SELECT DISTINCT p.product_id, 
       COALESCE(rp.new_price, 10) AS price
FROM Products p
LEFT JOIN RankedPrices rp 
       ON p.product_id = rp.product_id AND rp.rn = 1;



===== distinct를 쓰지 않고, 마스터 테이블을 활용하면 성능이 더 좋음.
-- 실무형 최적화 버전 (상품 마스터 테이블이 별도로 있을 경우)
WITH RankedPrices AS (
    SELECT product_id, new_price,
           ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT m.product_id, 
       COALESCE(rp.new_price, 10) AS price
FROM Product_Master m -- DISTINCT를 쓸 필요 없이 기본키(PK)를 가진 마스터 테이블 활용
LEFT JOIN RankedPrices rp 
       ON m.product_id = rp.product_id AND rp.rn = 1;


================================================================================


### 방법 1: UNION ALL 방식 (독립적인 두 조건 합치기)
* [A 그룹] 16일 이전 기록 존재 => 16일 이하 중 그룹바이에서 '최대 날짜(최신값)' 찾기 (`WHERE (id, date) IN` 구조)
* [B 그룹] 16일 이전 기록 전무 => 가격 10원 고정 (`HAVING MIN` 또는 `NOT EXISTS` 사용)

#### 치트키: NOT EXISTS 문법의 본질 (Correlated 상관 쿼리)
* 파이썬의 `if not (False) == True` 방식과 동일!
* 셔틀 구조: 바깥 테이블(p1)이 안쪽(p2)한테 "내 아이디 줄 테니까 검사해봐" 하고 조건 전달.
* 빈손(못 찾아야) 통과: 안쪽 서브쿼리가 '빈손(False)'으로 돌아와야 최종 합격시켜서 10원 낙찰

- union distinct는 중복을 제거하는데, 
  한 컬럼만 보는게 아니라 존재하는 모든 컬럼이 같은 값이여야 중복으로 보고 제거한다. 


1-1번. CTE, union all, inner join 방식 
- 가상의 임시 테이블(CTE)을 딱 필요한 만큼 메모리에 예쁘게 만들어두고, 원본 테이블과 JOIN을 걸어서, 
데이터베이스 엔진이 인덱스를 타서 초고속으로 매칭하기 아주 좋은 구조야. 가독성도 훌륭해.
- 3번 스캔함 
- 변경될 수 있는 날짜를 두번 넣어줘야해서 유지보수성이 떨어짐 
- 날짜 max(), min()으로 row_number() 윈도우 함수와 사용할 수 있는 유형 
- 16일 이후는 가격 고정이라 그룹바이하고 해빙 절에서 최소 값(처음 나타난 값)이 기준일 보다 큰 경우만 찾아줌

with before_16 as 
(select product_id, max(change_date) as change_date
from products 
where change_date <= '2019-08-16'
group by product_id)

select b.product_id, p.new_price as price
from before_16 b join products p
on p.product_id = b.product_id and p.change_date = b.change_date

union all

select product_id, 10 as price
from products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';

-- 이 부분 where로 하면 전체 데이터가 나와버림. 
-- 그룹을 지어놓고 역사적 첫 데이터 MIN()이 16일 이후인 것만 찾음 
-- group by가 이미 되어있으니 having 절 조건으로 각 아이디에 최소 날짜가 8월 16일보다 큰 것만 남게 됨. 
-- 앞에서 where에서 날짜 조건을 써서 뒤에서 그럼 이후의 최소날짜는 어떻게 구하지? 했던 것임. 
-- select 절에서 date가 필요하지 않아서 having에서 써도 되고, 앞에는 date를 구해야 price를 매칭할 수 있음 

- 태어나서 처음으로 가격이 바뀐 날짜조차도 16일 이후인 녀석들만 골라내야 해.
- 그래서 컴퓨터한테 제품별로 방을 묶어두고(GROUP BY product_id), 
그 방에서 가장 오래된 역사적 첫 기록(MIN(change_date))을 꺼내오라고 하는 거야.
---------------------------------------------------------------

1-2번 subquery not in, union all, not exists 방식 
- not exists는 성능이 그리 좋지 않다. 
- 3 or 4번 스캔 (not exists 상관쿼리) 

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
-- 어찌어찌 구하긴 했는데 성능 최적화가 필요함 7/7

with max_date as (select product_id, max(change_date) as change_date
from products where change_date <= '2019-08-16'
group by product_id),

new_products as (select p.product_id, p.change_date, p.new_price from max_date md join products p
on p.change_date = md.change_date and p.product_id = md.product_id) 

select distinct dp.product_id, coalesce(np.new_price, 10) as price from products dp
left join new_products np on np.product_id = dp.product_id


두번째 7/13
with before_16 as (select product_id, max(change_date) as change_date
from
products
where change_date <= '2019-08-16'
group by product_id)

select b.product_id, p.new_price as price
from before_16 b join products p
on b.product_id = p.product_id and b.change_date = p.change_date
union distinct

select product_id, 10 as price
from products 
where change_date > '2019-08-16' and
product_id not in (select product_id from before_16)