https://leetcode.com/problems/average-time-of-process-per-machine

조건부 집계 (conditional aggregation)
- 처음 이 문제를 풀 때 start 인 테이블과 end인 테이블을 조인해서 풀려고함. 똑같은 테이블 두번 읽으니 성능이 좋지않다. 
- CASE WHEN을 사용하면 full scan 한번에 start랑 end 계산을 끝낸다. 대용량 데이터 다루기 좋음. 
- 조건 검사를 먼저 하고나서 합산은 맨 마지막에 하는 것임. 조건에서 필터링했는데 합산을 바로 못함. 
  주머니 속에서 조건에 맞는 알맹이(로우)들만 쏙쏙 골라낸 뒤, 마지막에 합친다.
    안되는 이유.: CASE WHEN activity_type = 'start' THEN SUM(timestamp) END -> 순서가 꼬여버린다. sum()이 먼저 되서 다 더해버린 뒤에 조건을 걸어버리기 때문에 원하는 결과가 안나옴.

- 아래처럼 분리해서 써놓고나서 나누기하고 라운드 붙이기. 
select 
machine_id,
sum(case when activity_type = 'start' then timestamp end) as sum_start,
sum(case when activity_type = 'end' then timestamp end) as sum_end,
COUNT(DISTINCT process_id) cnt
from activity
group by machine_id

| machine_id | sum_start          | sum_end           | cnt |
| ---------- | ------------------ | ----------------- | --- |
| 0          | 3.852000117301941  | 5.639999866485596 | 2   |
| 1          | 0.9800000190734863 | 2.96999990940094  | 2   |


--
1. 그룹바이 조건부 집계
- `end`일 때의 시간들을 다 더한 값에서, `start`일 때의 시간들을 다 더한 값을 빼면? 그게 결국 그 머신이 일한 **순수 총합 시간**이 되겠지! 그걸 `COUNT(DISTINCT process_id)`(총 프로세스 개수)로 한 번에 나눠버리는 기법이야.

SELECT 
    machine_id,
    ROUND(
        (SUM(CASE WHEN activity_type = 'end' THEN timestamp END) - 
         SUM(CASE WHEN activity_type = 'start' THEN timestamp END)) 
        / COUNT(DISTINCT process_id), 
        3
    ) AS processing_time
FROM activity
GROUP BY machine_id;



-- 
2. CTE 사용 
- 각 머신의 프로세스별 토탈시간 구해놓은 주머닌에서 
- 이미 요약된 결과를 가지고 `machine_id`로만 다시 묶은 뒤, AVG() 바로 사용해서 구함. 

-- 1단계: 각 머신의 프로세스별로 걸린 시간(total_time)을 먼저 계산하는 주머니
WITH process_times AS (
    SELECT 
        machine_id, 
        process_id,
        MAX(timestamp) - MIN(timestamp) AS total_time
    FROM activity 
    GROUP BY machine_id, process_id
)

-- 2단계: 위에서 만든 주머니를 가지고, 머신별로 평균(AVG)을 낸다!
SELECT 
    machine_id, 
    ROUND(AVG(total_time), 3) AS processing_time -- 👈 굳이 갯수를 세서 나눌 필요 없이 AVG() 쓰면 끝!
FROM process_times 
GROUP BY machine_id;









======================
이전 쿼리
with t as (select machine_id, max(timestamp) - min(timestamp) as total_time, count(machine_id) as cnt
from activity 
group by machine_id, process_id)

select machine_id, round((sum(total_time) / cnt), 3) as processing_time
from t 
group by machine_id


select a1.machine_id, round(avg(a2.timestamp - a1.timestamp), 3) 
as processing_time
 from activity as a1 
left join activity as a2 
on a1.machine_id = a2.machine_id
and a1.process_id = a2.process_id 
where a1.activity_type = 'start' and a2.activity_type = 'end'
group by a1.machine_id



