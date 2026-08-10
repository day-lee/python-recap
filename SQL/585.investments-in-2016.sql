https://leetcode.com/problems/investments-in-2016

- 집합적 사고 (교집합)
- 2015년 보험료 겹치는 중복 사람들 주머니 A
- 위치가 유니크한 사람들 주머니 B

- 내 첫 접근은 절차적 접근. 동시 비교하지 않고 연쇄 필터링을 해서 데이터가 깎여나가서 필터링에 오류가 생김 
-  교집합 메인 쿼리에서 주머니 A 와 B를 동시에 만족하는 사람을 찾아야함 
- (lat, lon) tuple 세트, 쌍으로 일치할 때만 묶음이 그룹으로 간주됨. 이 페어로 파티션 나눌 수 있음을 기억하기. 

- 윈도우 함수 + aggregation 연습하기 너무 좋은 문제.

-- 윈도우 함수 + aggregation
-(lat, lon) 세트, 쌍으로 일치할 때만 묶음이 그룹으로 간주됨 

-- 계산 끝낸 base table
with cnt_insurance as (
select tiv_2016, tiv_2015, 
count(*) over(partition by tiv_2015) as cnt_15,
count(*) over(partition by lat, lon) as cnt_loc
from insurance) 

-- filtering 및 최종 계산 테이블
select round(sum(tiv_2016), 2) as tiv_2016
from cnt_insurance
where cnt_15 > 1 and cnt_loc = 1;

-- select * from cnt_insurance
- 쿼리에 윈도우 함수 집계가 두 줄 등장. 모든 로우에 집계 결과가 출력되어 나온다. 
- 윈도우 함수가 로우 한줄 한줄마다 적용이 되어서 각 컬럼에 조건1, 조건2에 해당하는 카운트 개수가 할당이 됨. 
- where 절로 필터링하면 최종 결과가 나옴 
                                              조건1       조건2
| pid | tiv_2015 | tiv_2016 | lat | lon | tiv_2015_cnt | loc |
| --- | -------- | -------- | --- | --- | ------------ | --- |
| 1   | 10       | 5        | 10  | 10  | 3            | 1   |
| 3   | 10       | 30       | 20  | 20  | 3            | 2   |
| 2   | 20       | 20       | 20  | 20  | 1            | 2   |
| 4   | 10       | 40       | 40  | 40  | 3            | 1   |


-- CTE & IN 
-- 3번 스캔이라 좋은 쿼리 아님  
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

