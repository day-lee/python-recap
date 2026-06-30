- 셀프조인과 datediff or date_add 활용해서 풀 수 있음
- window function lag로 풀수도 있음 



-- 이 방식은 전 날 데이터가 정확히 하루 차이어야만 비교가 가능함. 
with prev_temp as (
    select id, recordDate, temperature, date_add(recordDate, interval +1 day) as nextdate
    from weather ) 
-- today > yday temp 
select today.id from weather today join prev_temp yesterday on 
today.recordDate = yesterday.nextdate
where today.temperature > yesterday.temperature



-- 윈도우 함수 LAG로 한번에 읽고 끝낼 수 있음 
TBC