--  서브쿼리, CTE, window function을 이용한 aggregation

-- - 서브쿼리로 풀면서 조인시 ON 에서 alias를 써서 내부 오류가 났다.
-- - 내부 실행 계획 상 JOIN ON이 SELECT보다 먼저 실행되기 때문에 alias를 쓸 수 없었다.
-- - aggregation을 ON에 쓰는게 익숙하지 않았음 
--    on c.genre = g.genre and c.concert_revenue / c.number_of_members = g.revenue_per_member 
-- - 여기서 튜닝을 위해 window function을 쓰는 방법이 있다. 


-- Subquery 
SELECT c.artist_name, c.genre, c.concert_revenue / c.number_of_members as revenue_per_member
FROM concerts c
JOIN (
    SELECT genre, MAX(concert_revenue / number_of_members) as revenue_per_member 
    FROM concerts 
    GROUP BY genre
) g ON c.genre = g.genre AND c.concert_revenue / c.number_of_members = g.revenue_per_member
ORDER BY revenue_per_member DESC;



-- CTE
-- 대용량 데이터에서 성능적으로는 윈도우 함수에 뒤짐 
-- 먼저 테이블을 읽어서 그룹화 한 뒤에(스캔 1회), 그 결과를 원본에서 또 읽어서(스캔 2회) 조인해서 두 번 스캔   
WITH max_per_revenue_genre AS (
     SELECT genre, MAX(concert_revenue / number_of_members) as revenue_per_member 
    FROM concerts 
    GROUP BY genre
)

SELECT c.artist_name, c.genre, c.concert_revenue / c.number_of_members as revenue_per_member
FROM concerts c 
JOIN max_per_revenue_genre m
ON c.genre = m.genre 
AND c.concert_revenue / c.number_of_members = m.revenue_per_member
ORDER BY revenue_per_member DESC;



-- CTE with Window function 
-- with 절 내부에서 1번 스캔하고나면 바로 그 결과로 필터링만 해서 보여줌 
-- 물리적인 디스트 I/O 가장 느린 작업을 한번만 수행 

WITH RankedConcert AS (
    SELECT artist_name, genre, concert_revenue, number_of_members,
    (concert_revenue / number_of_members) as revenue_per_member,
    RANK() OVER 
    (PARTITION BY genre 
    ORDER BY (concert_revenue / number_of_members) DESC) AS rn
    FROM concerts) 
    
-- 위에서 등수를 메겨놨으니 1등만 필터링 함 
SELECT artist_name, concert_revenue, genre, number_of_members, revenue_per_member 
FROM RankedConcert 
WHERE rn = 1
ORDER BY revenue_per_member DESC;