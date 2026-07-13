# 1934. Confirmation Rate
튜닝, 리팩토링 과정 

### 1. 베이스 만들기 
'''
select s.user_id, c.action from signups as s 
left join confirmations as c 
on s.user_id = c.user_id;
'''
- 출력해보니 가입만 한 6은 null이 나오고 요청 여러번 한 사람은 user_id가 여러개 나오네. 
- left join이라도 드라이빙 테이블에서 연결하면서 데이터가 늘어나기도 하는구나.
- 모델링을 알면 하나씩 상상하지 않아도 직관적으로 접근 가능
- 1:N (드라이빙:드리븐) 관계: 총 로우수는 N개의 개수많큼 늘어난다. 
- 1 테이블에만 존재하는 키가 있다면 오른쪽에 null 값 도 생길 수 있다는 걸 인지하기 
- 엑셀 vlookup은 행 하나에 매핑을 하기때문에 늘어나지 않지만, join은 복사를 해서 행 개수를 늘릴 수 있다. 
- PK, FK 확인 습관: singup의 user_id는 고유 값, confirmation의 user_id는 FK -> 여러번 등장 가능: 내가 pk에 fk를 붙이는구나 그럼 행이 늘어나겠다.  
- N:M 조인은 행 수가 폭발

### 2. 기준에 맞춰 주머니로 묶기
-- 유저별로 묶어서 여러개 였던 행이 하나의 주머니로 압축됨 
-- group by 쓰느라고 c.action 는 제외해야함 

'''
select s.user_id from signups as s
left join confirmations as c
on s.user_id = c.user_id
group by s.user_id
'''

### 3. 주머니 내부 계산 
- count()로 전체 액션 계산 
- 조건문을 주머니 안에서 바로 분리하는 case 문으로 개수 세기 
'''
select
s.user_id,

sum(case when c.action = 'confirmed' then 1 else 0 end) as confirmed_cnt,

count(c.action) as total_cnt 

from signups as s 
left join confirmations as c
on s.user_id = c.user_id
group by s.user_id 
'''

### 4. 최종 계산 및 포맷팅
- 나눠주고 round() 씌워줌 
- ifnull 써서 null 처리 
'''
select
s.user_id,

ifnull(round(sum(case when c.action = 'confirmed' then 1 else 0 end) 
/count(c.action), 2), 0) as confirmation_rate

from signups as s 

left join confirmations as c
on s.user_id = c.user_id
group by s.user_id 
'''



''' 처음에 짰던 서브쿼리를 이어붙이는 조인은 성능과 가독성 문제있음
select s.user_id, ifnull(sub.confirmation_rate, 0) as confirmation_rate from signups as s 

left join (
select c1.user_id, round(ifnull(c2.confirm_count, 0)/ count(c1.action), 2) as confirmation_rate 
from confirmations as c1 

left join (select user_id, count(action) as confirm_count from confirmations 
 where action = 'confirmed'
 group by user_id) as c2

 on c1.user_id = c2.user_id
 group by c1.user_id) as sub
on s.user_id = sub.user_id
'''