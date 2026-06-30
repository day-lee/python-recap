- 셀프 조인 

- 메인 테이블은 직원의 정보 테이블이고, 추가적으로 알고자하는 매니저 테이블을 셀프 조인한다. 
- 직원의 매니저 id와 그의 실제 id를 매칭시켜서 조인한다. 
- 직원의 매니저 id 단서를 가지고 매니저 테이블의 실제 id와 매칭시키고자 한다. 

select em.name as Employee
from employee em
join employee m 
on em.manager_id = m.id 
where em.salary > m.salary