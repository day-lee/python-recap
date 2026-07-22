https://leetcode.com/problems/restaurant-growth

사고 과정 
- 날짜 하루 단위로 매출 합계를 구한다. 
- 현재일 + 직전 6일 윈도우를 정의한다. (이동평균)
    날짜 순 정렬, 내 앞의 6개 행(6일전) 부터 현재행(오늘)까지 더해서 평균 
    range between 6 preceding and current row 
    (rows between은 연속 날짜가 아니라 데이터가 존재하는 6개 행 가져옴)
- 날짜가 연속적이지 않기 때문에 
- 앞 부분 불완전한 데이터 잘라내기
    직전 6일 치 데이터가 없어서 이동평균 만들 수 없음. 
    가장 첫 날짜를 구해서 거기에 6일을 더한 날짜보다 크거나 같은 데이터만 필터링 
    스칼라 서브쿼리로 구한다. 


with mv_avg as (
    select visited_on, sum(amount) amount
from customer
group by visited_on),
moving_calc as (
select
visited_on,
sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as total_amount,
round(sum(amount) over(order by visited_on range between interval 6 day preceding and current row) / 7, 2) as average_amount
from mv_avg)


select visited_on, total_amount as amount, average_amount 
from moving_calc
where visited_on >= 
    (select date_add(min(visited_on), interval 6 day) 
    from customer)

order by visited_on

