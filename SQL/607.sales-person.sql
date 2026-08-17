https://leetcode.com/problems/sales-person/

- 한 번도 ~를 하지 않은 조건 
- ~를 한번이라도 한 사람을 먼저 구하고, 그 사람들을 전체 명단에서 제외 
- 전체 집합에서 - 부분 집합(red와 거래한 사원) = 여집합 (전체에서 나를 제외한 나머지 전부 - Complement)
===================================================
1. 전체 영업 사원 명단에서 - red랑 한번이라도 거래한 명단 뺴기 
-- - 이 방식은 sales_id 중에 단 하나라도 null이 있으면 아무 결과도 나오지 않을 수 있다. 
-- red와 거래한 명단
with red_sales as (
select s.sales_id from salesperson s
join orders o 
on s.sales_id = o.sales_id 
join company c 
on c.com_id = o.com_id
where c.name = 'RED')

-- 전체에서 red 명단에 없는 것 골라내기 not in 
select name from salesperson 
where sales_id NOT IN (select sales_id from red_sales)


===================================================
2. NOT EXISTS 가 안전하고 성능 좋음. 
-- 내가 가져온 데이터랑 짝꿍이 되는 데이터가 저 테이블에 단 한건이라도 있는지 확인 
-- 성능 최적화: 한건씩 모두 대조해보고, 하나라도 발견하면 더 읽지 않고 short circuit 중지해버림 

select s.name
from salesperson s 
where not exists ( -- not false == True, 결과값에 넣어서 보여준다. 
    select 1 -- T/F 존재유무 판단 
    from orders o 
    join company c on o.com_id = c.com_id 
    where o.sales_id = s.sales_id  -- 바깥 영업 사원과 내부 주문 o 를 연결함. 무전보내서 확인함 상관 서브쿼리 
    and c.name = 'RED'
)

"""
# SQL의 내부 작동을 파이썬으로 시각화한 구조
result = []
for s in salesperson:
    # NOT EXISTS 내부 서브쿼리 가동
    has_red_order = False
    for o in orders:
        if o.sales_id == s.sales_id AND o.company_name == 'RED':
            has_red_order = True
            break # 💡 RED 발견 즉시 검사 중단! (Short-Circuit)
            
    # 💡 RED 거래가 존재하지 않는(NOT EXISTS) 
    if NOT has_red_order: 경우만 결과에 추가
        result.append(s.name)
"""