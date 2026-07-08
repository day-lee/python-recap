https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee 

- 181이랑 같은 유형의 문제 self join
- 매니저 정보를 알고 싶으니까 메인 테이블로 둠 (문제에서 요구한 주인공이 누구인가)
- 테이블이 어떻게 연관이 되어서 행이 늘어나는지 그려지지가 않음 

- 일단 같은 테이블이라도 개념상 매니저 테이블, 직원 테이블로 나눠서 보면 좀 이해가 됨
- 실제 데이터 예시를 보면서..
- 로우 하나씩 보면 직원이 reports_to에 적힌 숫자를 보고
  매니저 테이블에 가서 매니저 employee_id 옆에 착 붙으면서 로우수가 늘어난다.  

- 드라이빙 테이블이 먼저 나오는 것이 맞으나 작성순서와 별개로 
  DB 엔진은 필터링이 많이 되는 테이블을 드라이빙 테이블로 쓴다. 

select 
 m.employee_id,
 m.name, 
 count(e.employee_id) as reports_count, 
 round(avg(e.age)) as average_age
 from employees e join employees m on e.reports_to = m.employee_id
 group by m.name, m.employee_id  -- 어차피 employee_id가 유니크하니까 m.name은 group by에 넣을 필요 없음.
 order by m.employee_id asc