https://datalemur.com/questions/time-spent-snaps

- 미디움은 항상 엣지 케이스가 있음 
- 먼저 로우 데이터 훑어보고 시작하기 
- 집합 관계 머릿속에 떠올려보고 시작하기 

- 조건부 집계
- % 퍼센트가 나오면 100.0 곱하기 기억하기 
- activity type의 종류가 여러개 였음. string ('send', 'open', 'chat') 이런 함정 조심! 
- case when then else end

with base as (
select 
    age_bucket, sum(time_spent) total, 
    sum(case when activity_type = 'send' then time_spent else 0 end) as send, 
    sum(case when activity_type = 'open' then time_spent else 0  end) as open
from activities a join age_breakdown b using(user_id)
where activity_type in ('open', 'send')
group by age_bucket
)

select 
age_bucket, 
round(send * 100.0 / total, 2) send_perc, 
round(open * 100.0 / total, 2) open_perc
from base 