- 체크리스트 단계를 따라가는 연습. 
- LEFT JOIN: ~가 없는 고객, No, Never Missing... 
- INNER JOIN: 모두 가진, 동시에 만족하는, 양쪽에 다 존재하는  
-- customer with no order record - Customers
-- o.customerId = c.id
-- 1:N 

-- c left join orders 
bc keeping all customer data is important. 
customer table has all the customers records, but orders might have multiple or none order data of those customers. 
if I use inner join, customers who never orders would be lost. bc inner join only keeps data that exists in both tables

-- find where o.id is null 

select c.name as Customers
from customers as c 
left join orders as o 
on c.id = o.customerId
where o.id is null