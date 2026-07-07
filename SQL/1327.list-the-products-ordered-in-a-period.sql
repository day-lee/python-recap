https://leetcode.com/problems/list-the-products-ordered-in-a-period


-- cte로 나눠서 풀었음. inner join 바로 연결해서 풀어도 되지만 가독성이나 성능면에서 cte가 나음 
-- whee between은 날짜 단위일때는 괜찮은데 시간이 붙으면 부등호를 붙이는게 정확함 
-- WHERE order_date >= '2020-02-01' AND order_date < '2020-03-01'

with result as (select product_id, sum(unit) as unit
from orders 
where order_date between '2020-02-01' and '2020-02-29'
group by product_id
having sum(unit) >= 100)

select p.product_name, r.unit  
from result r
join  products p on r.product_id = p.product_id
