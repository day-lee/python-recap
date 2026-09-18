https://datalemur.com/questions/sql-top-three-salaries

- instruction에서 tie(동점)일 때 sorting 기준을 자세하게 줘서 dense_rank()를 씀 

with base as (
SELECT *,
dense_rank() over(partition by department_id order by salary desc) rk 
FROM employee)
select d.department_name, b.name, b.salary from base b join department d
using(department_id)
where b.rk <= 3 
order by d.department_name asc, b.rk asc, b.name asc