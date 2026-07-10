https://leetcode.com/problems/average-selling-price

날짜 date 다루기
- date_col between a and b: 가독성 좋음 
- date_col >= a and date_col <= b : 시간까지 고려해야하면 이게 정확함 


COALESCE(col, 0)
- NULL인 경우 (한번도 안팔린 경우)에는 0으로 표시하라는 조건이 있음 
- round((sum(p.price * coalesce(u.units, 0)) / sum(coalesce(u.units)) ),2) as average_price 이렇게 쓰면 안됨. -> division by zero error 발생 
0 / 0을 만드는 바람에 수학적 오류로 결과가 NULL이 됨.

- NULL 처리시 연산 다 끝난뒤에 coalesce 사용, 연산 중간에 사용하면 division by zero 에러남 
- 계산 과정을 다 NULL로 흘려보낸 뒤, 마지막에 COALESCE로 뜰채 낚시하듯 NULL을 0으로 낚아챔.


LEFT JOIN 
- 가격은 등록되어 있지만 한 번도 안 팔린 제품까지 유실(Data Omission) 없이 살릴 수 있도록 

-- 프라이스에 유닛솔드 정보를 left 로 붙인다. 날짜 조건, id 
-- prices 테이블 기준으로 unitSold를 left join 해야 안팔린것도 계산이 가능하다. no data loss 
-- price * units 해서 sold price 총함계 만든다 
-- 그다음에 그룹바이를 해서 총계 
-- coalesce로 null 처리 

select p.product_id, coalesce(round((sum(price * units) / sum(units)), 2), 0) as average_price
from prices p 
left join unitsSold u 
on p.product_id = u.product_id 
and u.purchase_date >= p.start_date and u.purchase_date <= p.end_date
group by product_id



SELECT p.product_id, COALESCE(ROUND(SUM(price * units) / SUM(units), 2), 0) AS average_price
FROM prices p 
LEFT JOIN unitsSold u 
  ON p.product_id = u.product_id 
 AND u.purchase_date BETWEEN p.start_date AND p.end_date -- 👈 요렇게 한 줄로 가독성 UP!
GROUP BY product_id;