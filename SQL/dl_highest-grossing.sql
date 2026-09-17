https://datalemur.com/questions/sql-highest-grossing

- postgreSQL extract(year from date) 추출해라 년도 날짜 에서
- rank() 윈도우 함수와 group by를 같이 써서 집계 함수 sum()으로 order by 잘 생각해냈음


with base as (
select category, product, 
sum(spend) total_spend,
rank() over(partition by category order by sum(spend) desc) rk
from product_spend 
where extract(year from transaction_date) = '2022'
group by category, product)

select category, product, total_spend
from base
where rk <=2
