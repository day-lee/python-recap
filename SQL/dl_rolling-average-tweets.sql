https://datalemur.com/questions/rolling-average-tweets
1321.restaurant-growth 과 같은 문제 

- running sum은 누적 
- rolling, moving avg, running mean 이동 평균 

윈도우 함수 윈도우 계산은 over()문에 range, row btw을 넣는다. 
- avg() over(partition by user_id order by tweet_date asc rows between 2 preceding and current row) 

rows between vs range between 차이점 
- rows는 날짜와 관계 없이 물리적으로 존재하는 행 3개만 고려한다. 
- range는 논리적으로, 로우 존재여부와 상관없이, 기준 날짜로부터 3일을 고려한다. (날짜가 비어있으면 그 날짜는 무시됨) 

postgresql은 숫자를 '2'로 표현해야한다. 
- 3일 평균이라고 해서 interval 3 day를 써서 오답이 나옴. 현재 로우 포함 2일로 해야 총 3일이 되는 것. 

언제 range를 사용하고 언제 Row를 사용해야하는가? 
- range는 시간 기반 추세. 리텐션.
- row는 이벤트, 행동 기반 최근성 
- 실제 기간 동안 무슨일이 있었는가를 알고 싶다면 range로. 중간에 날짜 값이 비어도 됨. e.g. 최근 30일 매출합계
- 최근 n번의 이벤트 기준 평균 처럼 발생 횟수 자체가 의미가 있다면,  e.g. 직전 3번의 거래 평균 

앞의 이틀은 사실 평균값이 아닌데, 포함되어서 잘라내야 싶었지만 답안에서는 그냥 포함시켰다. 이게 회사에서도 이렇게 처리를 할까? 데이터 왜곡같은데? 
- burn-in period 초기 워밍업 구간 이슈 
- 대시보드 연속성 측면에서 포함시켜 보기도하나, 
- 정확성을 중요시해서, 딱 3일 평균을 보여줘야한다면 첫 2일을 제외하거나 Null 처리함 



select user_id,
tweet_date,
round(avg(tweet_count) over (
partition by user_id 
order by tweet_date asc
range between interval '2' day preceding and current row) ,2) as rolling_avg_3d
from tweets