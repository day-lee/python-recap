https://datalemur.com/questions/second-day-confirmation

- date function postgreSQL date_field + interval '1 day' 
- 2nd day 라고 해서 + interval '2 days' 라고 했는데 생각해보니 1일 뒤에 확인이었음. 

select e.user_id
from emails e
join texts t 
ON e.email_id = t.email_id
where t.signup_action = 'Confirmed' 
and e.signup_date + interval '1 days' = t.action_date 