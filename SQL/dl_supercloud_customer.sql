https://datalemur.com/questions/supercloud-customer

- CTE/ Subquery 
-- 이 문제는 성능면에서 cte나 subquery가 거의 동일하므로 가독성과 작성 의도(intent) 측면에서 서브쿼리가 우세
-- scalar value 유형 
-- 만약 여기서 다른 테이블과 더 조인을 해야한다거나 하면 cte가 우세해짐, 임시 테이블을 2회 이상 호출한다? CTE 

-- subquery (scala value)버젼 
select cc.customer_id
from customer_contracts cc 
join products p on cc.product_id = p.product_id
group by cc.customer_id
having count(distinct product_category) = (SELECT count(distinct(product_category)) FROM products)



-- CTE 
-- 여기서 scala value 서브쿼리를 활용함 
with category_group as (
    select cc.customer_id, count(distinct p.product_category) as product_count
    from customer_contracts cc 
    join products p on cc.product_id = p.product_id 
    group by cc.customer_id )

-- select * from category_group 

select customer_id from category_group 
where product_count = (select count(distinct product_category) from products)