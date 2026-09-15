https://projects.datacamp.com/projects/1590
analyzing_industry_carbon_emissions

-- 가장 최근의 데이터를 뽑기위해 subquery로 select max(year) from... 으로 구함 

SELECT industry_group, count(distinct company) num_companies, 
	round(sum(carbon_footprint_pcf), 1) total_industry_footprint
FROM product_emissions
where year = (select max(year) from public.product_emissions)
group by industry_group
order by total_industry_footprint desc