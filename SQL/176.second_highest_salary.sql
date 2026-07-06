- offset은 결과를 skip 해서 보여줌 
- 스칼라 서브쿼리: 딱 하나의 결과 값만 올 수 있음 
- 밖에서 select () 한 번 더 감싸서 쓴 이유는 NULL을 강제로 반환하기 위함
-> 내부 서브쿼리의 결과가 존재 하지 않을 때 sql 엔진은 NULL 이라는 하나의 값으로 변환해서 한개를 출력해줌 

select 
    (select distinct salary 
    from employee
    order by salary desc 
    limit 1 offset 1 
) AS SecondHighestSalary;

