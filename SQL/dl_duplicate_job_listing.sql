-- https://datalemur.com/questions/duplicate-job-listings
-- Definition: Duplicate job listings are defined as two job listings within the same company that share identical titles and descriptions.
-- 지문에서 중복의 기준이 되는 컬럼을 3개를 골라야함. 
-- 압축하는 group by 를 사용했지만 주머니에는 아직 남아있음. 
-- 본 쿼리에서 distinct를 써서 중복을 제거해야함. 


with base as (select company_id, title, description from job_listings 
group by company_id, title, description having count(*) > 1) 

select count(distinct company_id) duplicate_companies from base
