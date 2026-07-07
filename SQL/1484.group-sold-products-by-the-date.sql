https://leetcode.com/problems/group-sold-products-by-the-date/

- GROUP_CONCAT([DISTINCT] 연결할_컬럼 [ORDER BY 정렬_기준] [SEPARATOR '구분자'])
- group_concat(col order by col asc separator ',')
- 그루핑 하는거라 그룹 바이절 쓰고 나서 바로 써도 되는구나 


select sell_date, count(distinct product) as num_sold,
 group_concat(distinct product order by product asc separator ',') as products
from activities 
group by sell_date
order by sell_date asc
