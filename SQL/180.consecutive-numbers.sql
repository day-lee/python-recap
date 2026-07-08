https://leetcode.com/problems/consecutive-numbers

- lead, lag 윈도우 함수를 연습하기 아주 좋은 문제 
- easy 197.rising temperature 
- hard 601.Human Traffic of Stadium

- cte로 전 날, 오늘, 다음 날을 조합한 테이블을 만들어 두고,
 distinct로 유니크한 숫자이면서, 조건절에서 모든 컬럼이 매칭될 때를 찾는다. 
- lag() over(order by ) 여기서 order by가 생명이다. 정렬 기준을 줘야 순서가 고정된다. 

- 시계열, 연속성 데이터 검증, N번 연속 데이터가 발생했다, 이전/이후 상태와 비교한다 조건이 나오면 lag(), lead() 함수 
- 현재 행 기준으로 앞 뒤 데이터를 한줄로 붙여서 cte 테이블 만든 뒤에, 외부 메인 쿼리에서 단순 비교로 필터링 한다. 
연속성: 3일 연속 접속 유저 찾기. lag, lead로 앞 뒤칸 채워 한줄 만들기 
상태 변화 감지: (A 변경 후 B) 급격한 수치 변화. lag()로 직전 데이터 끌고 와서 현 상태와 비교하기 


with prev_next as (
select 
num, 
lag(num) over(order by id) as prev, 
lead(num) over(order by id) as next
from logs) 

select distinct(num) as ConsecutiveNums 
from prev_next
where num = prev and num = next