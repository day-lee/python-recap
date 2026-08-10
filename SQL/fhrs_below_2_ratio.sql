Conditional Aggregation 조건부 집계
- explain으로 비교해보며 최적화 해냈다!!!! 

- 로직 구상은 모집합(Population)을 정의하는데서 시작한다. 
where filtering은 입구컷 
case when 은 일단 다 들여보낸 뒤 분류 
전체 total도 필요하고, 일부 total도 필요하다면 일단 다 통과 시킨 뒤 안에서 분류해야겠다 판단. 

내가 짠 쿼리 
- explain seq scan 2번 일어나며 병목 가능성 있음. 8만건*2번 = 16만건
- case when 으로 1번 스캔으로 최적화 필요. 
- 인덱스가 있어도 group by 때문에 seq scan을 피할 수 없음 

WITH TOTAL_CNT AS (
    SELECT 
        LOCAL_AUTHORITY_CODE, 
        COUNT(*) AS CNT 
    FROM FACT_HYGIENE_RATINGS 
    GROUP BY LOCAL_AUTHORITY_CODE
),
BELOW_2_CNT AS (
    SELECT 
        LOCAL_AUTHORITY_CODE, 
        DIM.LOCAL_AUTHORITY_NAME, 
        COUNT(*) AS BELOW_2_TOTAL
    FROM FACT_HYGIENE_RATINGS FACT 
    JOIN DIM_LOCAL_AUTHORITIES DIM USING (LOCAL_AUTHORITY_CODE)
    WHERE RATING_SCORE IS NOT NULL 
      AND RATING_SCORE <= 2
    GROUP BY LOCAL_AUTHORITY_CODE, LOCAL_AUTHORITY_NAME
)
SELECT 
    BC.LOCAL_AUTHORITY_CODE, 
    BC.LOCAL_AUTHORITY_NAME, 
    BC.BELOW_2_TOTAL, 
    TC.CNT AS TOTAL, 
    ROUND((BC.BELOW_2_TOTAL * 100.0 / TC.CNT), 2) AS BELOW_2_PERCENTAGE 
FROM TOTAL_CNT TC 
JOIN BELOW_2_CNT BC USING (LOCAL_AUTHORITY_CODE) 
ORDER BY BELOW_2_PERCENTAGE DESC;

"""
Sort  (cost=4317.45..4318.93 rows=591 width=170)                        
  Sort Key: (round(((((count(*)))::numeric * 100.0) / (tc.cnt)::numeric)
  ->  Hash Join  (cost=4237.46..4290.24 rows=591 width=170)             
        Hash Cond: ((fact.local_authority_code)::text = (tc.local_author
        ->  HashAggregate  (cost=2043.16..2078.96 rows=3580 width=130)  
              Group Key: fact.local_authority_code, dim.local_authority_
              ->  Hash Join  (cost=16.75..2016.31 rows=3580 width=122)  
                    Hash Cond: ((fact.local_authority_code)::text = (dim
                    ->  Seq Scan on fact_hygiene_ratings fact  (cost=0.0
                          Filter: ((rating_score IS NOT NULL) AND (ratin
                    ->  Hash  (cost=13.00..13.00 rows=300 width=236)    
                          ->  Seq Scan on dim_local_authorities dim  (co
        ->  Hash  (cost=2193.89..2193.89 rows=33 width=12)              
              ->  Subquery Scan on tc  (cost=2193.23..2193.89 rows=33 wi
                    ->  HashAggregate  (cost=2193.23..2193.56 rows=33 wi
                          Group Key: fact_hygiene_ratings.local_authorit
                          ->  Seq Scan on fact_hygiene_ratings  (cost=0.
"""

AI가 다듬은 쿼리
- 조건부 집계 
- 8만건 1회 풀 스캔 

1.조인으로 베이스 만들기 (Hash Join)
팩트 테이블에서 시작해서 
딤 테이블을 조인해서 베이스 만들고, 셀렉트에 보로우 이름을 명시해줌

2. 그룹바이 (HashAggregate)
이후 나머지 계산은 팩트테이블에서만 일어남. 
그룹바이를 할 때 셀렉트에 온거 다 명시해줘야하고 fact의 코드와 dim의 name은 어차피 유니크한 조합이라 문제 없음

