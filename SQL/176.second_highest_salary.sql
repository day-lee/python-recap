- offset은 결과를 skip 해서 보여줌: 1은 건너뛰고 2번째 결과를 보여줌. 리미트 다음에 옴
- 스칼라 서브쿼리: 딱 하나의 결과 값만 올 수 있음 

- NULL fallback trick: 에러나 빈 결과 방지.
- 오라클에서는 select (...) as a from dual; 이런식임 
- 밖에서 select () 한 번 더 감싸서 쓴 이유는 NULL을 강제로 반환하기 위함
-> from 절이 없는 select는 무조건 1개 row 생성. sql 엔진은 NULL 이라는 하나의 값으로 변환해서 한개를 출력해줌 

select 
    (select distinct salary 
    from employee
    order by salary desc 
    limit 1 offset 1 
) AS SecondHighestSalary;

