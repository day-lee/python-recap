https://datalemur.com/questions/card-launch-success

-- 윈도우 펑션과 CTE 이용해서 풀기 
-- date 타입 변환: postgresql make_date(year, month, 1) 하면 컬럼에서 추출 가능
-- group by로 만들어야 할 때는 window function의 partition by로 풀 수 있을까? 생각해보기 

with card_launch as (
select card_name, issued_amount, 
make_date(issue_year, issue_month, 1) as issue_date, 

min(make_date(issue_year, issue_month, 1)) 
over (partition by card_name) as launch_date -- group by card_name 

from monthly_cards_issued 
)

-- where 조건절이 중요함 
select card_name, issued_amount from card_launch
where issue_date = launch_date 
order by issued_amount desc; 
