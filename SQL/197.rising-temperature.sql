https://leetcode.com/problems/rising-temperature

- 윈도우 함수의 lag()를 "날짜" 칼럼과 조합할 때 주의사항 
- 모든 데이터가 날짜 순서대로 쌓여 있지 않을 수 있다. 
- 1일 다음 (2일 missing)후에 3일이 올 수도 있고, 1,2,3일 데이터가 순서대로 쌓여있지 않을 수 있기 때문에, 
  문제에서 어제(바로 전날)을 명시한 경우 함정이 될 수 있다. 
- lag()는 '바로 전에 나타난 로우'를 의미하지 '전 날(yesterday)'을 의미하지는 않는다. 

- DATEDIFF(col1, col2) 함수는 col1 - col2 순서가 중요하다.
- join 시 on은 키를 엮는 것 뿐만아니라, 조건을 만족하는 로우를 찾아준다. 
- DATE_SUB는 SQL에서 "특정 날짜에서 원하는 만큼의 시간을 뒤로 빼라(Substract)"
- DATE_ADD(col, interval 1 day) 랑 짝꿍 (postgresql은 col + interval '2 day')  -> 복수형 신경쓰지말고 단수로 통일 


1. CTE, 윈도우 함수, datediff(col1, col2)
- OVER(ORDER BY recordDate)는 정렬 부하가 있을 수 있음 
-  원래 테이블에서 lag() 함수를 사용해서 전날 온도와 날짜를 붙여서 CTE를 만들었다. 
 이 테이블에서 where 조건절로 온도가 전날보다 높으면서, 두 날짜의 차이가 1인 날만 골라냈다. 

with prev_temp as (select id,
recordDate, 
temperature,
lag(temperature) over(order by recordDate asc) as prev_temp,
lag(recordDate) over(order by recordDate asc) as prev_date
from weather)

-- select * from prev_temp
select id as Id from prev_temp 
where prev_temp < temperature and 
 datediff(recordDate, prev_date) = 1



2. SELF JOIN 
- SQL에서 ON 절은 단순히 '똑같은 값 연결하기'가 아니라, 두 테이블을 합칠 때 통과해야 하는 '합격 조건문(Filter)'
- "w1의 날짜에서 w2의 날짜를 뺐을 때 정확히 1이 나온다(True)면, 이 두 테이블의 로우를 붙여줘."
- DATEDIFF(날짜A, 날짜B)는 항상 [날짜A] - [날짜B]로 계산해. 즉, 앞의 날짜에서 뒤의 날짜를 빼는 거지. 
- DATEDIFF('2026-07-02', '2026-07-01') ➡️ 7월 2일 - 7월 1일 = 1 (정답 ⭕) 미래 - 과거: 양수
- DATEDIFF('2026-07-01', '2026-07-02') ➡️ 7월 1일 - 7월 2일 = -1 
- 컴퓨터는 이 조건문을 보고 "(w1의 날짜) - (w2의 날짜) = 1" 인 조합만 찾아서 가로로 붙여줘. 

- ON 절에 똑같은 키 매칭(=)이 아니라 함수나 연산이 들어가면 컴퓨터는 Full Scan을 해서 성능이 안좋다. 
- 일반적으로 데이터베이스는 날짜 컬럼에 정렬 책갈피(인덱스)를 만들어둔다.
- 성능을 지키려면 한쪽 컬럼은 아무런 가공도 하지 않은 순수한 상태(w2.recordDate = ...)로 두고 반대편을 계산하는 식으로 쿼리를 튜닝해야 한다!
  ON w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY) subtract 1일이니까 하루전날

--
2-1
- 풀스캔을 돌기 때문에 실무에선 금지
- join on datediff(co1, co2) = 1 이건 쓰면 안됨. 뇌에서 지워

select w1.id, w1.recordDate, w1.temperature, 
from weather w1
join  weather w2 
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 --  "함수 가공 조인: w2가 무조건 w1의 하루 전날이어야 해"
where w1.temperature > w2.temperature 


2-2 
- 셀프 조인의 조건이 순수 상태 = 계산된 상태 
- 날짜에 인덱싱이 걸려있다면 가장 성능 좋은 쿼리 
- w2.recordDate 컬럼이 아무런 가공도 안 된 순수한 상태로 등호(=) 
왼쪽에서 컴퓨터가 날짜 인덱스를 그대로 타고 들어가서 정확히 하루 전 데이터만 쏙 필터링해서 조인

SELECT w1.id
FROM Weather w1
JOIN Weather w2 
ON w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;


''' 하루 전날이랑 조인하면 이렇게 이쁘게 연결됨 

| id | recordDate | temperature | id | recordDate | temperature |
| -- | ---------- | ----------- | -- | ---------- | ----------- |
| 2  | 2015-01-02 | 25          | 1  | 2015-01-01 | 10          |
| 3  | 2015-01-03 | 20          | 2  | 2015-01-02 | 25          |
| 4  | 2015-01-04 | 30          | 3  | 2015-01-03 | 20          |
'''