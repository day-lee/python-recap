https://leetcode.com/problems/department-top-three-salaries

-- 윈도우 함수와 이너조인
- dense_rank()는 동점자에게 같은 순위를 부여하고, 다음 순위는 건너뛰지 않음 
- 3명만 추리라고 하지않고, 샐러리를 기준으로 삼았음. 만약 3명만 순위를 메기라고 하면 동점자 처리에 대한 룰이 필요함. 'in the top three unique salaries'

WITH RankedEmployee AS (
    SELECT 
        name, 
        salary, 
        departmentId, 
        DENSE_RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employee
)

SELECT 
    d.name AS Department, 
    re.name AS Employee, 
    re.salary AS Salary
FROM RankedEmployee re 
JOIN Department d 
  ON re.departmentId = d.id
WHERE re.salary_rank <= 3;

---
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT
        *,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employee
) e
JOIN Department d
ON e.departmentId = d.id
WHERE salary_rank <= 3;
