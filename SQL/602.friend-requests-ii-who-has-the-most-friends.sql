https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends

순위 메기기
- If there is a tie, ..."(동점자가 있다면 어떻게 해라)라는 조건"을 유심히 본다. 
- 동점자 처리에 대한 언급이 없으면 DENSE_RANK()가 안전하다. 

--
1. union all 과 LIMIT 1 
- count()가 딱 하나의 결과만 있으면 깔끔하게 풀리지만, 만약 동점자가 나오면 다른 order by 조건을 추가해줘야한다. 
- union all로 중복 제거하지 않고서 합쳐준 뒤에, 같은 아이디 끼리 그루핑해서 전체 카운트로 순서대로 배치하고 그중 첫번째 반환한다. 
- 이 방법은 동점자가 존재하면, 그 중 한명만 반환한다. 
with total as (
select requester_id as id from RequestAccepted
union all 
select accepter_id as id from RequestAccepted)

select id, count(*) as num from total group by id 
order by num desc limit 1

--
2. 윈도우 함수 DENSE_RANK() 
- 공동1등이 존재하다면, 그 모든 사람을 다 출력해준다. 
- 중첩 cte로 처음 베이스는 나타난 모든 id를 합쳐준 뒤,  
  그 베이스에서 전체 카운트를 기준으로 dense_rank()를 만들어서 조건절에서 rk = 1을 모두 뽑아줌   

WITH total AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL 
    SELECT accepter_id AS id FROM RequestAccepted
),
friend_counts AS (
    SELECT id, COUNT(*) AS num,
           -- 친구 수(num)가 많은 순으로 순위를 매김 (공동 1등은 같은 순위)
           -- RANK()는 컬럼을 인자로 필요로 하지 않음. order by 정렬 기준은 필요함 
           -- order by 기준으로 집계 함수가 올 수 있음 
           DENSE_RANK() OVER(ORDER BY COUNT(*) DESC) AS rnk
    FROM total 
    GROUP BY id
)
SELECT id, num 
FROM friend_counts 
WHERE rnk = 1; -- 1등인 사람들을 전부 출력


-- NOTE
-- group by랑 윈도우 함수를 같이 쓰는게 약간 읭스러운데...?  
- 윈도우 함수를 그룹바이와 함께 쓸 수 있다. 
- 실행 순서상 group by, having, "window function", select...순으로 실행한다. 
- 그룹바이를 해둔 뒤 count(*) 집계 결과가 나올 시점에는 이미 윈도우 함수도 그룹화 된 집계 데이터를 바라보게 된다. 
- 따라서 윈도우 함수의 order by에서 count(*) 집계 기준으로 순서를 메길 수 있게 된다. 
- group by와 윈도우 함수를 같이 쓸 때 주의 할 점, 
    - group by "id" 를 했다면 윈도우 함수 안의 order by, partition by 안에는 "id" 컬럼이나, count(*) 같은 집계 함수만 들어올 수 있다. SELECT 절의 규칙과 같다. 
