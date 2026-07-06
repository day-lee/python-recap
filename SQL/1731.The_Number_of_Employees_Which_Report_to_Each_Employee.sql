https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee 

- 181이랑 같은 유형의 문제 self join
- 매니저 정보를 알고 싶으니까 메인 테이블로 둠 
- 테이블이 어떻게 연관이 되어서 행이 늘어나는지 그려지지가 않음 
=> 부하 직원 테이블이(출발) reports_to -> 매니저 테이블에 화살을 쏜다(도착) employee_id
    on m.employee_id = e.reports_to 
    e 들아 너의 reports_to에 적힌 숫자를 m employee_id에 맞춰 

- 드라이빙 테이블이 먼저 나오는 것이 맞으나 작성순서와 별개로 
DB 엔진은 필터링이 많이 되는 테이블을 드라이빙 테이블로 쓴다. 

select m.employee_id, m.name, count(e.employee_id) as reports_count, round(avg(e.age)) as average_age
 from employees e join employees m on e.reports_to = m.employee_id
 group by m.name, m.employee_id 
 order by m.employee_id asc