https://leetcode.com/problems/product-sales-analysis-iii

이게 함정
- '첫 출시 연도(First Year)'에 여러 번 판매된 기록 
- Return all sales entries for that product in that year.
- year 최솟값을 구한 뒤 원본 행들과 다시 매칭(필터링)해줘야 한다.

* 깔끔한 가독성과 단계별 흐름을 원할 때는 윈도우 함수(1번)
* 대용량 데이터에서 인덱스를 태워 초고속 성능을 원할 때는 서브쿼리 조인(2번)

---

1번 쿼리: 윈도우 함수(`OVER(PARTITION BY)`) 방식
- 직관적이고 가독성 좋지만, 실무에서는 성능 떨어질 수 있다. 윈도우 함수는 테이블을 한 번    훑으면서 각 행 옆에 출시 년도 챌갈피를 붙이는 것이다. 
- 최적화가 잘 되어 있을 때만 사용할 수 있다.  

-- 이 테이블에 세일즈를 조인한다. 조건은 이어 프로덕트아이디가 맞는걸로 
-- ======
-- 미니멈 이어를 찾는다. 
-- 파티션을 프로덕트 아이디로. 거기서 조건으로 찾는다. 

with min_year as (
select 
*,
min(year) over(partition by product_id) first_year
from sales 
) 

select product_id, first_year, quantity, price from min_year
where year = first_year


2번 쿼리: 서브쿼리 조인(`GROUP BY` + `JOIN`) 방식
- 인덱스 활용에 유리하다. 
- 서브쿼리에서 제품 별 최소 연도를 구하고, 이를 원본 테이블과 조인한다. 
- 만약 product_id, year 컬럼에 복합 인덱스가 걸려 있다면, 조인시 인덱스를 타고 빠르게 매칭 되는 행만 골라낼 수 있다. 
- 수억 건의 대용량 환경에서 인덱스를 태우기 좋은 방식. 

-- 각 제품의 미니멈 이어 테이블을 구한다. 
-- 이 테이블에 세일즈를 조인한다. 조건은 이어 프로덕트아이디가 맞는걸로 
select 
s.product_id, f.first_year, s.quantity, s.price
from 
(select product_id, min(year) as first_year
from sales 
group by product_id) as f
join sales s 
on f.product_id = s.product_id and s.year = f.first_year