3. 조건부 계산 
rating_score가 null이 아니고, 2보다 낮거나 같을 때 1을 주고 카운트함 
전체는 바로 모든 로우 카운트 해버림 

전체 비율 계산 시에도 중복 되더라도 앞에서 쓴 집계 쿼리를 다시 한번 써줘야함. 
조건부 case when 에서 조건에 맞지 않는 건 null을 뱉고 이건 자동으로 카운트에서 빠지므로 테이블 여러번 쪼개지 않고도 한번에 처리 


SELECT 
    fact.local_authority_code, 
    dim.local_authority_name,
    -- 2점 이하인 건수만 합산
    COUNT(CASE WHEN fact.rating_score IS NOT NULL AND fact.rating_score <= 2 THEN 1 END) AS below_2_total,
    -- 전체 건수
    COUNT(*) AS total,
    -- 비율 계산
    ROUND(
        COUNT(CASE WHEN fact.rating_score IS NOT NULL AND fact.rating_score <= 2 THEN 1 END) * 100.0 / COUNT(*), 
        2
    ) AS below_2_percentage
FROM fact_hygiene_ratings fact
JOIN dim_local_authorities dim ON fact.local_authority_code = dim.local_authority_code
GROUP BY fact.local_authority_code, dim.local_authority_name
ORDER BY below_2_percentage DESC;


"""
QUERY PLAN                                                                              
----------------------------------------------------------------------------------------
Sort  (cost=3603.19..3619.69 rows=6600 width=170)                                       
  Sort Key: (round((((count(CASE WHEN ((fact.rating_score IS NOT NULL) AND (fact.rating_
  ->  HashAggregate  (cost=3035.98..3184.48 rows=6600 width=170)                        
        Group Key: fact.local_authority_code, dim.local_authority_name                  
        ->  Hash Join  (cost=16.75..2019.95 rows=81282 width=126)                       
              Hash Cond: ((fact.local_authority_code)::text = (dim.local_authority_code)
              ->  Seq Scan on fact_hygiene_ratings fact  (cost=0.00..1786.82 rows=81282 
              ->  Hash  (cost=13.00..13.00 rows=300 width=236)                          
                    ->  Seq Scan on dim_local_authorities dim  (cost=0.00..13.00 rows=30
"""

🌟 최종 튜닝!
(베이스에서 조인하고 조건부 집계하기와 비교)
조건부 집계 하고 나서 33개끼리 조인하기 

WITH fhrs_summary AS (
    SELECT 
        local_authority_code,
        -- rating_score가 <= 2이면 참(1)이므로 IS NOT NULL은 생략 가능합니다.
        COUNT(CASE WHEN rating_score <= 2 THEN 1 END) AS below_2_cnt,
        COUNT(*) AS total_cnt
    FROM fact_hygiene_ratings 
    GROUP BY local_authority_code
) 
SELECT 
    f.local_authority_code, 
    dim.local_authority_name, 
    f.below_2_cnt, 
    f.total_cnt,
    -- 최종 출력 단계에서 비율 계산
    ROUND(f.below_2_cnt * 100.0 / f.total_cnt, 2) AS ratio
FROM fhrs_summary f
JOIN dim_local_authorities dim USING (local_authority_code)
ORDER BY ratio DESC;


"""
QUERY PLAN                                                                                        
--------------------------------------------------------------------------------------------------
Sort  (cost=2615.43..2615.51 rows=33 width=170)                                                   
  Sort Key: (round((((count(CASE WHEN ((fact_hygiene_ratings.rating_score IS NOT NULL) AND (fact_h
  ->  Hash Join  (cost=2600.80..2614.59 rows=33 width=170)                                        
        Hash Cond: ((dim_local_authorities.local_authority_code)::text = (fact_hygiene_ratings.loc
        ->  Seq Scan on dim_local_authorities  (cost=0.00..13.00 rows=300 width=236)              
        ->  Hash  (cost=2600.38..2600.38 rows=33 width=52)                                        
              ->  HashAggregate  (cost=2599.64..2600.38 rows=33 width=52)                         
                    Group Key: fact_hygiene_ratings.local_authority_code                          
                    ->  Seq Scan on fact_hygiene_ratings  (cost=0.00..1786.82 rows=81282 width=8) 

"""