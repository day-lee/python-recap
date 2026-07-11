https://leetcode.com/problems/delete-duplicate-emails
- 문제 채점에 오류있음

- 중복 이메일이 있다면 id가 가장 작은 로우만 남기고 나머지는 삭제 
- 테이블을 셀프 조인해서 연결하는데 이메일이 같은 행끼리 매칭을 하고나서
- where 절에서 p1.id > p2.id로 필터링을 한다. 
- 지우는 연산이므로 DELETE p1으로 테이블 지움 

DELETE p1
FROM person p1
join person p2
on p1.email = p2.email
where p1.id > p2.id


왼쪽의 테이블 이메일을 기준으로 하나씩 다 비교해나감 
(p1) id=1, john  ↔  (p2) id=1, john
(p1) id=1, john  ↔  (p2) id=3, john

(p1) id=2, bob   ↔  (p2) id=2, bob

(p1) id=3, john  ↔  (p2) id=1, john  ★ DELETE
(p1) id=3, john  ↔  (p2) id=3, john