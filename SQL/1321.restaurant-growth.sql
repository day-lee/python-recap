https://leetcode.com/problems/restaurant-growth

사고 과정 
- 1. 날짜 하루 단위로 매출 합계를 구한다. 

- 2. 현재일 + 직전 6일 윈도우를 정의한다. (이동평균)
    날짜 순 정렬, 내 앞의 6개 행(6일전) 부터 현재행(오늘)까지 더해서 평균 
    RANGE vs ROWS
    - (기간) "RANGE" BETWEEN "INTERVAL 6 DAY PRECEDING" AND CURRENT ROW 
        -> 특정 날짜 범위의 모든 행을 가져와라. 
    - (행 개수) "ROWS" BETWEEN "6 PRECEDING" AND CURRENT ROW 
        -> 현재 행 포함 위로 6개 행을 가져온다. 날짜 조건이 없으므로 최근 7일 통계에는 부적절하다.  
- 날짜 순서가 중요하니 partition by가 아니라 order by를 사용해야한다. 
- 만약 id별로 구분을 해야한다면 partition by id order by visited_on을 사용하면 된다.

- 3. 앞 부분 불완전한 데이터 잘라내기
    직전 6일 치 데이터가 없어서 이동평균 만들 수 없음. 
    가장 첫 날짜를 구해서 거기에 6일을 더한 날짜보다 크거나 같은 데이터만 필터링 
    스칼라 서브쿼리로 구한다. 

- 유지보수, 가독성 측면에서 윈도우 함수 한번으로 리팩토링하고, 본 쿼리에서 윈도우 함수로 구한 total_amount를 /7 으로 평균 연산해줌. 

with sum_date as (
    select visited_on, sum(amount) as amount
    from customer
    group by visited_on
), 
7_days_window as (
    select visited_on, 
    sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as total_amount
    from sum_date
)
select visited_on, total_amount as amount, 
round((total_amount / 7 ), 2) average_amount
from 7_days_window
where visited_on >= (select date_add(min(visited_on), interval 6 day) from sum_date)



심화
고객별로 나뉘어야함 
고객별 날짜 순서로 30일 전까지를 줄세워야함. 
누적 주문금액을 구해야함 
-> partition by 고객 아이디

select 
customer_id,
sum(price) over(partition by customer_id order by order_date range between interval 30 day preceding and current row) as 30days_total_price
from orders
