https://projects.datacamp.com/projects/2190
Impact Analysis of GoodThought NGO Initiatives - intermediate sql

List the top five assignments based on total value of donations, categorized by donor type. 

- 1. 문제를 보면 테이블의 관계와 구조를 먼저 파악해야한다 
    - M2M 의 중간 테이블인 donations를 중심으로 (transaction 정보)
- 2. 최종 출력 형태를 상상한다
    - 최종 행이 5개 나와야한다. 
    - 컬럼은 4개가 나온다. 
- 3. 집합 구조 
    - donations와 donor를 조인하고, 총액 함산 집계를 하며 그룹바이로 압축한다. 
    - region 정보를 붙이기 위해 5개 로우에 assignments를 조인해준다. 
    - 5개 잘라준다. 


-- 모범답안
-- highest_donation_assignments
-- 그룹바이로 먼저 합산해두고, 뒤에서 조인을 붙여서 정보 더해줌. 

WITH donation_details AS (
    SELECT
        d.assignment_id,
        ROUND(SUM(d.amount), 2) AS rounded_total_donation_amount,
        dn.donor_type
    FROM
        donations d
    JOIN donors dn ON d.donor_id = dn.donor_id
    GROUP BY
        d.assignment_id, dn.donor_type
)

SELECT
    a.assignment_name,
    a.region,
    dd.rounded_total_donation_amount,
    dd.donor_type
FROM
    assignments a
JOIN
    donation_details dd ON a.assignment_id = dd.assignment_id
ORDER BY
    dd.rounded_total_donation_amount DESC
LIMIT 5;


-- 오답 분석
-- 잘못된 접근임. 값 합산시에는 group by로 압축해놓고 시작해야함 
-- 윈도우 함수의 특성상 데이터를 압축하지 않고 원래 있던 행 개수를 그대로 유지하기 때문에 왜곡일어난다. 
-- 지문이 모호하기때문에 정확히 물어봐야함. 카테고리별 5개인가 (총15개), 전체에서 5개인가
-- highest_donation_assignments
with base as (select assignment_id, donor_type, 
	        round(sum(amount) over(partition by assignment_id, donor_type), 2) amount 		 
	        from donations d1 
	        join donors d2 using(donor_id)),
	
result_table as (
	select assignment_id, donor_type, amount 
	from base group by assignment_id, donor_type, amount 
	order by amount desc limit 5)
	
select assignment_name, a.region, amount as rounded_total_donation_amount, donor_type 
	from result_table r 
	join assignments a on r.assignment_id = a.assignment_id


