https://datalemur.com/questions/sql-third-transaction

- row number 구해서 필터링 해주면 됨. 

with base as (SELECT user_id, spend, transaction_date,
row_number() over(partition by user_id order by transaction_date asc) as rn
FROM transactions)

select user_id, spend, transaction_date
from base
where rn = 3;

