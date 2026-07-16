https://leetcode.com/problems/monthly-transactions-i


조건 aggregation 
- 날짜 추출: DATE_FORMAT(trans_date, '%Y-%m') 
- mysql은 sum(state = 'approved')를 1, 0 숫자로 결과를 내주지만 
  postgresql에서는 True/False로 나와서 숫자가 아닌 타입을 SUM()할 수가 없다.
  1. 형변환해서 써준다. SUM((state = 'approved')::int) AS approved_count
  2. 필터 문법을 쓴다 SUM(amount) FILTER (WHERE state = 'approved') AS approved_total_amount
  
생각 과정 
- 더 작게 쪼갤 수 없는 최소 그룹단위는 무엇인가? group by를 먼저 적고 시작한다. 
- 조건별 집계는 case when 보다 조건식 연산 SUM(state='approved') -> 1 or 0 활용
- 날짜 함수는 문자열 날짜일때 LEFT(date, 7) 으로 잘라서 쓰는 것이 쉬움 

모범 답안
SELECT 
    LEFT(trans_date, 7) AS month,
    country, 
    COUNT(id) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM((state = 'approved') * amount) AS approved_total_amount
FROM 
    Transactions
GROUP BY 
    month, country;


--

내 답변 
with ym as (
select  *, date_format(trans_date, '%Y-%m') as y_m
from transactions),
base as (
select y_m as 'month', country,
amount,
(case when state = 'approved' then 1 else 0 end) as approved_count,
(case when state = 'approved' then amount else 0 end) as approved_total_amount
from ym
) 

select month, country, count(*) as trans_count, 
sum(approved_count) as approved_count,
sum(amount) as trans_total_amount, 
sum(approved_total_amount) as approved_total_amount
from base 
group by month, country