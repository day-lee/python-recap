https://leetcode.com/problems/movie-rating

- 두 집합의 랭킹 구해서 union all 로 이어붙임
- 각 테이블이 movierating - users, movierating - movies랑만 서로 연관이 있음
- 통채로 조인해서 cte만들면 성능 저하

- 연결 컬럼명이 같을 때는 USING(col)이 깔끔함
- 날짜 필터링
  date_col BETWEEN a AND b 는 인덱스 활용 측면에서 성능에 도움 
  EXTRACT(YEAR_MONTH FROM date_col) = 202002 는 직관적인 표현임 

EXTRACT(YEAR_MONTH FROM mr.created_at) = 202002


-- 2020 2월 가장 높은 평균 레이팅을 가진 영화 이름 찾기
-- 20년 2월 created_at 인것만 필터링 한 뒤 무비id, user_id로 이너조인
-- 유저아이디로 그루핑해서 카운트해 그다움 오더바이를해
-- 유니온 올로 묶으라는거구나

내 답
- 한번에 베이스 테이블에서 모두 조인을 해두고 시작함 (이 문제에서는 불필요함)

with base_t as (
select m.movie_id, m.title, u.user_id, u.name,
mr.movie_id as mr_movie_id, mr.user_id as mr_user_id, mr.rating, mr.created_at from
MovieRating mr
join users u
on mr.user_id = u.user_id
join movies m
on m.movie_id = mr.movie_id
)

(select name as results from base_t
group by user_id
order by count(user_id) desc, name asc
limit 1)
union all
(select
title as results
from base_t
where created_at between '20200201' and '20200229'
group by title
order by avg(rating) desc, title asc limit 1) 



모범 답안 
- movierating이랑 users만 관련있으니 조인해서 결과내고
- movierating이랑 movies 조인해서 결과내서 union all로 묶음 
- 조인 컬럼명이 같으면 USING을 쓰면 간결

-- 1. 가장 평점을 많이 남긴 유저 구하기 (영화 테이블 조인 제거)
(SELECT u.name AS results
 FROM MovieRating mr
 JOIN Users u USING(user_id)
 GROUP BY mr.user_id     -- 안전하게 ID로 그룹화!
 ORDER BY COUNT(*) DESC, u.name ASC
 LIMIT 1)

UNION ALL

-- 2. 2020년 2월 평균 평점이 가장 높은 영화 구하기 (유저 테이블 조인 제거)
(SELECT m.title AS results
 FROM MovieRating mr
 JOIN Movies m USING(movie_id)
 WHERE EXTRACT(YEAR_MONTH FROM mr.created_at) = 202002
 GROUP BY mr.movie_id    -- 안전하게 ID로 그룹화!
 ORDER BY AVG(mr.rating) DESC, m.title ASC
 LIMIT 1);


