- https://datalemur.com/questions/top-fans-rank

Filter Pushdown: FROM, JOIN, JOIN, WHERE 는 "조인 전 미리 필터링"이 이루어진다. 
- 논리적 순서, 또는 작성된 순서로는 일단 3개 테이블을 이너조인 시킨다음에 where로 필터링 하는 것 처럼 보이지만 
물리적 디비 엔진의 순서는 모든 테이블에서 WHERE절 필터링을 먼저 해두고서 조인을 한다. 

- 대원칙: 메모리에 올라가는 데이터 (Row * Column) 를 최소화 시키는 것이 성능 최적화의 핵심이다.
- 1:1관계일 때는 행 수가 늘어나지 않으니 조인 먼저
- where 절에서 필터링 가능하면 한번에 필터링
- 가수는 여러개의 song을 가질 수 있으므로 artist_id로 그루핑을 해야한다. 
- 테이블이 늘어날 것 같으면 CTE를 만들어서 중간 결과를 저장하고 그 결과를 가지고 최종 쿼리를 작성하는 것이 좋다. 


WITH top_10_cte as (SELECT 
  artists.artist_name,
  count(songs.song_id),
  DENSE_RANK() OVER (
    ORDER BY COUNT(songs.song_id) DESC) AS artist_rank
FROM artists
INNER JOIN songs
  ON artists.artist_id = songs.artist_id
INNER JOIN global_song_rank AS ranking
  ON songs.song_id = ranking.song_id
WHERE ranking.rank <= 10
group by artists.artist_name)

-- window function은 where 절에 나올 수가 없어서 CTE로 만든 뒤에 where 절에서 필터링을 한다.
select artist_name, artist_rank 
from top_10_cte 
where artist_rank <= 5; 