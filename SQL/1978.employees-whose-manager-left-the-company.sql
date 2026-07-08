https://leetcode.com/problems/employees-whose-manager-left-the-company

특정 그룹에 포함되지 않는 데이터(A Not In B) 찾기
not exists를 쓰기 좋은 유형 


SELECT employee_id
FROM Employees e
WHERE salary < 30000
  AND NOT EXISTS (
      SELECT 1 
      FROM Employees m 
      WHERE m.employee_id = e.manager_id
  )
ORDER BY employee_id;