https://leetcode.com/problems/game-play-analysis-iv/

- DATE_ADD(date_col, INTERVAL 1 DAY) : ADD_DATE()아님, interval day 1 아님, interval '1 day' 아님 
- 날짜_더한다() 동사로 시작 아님 주의 
- 서브쿼리는 괄호로 꼭 묶어줘야햠
- ROUND() 함수쓸 때 괄호 위치 재확인 
- CTE로 풀어도 되지만 서브쿼리로 푸는게 가독성이 더 좋은 경우였음. 
 

-- 성능 최적화 답안 쿼리 
- 플레이어 별로 그룹바이 한 뒤에 가장 첫번째 로그인 날짜를 min()를 구해서 베이스 테이블로 삼는다. 로우 수가 훅 줄어든다. 
- 여기에 셀프 조인을해서 아이디가 같은데, 다음날 로그인한 정보가 있을 경우에만 조인을 시킨다. 날짜 연결은 date_add(date_field, interval 1 day) 함수를 이용한다. 
- 이제 조인까지되어 완전해진 베이스 테이블에서 스칼라 서브쿼리를 진행한다. 조인 테이블의 distinct 나누기 / 전체 테이블의 distinct를 셀렉트 절에서 계산한다.. 

- 이 답안은 최초에 드라이빙 테이블의 숫자를 줄여놓고 다음날 데이터를 셀프조인으로 덧붙이는게 중요하다. 
- 스칼라 서브쿼리를 이용해 셀렉트 절에서 fraction을 구한 것도 포인트. 

- 최초 방문 후 재방문(리텐션) 구하기
1. Min() + group by로 유저별 최초 방문일 테이블로 좁혀놓는다. 
2. 첫방문 테이블과 원본을 self 조인해서, 조건에 date_add(date_field, interval 1 day)를 붙여 다음 날 방문 기록을 붙인다.
3. select 절에서 (조인에 성공한 재방문 유저수) / (전체 유저 수 스칼라 쿼리)로 비율(fraction)을 구한다. 

SELECT 
    ROUND(
        COUNT(DISTINCT a1.player_id) / 
        (SELECT COUNT(DISTINCT player_id) FROM activity) 
    ,2) 
    AS fraction
FROM 
    (SELECT player_id, MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id) a1
JOIN activity a2
    ON a1.player_id=a2.player_id
    AND a2.event_date=DATE_ADD(a1.first_login, INTERVAL 1 DAY)




------------------------------------------------------------------
-- 필터링을 많이 해두고 시작할 수 있는 조건을 찾는게 중요하다 
-- 

-- 처음 로그인하고나서 한번 더 로그인한 플레이어, fraction뭐야 / 전체에서 나누기 
-- round(a, 2)
-- 처음 로그인 min(date)
-- 그룹에서 순서대로 나열한뒤  1이랑 2 날짜 차이가 1이면 1점을 주고 아니면 0 
-- 1점인 플레이어만 카운트 

-- 전체 플레이어 카운트 구해서 나누기  count(distinct player_id)

-- 그룹내의 미니멈데이트 + 1 이 존재하는가? 


-- 처음 짠 쿼리 
-- 윈도우 함수로 풀고 datediff()로 풀었음 
with rk_activity as (select *, 
row_number() over(partition by player_id order by event_date) as rn
from activity)

select round(
(select count(*) as cnt from rk_activity a1 
join rk_activity a2 on a1.player_id = a2.player_id 
where a1.rn = 1 and a2.rn = 2 
and datediff( a2.event_date, a1.event_date) = 1) 
/
(select count(distinct player_id) from activity), 2) as fraction
;