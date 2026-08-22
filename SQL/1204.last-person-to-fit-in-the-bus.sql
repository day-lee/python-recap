https://leetcode.com/problems/last-person-to-fit-in-the-bus

aggregate window functions
https://datalemur.com/sql-tutorial/sql-aggregate-window-functions

누적 합 Running Sum 
(달리다 느낌이 아니라 계속 이어지다의 느낌 기찻길🚂)
- 윈도우 함수로 누적합 구할 수 있음 
- cte에서 turn 기준으로 정렬후 몸무게 누적합 컬럼추가 
- 외부 쿼리에서 누적합이 1000 이하인 사람들 중 마지막 사람을 가져오기위해 
  누적합을 내림차순으로 정렬 후 limit 1로 마지막 사람 가져오기

이동 합 Rolling sum, Moving sum 
(rolling, moving은 일정한 크기의 관람차가 굴러가는 모양 🎡)
- 특정 윈도우에서 시간이 흐르면서 더해지는 것 e.g. 최근 7일간 방문자 수 합계 

==========================================================
WITH rs AS (
    SELECT 
        person_name, 
        SUM(weight) OVER(ORDER BY turn ASC) AS runningsum
    FROM queue
)
SELECT person_name
FROM rs 
WHERE runningsum <= 1000
ORDER BY runningsum DESC
LIMIT 1;

--
Explanation: The following table is ordered by the turn for simplicity.
+------+----+-----------+--------+--------------+
| Turn | ID | Name      | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1    | 5  | Alice     | 250    | 250          |
| 2    | 3  | Alex      | 350    | 600          |
| 3    | 6  | John Cena | 400    | 1000         | (last person)
| 4    | 2  | Marie     | 200    | 1200         | (cannot board)
| 5    | 4  | Bob       | 175    | ___          |
| 6    | 1  | Winston   | 500    | ___          |
+------+----+-----------+--------+--------------+