https://leetcode.com/problems/count-salary-categories/

- 문제의 핵심은 데이터가 없는 카테고리도 결과에 0으로 반드시 포함해야 한다
- COUNT(NULL)은 0을 반환
- 집합의 결합: 컬럼을 동일하게 만들어주고, union으로 합쳐준다. 
--

SELECT 'Low Salary' AS category, COUNT(account_id) AS accounts_count
FROM Accounts
WHERE income < 20000

UNION

SELECT 'Average Salary' AS category, COUNT(account_id) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000

UNION

SELECT 'High Salary' AS category, COUNT(account_id) AS accounts_count
FROM Accounts
WHERE income > 50000;


--
left join 이용
- 복잡함  

WITH categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL 
    SELECT 'High Salary'
)

SELECT 
    c.category, 
    COUNT(a.account_id) AS accounts_count
FROM categories c 
LEFT JOIN accounts a 
    ON (c.category = 'Low Salary' AND a.income < 20000)
    OR (c.category = 'Average Salary' AND a.income BETWEEN 20000 AND 50000)
    OR (c.category = 'High Salary' AND a.income > 50000)
GROUP BY c.category;




-- 내 답안 
- cte 두개 만들어서 비효율 

with categorised as (
select
account_id, income, 
(case 
when income < 20000 then 'Low Salary'
when income >= 20000 and income <= 50000 then 'Average Salary'
else 'High Salary' end) as category 
from accounts),

categories as (
    Select 'Low Salary' as category
    union all
    select 'Average Salary'
    union all 
    select 'High Salary'
)

select c.category, count(c2.category) as accounts_count
from categories c left join categorised c2 
on c.category = c2.category
group by c.category