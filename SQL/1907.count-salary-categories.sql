https://leetcode.com/problems/count-salary-categories/

- 문제의 핵심은 데이터가 없는 카테고리도 결과에 0으로 반드시 포함해야 한다


--
CTE, JOIN, CASE WHEN THEN END 이용 - 모범 답안
- 이미 다 계산 된 뒤에 필터링된 적은 로우에서 조인 부하가 가장 적음
- 선집계 후 카테고리를 조인(3건 조인) 
- group by 1은 첫번째 컬럼 category를 의미함. 

| category       |
| -------------- |
| Low Salary     |
| Average Salary |
| High Salary    |

WITH categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL SELECT 'Average Salary'
    UNION ALL SELECT 'High Salary'
),
account_counts AS (
    SELECT 
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category,
        COUNT(account_id) AS accounts_count
    FROM Accounts
    GROUP BY 1
)
SELECT 
    c.category,
    COALESCE(a.accounts_count, 0) AS accounts_count
FROM categories c
LEFT JOIN account_counts a ON c.category = a.category;


--
가독성 제일 좋지만 3번 풀 스캔해서 성능은 탈락 
- `COUNT(NULL)은 0을 반환`
- 집합의 결합: 컬럼을 동일하게 만들어주고, union으로 합쳐준다. 

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