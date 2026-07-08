https://leetcode.com/problems/customers-who-bought-all-products/

- This table may contain duplicates rows. -> 제약 사항 함정!! 
- 중복 구매가 있을 수 있으므로 distinct를 사용해야 한다. 

- 집계 함수니까 전체 상품 개수를 서브쿼리로 구한 뒤 having에서 비교하겠다 접근은 맞음 
- 서브쿼리는 () 괄호로 묶어줘야한다. 

select customer_id
from customer 
group by customer_id
having count(distinct product_key) = (select count(product_key) from product)
