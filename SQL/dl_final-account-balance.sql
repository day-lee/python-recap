https://datalemur.com/questions/final-account-balance

-- transaction_type의 값이 두가지밖에 없음을 파악함 
-- sum((case when .....end)) conditional aggregation 


SELECT account_id, 
sum((case when transaction_type = 'Deposit' then amount else amount * -1 end)) as final_balance
FROM transactions group by account_id
