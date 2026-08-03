https://leetcode.com/problems/investments-in-2016

- 집합적 사고 (교집합)
- 2015년 보험료 겹치는 중복 사람들 주머니 A
- 위치가 유니크한 사람들 주머니 B

- 내 첫 접근은 절차적 접근. 동시 비교하지 않고 연쇄 필터링을 해서 데이터가 깎여나가서 필터링에 오류가 생김 
-  교집합 메인 쿼리에서 주머니 A 와 B를 동시에 만족하는 사람을 찾아야함 
- (lat, lon) tuple 세트, 쌍으로 일치할 때만 묶음이 그룹으로 간주됨. 이 페어로 파티션 나눌 수 있음을 기억하기. 


-- 윈도우 함수 
with cnt_insurance as (
select tiv_2016, tiv_2015, 
count(*) over(partition by tiv_2015) as cnt_15,
-- (lat, lon) 세트, 쌍으로 일치할 때만 묶음이 그룹으로 간주됨 
count(*) over(partition by lat, lon) as cnt_loc
from insurance) 

-- select * from cnt_insurance

select round(sum(tiv_2016), 2) as tiv_2016
from cnt_insurance
where cnt_15 > 1 and cnt_loc = 1;



-- CTE
-- 3번 스캔
with unique_lat_lon as (select lat, lon
from insurance
group by lat, lon
having count(*) = 1 ),

15_unique as (
    select tiv_2015
    from
    insurance
    group by tiv_2015
    having count(tiv_2015) > 1
)

select round(sum(tiv_2016), 2) as tiv_2016 from insurance
where (lat, lon) in (select lat, lon from unique_lat_lon) and tiv_2015 in (select tiv_2015 from 15_unique)

